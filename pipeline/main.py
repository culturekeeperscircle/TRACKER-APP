"""TCKC Threat Tracker — Autonomous Daily Update Pipeline.

Fetches from Federal Register, Congress.gov, CourtListener, and News APIs.
Uses Claude AI to screen relevance, generate entries, and validate quality.
Updates data/data.json and commits changes for GitHub Pages deployment.
"""
import json
import sys
from datetime import date, timedelta
from pathlib import Path

from .config import LOOKBACK_DAYS, DRY_RUN, SOURCE_FILTER, ANTHROPIC_API_KEY
from .utils.logger import setup_logger
from .utils.rate_limiter import RateLimiter
from .sources import federal_register, congress_gov, courtlistener, news_api
from .processing.relevance_filter import filter_items
from .processing.claude_analyzer import screen_relevance, generate_entry, validate_entry
from .processing.deduplicator import deduplicate
from .processing.validator import validate_entry as schema_validate
from .data.data_manager import (
    load_data, save_data, get_all_entries, add_entries,
    update_meta, update_last_api_pull, get_examples_for_category,
)

logger = setup_logger()

STATE_PATH = Path(__file__).parent.parent / 'data' / 'state.json'

SOURCES = {
    'federal_register': federal_register,
    'congress': congress_gov,
    'courtlistener': courtlistener,
    'news': news_api,
}


def load_state():
    if STATE_PATH.exists():
        return json.loads(STATE_PATH.read_text())
    return {
        'last_successful_run': None,
        'last_run_new_entries': 0,
        'sources': {},
        'processed_ids': {},
        'cumulative_stats': {'total_runs': 0, 'total_entries_added': 0},
    }


def save_state(state):
    STATE_PATH.write_text(json.dumps(state, indent=2))


