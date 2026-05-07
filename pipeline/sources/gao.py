"""GAO.gov API client — Government Accountability Office reports.

GAO is where you find quantitative critiques of how agencies execute on
cultural-community statutes: NAGPRA backlogs, IHS funding adequacy, Title VI
enforcement gaps, civil-rights complaint processing times, federal data
disaggregation by race and ethnicity.

The public API requires no key. Endpoint shape varies; this connector tries
the documented JSON endpoint first and falls back to defensive parsing.
"""
import logging

import requests

from ..utils.retry import retry_with_backoff
from .base import BaseSourceConnector

logger = logging.getLogger('tckc_pipeline')

API_BASE = 'https://www.gao.gov/api/v1'
PER_PAGE = 50
MAX_PAGES = 6  # 300 reports max per run


@retry_with_backoff(max_retries=3, exceptions=(requests.RequestException,))
def fetch_products(since_date, page=1, per_page=PER_PAGE):
    """Fetch GAO products (reports, testimony, decisions) since the given date."""
    params = {
        'releasedFromDate': since_date,
        'limit': per_page,
        'offset': (page - 1) * per_page,
        'sort': '-release_date',
    }
    resp = requests.get(f'{API_BASE}/products', params=params, timeout=30)
    resp.raise_for_status()
    return resp.json()


class GAOConnector(BaseSourceConnector):
    source_name = 'gao'
    category = 'agency_actions'

    def _fetch_page(self, since_date, **kwargs):
        page = kwargs.get('page', 1)
        if page > MAX_PAGES:
            return [], False
        try:
            data = fetch_products(since_date, page=page)
        except requests.RequestException as e:
            logger.warning(f'gao: API error on page {page}: {e}')
            return [], False
        products = data.get('products') or data.get('results') or data.get('data') or []
        total = data.get('total') or data.get('pagination', {}).get('total') or 0
        has_more = (page * PER_PAGE) < total and page < MAX_PAGES
        return products, has_more

    def _parse_result(self, doc):
        attrs = doc.get('attributes') or doc
        return {
            'source_id': str(doc.get('id') or attrs.get('gao_id') or attrs.get('product_number', '')),
            'title': attrs.get('title', ''),
            'abstract': attrs.get('summary', '') or attrs.get('highlights', '') or attrs.get('description', ''),
            'date': (attrs.get('release_date') or attrs.get('date_published') or '')[:10],
            'product_type': attrs.get('product_type', ''),
            'agencies': attrs.get('agencies') or [],
            'topics': attrs.get('topics') or attrs.get('subjects') or [],
            'recommendations_count': attrs.get('recommendations_count'),
            'url': attrs.get('html_url') or attrs.get('url') or '',
            'pdf_url': attrs.get('pdf_url', ''),
        }


_connector = GAOConnector()
fetch_since = _connector.fetch_since
get_category = _connector.get_category
