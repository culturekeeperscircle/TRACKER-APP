"""Fast keyword-based pre-filter to reduce Claude API calls."""
import logging
from ..config import RELEVANCE_KEYWORDS

logger = logging.getLogger('tckc_pipeline')

# Max items to send to Claude screening (prevents timeout)
MAX_SCREENING_ITEMS = 150


def keyword_score(item):
    """Count how many relevance keywords appear in the item. Higher = more likely relevant."""
    searchable = ' '.join([
        item.get('title') or '',
        item.get('abstract') or '',
        item.get('description') or '',
        item.get('snippet') or '',
        item.get('content') or '',
        item.get('action') or '',
        item.get('latest_action') or '',
    ]).lower()

    score = 0
    for keyword in RELEVANCE_KEYWORDS:
        if keyword.lower() in searchable:
            score += 1
    return score


def filter_items(items):
    """Filter items by keyword relevance, capped to prevent Claude API timeout."""
    # Score all items by keyword density
    scored = []
    for item in items:
        score = keyword_score(item)
        if score > 0:
            item['_keyword_score'] = score
            scored.append(item)

    logger.info(f'Pre-filter: {len(scored)}/{len(items)} items matched at least 1 keyword')

    # Sort by keyword score (most relevant first) and cap
    scored.sort(key=lambda x: x.get('_keyword_score', 0), reverse=True)

    if len(scored) > MAX_SCREENING_ITEMS:
        logger.warning(
            f'Capping screening at {MAX_SCREENING_ITEMS} items (had {len(scored)}). '
            f'Top score: {scored[0].get("_keyword_score", 0)}, '
            f'cutoff score: {scored[MAX_SCREENING_ITEMS - 1].get("_keyword_score", 0)}'
        )
        scored = scored[:MAX_SCREENING_ITEMS]

    return scored
