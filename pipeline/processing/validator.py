"""Schema validation for generated tracker entries."""
import re
import logging

logger = logging.getLogger('tckc_pipeline')

VALID_THREAT_LEVELS = ['SEVERE', 'HARMFUL', 'PROTECTIVE']
VALID_CATEGORIES = ['executive_orders', 'agency_actions', 'legislation', 'litigation', 'other_domestic', 'international']
VALID_ADMINISTRATIONS = ['Trump I', 'Trump II', 'Biden', 'Obama']


def validate_entry(entry, category):
    """Validate an entry against the tracker schema. Returns list of errors."""
    errors = []

    # Check ID field (legislation uses 'id', others use 'i')
    if category == 'legislation':
        if 'id' not in entry:
            errors.append('Missing required field: id')
    else:
        if 'i' not in entry:
            errors.append('Missing required field: i')

    # Required fields
    for field in ['t', 'n', 'T', 's', 'd', 'a', 'A', 'S', 'L', 'D', 'I', 'c']:
        if field not in entry:
            errors.append(f'Missing required field: {field}')

    # Threat level
    if entry.get('L') not in VALID_THREAT_LEVELS:
        errors.append(f'Invalid threat level: {entry.get("L")}')

    # Date format
    date_str = entry.get('d', '')
    if not re.match(r'^\d{4}-\d{2}-\d{2}$', date_str):
        errors.append(f'Invalid date format: {date_str} (expected YYYY-MM-DD)')

    # Administration
    if entry.get('a') not in VALID_ADMINISTRATIONS:
        errors.append(f'Invalid administration: {entry.get("a")}')

    # Agencies must be array
    if not isinstance(entry.get('A'), list):
        errors.append('A (agencies) must be an array')

    # Communities must be array
    if not isinstance(entry.get('c'), list):
        errors.append('c (communities) must be an array')

    # Impact must be object with community keys
    impact = entry.get('I')
    if isinstance(impact, dict):
        for community, data in impact.items():
            if isinstance(data, dict):
                for field in ['people', 'places', 'practices', 'treasures']:
                    if field not in data:
                        errors.append(f'Impact {community} missing 4P field: {field}')
    elif impact is not None:
        errors.append('I (impact) must be an object')

    # Description length check
    desc = entry.get('D', '')
    word_count = len(desc.split())
    if word_count < 100:
        errors.append(f'Description too short: {word_count} words (min 100)')

    # Title should have HTML color span for SEVERE/PROTECTIVE
    title = entry.get('T', '')
    if entry.get('L') == 'SEVERE' and '#991B1B' not in title:
        errors.append('SEVERE entries should have red (#991B1B) color span in title')
    if entry.get('L') == 'PROTECTIVE' and '#065F46' not in title:
        errors.append('PROTECTIVE entries should have green (#065F46) color span in title')

    if errors:
        entry_id = entry.get('i') or entry.get('id', 'unknown')
        logger.warning(f'Validation errors for {entry_id}: {errors}')

    return errors
