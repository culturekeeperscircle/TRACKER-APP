"""News API client — breaking news coverage of cultural resource issues."""
import requests
import logging
from ..config import NEWS_API_KEY
from ..utils.retry import retry_with_backoff

logger = logging.getLogger('tckc_pipeline')

API_BASE = 'https://newsapi.org/v2'

# Search queries targeting cultural resource news
SEARCH_QUERIES = [
    '"cultural resources" OR "historic preservation" OR "national monument"',
    'tribal sovereignty OR "sacred sites" OR NAGPRA',
    '"environmental justice" OR "civil rights" executive order',
    'NEA OR NEH OR Smithsonian funding cuts',
    'immigration policy deportation "cultural impact"',
]


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


def fetch_since(since_date, rate_limiter=None):
    """Fetch relevant news articles since the given date."""
    results = []
    seen_urls = set()

    for query in SEARCH_QUERIES:
        if rate_limiter:
            rate_limiter.wait_if_needed('news_api')

        try:
            data = search_articles(query, since_date)
            for article in data.get('articles', [])[:10]:  # Limit per query
                url = article.get('url', '')
                if url in seen_urls:
                    continue
                seen_urls.add(url)

                results.append({
                    'source': 'news_api',
                    'source_id': url,
                    'title': article.get('title', ''),
                    'description': article.get('description', ''),
                    'content': article.get('content', ''),
                    'date': (article.get('publishedAt', '') or '')[:10],
                    'source_name': article.get('source', {}).get('name', ''),
                    'url': url,
                    'author': article.get('author', ''),
                })
        except Exception as e:
            logger.warning(f'NewsAPI query failed: {e}')
            continue

    logger.info(f'NewsAPI: fetched {len(results)} articles since {since_date}')
    return results


def get_category(doc):
    """Category determined by Claude during analysis."""
    return None  # AI determines this
