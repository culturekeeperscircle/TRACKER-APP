#!/usr/bin/env python3
"""
Analyze TCKC Threat Tracker entries from April-June 2025 that have exactly 3
community sub-objects in their I (Impact Analysis) object, and report those
where at least one community section has < 250 words total across its
people+places+practices+treasures fields.

Also checks for nesting (community objects inside other community objects).
Reports the line number in the HTML file where each matching entry starts.
"""

import json
import re
import sys

HTML_FILE = "/Users/a.princealbert3/Desktop/TRACKER APP/tckc-threat-tracker-v10-Jan30final.html"

COMMUNITY_FIELDS = {"people", "places", "practices", "treasures"}


def extract_data_json(html_text):
    """Extract the DATA JSON object from the HTML file."""
    # Find 'const DATA = {' and extract everything until the closing '};'
    match = re.search(r'const DATA = (\{)', html_text)
    if not match:
        print("ERROR: Could not find 'const DATA = {' in the file.")
        sys.exit(1)

    start = match.start(1)
    # We need to find the matching closing brace
    depth = 0
    i = start
    while i < len(html_text):
        ch = html_text[i]
        if ch == '{':
            depth += 1
        elif ch == '}':
            depth -= 1
            if depth == 0:
                end = i + 1
                break
        elif ch == '"':
            # Skip string contents to avoid counting braces inside strings
            i += 1
            while i < len(html_text):
                if html_text[i] == '\\':
                    i += 2  # skip escaped character
                    continue
                if html_text[i] == '"':
                    break
                i += 1
        i += 1
    else:
        print("ERROR: Could not find matching closing brace for DATA object.")
        sys.exit(1)

    json_str = html_text[start:end]

    # The JSON may contain HTML in strings (like <span> tags), which is fine for json.loads
    try:
        data = json.loads(json_str)
    except json.JSONDecodeError as e:
        print(f"ERROR: Failed to parse DATA JSON: {e}")
        # Try to show context around error
        pos = e.pos if hasattr(e, 'pos') else 0
        print(f"Context: ...{json_str[max(0,pos-100):pos+100]}...")
        sys.exit(1)

    return data


def count_words(text):
    """Count words in a string."""
    if not text or not isinstance(text, str):
        return 0
    return len(text.split())


def find_community_subobjects(impact_obj):
    """
    Find all community sub-objects in an I (Impact) object.

    A community sub-object is a dict that has at least some of the
    people/places/practices/treasures keys. We look at all top-level keys
    of the impact_obj.

    Returns a list of (key_name, community_dict, is_top_level) tuples.
    """
    communities = []
    if not isinstance(impact_obj, dict):
        return communities

    for key, value in impact_obj.items():
        if isinstance(value, dict):
            # Check if this dict has community fields
            has_community_fields = bool(set(value.keys()) & COMMUNITY_FIELDS)
            if has_community_fields:
                communities.append((key, value))

    return communities


def find_all_communities_recursive(obj, path=""):
    """
    Recursively find all community sub-objects (dicts with people/places/practices/treasures).
    Returns list of (path, community_dict) where path shows nesting.
    """
    results = []
    if not isinstance(obj, dict):
        return results

    for key, value in obj.items():
        if isinstance(value, dict):
            has_community_fields = bool(set(value.keys()) & COMMUNITY_FIELDS)
            current_path = f"{path}.{key}" if path else key
            if has_community_fields:
                results.append((current_path, value))
            # Recurse into the value to find nested communities
            results.extend(find_all_communities_recursive(value, current_path))

    return results


