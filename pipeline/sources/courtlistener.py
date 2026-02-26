"""CourtListener API client — federal litigation, court opinions."""
import requests
import logging
from ..config import COURTLISTENER_TOKEN
from ..utils.retry import retry_with_backoff

logger = logging.getLogger('tckc_pipeline')

API_BASE = 'https://www.courtlistener.com/api/rest/v4'

# Search queries for cultural resource litigation
SEARCH_QUERIES = [
    'cultural resources historic preservation',
    'tribal sovereignty sacred sites NAGPRA',
    'national monument executive order',
    'environmental justice civil rights Title VI',
    'immigration deportation asylum TPS DACA',
    'NEA NEH arts funding Smithsonian',
    'treaty rights indigenous',
]


@retry_with_backoff(max_retries=3, exceptions=(requests.RequestException,))
def search_opinions(query, filed_after, page=1):
    """Search court opinions."""
    headers = {'Authorization': f'Token {COURTLISTENER_TOKEN}'} if COURTLISTENER_TOKEN else {}
    params = {
        'q': query,
        'filed_after': filed_after,
        'order_by': 'dateFiled desc',
        'type': 'o',  # opinions
        'page': page,
    }
    resp = requests.get(f'{API_BASE}/search/', params=params, headers=headers, timeout=30)
    resp.raise_for_status()
    return resp.json()


def fetch_since(since_date, rate_limiter=None):
    """Fetch relevant court opinions since the given date."""
    results = []
    seen_ids = set()

    for query in SEARCH_QUERIES:
        if rate_limiter:
            rate_limiter.wait_if_needed('courtlistener')

        try:
            data = search_opinions(query, since_date)
            for result in data.get('results', [])[:20]:  # Limit per query
                case_id = str(result.get('id', ''))
                if case_id in seen_ids:
                    continue
                seen_ids.add(case_id)

                results.append({
                    'source': 'courtlistener',
                    'source_id': case_id,
                    'title': result.get('caseName', ''),
                    'court': result.get('court', ''),
                    'date': result.get('dateFiled', '')[:10],
                    'docket_number': result.get('docketNumber', ''),
                    'snippet': result.get('snippet', ''),
                    'citation': result.get('citation', []),
                    'url': f"https://www.courtlistener.com{result.get('absolute_url', '')}",
                    'status': result.get('status', ''),
                })
        except Exception as e:
            logger.warning(f'CourtListener query "{query}" failed: {e}')
            continue

    logger.info(f'CourtListener: fetched {len(results)} opinions since {since_date}')
    return results


def get_category(doc):
    return 'litigation'
