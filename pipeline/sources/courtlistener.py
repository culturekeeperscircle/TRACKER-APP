"""CourtListener API client — federal litigation, court opinions."""
import requests
import logging
from ..config import COURTLISTENER_TOKEN
from ..utils.retry import retry_with_backoff
from .base import MultiQuerySourceConnector

logger = logging.getLogger('tckc_pipeline')

API_BASE = 'https://www.courtlistener.com/api/rest/v4'


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


class CourtListenerConnector(MultiQuerySourceConnector):
    source_name = 'courtlistener'
    category = 'litigation'
    max_per_query = 20

    search_queries = [
        'cultural resources historic preservation heritage',
        'tribal sovereignty sacred sites NAGPRA indigenous',
        'national monument Antiquities Act preservation',
        'environmental justice civil rights Title VI discrimination',
        'immigration deportation asylum TPS DACA refugee',
        'NEA NEH arts funding Smithsonian IMLS',
        'treaty rights Native American tribal consultation',
        'African American civil rights racial equity HBCU',
        'Latino Hispanic farmworker immigrant community',
        'Asian American Pacific Islander AAPI hate crime',
        'cultural practice traditional knowledge language preservation',
        'museum library school university cultural programming education',
        'foodways folk arts cultural arts celebration parade festival',
    ]

    def _search(self, query, since_date):
        data = search_opinions(query, since_date)
        return data.get('results', [])

    def _get_id(self, raw):
        return str(raw.get('id', ''))

    def _parse_result(self, result):
        return {
            'source_id': str(result.get('id', '')),
            'title': result.get('caseName', ''),
            'court': result.get('court', ''),
            'date': (result.get('dateFiled') or '')[:10],
            'docket_number': result.get('docketNumber', ''),
            'snippet': result.get('snippet', ''),
            'citation': result.get('citation', []),
            'url': f"https://www.courtlistener.com{result.get('absolute_url', '')}",
            'status': result.get('status', ''),
        }


# Backwards-compatible module-level functions
_connector = CourtListenerConnector()
fetch_since = _connector.fetch_since
get_category = _connector.get_category
