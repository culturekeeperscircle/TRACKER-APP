"""Congress.gov API client — bills, resolutions, public laws."""
import requests
import logging
from ..config import CONGRESS_API_KEY
from ..utils.retry import retry_with_backoff

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


def fetch_since(since_date, rate_limiter=None):
    """Fetch all relevant bills since the given date."""
    results = []
    offset = 0

    while True:
        if rate_limiter:
            rate_limiter.wait_if_needed('congress_gov')

        data = fetch_bills(since_date, offset=offset)
        bills = data.get('bills', [])

        if not bills:
            break

        for bill in bills:
            results.append({
                'source': 'congress_gov',
                'source_id': f"{bill.get('type', '')}{bill.get('number', '')}-{bill.get('congress', '')}",
                'title': bill.get('title', ''),
                'bill_type': bill.get('type', ''),
                'bill_number': bill.get('number', ''),
                'congress': bill.get('congress', ''),
                'date': bill.get('updateDate', '')[:10],
                'latest_action': bill.get('latestAction', {}).get('text', ''),
                'latest_action_date': bill.get('latestAction', {}).get('actionDate', ''),
                'url': bill.get('url', ''),
                'origin_chamber': bill.get('originChamber', ''),
            })

        if len(bills) < 100:
            break
        offset += 100

    logger.info(f'Congress.gov: fetched {len(results)} bills since {since_date}')
    return results


def get_category(doc):
    return 'legislation'
