"""Federal Register API client — executive actions, agency rules, notices.

Fetches ALL agencies (no agency filter) to ensure exhaustive coverage of
actions affecting ethnic communities and cultural heritage/practice.
"""
import requests
import logging
from datetime import date, timedelta
from ..utils.retry import retry_with_backoff

logger = logging.getLogger('tckc_pipeline')

API_BASE = 'https://www.federalregister.gov/api/v1'

# Document types we care about — all actionable federal documents
DOC_TYPES = ['PRESDOCU', 'RULE', 'PRORULE', 'NOTICE']


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


MAX_PAGES = 10  # Cap at 1000 documents — exhaustive daily search


def fetch_since(since_date, rate_limiter=None):
    """Fetch ALL documents since the given date (exhaustive, all agencies)."""
    results = []
    page = 1

    while page <= MAX_PAGES:
        if rate_limiter:
            rate_limiter.wait_if_needed('federal_register')

        data = fetch_documents(since_date, page=page)
        documents = data.get('results', [])

        if not documents:
            break

        for doc in documents:
            results.append({
                'source': 'federal_register',
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
            })

        total_pages = data.get('total_pages', 1)
        if page >= total_pages:
            break
        page += 1

    if page > MAX_PAGES:
        logger.warning(f'Federal Register: hit {MAX_PAGES}-page cap, some documents may be skipped')
    logger.info(f'Federal Register: fetched {len(results)} documents since {since_date}')
    return results


def get_category(doc):
    """Map a Federal Register document to a tracker category."""
    if doc.get('doc_type') == 'PRESDOCU':
        return 'executive_actions'
    return 'agency_actions'
