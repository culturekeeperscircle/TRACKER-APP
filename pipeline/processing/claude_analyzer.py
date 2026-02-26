"""Claude AI integration — 3-tier analysis pipeline."""
import json
import logging
import anthropic
from pathlib import Path
from ..config import ANTHROPIC_API_KEY, CLAUDE_SCREENING_MODEL, CLAUDE_GENERATION_MODEL, CLAUDE_VALIDATION_MODEL, PROMPTS_DIR

logger = logging.getLogger('tckc_pipeline')

client = None


def get_client():
    global client
    if client is None:
        client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
    return client


def load_prompt(name):
    """Load a prompt template from the prompts directory."""
    path = Path(PROMPTS_DIR) / f'{name}.txt'
    return path.read_text()


def screen_relevance(item, rate_limiter=None):
    """Tier 1: Screen an item for relevance using Haiku (cheap)."""
    if rate_limiter:
        rate_limiter.wait_if_needed('anthropic')

    prompt = load_prompt('relevance_screening')
    item_text = json.dumps({
        'title': item.get('title') or '',
        'abstract': item.get('abstract') or item.get('description') or '',
        'source': item.get('source') or '',
        'date': item.get('date') or '',
        'agencies': item.get('agencies') or [],
        'action': item.get('action') or item.get('latest_action') or '',
    }, indent=2)

    try:
        resp = get_client().messages.create(
            model=CLAUDE_SCREENING_MODEL,
            max_tokens=300,
            messages=[{'role': 'user', 'content': prompt.replace('{ITEM_DATA}', item_text)}],
        )
        text = resp.content[0].text.strip()
        # Extract JSON from response
        if '{' in text:
            json_str = text[text.index('{'):text.rindex('}') + 1]
            result = json.loads(json_str)
            return result
    except Exception as e:
        logger.warning(f'Relevance screening failed: {e}')
    return {'relevant': False, 'confidence': 0, 'category': '', 'brief_reason': 'screening error'}


def generate_entry(item, category, existing_examples, rate_limiter=None):
    """Tier 2: Generate a full tracker entry using Sonnet (detailed)."""
    if rate_limiter:
        rate_limiter.wait_if_needed('anthropic')

    prompt = load_prompt('entry_generation')
    item_text = json.dumps(item, indent=2, default=str)

    # Include 2 existing examples for few-shot learning
    examples_text = ''
    if existing_examples:
        examples_text = '\n\nEXISTING ENTRY EXAMPLES (match this style):\n'
        for ex in existing_examples[:2]:
            examples_text += json.dumps(ex, indent=2, ensure_ascii=False)[:3000] + '\n---\n'

    full_prompt = prompt.replace('{ITEM_DATA}', item_text).replace(
        '{CATEGORY}', category
    ).replace('{EXAMPLES}', examples_text)

    try:
        resp = get_client().messages.create(
            model=CLAUDE_GENERATION_MODEL,
            max_tokens=6000,
            messages=[{'role': 'user', 'content': full_prompt}],
        )
        text = resp.content[0].text.strip()
        if '{' in text:
            json_str = text[text.index('{'):text.rindex('}') + 1]
            entry = json.loads(json_str)
            logger.info(f'Generated entry: {entry.get("i", entry.get("id", "unknown"))}')
            return entry
    except Exception as e:
        logger.error(f'Entry generation failed: {e}')
    return None


def validate_entry(entry, rate_limiter=None):
    """Tier 3: Quality check using Haiku (cheap)."""
    if rate_limiter:
        rate_limiter.wait_if_needed('anthropic')

    prompt = load_prompt('quality_check')
    entry_text = json.dumps(entry, indent=2, ensure_ascii=False)

    try:
        resp = get_client().messages.create(
            model=CLAUDE_VALIDATION_MODEL,
            max_tokens=500,
            messages=[{'role': 'user', 'content': prompt.replace('{ENTRY_DATA}', entry_text)}],
        )
        text = resp.content[0].text.strip()
        if '{' in text:
            json_str = text[text.index('{'):text.rindex('}') + 1]
            result = json.loads(json_str)
            return result
    except Exception as e:
        logger.warning(f'Validation failed: {e}')
    return {'valid': True, 'issues': []}
