"""Fast keyword-based pre-filter to reduce Claude API calls."""
import logging
from ..config import RELEVANCE_KEYWORDS

logger = logging.getLogger('tckc_pipeline')


def is_potentially_relevant(item):
    """Check if an item contains any relevance keywords. Fast, cheap pre-filter."""
    searchable = ' '.join([
        item.get('title', ''),
        item.get('abstract', ''),
        item.get('description', ''),
        item.get('snippet', ''),
        item.get('content', ''),
        item.get('action', ''),
        item.get('latest_action', ''),
    ]).lower()

    for keyword in RELEVANCE_KEYWORDS:
        if keyword.lower() in searchable:
            return True
    return False


def filter_items(items):
    """Filter a list of items, keeping only potentially relevant ones."""
    relevant = [item for item in items if is_potentially_relevant(item)]
    logger.info(f'Pre-filter: {len(relevant)}/{len(items)} items passed keyword check')
    return relevant
