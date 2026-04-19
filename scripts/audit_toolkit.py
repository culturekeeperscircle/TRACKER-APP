#!/usr/bin/env python3
"""
TCKC Threat Tracker — Unified Audit Toolkit
============================================
Consolidates the functionality of five former one-off audit scripts:
  - audit jan mar 2025.py   → --period 2025-01 2025-03
  - audit apr jun 2025.py   → --period 2025-04 2025-06
  - analyze entries.py      → --word-counts --since 2025-10
  - analyze word counts.py  → --word-counts
  - audit impact wordcounts → --word-counts --period 2025-07 2025-09

Usage:
    python audit_toolkit.py --word-counts                          # All entries
    python audit_toolkit.py --word-counts --period 2025-01 2025-03 # Date range
    python audit_toolkit.py --word-counts --since 2025-10          # Since date
    python audit_toolkit.py --structure                            # Malformed/nesting
    python audit_toolkit.py --full --period 2025-04 2025-06        # Full audit
    python audit_toolkit.py --summary                              # Quick summary
"""

import json
import re
import sys
import argparse
from pathlib import Path
from collections import defaultdict

TRACKER_DIR = Path(__file__).parent.parent
DATA_FILE = TRACKER_DIR / "data" / "data.json"

IMPACT_FIELDS = {'people', 'places', 'practices', 'treasures'}
MIN_WORDS = 250
CATEGORIES = ['executive_actions', 'legislation', 'litigation',
              'agency_actions', 'international']


def load_data():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)


def count_words(text):
    if not text or not isinstance(text, str):
        return 0
    text = re.sub(r'<[^>]+>', '', text)
    return len(text.split())


def strip_html(text):
    if not text:
        return ""
    return re.sub(r'<[^>]+>', '', text)


def is_community_object(obj):
    if not isinstance(obj, dict):
        return False
    return bool(IMPACT_FIELDS & set(obj.keys()))


def in_date_range(date_str, start=None, end=None, since=None):
    """Check if a date falls in the specified range."""
    if not date_str:
        return False
    if since:
        return date_str >= since
    if start and end:
        return date_str[:7] >= start and date_str[:7] <= end
    return True  # no filter = all entries


def analyze_impact(impact_obj):
    """Analyze an I object for structure and word counts.
    Returns (communities, malformed, nested) tuples."""
    communities = []  # (path, name, field_counts, total)
    malformed = []    # (field_name,) for top-level PPPT fields
    nested = []       # (outer_path, inner_name)

    if not isinstance(impact_obj, dict):
        return communities, malformed, nested

    for key, val in impact_obj.items():
        # Top-level impact fields = malformed structure
        if key in IMPACT_FIELDS:
            if isinstance(val, (str, dict)):
                malformed.append(key)
            continue

        if not isinstance(val, dict) or not is_community_object(val):
            continue

        # This is a community object
        field_counts = {}
        for field in IMPACT_FIELDS:
            field_counts[field] = count_words(val.get(field, ''))
        total = sum(field_counts.values())
        communities.append((key, field_counts, total))

        # Check for nested communities
        for sub_key, sub_val in val.items():
            if sub_key in IMPACT_FIELDS:
                continue
            if isinstance(sub_val, dict) and is_community_object(sub_val):
                nested.append((key, sub_key))
                sub_counts = {}
                for field in IMPACT_FIELDS:
                    sub_counts[field] = count_words(sub_val.get(field, ''))
                sub_total = sum(sub_counts.values())
                communities.append((f'{key}.{sub_key}', sub_counts, sub_total))

    return communities, malformed, nested


def run_audit(data, start=None, end=None, since=None, min_words=MIN_WORDS,
              check_structure=True, check_words=True):
    """Run audit across all entries matching the date filter."""
    results = {
        'entries_audited': 0,
        'entries_no_impact': [],
        'passing': [],
        'failing': [],
        'malformed': [],
        'nested': [],
        'summary_by_category': defaultdict(lambda: {'total': 0, 'pass': 0, 'fail': 0}),
    }

    for cat in CATEGORIES:
        if cat not in data or not isinstance(data[cat], list):
            continue
        for entry in data[cat]:
            if not isinstance(entry, dict):
                continue
            date_str = entry.get('d', '')
            if not in_date_range(date_str, start, end, since):
                continue

            results['entries_audited'] += 1
            results['summary_by_category'][cat]['total'] += 1

            eid = entry.get('i', entry.get('id', 'UNKNOWN'))
            title = strip_html(entry.get('T', entry.get('n', entry.get('s', 'No title'))))[:85]
            severity = entry.get('L', '?')
            impact = entry.get('I')

            entry_info = {
                'id': eid, 'date': date_str, 'title': title,
                'category': cat, 'severity': severity,
            }

            if not isinstance(impact, dict) or len(impact) == 0:
                results['entries_no_impact'].append(entry_info)
                continue

            communities, malformed, nested = analyze_impact(impact)

            # Structure checks
            if check_structure:
                for field_name in malformed:
                    results['malformed'].append({**entry_info, 'field': field_name})
                for outer, inner in nested:
                    results['nested'].append({**entry_info, 'outer': outer, 'inner': inner})

            # Word count checks
            if check_words and communities:
                failing_comms = [(name, counts, total) for name, counts, total in communities
                                if total < min_words]
                passing_comms = [(name, counts, total) for name, counts, total in communities
                                if total >= min_words]

                info = {
                    **entry_info,
                    'failing': failing_comms,
                    'passing': passing_comms,
                    'total_communities': len(communities),
                }

                if failing_comms:
                    results['failing'].append(info)
                    results['summary_by_category'][cat]['fail'] += 1
                else:
                    results['passing'].append(info)
                    results['summary_by_category'][cat]['pass'] += 1

    return results


