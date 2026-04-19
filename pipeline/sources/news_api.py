"""News API client — breaking news coverage of cultural resource issues."""
import requests
import logging
from ..config import NEWS_API_KEY
from ..utils.retry import retry_with_backoff
from .base import MultiQuerySourceConnector

logger = logging.getLogger('tckc_pipeline')

API_BASE = 'https://newsapi.org/v2'


@retry_with_backoff(max_retries=3, exceptions=(requests.RequestException,))
def search_articles(query, from_date, page=1, page_size=50):
    """Search news articles."""
    params = {
        'q': query,
        'from': from_date,
        'sortBy': 'publishedAt',
        'language': 'en',
        'page': page,
        'pageSize': page_size,
        'apiKey': NEWS_API_KEY,
    }
    resp = requests.get(f'{API_BASE}/everything', params=params, timeout=30)
    resp.raise_for_status()
    return resp.json()


class NewsAPIConnector(MultiQuerySourceConnector):
    source_name = 'news_api'
    category = None  # AI determines category during analysis
    max_per_query = 20

    search_queries = [
        '"cultural resources" OR "historic preservation" OR "cultural heritage" OR "national monument"',
        '"tribal sovereignty" OR "sacred sites" OR NAGPRA OR "indigenous rights" OR "Native American"',
        '"environmental justice" OR "civil rights" OR "racial equity" OR "Title VI" OR discrimination',
        'NEA OR NEH OR Smithsonian OR IMLS OR "arts funding" OR "cultural institution"',
        'immigration OR deportation OR "refugee policy" OR DACA OR TPS OR asylum',
        '"African American" OR "Black community" OR HBCU OR "racial justice" OR reparations',
        '"Latino" OR "Hispanic" OR "farmworker" OR "immigrant community" OR Latinx',
        '"Asian American" OR "Pacific Islander" OR AAPI OR "hate crime" OR "anti-Asian"',
        '"cultural practice" OR "language preservation" OR "traditional knowledge" OR "folk art"',
        'foodways OR "folk arts" OR "cultural arts" OR parade OR "cultural festival" OR celebration',
        'museum OR library OR university OR school OR "cultural programming" OR "cultural center"',
    ]

    def _search(self, query, since_date):
        data = search_articles(query, since_date)
        return data.get('articles', [])

    def _get_id(self, raw):
        return raw.get('url', '')

    def _parse_result(self, article):
        return {
            'source_id': article.get('url', ''),
            'title': article.get('title', ''),
            'description': article.get('description', ''),
            'content': article.get('content', ''),
            'date': (article.get('publishedAt', '') or '')[:10],
            'source_name': article.get('source', {}).get('name', ''),
            'url': article.get('url', ''),
            'author': article.get('author', ''),
        }


# Backwards-compatible module-level functions
_connector = NewsAPIConnector()
fetch_since = _connector.fetch_since
get_category = _connector.get_category
