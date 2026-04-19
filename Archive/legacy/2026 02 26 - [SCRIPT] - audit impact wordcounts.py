#!/usr/bin/env python3
"""
Audit word counts for Impact Analysis (I) fields in the TCKC Threat Tracker.
Finds all entries dated July, August, September 2025 and counts words
in each community section's people/places/practices/treasures fields.
"""

import re
import json
import sys


def extract_data_object(html_content):
    """Extract the DATA JavaScript object from the HTML file."""
    # Find the start of the DATA object
    match = re.search(r'const\s+DATA\s*=\s*\{', html_content)
    if not match:
        print("ERROR: Could not find 'const DATA = {' in the file.")
        sys.exit(1)

    start_idx = match.start() + len('const DATA = ')

    # Now we need to find the matching closing brace
    # We'll track brace depth
    depth = 0
    in_string = False
    escape_next = False
    end_idx = start_idx

    for i in range(start_idx, len(html_content)):
        ch = html_content[i]

        if escape_next:
            escape_next = False
            continue

        if ch == '\\' and in_string:
            escape_next = True
            continue

        if ch == '"' and not escape_next:
            in_string = not in_string
            continue

        if in_string:
            continue

        if ch == '{':
            depth += 1
        elif ch == '}':
            depth -= 1
            if depth == 0:
                end_idx = i + 1
                break

    json_str = html_content[start_idx:end_idx]

    try:
        data = json.loads(json_str)
    except json.JSONDecodeError as e:
        print(f"ERROR: Failed to parse JSON: {e}")
        # Try to show context around the error
        line_no = json_str[:e.pos].count('\n') + 1
        print(f"  Error at approximately line {line_no} of the JSON object")
        sys.exit(1)

    return data


def count_words(text):
    """Count words in a string."""
    if not isinstance(text, str):
        return 0
    return len(text.split())


def is_community_object(obj):
    """Check if an object looks like a community impact object (has people/places/practices/treasures)."""
    if not isinstance(obj, dict):
        return False
    expected_fields = {'people', 'places', 'practices', 'treasures'}
    return bool(expected_fields & set(obj.keys()))


def analyze_entry_impact(impact_obj):
    """
    Analyze the Impact Analysis object for an entry.
    Only count top-level community keys. Skip any nested community objects.
    Returns a list of (community_name, word_count, field_details, notes) tuples.
    """
    results = []

    if not isinstance(impact_obj, dict):
        return results

    for community_key, community_data in impact_obj.items():
        if not isinstance(community_data, dict):
            results.append((community_key, 0, {}, "MALFORMED: community data is not a dict"))
            continue

        total_words = 0
        field_details = {}
        notes = []

        for field_name in ['people', 'places', 'practices', 'treasures']:
            if field_name not in community_data:
                # The field might be missing - check if it's a community key instead
                # (this handles the nesting issue)
                field_details[field_name] = 0
                notes.append(f"missing '{field_name}'")
                continue

            field_val = community_data[field_name]
            if isinstance(field_val, str):
                wc = count_words(field_val)
                field_details[field_name] = wc
                total_words += wc
            elif isinstance(field_val, dict):
                # This is a nested community object inside a field name
                # that coincidentally matches - skip it
                field_details[field_name] = 0
                notes.append(f"'{field_name}' is a nested object (not a string)")
            else:
                field_details[field_name] = 0
                notes.append(f"'{field_name}' is type {type(field_val).__name__}")

        # Check for nested community objects (keys that are not standard fields)
        standard_fields = {'people', 'places', 'practices', 'treasures'}
        nested_communities = [k for k in community_data.keys() if k not in standard_fields]
        if nested_communities:
            notes.append(f"NESTED communities skipped: {', '.join(nested_communities)}")

        note_str = "; ".join(notes) if notes else ""
        results.append((community_key, total_words, field_details, note_str))

    return results