def print_report(results, min_words=MIN_WORDS, check_structure=True, check_words=True,
                 verbose=True):
    """Print formatted audit report."""
    print(f'\n{"=" * 100}')
    print(f'TCKC THREAT TRACKER — AUDIT REPORT')
    print(f'{"=" * 100}')
    print(f'Entries audited: {results["entries_audited"]}')
    print(f'Entries without I object: {len(results["entries_no_impact"])}')

    # Structure report
    if check_structure:
        print(f'\n{"=" * 100}')
        print(f'STRUCTURAL CHECK: MALFORMED I OBJECTS')
        print(f'{"=" * 100}')
        if results['malformed']:
            print(f'  FOUND {len(results["malformed"])} malformed field(s):')
            for m in results['malformed']:
                print(f'    [{m["date"]}] {m["id"]}')
                print(f'      Title: {m["title"]}')
                print(f'      Issue: \'{m["field"]}\' at top level (should be inside a community key)')
        else:
            print(f'  PASS — No malformed I objects found.')

        print(f'\n{"=" * 100}')
        print(f'STRUCTURAL CHECK: NESTED COMMUNITIES')
        print(f'{"=" * 100}')
        if results['nested']:
            print(f'  FOUND {len(results["nested"])} nesting issue(s):')
            for n in results['nested']:
                print(f'    [{n["date"]}] {n["id"]}')
                print(f'      Issue: \'{n["inner"]}\' nested inside \'{n["outer"]}\'')
        else:
            print(f'  PASS — No nested community objects found.')

    # Word count report
    if check_words:
        print(f'\n{"=" * 100}')
        print(f'WORD COUNT AUDIT ({min_words}-word minimum per community)')
        print(f'{"=" * 100}')
        print(f'  Passing entries: {len(results["passing"])}')
        print(f'  Failing entries: {len(results["failing"])}')

        if results['failing'] and verbose:
            print(f'\n  --- FAILING ENTRIES ---')
            for idx, er in enumerate(sorted(results['failing'], key=lambda x: x['date']), 1):
                print(f'\n  [{idx}] {er["id"]} ({er["date"]}) — {er["title"]}')
                print(f'      Category: {er["category"]} | Severity: {er["severity"]}')
                for name, counts, total in er['failing']:
                    deficit = min_words - total
                    print(f'      *** FAIL *** {name}: {total} words (needs {deficit} more)')
                    print(f'                   people={counts["people"]}  places={counts["places"]}  '
                          f'practices={counts["practices"]}  treasures={counts["treasures"]}')
                for name, counts, total in er['passing']:
                    print(f'          pass     {name}: {total} words')

    # Entries without impact
    if results['entries_no_impact'] and verbose:
        print(f'\n{"=" * 100}')
        print(f'ENTRIES WITHOUT IMPACT (I) OBJECT ({len(results["entries_no_impact"])})')
        print(f'{"=" * 100}')
        for e in sorted(results['entries_no_impact'], key=lambda x: x['date']):
            print(f'  [{e["date"]}] {e["id"]} | {e["category"]}')

    # Category summary
    print(f'\n{"=" * 100}')
    print(f'PER-CATEGORY BREAKDOWN')
    print(f'{"=" * 100}')
    for cat, counts in sorted(results['summary_by_category'].items()):
        print(f'  {cat}: {counts["total"]} entries ({counts["pass"]} pass, {counts["fail"]} fail)')

    # Grand summary
    total_issues = len(results['malformed']) + len(results['nested']) + len(results['failing'])
    print(f'\n{"#" * 100}')
    if total_issues == 0:
        print(f'  VERDICT: ALL CLEAR — Zero issues found.')
    else:
        print(f'  VERDICT: {total_issues} ISSUE(S) REQUIRE ATTENTION')
    print(f'{"#" * 100}')


def main():
    parser = argparse.ArgumentParser(
        description='TCKC Threat Tracker — Unified Audit Toolkit',
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument('--word-counts', action='store_true',
                       help='Check word counts per community (default min: 250)')
    parser.add_argument('--structure', action='store_true',
                       help='Check for malformed I objects and nested communities')
    parser.add_argument('--full', action='store_true',
                       help='Run both word-count and structure checks')
    parser.add_argument('--summary', action='store_true',
                       help='Quick summary only (no verbose details)')
    parser.add_argument('--period', nargs=2, metavar=('START', 'END'),
                       help='Date range as YYYY-MM YYYY-MM (e.g., 2025-01 2025-03)')
    parser.add_argument('--since', metavar='YYYY-MM',
                       help='Show entries from this month onward (e.g., 2025-10)')
    parser.add_argument('--min-words', type=int, default=MIN_WORDS,
                       help=f'Minimum words per community (default: {MIN_WORDS})')

    args = parser.parse_args()

    if not any([args.word_counts, args.structure, args.full, args.summary]):
        parser.print_help()
        sys.exit(1)

    check_structure = args.structure or args.full or args.summary
    check_words = args.word_counts or args.full or args.summary
    verbose = not args.summary

    start = args.period[0] if args.period else None
    end = args.period[1] if args.period else None
    since = args.since

    scope_desc = 'all entries'
    if args.period:
        scope_desc = f'{start} to {end}'
    elif args.since:
        scope_desc = f'since {since}'

    print(f'=== TCKC Audit Toolkit — Scope: {scope_desc} ===')

    data = load_data()
    results = run_audit(data, start=start, end=end, since=since,
                       min_words=args.min_words,
                       check_structure=check_structure, check_words=check_words)
    print_report(results, min_words=args.min_words,
                check_structure=check_structure, check_words=check_words,
                verbose=verbose)


if __name__ == '__main__':
    main()