def check_nesting(impact_obj):
    """
    Check if there are community objects nested inside other community objects.
    Returns list of nesting descriptions.
    """
    nesting_info = []
    if not isinstance(impact_obj, dict):
        return nesting_info

    def _check(obj, parent_path="", parent_is_community=False):
        if not isinstance(obj, dict):
            return
        for key, value in obj.items():
            if key in COMMUNITY_FIELDS:
                continue  # skip the text fields themselves
            if isinstance(value, dict):
                has_community_fields = bool(set(value.keys()) & COMMUNITY_FIELDS)
                current_path = f"{parent_path}.{key}" if parent_path else key
                if has_community_fields and parent_is_community:
                    nesting_info.append(f"{current_path} nested inside {parent_path}")
                _check(value, current_path, has_community_fields)

    for key, value in impact_obj.items():
        if isinstance(value, dict):
            has_community_fields = bool(set(value.keys()) & COMMUNITY_FIELDS)
            if has_community_fields:
                _check(value, key, True)

    return nesting_info


def get_community_word_counts(community_dict):
    """
    Get word counts for people, places, practices, treasures in a community dict.
    Returns dict of field -> word_count and total.
    """
    counts = {}
    total = 0
    for field in ["people", "places", "practices", "treasures"]:
        wc = count_words(community_dict.get(field, ""))
        counts[field] = wc
        total += wc
    counts["total"] = total
    return counts


def count_top_level_communities(impact_obj):
    """
    Count the number of top-level community sub-objects in I.
    A top-level community sub-object is a direct child of I that is a dict
    with at least one of people/places/practices/treasures keys.
    """
    count = 0
    communities = []
    if not isinstance(impact_obj, dict):
        return 0, []

    for key, value in impact_obj.items():
        if isinstance(value, dict):
            has_community_fields = bool(set(value.keys()) & COMMUNITY_FIELDS)
            if has_community_fields:
                count += 1
                communities.append(key)

    return count, communities


def find_entry_line_numbers(html_lines, entry_ids):
    """
    Find the line number where each entry starts (the line with "i": "entry_id").
    Returns dict of entry_id -> line_number.
    """
    result = {}
    for line_no, line in enumerate(html_lines, 1):
        for eid in entry_ids:
            # Look for "i": "eid" pattern
            if f'"i": "{eid}"' in line:
                # The entry object starts a few lines before (the opening {)
                # Search backwards for the opening brace
                for back in range(line_no - 1, max(0, line_no - 5), -1):
                    stripped = html_lines[back - 1].strip()
                    if stripped == '{':
                        result[eid] = back
                        break
                else:
                    result[eid] = line_no
    return result


