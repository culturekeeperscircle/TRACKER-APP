"""Fast keyword-based pre-filter to reduce Claude API calls."""
import logging
import os
from ..config import RELEVANCE_KEYWORDS, TRACKED_BILLS

logger = logging.getLogger('tckc_pipeline')

# Max items to send to Claude screening (prevents timeout)
MAX_SCREENING_ITEMS = int(os.environ.get('MAX_SCREENING_ITEMS', 150))

# Normalize tracked bill IDs for matching
_TRACKED_IDS = {bid.upper() for bid in TRACKED_BILLS}


def is_tracked_bill(item):
    """Check if this item matches a specifically tracked bill number."""
    source_id = (item.get('source_id') or '').upper()
    return source_id in _TRACKED_IDS


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
    tracked = []
    scored = []

    for item in items:
        # Tracked bills always pass with highest priority
        if is_tracked_bill(item):
            item['_keyword_score'] = 999
            tracked.append(item)
            continue

        score = keyword_score(item)
        if score > 0:
            item['_keyword_score'] = score
            scored.append(item)

    logger.info(f'Pre-filter: {len(tracked)} tracked bills, {len(scored)}/{len(items)} keyword matches')

    # Sort by keyword score (most relevant first) and cap
    scored.sort(key=lambda x: x.get('_keyword_score', 0), reverse=True)

    # Tracked bills always included; remaining slots filled by keyword score
    remaining_slots = max(0, MAX_SCREENING_ITEMS - len(tracked))
    if len(scored) > remaining_slots:
        logger.warning(
            f'Capping screening at {MAX_SCREENING_ITEMS} items (had {len(tracked) + len(scored)}). '
            f'Top score: {scored[0].get("_keyword_score", 0)}, '
            f'cutoff score: {scored[remaining_slots - 1].get("_keyword_score", 0)}'
        )
        scored = scored[:remaining_slots]

    return tracked + scored
