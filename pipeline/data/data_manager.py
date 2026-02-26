"""Read/write data.json and update index.html."""
import json
import re
import logging
from pathlib import Path
from ..config import DATA_JSON_PATH, INDEX_HTML_PATH

logger = logging.getLogger('tckc_pipeline')

CATEGORIES = ['executive_orders', 'agency_actions', 'legislation', 'litigation', 'other_domestic', 'international']


def load_data():
    """Load and parse data.json."""
    path = Path(DATA_JSON_PATH)
    with open(path, 'r') as f:
        return json.load(f)


def save_data(data):
    """Write updated data.json."""
    path = Path(DATA_JSON_PATH)
    with open(path, 'w') as f:
        json.dump(data, f, ensure_ascii=False, separators=(',', ':'))
    size = path.stat().st_size
    logger.info(f'Saved data.json: {size:,} bytes')


def get_all_entries(data):
    """Get a flat list of all entries across all categories."""
    entries = []
    for cat in CATEGORIES:
        entries.extend(data.get(cat, []))
    return entries


def add_entries(data, category, new_entries):
    """Add new entries to the appropriate category, sorted by date descending."""
    if category not in data:
        data[category] = []

    data[category].extend(new_entries)

    # Sort by date descending
    data[category].sort(key=lambda x: x.get('d', ''), reverse=True)

    logger.info(f'Added {len(new_entries)} entries to {category}')


def update_meta(data):
    """Recalculate meta counts."""
    total = sum(len(data.get(c, [])) for c in CATEGORIES)
    data['meta'] = {
        'total': total,
        'by_category': {c: len(data.get(c, [])) for c in CATEGORIES},
        '_crossRefCount': data.get('meta', {}).get('_crossRefCount', 30),
        '_note': data.get('meta', {}).get('_note', ''),
    }
    logger.info(f'Updated meta: {total} total entries')


def update_last_api_pull(date_str):
    """Update LAST_API_PULL constant in index.html."""
    path = Path(INDEX_HTML_PATH)
    content = path.read_text()
    new_content = re.sub(
        r'const LAST_API_PULL = "[^"]*"',
        f'const LAST_API_PULL = "{date_str}"',
        content
    )
    path.write_text(new_content)
    logger.info(f'Updated LAST_API_PULL to {date_str}')


def get_examples_for_category(data, category, threat_level=None, count=2):
    """Get example entries from a category for few-shot prompting."""
    entries = data.get(category, [])
    if threat_level:
        entries = [e for e in entries if e.get('L') == threat_level]
    return entries[:count]
