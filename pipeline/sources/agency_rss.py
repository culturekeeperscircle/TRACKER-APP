"""Agency RSS aggregator — direct newsroom feeds for ~17 cultural-relevant agencies.

The Federal Register catches rules and notices but misses press releases,
operational announcements, leadership changes, dear-colleague letters, and
subagency moves. This connector polls each agency's official RSS feed and
funnels every entry through the same downstream keyword + Haiku screen.

No API key required. Uses the standard library's xml.etree to avoid an
external feedparser dependency.
"""
import logging
import re
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from xml.etree import ElementTree as ET

import requests

from ..utils.retry import retry_with_backoff
from .base import BaseSourceConnector

logger = logging.getLogger('tckc_pipeline')

# Each entry: (agency_tag, feed_url, default_category).
# default_category is the tracker category to assign when the AI screen
# does not override it.
FEEDS = [
    ('DOJ',         'https://www.justice.gov/feeds/justice-news.xml', 'agency_actions'),
    ('DHS',         'https://www.dhs.gov/feeds/news.xml', 'agency_actions'),
    ('DOI',         'https://www.doi.gov/news/RSS', 'agency_actions'),
    ('ICE',         'https://www.ice.gov/news/releases/feed', 'agency_actions'),
    ('CBP',         'https://www.cbp.gov/newsroom/all-news/rss.xml', 'agency_actions'),
    ('USCIS',       'https://www.uscis.gov/news/rss', 'agency_actions'),
    ('ED',          'https://www.ed.gov/feed', 'agency_actions'),
    ('EPA',         'https://www.epa.gov/newsroom/search/rss/all', 'agency_actions'),
    ('NEA',         'https://www.arts.gov/feed', 'agency_actions'),
    ('NEH',         'https://www.neh.gov/feed', 'agency_actions'),
    ('IMLS',        'https://www.imls.gov/news/rss.xml', 'agency_actions'),
    ('SMITHSONIAN', 'https://www.si.edu/newsdesk/rss/all.xml', 'agency_actions'),
    ('ACHP',        'https://www.achp.gov/rss.xml', 'agency_actions'),
    ('BIA',         'https://www.bia.gov/rss/news', 'agency_actions'),
    ('NPS',         'https://www.nps.gov/news/rss-feed.htm', 'agency_actions'),
    ('NOAA',        'https://www.noaa.gov/news/feed', 'agency_actions'),
    ('USAID',       'https://www.usaid.gov/news-information/press-releases/feed', 'agency_actions'),
]

# RSS / Atom namespaces we care about.
NS = {
    'atom':    'http://www.w3.org/2005/Atom',
    'content': 'http://purl.org/rss/1.0/modules/content/',
    'dc':      'http://purl.org/dc/elements/1.1/',
}


def _strip_html(text):
    """Crude HTML strip for RSS descriptions."""
    if not text:
        return ''
    return re.sub(r'<[^>]+>', '', text).strip()


def _coerce_date(s):
    """Parse a date string from RSS pubDate, Atom updated, or ISO. Returns YYYY-MM-DD or ''."""
    if not s:
        return ''
    s = s.strip()
    # ISO 8601 with or without time / zone
    try:
        return datetime.fromisoformat(s.replace('Z', '+00:00')).date().isoformat()
    except (ValueError, AttributeError):
        pass
    # RFC 2822 (RSS pubDate)
    try:
        dt = parsedate_to_datetime(s)
        if dt:
            return dt.date().isoformat()
    except (TypeError, ValueError):
        pass
    # Bare YYYY-MM-DD prefix
    if re.match(r'^\d{4}-\d{2}-\d{2}', s):
        return s[:10]
    return ''


@retry_with_backoff(max_retries=2, exceptions=(requests.RequestException,))
def fetch_feed(url):
    """Fetch and parse an RSS/Atom feed. Returns a list of normalized entries."""
    resp = requests.get(url, timeout=30, headers={'User-Agent': 'TCKC-Tracker/1.0'})
    resp.raise_for_status()
    return resp.content


def _parse_feed_xml(raw_bytes):
    """Yield dict-shaped entries from RSS or Atom XML."""
    try:
        root = ET.fromstring(raw_bytes)
    except ET.ParseError:
        return
    # RSS 2.0
    for item in root.iter('item'):
        link = (item.findtext('link') or '').strip()
        title = (item.findtext('title') or '').strip()
        desc = item.findtext('description') or item.findtext(f'{{{NS["content"]}}}encoded') or ''
        pub = item.findtext('pubDate') or item.findtext(f'{{{NS["dc"]}}}date') or ''
        guid = (item.findtext('guid') or link).strip()
        yield {
            'guid': guid,
            'title': title,
            'description': _strip_html(desc),
            'pub_date': pub,
            'link': link,
        }
    # Atom
    for entry in root.iter(f'{{{NS["atom"]}}}entry'):
        link_el = entry.find(f'{{{NS["atom"]}}}link')
        link = link_el.get('href', '') if link_el is not None else ''
        title = (entry.findtext(f'{{{NS["atom"]}}}title') or '').strip()
        summary = (entry.findtext(f'{{{NS["atom"]}}}summary') or
                   entry.findtext(f'{{{NS["atom"]}}}content') or '')
        updated = (entry.findtext(f'{{{NS["atom"]}}}updated') or
                   entry.findtext(f'{{{NS["atom"]}}}published') or '')
        guid = (entry.findtext(f'{{{NS["atom"]}}}id') or link).strip()
        yield {
            'guid': guid,
            'title': title,
            'description': _strip_html(summary),
            'pub_date': updated,
            'link': link,
        }


class AgencyRSSConnector(BaseSourceConnector):
    source_name = 'agency_rss'
    category = 'agency_actions'

    # We override fetch_since directly so we can iterate feeds. The base
    # paginated _fetch_page model doesn't fit a multi-feed aggregator.
    def _fetch_page(self, since_date, **kwargs):
        raise NotImplementedError

    def _parse_result(self, raw):
        return raw  # Already normalized in fetch_since

    def fetch_since(self, since_date, rate_limiter=None):
        results = []
        seen_ids = set()

        for agency_tag, feed_url, default_cat in FEEDS:
            if rate_limiter:
                rate_limiter.wait_if_needed(self.source_name)

            try:
                raw_xml = fetch_feed(feed_url)
            except requests.RequestException as e:
                logger.warning(f'agency_rss[{agency_tag}]: feed fetch failed: {e}')
                continue

            for entry in _parse_feed_xml(raw_xml):
                pub = _coerce_date(entry['pub_date'])
                if pub and pub < since_date:
                    continue

                sid = f'{agency_tag}:{entry["guid"]}'
                if sid in seen_ids:
                    continue
                seen_ids.add(sid)

                results.append({
                    'source_id': sid,
                    'title': entry['title'],
                    'abstract': entry['description'],
                    'description': entry['description'],
                    'date': pub,
                    'agencies': [agency_tag],
                    'url': entry['link'],
                    'source': self.source_name,
                    '_feed_agency': agency_tag,
                })

        logger.info(f'agency_rss: fetched {len(results)} entries from {len(FEEDS)} feeds since {since_date}')
        return results


_connector = AgencyRSSConnector()
fetch_since = _connector.fetch_since
get_category = _connector.get_category
