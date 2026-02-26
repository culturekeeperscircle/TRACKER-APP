"""Multi-strategy deduplication against existing entries."""
import logging
import re

logger = logging.getLogger('tckc_pipeline')


def strip_html(text):
    """Remove HTML tags from a string."""
    return re.sub(r'<[^>]+>', '', text or '')


def normalize(text):
    """Normalize text for comparison."""
    return re.sub(r'\s+', ' ', strip_html(text or '')).strip().lower()


def levenshtein_ratio(s1, s2):
    """Simple similarity ratio between two strings."""
    if not s1 or not s2:
        return 0.0
    # Use length-based quick check first
    if abs(len(s1) - len(s2)) / max(len(s1), len(s2)) > 0.5:
        return 0.0
    # Simple character overlap ratio
    s1_set = set(s1.lower().split())
    s2_set = set(s2.lower().split())
    if not s1_set or not s2_set:
        return 0.0
    intersection = s1_set & s2_set
    union = s1_set | s2_set
    return len(intersection) / len(union)


def is_duplicate(new_entry, existing_entries, threshold=0.85):
    """Check if a new entry is a duplicate of any existing entry."""
    new_id = new_entry.get('i') or new_entry.get('id', '')
    new_n = new_entry.get('n', '')
    new_title = normalize(new_entry.get('T', ''))

    for existing in existing_entries:
        existing_id = existing.get('i') or existing.get('id', '')

        # Strategy 1: Exact ID match
        if new_id and new_id == existing_id:
            return True, 'exact_id_match'

        # Strategy 2: Document number match
        existing_n = existing.get('n', '')
        if new_n and existing_n and new_n.strip() == existing_n.strip():
            return True, 'document_number_match'

        # Strategy 3: Title similarity
        existing_title = normalize(existing.get('T', ''))
        if new_title and existing_title:
            ratio = levenshtein_ratio(new_title, existing_title)
            if ratio >= threshold:
                return True, f'title_similarity ({ratio:.2f})'

    return False, None


def deduplicate(new_entries, existing_entries):
    """Filter out duplicates from a list of new entries."""
    unique = []
    for entry in new_entries:
        is_dup, reason = is_duplicate(entry, existing_entries)
        if is_dup:
            entry_id = entry.get('i') or entry.get('id', 'unknown')
            logger.info(f'Duplicate skipped: {entry_id} ({reason})')
        else:
            unique.append(entry)

    logger.info(f'Dedup: {len(unique)}/{len(new_entries)} entries are new')
    return unique
