"""Federal Register API client — executive actions, agency rules, notices.

Fetches ALL agencies (no agency filter) to ensure exhaustive coverage of
actions affecting ethnic communities and cultural heritage/practice.
"""
import requests
import logging
from datetime import date, timedelta
from ..utils.retry import retry_with_backoff
from .base import BaseSourceConnector

logger = logging.getLogger('tckc_pipeline')

API_BASE = 'https://www.federalregister.gov/api/v1'

# Document types we care about — all actionable federal documents
DOC_TYPES = ['PRESDOCU', 'RULE', 'PRORULE', 'NOTICE']

MAX_PAGES = 10  # Cap at 1000 documents — exhaustive daily search


@retry_with_backoff(max_retries=3, exceptions=(requests.RequestException,))
def fetch_documents(since_date, page=1, per_page=100):
    """Fetch documents from Federal Register API."""
    params = {
        'conditions[publication_date][gte]': since_date,
        'conditions[type][]': DOC_TYPES,
        'fields[]': [
            'document_number', 'title', 'type', 'abstract', 'publication_date',
            'agencies', 'action', 'dates', 'full_text_xml_url', 'html_url',
            'pdf_url', 'executive_order_number', 'signing_date', 'subtype',
        ],
        'per_page': per_page,
        'page': page,
        'order': 'newest',
    }
    resp = requests.get(f'{API_BASE}/documents.json', params=params, timeout=30)
    resp.raise_for_status()
    return resp.json()


class FederalRegisterConnector(BaseSourceConnector):
    source_name = 'federal_register'
    category = 'agency_actions'

    def _fetch_page(self, since_date, **kwargs):
        page = kwargs.get('page', 1)
        if page > MAX_PAGES:
            return [], False
        data = fetch_documents(since_date, page=page)
        documents = data.get('results', [])
        total_pages = data.get('total_pages', 1)
        has_more = page < total_pages and page < MAX_PAGES
        return documents, has_more

    def _parse_result(self, doc):
        return {
            'source_id': doc.get('document_number', ''),
            'title': doc.get('title', ''),
            'abstract': doc.get('abstract', ''),
            'doc_type': doc.get('type', ''),
            'subtype': doc.get('subtype', ''),
            'date': doc.get('publication_date', ''),
            'agencies': [a.get('name', '') for a in doc.get('agencies', []) if a],
            'agency_slugs': [a.get('slug', '') for a in doc.get('agencies', []) if a],
            'action': doc.get('action', ''),
            'eo_number': doc.get('executive_order_number'),
            'url': doc.get('html_url', ''),
            'pdf_url': doc.get('pdf_url', ''),
        }

    def get_category(self, doc):
        if doc.get('doc_type') == 'PRESDOCU':
            return 'executive_actions'
        return 'agency_actions'


# Backwards-compatible module-level functions
_connector = FederalRegisterConnector()
fetch_since = _connector.fetch_since
get_category = _connector.get_category