def main():
    filepath = "/Users/a.princealbert3/Desktop/TRACKER APP/tckc-threat-tracker-v10-Jan30final.html"

    print("=" * 120)
    print("TCKC THREAT TRACKER - IMPACT ANALYSIS WORD COUNT AUDIT")
    print("Entries dated: July 2025, August 2025, September 2025")
    print("Threshold: 300 words minimum per community section")
    print("=" * 120)
    print()

    # Read file
    print("Reading file...")
    with open(filepath, 'r', encoding='utf-8') as f:
        html_content = f.read()
    print(f"  File size: {len(html_content):,} characters")

    # Extract DATA
    print("Extracting DATA object...")
    data = extract_data_object(html_content)

    categories = ['executive_actions', 'agency_actions', 'legislation', 'litigation', 'international']
    found_categories = [c for c in categories if c in data]
    print(f"  Found categories: {', '.join(found_categories)}")

    # Collect all entries in date range
    target_entries = []
    total_entries = 0

    for category in found_categories:
        entries = data[category]
        if not isinstance(entries, list):
            print(f"  WARNING: {category} is not a list, skipping")
            continue

        for entry in entries:
            total_entries += 1
            date_str = entry.get('d', '')
            if not date_str:
                continue

            # Check if date is in July, August, or September 2025
            if (date_str.startswith('2025-07') or
                date_str.startswith('2025-08') or
                date_str.startswith('2025-09')):
                target_entries.append((category, entry))

    print(f"  Total entries scanned: {total_entries}")
    print(f"  Entries in Jul/Aug/Sep 2025: {len(target_entries)}")
    print()

    # Analyze each entry
    all_community_results = []  # (entry_id, date, title, category, community, word_count, field_details, notes)

    entries_without_impact = []
    entries_with_impact = []

    for category, entry in target_entries:
        entry_id = entry.get('i', 'NO-ID')
        date_str = entry.get('d', 'NO-DATE')
        title = entry.get('t', 'NO-TITLE')
        # Get the full title with HTML stripped
        full_title = entry.get('T', title)
        # Strip HTML tags for display
        clean_title = re.sub(r'<[^>]+>', '', full_title)

        impact = entry.get('I')
        if not impact or not isinstance(impact, dict):
            entries_without_impact.append((entry_id, date_str, clean_title, category))
            continue

        entries_with_impact.append((entry_id, date_str, clean_title, category))
        community_results = analyze_entry_impact(impact)

        for community_name, word_count, field_details, notes in community_results:
            all_community_results.append(
                (entry_id, date_str, clean_title, category, community_name,
                 word_count, field_details, notes)
            )

    # Sort by word count ascending (most problematic first)
    all_community_results.sort(key=lambda x: x[5])

    # Print report
    print("=" * 120)
    print("DETAILED REPORT: Community Word Counts (Sorted by Word Count - Ascending)")
    print("=" * 120)

    flagged_count = 0
    ok_count = 0

    for (entry_id, date_str, clean_title, category, community_name,
         word_count, field_details, notes) in all_community_results:

        flag = "** UNDER 300 **" if word_count < 300 else "OK"
        if word_count < 300:
            flagged_count += 1
        else:
            ok_count += 1

        print()
        print("-" * 120)
        print(f"  Entry ID   : {entry_id}")
        print(f"  Date       : {date_str}")
        print(f"  Category   : {category}")
        print(f"  Title      : {clean_title[:100]}{'...' if len(clean_title) > 100 else ''}")
        print(f"  Community  : {community_name}")
        print(f"  TOTAL WORDS: {word_count}  [{flag}]")
        if field_details:
            print(f"    - people   : {field_details.get('people', 'N/A'):>4} words")
            print(f"    - places   : {field_details.get('places', 'N/A'):>4} words")
            print(f"    - practices: {field_details.get('practices', 'N/A'):>4} words")
            print(f"    - treasures: {field_details.get('treasures', 'N/A'):>4} words")
        if notes:
            print(f"  NOTES      : {notes}")

    # Print entries without Impact Analysis
    if entries_without_impact:
        print()
        print()
        print("=" * 120)
        print("ENTRIES IN DATE RANGE WITHOUT IMPACT ANALYSIS (I) FIELD")
        print("=" * 120)
        for entry_id, date_str, clean_title, category in sorted(entries_without_impact, key=lambda x: x[1]):
            print(f"  {entry_id:30s}  {date_str}  [{category:20s}]  {clean_title[:70]}")

    # Summary
    print()
    print()
    print("=" * 120)
    print("SUMMARY")
    print("=" * 120)
    print(f"  Date range: July 2025 - September 2025")
    print(f"  Total entries in range: {len(target_entries)}")
    print(f"  Entries WITH Impact Analysis: {len(entries_with_impact)}")
    print(f"  Entries WITHOUT Impact Analysis: {len(entries_without_impact)}")
    print(f"  Total community sections audited: {len(all_community_results)}")
    print(f"  Community sections UNDER 300 words (flagged): {flagged_count}")
    print(f"  Community sections at/above 300 words (OK): {ok_count}")
    print()

    # Per-month breakdown
    print("  PER-MONTH BREAKDOWN:")
    for month_prefix, month_name in [('2025-07', 'July 2025'), ('2025-08', 'August 2025'), ('2025-09', 'September 2025')]:
        month_entries = [(c, e) for c, e in target_entries if e.get('d', '').startswith(month_prefix)]
        print(f"    {month_name}: {len(month_entries)} entries")

    # Per-category breakdown
    print()
    print("  PER-CATEGORY BREAKDOWN:")
    for cat in found_categories:
        cat_entries = [(c, e) for c, e in target_entries if c == cat]
        if cat_entries:
            print(f"    {cat}: {len(cat_entries)} entries")

    # Flagged entries summary
    if flagged_count > 0:
        print()
        print(f"  FLAGGED COMMUNITY SECTIONS (under 300 words) - {flagged_count} total:")
        for (entry_id, date_str, clean_title, category, community_name,
             word_count, field_details, notes) in all_community_results:
            if word_count < 300:
                print(f"    {entry_id:30s} | {date_str} | {community_name:25s} | {word_count:4d} words")

    print()
    print("=" * 120)
    print("END OF AUDIT REPORT")
    print("=" * 120)


if __name__ == '__main__':
    main()
