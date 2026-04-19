#!/usr/bin/env python3
"""
TCKC Threat Tracker - Final Verification Audit: April-June 2025
================================================================
Checks ALL entries dated April-June 2025 for:
  1. Community word counts (minimum 250 words total per community across people/places/practices/treasures)
  2. Malformed I objects (top-level people/places/practices/treasures without community wrappers)
  3. Nested communities (community objects inside other community objects)
Skips reference entries (_isRef: true) from the word count check.
"""

import re
import json
import sys
from collections import defaultdict

HTML_FILE = "/Users/a.princealbert3/Desktop/TRACKER APP/tckc-threat-tracker-v10-Jan30final.html"

# The four expected fields in a community impact sub-object
IMPACT_FIELDS = {"people", "places", "practices", "treasures"}
MIN_WORDS = 250


def extract_data_object(html_content):
    """Extract the JavaScript DATA object from the HTML file and parse as JSON."""
    start_match = re.search(r'const DATA\s*=\s*\{', html_content)
    if not start_match:
        print("ERROR: Could not find 'const DATA = {' in the file.")
        sys.exit(1)

    start_idx = start_match.start() + len("const DATA = ")
    depth = 0
    in_string = False
    escape_next = False

    for idx in range(start_idx, len(html_content)):
        ch = html_content[idx]
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
                end_idx = idx + 1
                break

    json_str = html_content[start_idx:end_idx]
    json_str = re.sub(r',\s*([}\]])', r'\1', json_str)

    try:
        data = json.loads(json_str)
    except json.JSONDecodeError as e:
        print(f"ERROR: Failed to parse DATA as JSON: {e}")
        sys.exit(1)

    return data


def count_words(text):
    """Count words in a string."""
    if not text or not isinstance(text, str):
        return 0
    return len(text.split())


def strip_html(text):
    """Remove HTML tags from a string."""
    if not text:
        return ""
    return re.sub(r'<[^>]+>', '', text)


def is_community_object(obj):
    """Check if a dict looks like a community impact object (has people/places/practices/treasures strings)."""
    if not isinstance(obj, dict):
        return False
    return any(k in IMPACT_FIELDS and isinstance(obj[k], str) for k in obj)


def analyze_impact_object(impact_obj, entry_id, path_prefix="I"):
    """
    Recursively analyze an I object.
    Returns:
      communities: list of (path, {field: word_count}, total_words)
      malformed: list of (path, field_name) for top-level impact fields
      nested: list of (outer_path, inner_community_name) for nesting issues
    """
    communities = []
    malformed = []
    nested = []

    if not isinstance(impact_obj, dict):
        return communities, malformed, nested

    for key, val in impact_obj.items():
        if key in IMPACT_FIELDS:
            # Top-level impact field = malformed
            if isinstance(val, str):
                malformed.append((path_prefix, key))
            elif isinstance(val, dict) and is_community_object(val):
                malformed.append((path_prefix, key))
            continue

        if not isinstance(val, dict):
            continue

        if not is_community_object(val):
            continue

        # This is a community object
        comm_path = f"{path_prefix}.{key}"
        field_counts = {}
        for field in IMPACT_FIELDS:
            field_counts[field] = count_words(val.get(field, ""))
        total = sum(field_counts.values())
        communities.append((comm_path, key, field_counts, total))

        # Check for nested communities inside this community
        for sub_key, sub_val in val.items():
            if sub_key in IMPACT_FIELDS:
                continue
            if isinstance(sub_val, dict) and is_community_object(sub_val):
                nested.append((comm_path, sub_key))
                # Also audit the nested community
                nested_path = f"{comm_path}.{sub_key}"
                n_field_counts = {}
                for field in IMPACT_FIELDS:
                    n_field_counts[field] = count_words(sub_val.get(field, ""))
                n_total = sum(n_field_counts.values())
                communities.append((nested_path, sub_key, n_field_counts, n_total))

                # Check for even deeper nesting
                for deep_key, deep_val in sub_val.items():
                    if deep_key in IMPACT_FIELDS:
                        continue
                    if isinstance(deep_val, dict) and is_community_object(deep_val):
                        nested.append((nested_path, deep_key))
                        d_path = f"{nested_path}.{deep_key}"
                        d_field_counts = {}
                        for field in IMPACT_FIELDS:
                            d_field_counts[field] = count_words(deep_val.get(field, ""))
                        d_total = sum(d_field_counts.values())
                        communities.append((d_path, deep_key, d_field_counts, d_total))

                        # Check depth 4
                        for d4_key, d4_val in deep_val.items():
                            if d4_key in IMPACT_FIELDS:
                                continue
                            if isinstance(d4_val, dict) and is_community_object(d4_val):
                                nested.append((d_path, d4_key))
                                d4_path = f"{d_path}.{d4_key}"
                                d4_fc = {}
                                for field in IMPACT_FIELDS:
                                    d4_fc[field] = count_words(d4_val.get(field, ""))
                                d4_total = sum(d4_fc.values())
                                communities.append((d4_path, d4_key, d4_fc, d4_total))

    return communities, malformed, nested