def run():
    logger.info('=' * 60)
    logger.info('TCKC Threat Tracker — Daily Update Pipeline')
    logger.info(f'DRY_RUN={DRY_RUN}, LOOKBACK_DAYS={LOOKBACK_DAYS}, SOURCE_FILTER={SOURCE_FILTER}')
    logger.info('=' * 60)

    if not ANTHROPIC_API_KEY:
        logger.error('ANTHROPIC_API_KEY not set. Aborting.')
        sys.exit(1)

    rate_limiter = RateLimiter()
    state = load_state()

    # Determine since_date: use last successful run if available, else fall back
    if LOOKBACK_DAYS > 0:
        # Manual override via env var
        since_date = (date.today() - timedelta(days=LOOKBACK_DAYS)).isoformat()
        logger.info(f'Using manual lookback: {LOOKBACK_DAYS} days → since {since_date}')
    elif state.get('last_successful_run'):
        # Exhaustive: search only since last successful run
        since_date = state['last_successful_run']
        logger.info(f'Searching since last successful run: {since_date}')
    else:
        # First run ever — look back 7 days
        since_date = (date.today() - timedelta(days=7)).isoformat()
        logger.info(f'First run, defaulting to 7-day lookback: {since_date}')
    logger.info(f'Fetching items since {since_date}')

    # Load existing data for dedup
    data = load_data()
    existing_entries = get_all_entries(data)
    logger.info(f'Existing entries: {len(existing_entries)}')

    # ── Phase 1: Fetch from all sources ──
    all_raw_items = []
    for source_name, source_module in SOURCES.items():
        if SOURCE_FILTER != 'all' and SOURCE_FILTER != source_name:
            continue

        logger.info(f'--- Fetching from {source_name} ---')
        try:
            items = source_module.fetch_since(since_date, rate_limiter=rate_limiter)
            all_raw_items.extend(items)
            state['sources'][source_name] = {
                'last_fetched_date': since_date,
                'items_fetched': len(items),
                'status': 'success',
            }
        except Exception as e:
            logger.error(f'{source_name} fetch failed: {e}')
            state['sources'][source_name] = {
                'last_fetched_date': since_date,
                'items_fetched': 0,
                'status': f'error: {e}',
            }

    logger.info(f'Total raw items fetched: {len(all_raw_items)}')

    if not all_raw_items:
        logger.info('No items fetched. Nothing to process.')
        state['last_successful_run'] = date.today().isoformat()
        state['last_run_new_entries'] = 0
        save_state(state)
        return

    # ── Phase 2: Keyword pre-filter ──
    filtered_items = filter_items(all_raw_items)

    # Remove already-processed items
    processed_ids = set()
    for ids in state.get('processed_ids', {}).values():
        processed_ids.update(ids)

    filtered_items = [
        item for item in filtered_items
        if item.get('source_id', '') not in processed_ids
    ]
    logger.info(f'After dedup against processed IDs: {len(filtered_items)} items')

    # ── Phase 3: Claude relevance screening (Tier 1) ──
    relevant_items = []
    for item in filtered_items:
        result = screen_relevance(item, rate_limiter=rate_limiter)
        if result.get('relevant') and result.get('confidence', 0) >= 0.6:
            item['_ai_category'] = result.get('category', '')
            item['_ai_threat'] = result.get('threat_level', '')
            item['_ai_reason'] = result.get('brief_reason', '')
            relevant_items.append(item)
            logger.info(f'  Relevant: {item.get("title", "")[:80]}... [{result.get("category")}]')
        else:
            logger.info(f'  Filtered: {item.get("title", "")[:80]}...')

    logger.info(f'AI-relevant items: {len(relevant_items)}')

    # Cap to prevent timeout — process highest-confidence items first
    MAX_ENTRIES_PER_RUN = 25
    if len(relevant_items) > MAX_ENTRIES_PER_RUN:
        relevant_items.sort(key=lambda x: x.get('_ai_threat', ''), reverse=True)
        logger.warning(f'Capping entry generation at {MAX_ENTRIES_PER_RUN} items (had {len(relevant_items)})')
        relevant_items = relevant_items[:MAX_ENTRIES_PER_RUN]

    # ── Phase 4: Generate full entries (Tier 2) ──
    new_entries_by_category = {}
    for item in relevant_items:
        source_module = SOURCES.get(item.get('source', '').replace('_api', '').replace('_gov', ''), None)
        category = item.get('_ai_category', '')

        # Fall back to source-default category
        if not category and source_module:
            category = source_module.get_category(item) or 'agency_actions'
        if not category:
            category = 'agency_actions'

        # Get examples for few-shot prompting
        examples = get_examples_for_category(data, category, item.get('_ai_threat'), count=2)

        entry = generate_entry(item, category, examples, rate_limiter=rate_limiter)
        if entry is None:
            logger.warning(f'Entry generation failed for: {item.get("title", "")[:60]}')
            continue

        # Schema validation
        errors = schema_validate(entry, category)
        if errors:
            logger.warning(f'Schema errors, attempting AI fix: {errors}')
            # Try AI quality check to fix issues
            ai_check = validate_entry(entry, rate_limiter=rate_limiter)
            if ai_check.get('severity') == 'major':
                logger.error(f'Entry rejected by quality check: {ai_check.get("issues")}')
                continue

        if category not in new_entries_by_category:
            new_entries_by_category[category] = []
        new_entries_by_category[category].append(entry)

    # ── Phase 5: Deduplicate against existing data ──
    total_new = 0
    for category, entries in new_entries_by_category.items():
        unique = deduplicate(entries, existing_entries)
        if unique:
            if not DRY_RUN:
                add_entries(data, category, unique)
            total_new += len(unique)
            logger.info(f'{category}: {len(unique)} new entries')
            for e in unique:
                eid = e.get('i') or e.get('id', '?')
                logger.info(f'  + {eid}: {e.get("s", "")}')

    # ── Phase 6: Save results ──
    if total_new > 0 and not DRY_RUN:
        update_meta(data)
        save_data(data)
        update_last_api_pull(date.today().isoformat())
        logger.info(f'Saved {total_new} new entries to data.json')
    elif DRY_RUN and total_new > 0:
        logger.info(f'DRY RUN: Would have added {total_new} entries')
    else:
        logger.info('No new entries to add.')

    # Update state
    state['last_successful_run'] = date.today().isoformat()
    state['last_run_new_entries'] = total_new
    stats = state.get('cumulative_stats', {})
    stats['total_runs'] = stats.get('total_runs', 0) + 1
    stats['total_entries_added'] = stats.get('total_entries_added', 0) + total_new
    state['cumulative_stats'] = stats

    # Track processed IDs
    for item in all_raw_items:
        src = item.get('source', '')
        if src not in state.get('processed_ids', {}):
            state['processed_ids'][src] = []
        sid = item.get('source_id', '')
        if sid and sid not in state['processed_ids'][src]:
            state['processed_ids'][src].append(sid)
        # Keep only last 1000 IDs per source
        state['processed_ids'][src] = state['processed_ids'][src][-1000:]

    save_state(state)
    logger.info(f'Pipeline complete. {total_new} new entries added.')
    logger.info('=' * 60)


if __name__ == '__main__':
    run()
