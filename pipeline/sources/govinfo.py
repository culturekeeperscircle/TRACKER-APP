"""GovInfo.gov API client — congressional hearings, committee prints,
public laws, full-text statutes.

Primary value for the tracker: the CHRG (Congressional Hearings) collection,
which contains the canonical text of submitted testimony. Witness statements
about cultural-community impact at congressional hearings live here, not in
the Congress.gov bill metadata feed.

Key registration: https://api.data.gov/signup (single key works across
regulations.gov and govinfo.gov). Set as GOVINFO_API_KEY in .env or as a
GitHub Actions secret. The same value as REGULATIONS_GOV_API_KEY is fine.
"""
import logging
import os
from datetime import date, datetime, timezone

import requests

from ..utils.retry import retry_with_backoff
from .base import BaseSourceConnector

logger = logging.getLogger('tckc_pipeline')

API_BASE = 'https://api.govinfo.gov'
API_KEY = os.environ.get('GOVINFO_API_KEY', '') or os.environ.get('REGULATIONS_GOV_API_KEY', '')
PER_PAGE = 100
MAX_PAGES = 5  # 500 hearings max per run

COLLECTION = 'CHRG'  # Congressional hearings


def _to_iso_z(d_str):
    """Convert YYYY-MM-DD to GovInfo's required ISO 8601 Z format."""
    return f'{d_str}T00:00:00Z'


@retry_with_backoff(max_retries=3, exceptions=(requests.RequestException,))
def fetch_collection_page(since_date, until_date, offset=0, per_page=PER_PAGE):
    """Fetch one page of a GovInfo collection.

    GovInfo's collections endpoint is:
        /collections/{collectionCode}/{startDate}/{endDate}
    """
    if not API_KEY:
        raise RuntimeError('GOVINFO_API_KEY (or REGULATIONS_GOV_API_KEY fallback) not set')
    url = f'{API_BASE}/collections/{COLLECTION}/{_to_iso_z(since_date)}/{_to_iso_z(until_date)}'
    params = {
        'pageSize': per_page,
        'offset': offset,
        'api_key': API_KEY,
    }
    resp = requests.get(url, params=params, timeout=30)
    resp.raise_for_status()
    return resp.json()


class GovInfoCHRGConnector(BaseSourceConnector):
    source_name = 'govinfo_chrg'
    category = 'other_domestic'  # Hearings are testimony events, not agency actions

    def _fetch_page(self, since_date, **kwargs):
        if not API_KEY:
            logger.info('govinfo_chrg: GOVINFO_API_KEY not set; skipping source')
            return [], False
        page = kwargs.get('page', 1)
        if page > MAX_PAGES:
            return [], False
        until_date = date.today().isoformat()
        offset = (page - 1) * PER_PAGE
        try:
            data = fetch_collection_page(since_date, until_date, offset=offset)
        except requests.RequestException as e:
            logger.warning(f'govinfo_chrg: API error on page {page}: {e}')
            return [], False
        packages = data.get('packages') or []
        count = data.get('count') or 0
        has_more = (offset + PER_PAGE) < count and page < MAX_PAGES
        return packages, has_more

    def _parse_result(self, pkg):
        return {
            'source_id': pkg.get('packageId', ''),
            'title': pkg.get('title', ''),
            'abstract': '',
            'date': (pkg.get('dateIssued') or pkg.get('lastModified') or '')[:10],
            'doc_class': pkg.get('docClass', ''),
            'congress': pkg.get('congress', ''),
            'committee': pkg.get('chamber', ''),
            'url': pkg.get('packageLink', '') or pkg.get('detailsLink', ''),
        }


_connector = GovInfoCHRGConnector()
fetch_since = _connector.fetch_since
get_category = _connector.get_category