def main():
    print("=" * 100)
    print("TCKC THREAT TRACKER - FINAL VERIFICATION AUDIT")
    print("Scope: ALL entries dated April 1 - June 30, 2025")
    print("Threshold: 250 words minimum per community (across people+places+practices+treasures)")
    print("=" * 100)
    print()

    # ---- Read & Parse ----
    with open(HTML_FILE, 'r', encoding='utf-8') as f:
        html = f.read()
    print(f"Read {len(html):,} characters from HTML file.")

    data = extract_data_object(html)
    categories = [k for k in data.keys() if k != "meta"]
    print(f"Categories found: {', '.join(categories)}")
    print()

    # ---- Collect Apr-Jun 2025 entries ----
    all_entries = []
    total_in_db = 0
    for cat in categories:
        if not isinstance(data[cat], list):
            continue
        for entry in data[cat]:
            if not isinstance(entry, dict):
                continue
            total_in_db += 1
            d = entry.get("d", "")
            if d >= "2025-04-01" and d <= "2025-06-30":
                entry["_cat"] = cat
                all_entries.append(entry)

    ref_entries = [e for e in all_entries if e.get("_isRef") is True]
    audit_entries = [e for e in all_entries if not e.get("_isRef")]

    print(f"Total entries in database: {total_in_db}")
    print(f"Entries in Apr-Jun 2025:   {len(all_entries)}")
    print(f"  Regular (audited):       {len(audit_entries)}")
    print(f"  Reference (_isRef=true): {len(ref_entries)} (skipped for word count)")
    print()

    # ---- Run the audit ----
    # Track results per entry
    entry_results = []  # list of dicts with full audit info
    all_malformed = []
    all_nested = []
    entries_no_impact = []

    for entry in audit_entries:
        eid = entry.get("i", entry.get("id", "UNKNOWN"))
        title = strip_html(entry.get("T", entry.get("n", entry.get("s", "No title"))))
        date = entry.get("d", "?")
        cat = entry.get("_cat", "?")
        severity = entry.get("L", "?")
        impact = entry.get("I")

        if not isinstance(impact, dict) or len(impact) == 0:
            entries_no_impact.append({"id": eid, "title": title, "date": date, "cat": cat})
            continue

        communities, malformed, nested = analyze_impact_object(impact, eid)

        for path, field_name in malformed:
            all_malformed.append({"id": eid, "title": title, "date": date, "path": path, "field": field_name})

        for outer_path, inner_name in nested:
            all_nested.append({"id": eid, "title": title, "date": date, "outer": outer_path, "inner": inner_name})

        # Determine pass/fail
        failing_comms = []
        passing_comms = []
        for (path, comm_name, field_counts, total) in communities:
            info = {"path": path, "name": comm_name, "counts": field_counts, "total": total}
            if total < MIN_WORDS:
                failing_comms.append(info)
            else:
                passing_comms.append(info)

        entry_pass = len(failing_comms) == 0 and len(communities) > 0
        entry_results.append({
            "id": eid,
            "title": title,
            "date": date,
            "cat": cat,
            "severity": severity,
            "communities": communities,
            "failing": failing_comms,
            "passing": passing_comms,
            "entry_pass": entry_pass,
            "has_communities": len(communities) > 0
        })

    # Also check structural issues in ref entries (but not word count)
    for entry in ref_entries:
        eid = entry.get("i", entry.get("id", "UNKNOWN"))
        title = strip_html(entry.get("T", entry.get("n", entry.get("s", "No title"))))
        date = entry.get("d", "?")
        impact = entry.get("I")
        if isinstance(impact, dict):
            _, malformed, nested = analyze_impact_object(impact, eid)
            for path, field_name in malformed:
                all_malformed.append({"id": eid, "title": title, "date": date, "path": path, "field": field_name, "is_ref": True})
            for outer_path, inner_name in nested:
                all_nested.append({"id": eid, "title": title, "date": date, "outer": outer_path, "inner": inner_name, "is_ref": True})

    # ======================================================================
    # REPORT
    # ======================================================================
    passing_entries = [r for r in entry_results if r["entry_pass"]]
    failing_entries = [r for r in entry_results if not r["entry_pass"] and r["has_communities"]]
    no_comm_entries = [r for r in entry_results if not r["has_communities"]]

    print("=" * 100)
    print("STRUCTURAL CHECK 1: MALFORMED I OBJECTS")
    print("(Top-level people/places/practices/treasures without community wrapper)")
    print("=" * 100)
    if all_malformed:
        print(f"\n  FOUND {len(all_malformed)} malformed field(s):\n")
        for m in all_malformed:
            ref_tag = " [REF]" if m.get("is_ref") else ""
            print(f"    [{m['date']}] {m['id']}{ref_tag}")
            print(f"      Title: {m['title'][:85]}")
            print(f"      Issue: '{m['field']}' found directly at {m['path']} level (should be inside a community key)")
            print()
    else:
        print("\n  PASS - No malformed I objects found.\n")

    print("=" * 100)
    print("STRUCTURAL CHECK 2: NESTED COMMUNITIES")
    print("(Community objects inside other community objects)")
    print("=" * 100)
    if all_nested:
        print(f"\n  FOUND {len(all_nested)} nesting issue(s):\n")
        for n in all_nested:
            ref_tag = " [REF]" if n.get("is_ref") else ""
            print(f"    [{n['date']}] {n['id']}{ref_tag}")
            print(f"      Title: {n['title'][:85]}")
            print(f"      Issue: Community '{n['inner']}' is nested inside {n['outer']}")
            print()
    else:
        print("\n  PASS - No nested community objects found.\n")

    print("=" * 100)
    print(f"WORD COUNT AUDIT: FAILING ENTRIES ({len(failing_entries)} entries)")
    print(f"(Any community with < {MIN_WORDS} words total across people+places+practices+treasures)")
    print("=" * 100)
    if failing_entries:
        for idx, er in enumerate(sorted(failing_entries, key=lambda x: x["date"]), 1):
            print(f"\n  {'~' * 94}")
            print(f"  [{idx}] {er['id']}")
            print(f"      Date:     {er['date']}")
            print(f"      Title:    {er['title'][:85]}")
            print(f"      Category: {er['cat']} | Severity: {er['severity']}")
            print()
            # Show failing communities
            for fc in er["failing"]:
                deficit = MIN_WORDS - fc["total"]
                print(f"      *** FAIL *** {fc['name']}: {fc['total']} words (needs {deficit} more)")
                print(f"                   people={fc['counts']['people']}  places={fc['counts']['places']}  "
                      f"practices={fc['counts']['practices']}  treasures={fc['counts']['treasures']}")
            # Show passing communities for context
            for pc in er["passing"]:
                print(f"          pass     {pc['name']}: {pc['total']} words")
                print(f"                   people={pc['counts']['people']}  places={pc['counts']['places']}  "
                      f"practices={pc['counts']['practices']}  treasures={pc['counts']['treasures']}")
    else:
        print("\n  No failing entries found - all communities meet the 250-word minimum!\n")

    if entries_no_impact:
        print()
        print("=" * 100)
        print(f"ENTRIES WITH NO IMPACT (I) OBJECT ({len(entries_no_impact)})")
        print("=" * 100)
        for e in sorted(entries_no_impact, key=lambda x: x["date"]):
            print(f"  [{e['date']}] {e['id']} | {e['cat']}")
            print(f"    Title: {e['title'][:85]}")

    if no_comm_entries:
        print()
        print("=" * 100)
        print(f"ENTRIES WITH I OBJECT BUT NO RECOGNIZABLE COMMUNITIES ({len(no_comm_entries)})")
        print("=" * 100)
        for er in sorted(no_comm_entries, key=lambda x: x["date"]):
            print(f"  [{er['date']}] {er['id']} | {er['cat']}")
            print(f"    Title: {er['title'][:85]}")

    # ---- PASSING ENTRIES (detailed) ----
    print()
    print("=" * 100)
    print(f"PASSING ENTRIES ({len(passing_entries)} entries) - all communities >= {MIN_WORDS} words")
    print("=" * 100)
    for er in sorted(passing_entries, key=lambda x: x["date"]):
        comm_summary = ", ".join(
            f"{c['name']}={c['total']}w" for c in er["passing"]
        )
        print(f"  [{er['date']}] {er['id']} | {er['cat']}")
        print(f"    {er['title'][:85]}")
        print(f"    Communities: {comm_summary}")

    # ---- GRAND SUMMARY ----
    print()
    print()
    print("#" * 100)
    print("#" + " " * 30 + "GRAND SUMMARY" + " " * 55 + "#")
    print("#" * 100)
    print()
    print(f"  Date range audited:           April 1 - June 30, 2025")
    print(f"  Total entries in range:        {len(all_entries)}")
    print(f"  Reference entries (skipped):   {len(ref_entries)}")
    print(f"  Entries audited:               {len(audit_entries)}")
    print()
    print(f"  --- Structural Issues ---")
    print(f"  Malformed I objects:           {len(all_malformed)}")
    print(f"  Nested communities:            {len(all_nested)}")
    print()
    print(f"  --- Word Count ({MIN_WORDS}-word min per community) ---")
    print(f"  Entries PASSING:               {len(passing_entries)}")
    print(f"  Entries FAILING:               {len(failing_entries)}")
    print(f"  Entries w/o I object:          {len(entries_no_impact)}")
    print(f"  Entries w/ I but no comms:     {len(no_comm_entries)}")
    print()

    total_comms = sum(len(er["communities"]) for er in entry_results)
    total_failing_comms = sum(len(er["failing"]) for er in entry_results)
    total_passing_comms = sum(len(er["passing"]) for er in entry_results)
    print(f"  Total community sections:      {total_comms}")
    print(f"    Passing:                     {total_passing_comms}")
    print(f"    Failing:                     {total_failing_comms}")
    if total_comms > 0:
        print(f"    Pass rate:                   {total_passing_comms/total_comms*100:.1f}%")
    print()

    total_issues = len(all_malformed) + len(all_nested) + len(failing_entries)
    if total_issues == 0:
        print("  *** VERDICT: ALL CLEAR - Zero issues found. ***")
    else:
        print(f"  *** VERDICT: {total_issues} ISSUE(S) REQUIRE ATTENTION ***")
    print()
    print("#" * 100)


if __name__ == "__main__":
    main()
