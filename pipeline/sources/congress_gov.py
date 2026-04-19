"""Congress.gov API client — bills, resolutions, public laws."""
import requests
import logging
from ..config import CONGRESS_API_KEY
from ..utils.retry import retry_with_backoff
from .base import BaseSourceConnector

logger = logging.getLogger('tckc_pipeline')

API_BASE = 'https://api.congress.gov/v3'

# Subjects of interest
RELEVANT_SUBJECTS = [
    'Arts, Culture, Religion', 'Civil Rights and Liberties, Minority Issues',
    'Environmental Protection', 'Immigration', 'Indian, Inuit, Alaskan Native Affairs',
    'International Affairs', 'Government Operations and Politics',
    'Public Lands and Natural Resources', 'Education', 'Social Welfare',
    'Native Americans', 'Historic Preservation',
]

MAX_RESULTS = 500  # Exhaustive daily search


@retry_with_backoff(max_retries=3, exceptions=(requests.RequestException,))
def fetch_bills(since_date, offset=0, limit=100):
    """Fetch bills updated since the given date."""
    params = {
        'fromDateTime': f'{since_date}T00:00:00Z',
        'sort': 'updateDate+desc',
        'limit': limit,
        'offset': offset,
        'api_key': CONGRESS_API_KEY,
    }
    resp = requests.get(f'{API_BASE}/bill', params=params, timeout=30)
    resp.raise_for_status()
    return resp.json()


@retry_with_backoff(max_retries=3, exceptions=(requests.RequestException,))
def fetch_bill_detail(congress, bill_type, bill_number):
    """Fetch detailed info for a specific bill."""
    params = {'api_key': CONGRESS_API_KEY}
    resp = requests.get(
        f'{API_BASE}/bill/{congress}/{bill_type}/{bill_number}',
        params=params, timeout=30
    )
    resp.raise_for_status()
    return resp.json().get('bill', {})


class CongressGovConnector(BaseSourceConnector):
    source_name = 'congress_gov'
    category = 'legislation'

    def _fetch_page(self, since_date, **kwargs):
        offset = (kwargs.get('page', 1) - 1) * 100
        if offset >= MAX_RESULTS:
            return [], False
        data = fetch_bills(since_date, offset=offset)
        bills = data.get('bills', [])
        has_more = len(bills) >= 100 and (offset + 100) < MAX_RESULTS
        return bills, has_more

    def _parse_result(self, bill):
        return {
            'source_id': f"{bill.get('type', '')}{bill.get('number', '')}-{bill.get('congress', '')}",
            'title': bill.get('title', ''),
            'bill_type': bill.get('type', ''),
            'bill_number': bill.get('number', ''),
            'congress': bill.get('congress', ''),
            'date': (bill.get('updateDate') or '')[:10],
            'latest_action': (bill.get('latestAction') or {}).get('text') or '',
            'latest_action_date': (bill.get('latestAction') or {}).get('actionDate') or '',
            'url': bill.get('url', ''),
            'origin_chamber': bill.get('originChamber', ''),
        }


# Backwards-compatible module-level functions
_connector = CongressGovConnector()
fetch_since = _connector.fetch_since
get_category = _connector.get_category
