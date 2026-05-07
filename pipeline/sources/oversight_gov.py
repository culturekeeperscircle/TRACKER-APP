"""Oversight.gov API client — federation of all federal Inspector General reports.

Public API at api.oversight.gov requires no key. Returns OIG reports across
70+ federal Inspector General offices: DOI-OIG, DOJ-OIG, DHS-OIG, ED-OIG,
HHS-OIG, EPA-OIG, plus IG offices for every cabinet department and most
independent agencies.

OIG reports include audits, inspections, evaluations, and investigative
summaries — direct insight into agency wrongdoing, racial-disparity findings,
NAGPRA-compliance gaps, civil-rights enforcement failures.
"""
import logging

import requests

from ..utils.retry import retry_with_backoff
from .base import BaseSourceConnector

logger = logging.getLogger('tckc_pipeline')

API_BASE = 'https://api.oversight.gov/v1'
PER_PAGE = 100
MAX_PAGES = 10  # 1000 reports max per run


@retry_with_backoff(max_retries=3, exceptions=(requests.RequestException,))
def fetch_reports(since_date, page=1, per_page=PER_PAGE):
    """Fetch OIG reports posted since the given date."""
    params = {
        'date_posted_after': since_date,
        'limit': per_page,
        'page': page,
        'sort': '-date_posted',
    }
    resp = requests.get(f'{API_BASE}/reports', params=params, timeout=30)
    resp.raise_for_status()
    return resp.json()


class OversightGovConnector(BaseSourceConnector):
    source_name = 'oversight_gov'
    category = 'agency_actions'

    def _fetch_page(self, since_date, **kwargs):
        page = kwargs.get('page', 1)
        if page > MAX_PAGES:
            return [], False
        data = fetch_reports(since_date, page=page)
        # Different shapes are possible depending on API version; defend against both.
        results = data.get('results') or data.get('data') or data.get('reports') or []
        total_pages = data.get('total_pages') or data.get('pagination', {}).get('total_pages') or 1
        has_more = page < total_pages and page < MAX_PAGES
        return results, has_more

    def _parse_result(self, doc):
        # Defend against both flat and nested attribute shapes.
        attrs = doc.get('attributes') or doc
        return {
            'source_id': str(doc.get('id') or attrs.get('id') or attrs.get('report_number', '')),
            'title': attrs.get('title', '') or attrs.get('report_title', ''),
            'abstract': attrs.get('summary', '') or attrs.get('abstract', '') or attrs.get('description', ''),
            'date': (attrs.get('date_posted') or attrs.get('posted_date') or attrs.get('report_date') or '')[:10],
            'agencies': [
                a for a in [
                    attrs.get('agency'),
                    attrs.get('agency_name'),
                    attrs.get('inspector_general'),
                    attrs.get('ig_name'),
                ] if a
            ],
            'report_type': attrs.get('report_type', '') or attrs.get('document_type', ''),
            'url': attrs.get('url', '') or attrs.get('report_url', '') or attrs.get('html_url', ''),
            'pdf_url': attrs.get('pdf_url', '') or attrs.get('document_url', ''),
            'recommendations_count': attrs.get('recommendations_count') or attrs.get('open_recommendations'),
        }


_connector = OversightGovConnector()
fetch_since = _connector.fetch_since
get_category = _connector.get_category
