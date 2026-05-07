"""Regulations.gov v4 API client — public rulemaking dockets.

Captures proposed and final rules, supporting documents, and federal notices
that may not always cross-publish in the Federal Register. The dockets are
where the deeper substructure of a regulation lives: economic analyses,
agency responses to comments, supplementary submissions.

Key registration: https://api.data.gov/signup (single key works across
regulations.gov and govinfo.gov). Set as REGULATIONS_GOV_API_KEY in .env
or as a GitHub Actions secret.
"""
import logging
import os

import requests

from ..utils.retry import retry_with_backoff
from .base import BaseSourceConnector

logger = logging.getLogger('tckc_pipeline')

API_BASE = 'https://api.regulations.gov/v4'
API_KEY = os.environ.get('REGULATIONS_GOV_API_KEY', '')
PER_PAGE = 100
MAX_PAGES = 10  # 1000 documents max per run


@retry_with_backoff(max_retries=3, exceptions=(requests.RequestException,))
def fetch_documents(since_date, page=1, per_page=PER_PAGE):
    """Fetch documents posted since the given date."""
    if not API_KEY:
        raise RuntimeError('REGULATIONS_GOV_API_KEY not set')
    params = {
        'filter[postedDate][ge]': since_date,
        'page[size]': per_page,
        'page[number]': page,
        'sort': '-postedDate',
        'api_key': API_KEY,
    }
    resp = requests.get(f'{API_BASE}/documents', params=params, timeout=30)
    resp.raise_for_status()
    return resp.json()


class RegulationsGovConnector(BaseSourceConnector):
    source_name = 'regulations_gov'
    category = 'agency_actions'

    def _fetch_page(self, since_date, **kwargs):
        if not API_KEY:
            logger.info('regulations_gov: REGULATIONS_GOV_API_KEY not set; skipping source')
            return [], False
        page = kwargs.get('page', 1)
        if page > MAX_PAGES:
            return [], False
        data = fetch_documents(since_date, page=page)
        documents = data.get('data') or []
        meta = data.get('meta') or {}
        total_pages = meta.get('totalPages') or meta.get('lastPage') or 1
        has_more = page < total_pages and page < MAX_PAGES
        return documents, has_more

    def _parse_result(self, doc):
        attrs = doc.get('attributes') or {}
        return {
            'source_id': doc.get('id', '') or attrs.get('documentId', ''),
            'title': attrs.get('title', ''),
            'abstract': attrs.get('subtype', '') or '',
            'doc_type': attrs.get('documentType', ''),
            'date': (attrs.get('postedDate') or attrs.get('lastModifiedDate') or '')[:10],
            'agencies': [attrs.get('agencyId')] if attrs.get('agencyId') else [],
            'docket_id': attrs.get('docketId', ''),
            'comment_period_start': attrs.get('commentStartDate'),
            'comment_period_end': attrs.get('commentEndDate'),
            'url': f"https://www.regulations.gov/document/{doc.get('id', '')}",
        }


_connector = RegulationsGovConnector()
fetch_since = _connector.fetch_since
get_category = _connector.get_category