def main():
    print(f"Reading file: {HTML_FILE}")
    with open(HTML_FILE, 'r', encoding='utf-8') as f:
        html_text = f.read()

    html_lines = html_text.split('\n')

    print("Extracting DATA JSON object...")
    data = extract_data_json(html_text)

    # Categories to scan
    categories = ["executive_actions", "agency_actions", "legislation", "litigation",
                   "other_domestic", "international"]

    # Collect all entries from April-June 2025
    target_months = {"2025-04", "2025-05", "2025-06"}
    apr_jun_entries = []

    for cat in categories:
        entries = data.get(cat, [])
        if not isinstance(entries, list):
            continue
        for entry in entries:
            date = entry.get("d", "")
            if date[:7] in target_months:
                apr_jun_entries.append((cat, entry))

    print(f"\nTotal entries with dates in April-June 2025: {len(apr_jun_entries)}")

    # Filter to entries with exactly 3 top-level community sub-objects in I
    three_community_entries = []
    for cat, entry in apr_jun_entries:
        impact = entry.get("I")
        if not impact or not isinstance(impact, dict):
            continue
        count, comm_keys = count_top_level_communities(impact)
        if count == 3:
            three_community_entries.append((cat, entry, comm_keys))

    print(f"Entries with exactly 3 community sub-objects in I: {len(three_community_entries)}")

    # Find line numbers for all matching entries
    all_ids = [entry["i"] for _, entry, _ in three_community_entries]
    line_numbers = find_entry_line_numbers(html_lines, all_ids)

    # Check word counts and nesting
    print("\n" + "=" * 100)
    print("ENTRIES WITH EXACTLY 3 COMMUNITY SUB-OBJECTS (April-June 2025)")
    print("Filtering to those where ANY community section has < 250 words total")
    print("=" * 100)

    matching_entries = []

    for cat, entry, comm_keys in three_community_entries:
        impact = entry.get("I", {})
        entry_id = entry.get("i", "unknown")

        # Get word counts for each top-level community
        community_data = []
        has_under_250 = False

        for key in comm_keys:
            comm_dict = impact[key]
            wc = get_community_word_counts(comm_dict)
            community_data.append((key, wc))
            if wc["total"] < 250:
                has_under_250 = True

        # Check for nesting
        nesting = check_nesting(impact)

        # Also find ALL communities recursively (for complete picture)
        all_communities = find_all_communities_recursive(impact)

        if has_under_250:
            matching_entries.append({
                "id": entry_id,
                "category": cat,
                "date": entry.get("d"),
                "title": entry.get("s", entry.get("n", "")),
                "comm_keys": comm_keys,
                "community_data": community_data,
                "nesting": nesting,
                "all_communities_recursive": all_communities,
                "line_number": line_numbers.get(entry_id, "unknown"),
            })

    print(f"\nMatching entries (3 communities, at least one < 250 words): {len(matching_entries)}")
    print()

    for idx, m in enumerate(matching_entries, 1):
        print(f"\n{'─' * 100}")
        print(f"ENTRY #{idx}")
        print(f"  ID:           {m['id']}")
        print(f"  Category:     {m['category']}")
        print(f"  Date:         {m['date']}")
        print(f"  Title:        {m['title']}")
        print(f"  Line Number:  {m['line_number']}")
        print(f"  Top-level community keys: {m['comm_keys']}")
        print()

        print(f"  COMMUNITY WORD COUNTS (top-level):")
        for key, wc in m['community_data']:
            flag = " *** UNDER 250 ***" if wc['total'] < 250 else ""
            print(f"    {key}:")
            print(f"      people:    {wc['people']:>4} words")
            print(f"      places:    {wc['places']:>4} words")
            print(f"      practices: {wc['practices']:>4} words")
            print(f"      treasures: {wc['treasures']:>4} words")
            print(f"      TOTAL:     {wc['total']:>4} words{flag}")
            print()

        print(f"  NESTING: {'Yes' if m['nesting'] else 'No'}")
        if m['nesting']:
            for n in m['nesting']:
                print(f"    -> {n}")

        # Show all communities found recursively
        all_recursive = m['all_communities_recursive']
        if len(all_recursive) > len(m['comm_keys']):
            print(f"\n  ALL COMMUNITIES (recursive, including nested):")
            for path, comm_dict in all_recursive:
                wc = get_community_word_counts(comm_dict)
                depth = path.count('.')
                indent = "    " + "  " * depth
                print(f"{indent}{path}: {wc['total']} words (p:{wc['people']} pl:{wc['places']} pr:{wc['practices']} t:{wc['treasures']})")

    # Also print summary of ALL 3-community entries (even those without < 250)
    print(f"\n\n{'=' * 100}")
    print("SUMMARY: ALL ENTRIES WITH EXACTLY 3 COMMUNITIES (April-June 2025)")
    print(f"{'=' * 100}")
    print(f"{'ID':<30} {'Date':<12} {'Line':<8} {'Communities':<60} {'Min Words':<10} {'<250?'}")
    print("-" * 130)
    for cat, entry, comm_keys in three_community_entries:
        impact = entry.get("I", {})
        entry_id = entry.get("i", "unknown")
        date = entry.get("d", "")
        ln = line_numbers.get(entry_id, "?")

        min_words = float('inf')
        for key in comm_keys:
            wc = get_community_word_counts(impact[key])
            min_words = min(min_words, wc["total"])

        keys_str = ", ".join(comm_keys)
        flag = "YES" if min_words < 250 else "no"
        print(f"{entry_id:<30} {date:<12} {str(ln):<8} {keys_str:<60} {min_words:<10} {flag}")


if __name__ == "__main__":
    main()
