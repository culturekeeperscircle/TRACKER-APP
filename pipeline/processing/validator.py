"""Schema validation for generated tracker entries."""
import re
import logging

logger = logging.getLogger('tckc_pipeline')

VALID_THREAT_LEVELS = ['SEVERE', 'HARMFUL', 'PROTECTIVE']
VALID_CATEGORIES = ['executive_actions', 'agency_actions', 'legislation', 'litigation', 'other_domestic', 'international']
VALID_ADMINISTRATIONS = ['Trump I', 'Trump II', 'Biden', 'Obama']

# Fingerprint sentences from a prior enrichment leak (see 2026-04-19 audit
# and scripts/clean_boilerplate.py). Any new entry containing these is
# rejected unless its topic legitimately matches.
BOILERPLATE_FINGERPRINTS = {
    'immigration': {
        'marker': 'Migration Policy Institute, approximately 11 million undocumented',
        'topic_agencies': {'DHS', 'ICE', 'CBP', 'USCIS', 'EOIR', 'DOS'},
        'topic_keywords': [
            'immigra', 'deport', 'undocument', 'asylum', 'refugee', 'daca',
            'tps', 'visa', 'border', 'sanctuary', 'naturalization',
            'citizenship', 'travel ban', 'alien',
        ],
    },
    'congress-gov-procedure': {
        'marker': 'tracked via Congress.gov. The bill has been referred to the relevant committee',
        'topic_origins': {None},  # only allowed for non-state federal entries
        'topic_keywords': [],
    },
}


def _check_boilerplate_leak(entry):
    """Detect leaked boilerplate that doesn't match the entry's topic."""
    errors = []
    desc = entry.get('D') or ''
    if not desc:
        return errors

    agencies = {str(a).upper() for a in (entry.get('A') or [])}
    origin = entry.get('_origin')
    blob = (
        (entry.get('T') or '') + ' ' +
        (entry.get('s') or '') + ' ' +
        (entry.get('n') or '')
    ).lower()
    communities_blob = ' '.join(
        str(c).lower() for c in (entry.get('c') or [])
    )

    for name, spec in BOILERPLATE_FINGERPRINTS.items():
        if spec['marker'] not in desc:
            continue
        on_topic = False
        if name == 'immigration':
            if agencies & spec['topic_agencies']:
                on_topic = True
            elif 'immigrant' in communities_blob:
                on_topic = True
            elif any(kw in blob for kw in spec['topic_keywords']):
                on_topic = True
        elif name == 'congress-gov-procedure':
            # Procedural language only valid for federal-origin legislation
            # without an "xxx" placeholder ID.
            eid = entry.get('i') or entry.get('id') or ''
            on_topic = (origin != 'state') and ('xxx' not in eid.lower())
        if not on_topic:
            errors.append(
                f'Boilerplate leak detected ({name}): description contains '
                f'"{spec["marker"]}" but entry topic does not match'
            )
    return errors


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

    # Title should have HTML color span for all threat levels
    title = entry.get('T', '')
    if entry.get('L') == 'SEVERE' and '#991B1B' not in title:
        errors.append('SEVERE entries should have red (#991B1B) color span in title')
    if entry.get('L') == 'HARMFUL' and '#CA8A04' not in title:
        errors.append('HARMFUL entries should have amber (#CA8A04) color span in title')
    if entry.get('L') == 'PROTECTIVE' and '#065F46' not in title:
        errors.append('PROTECTIVE entries should have green (#065F46) color span in title')

    # Source URL should be present
    if not entry.get('U'):
        errors.append('Missing source URL field: U')

    # Topic-mismatched boilerplate leakage
    errors.extend(_check_boilerplate_leak(entry))

    if errors:
        entry_id = entry.get('i') or entry.get('id', 'unknown')
        logger.warning(f'Validation errors for {entry_id}: {errors}')

    return errors
