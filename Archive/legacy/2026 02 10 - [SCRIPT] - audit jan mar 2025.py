#!/usr/bin/env python3
"""Audit Jan-Mar 2025 entries for 250-word minimum per community in Impact Analysis."""

import re
import json
import sys

# Read the HTML file
with open("tckc-threat-tracker-v10-Jan30final.html", "r", encoding="utf-8") as f:
    content = f.read()

# Extract the DATA object
match = re.search(r'const DATA = ({.*?});', content, re.DOTALL)
if not match:
    print("ERROR: Could not find DATA object")
    sys.exit(1)

data_str = match.group(1)
# Fix trailing commas for JSON parsing
data_str = re.sub(r',(\s*[}\]])', r'\1', data_str)
data = json.loads(data_str)

def count_words(text):
    if not isinstance(text, str):
        return 0
    return len(text.split())

def check_community(name, obj, depth=0):
    """Check a community object. Returns (total_words, issues_list)."""
    issues = []
    total = 0
    nested = []

    fields = ["people", "places", "practices", "treasures"]
    for field in fields:
        if field in obj and isinstance(obj[field], str):
            wc = count_words(obj[field])
            total += wc

    # Check for nested communities (keys that aren't people/places/practices/treasures)
    for key in obj:
        if key not in fields:
            if isinstance(obj[key], dict):
                nested.append(key)

    return total, nested

def analyze_entry(entry):
    """Analyze an entry's I object for word count and nesting issues."""
    entry_id = entry.get("i") or entry.get("id", "UNKNOWN")
    date = entry.get("d", "")
    communities = entry.get("c", [])
    impact = entry.get("I", {})
    title_raw = entry.get("T", "")
    title = re.sub(r'<[^>]+>', '', title_raw)

    if not impact or not isinstance(impact, dict):
        return None

    results = {
        "id": entry_id,
        "date": date,
        "title": title[:80],
        "communities_in_c": len(communities),
        "communities_in_I": 0,
        "passing": [],
        "failing": [],
        "malformed": False,
        "nesting_issues": [],
    }

    # Check if I has top-level people/places/practices/treasures (malformed)
    top_level_fields = [k for k in impact if k in ["people", "places", "practices", "treasures"]]
    if top_level_fields:
        results["malformed"] = True

    # Check each community wrapper
    community_keys = [k for k in impact if k not in ["people", "places", "practices", "treasures"]]
    results["communities_in_I"] = len(community_keys)

    for comm_key in community_keys:
        comm_obj = impact[comm_key]
        if not isinstance(comm_obj, dict):
            continue
        total, nested = check_community(comm_key, comm_obj)

        if nested:
            results["nesting_issues"].append(f"{comm_key} contains nested: {nested}")

        if total >= 250:
            results["passing"].append((comm_key, total))
        else:
            results["failing"].append((comm_key, total))

    return results

# Collect all Jan-Mar 2025 entries
all_entries = []
for category, entries in data.items():
    if not isinstance(entries, list):
        continue
    for entry in entries:
        date = entry.get("d", "")
        if date.startswith("2025-01") or date.startswith("2025-02") or date.startswith("2025-03"):
            all_entries.append((category, entry))

# Sort by date
all_entries.sort(key=lambda x: x[1].get("d", ""))

print(f"=" * 100)
print(f"AUDIT: Jan-Mar 2025 Entries - Community Impact Word Count Analysis")
print(f"=" * 100)
print(f"\nTotal entries found: {len(all_entries)}")
print()

pass_count = 0
fail_count = 0
malformed_count = 0
nesting_count = 0
no_impact = 0

failing_entries = []
malformed_entries = []
nesting_entries = []

for category, entry in all_entries:
    result = analyze_entry(entry)
    if result is None:
        no_impact += 1
        entry_id = entry.get("i") or entry.get("id", "UNKNOWN")
        print(f"  [NO I] {entry_id} ({entry.get('d', '')})")
        continue

    has_issues = False

    if result["malformed"]:
        malformed_count += 1
        malformed_entries.append(result)
        has_issues = True

    if result["nesting_issues"]:
        nesting_count += 1
        nesting_entries.append(result)
        has_issues = True

    if result["failing"]:
        fail_count += 1
        failing_entries.append(result)
        has_issues = True
    else:
        if not has_issues:
            pass_count += 1

print(f"\n{'=' * 100}")
print(f"SUMMARY")
print(f"{'=' * 100}")
print(f"Total entries with I object: {len(all_entries) - no_impact}")
print(f"Entries without I object: {no_impact}")
print(f"PASS (all communities >= 250 words): {pass_count}")
print(f"FAIL (at least one community < 250 words): {fail_count}")
print(f"Malformed (top-level fields without community wrapper): {malformed_count}")
print(f"Nesting issues: {nesting_count}")

if malformed_entries:
    print(f"\n{'=' * 100}")
    print(f"MALFORMED ENTRIES (top-level people/places/practices/treasures without community wrapper)")
    print(f"{'=' * 100}")
    for r in malformed_entries:
        print(f"\n  [{r['id']}] {r['date']} - {r['title']}")
        print(f"    Communities in c[]: {r['communities_in_c']}, Wrappers in I: {r['communities_in_I']}")

if nesting_entries:
    print(f"\n{'=' * 100}")
    print(f"NESTING ISSUES")
    print(f"{'=' * 100}")
    for r in nesting_entries:
        print(f"\n  [{r['id']}] {r['date']} - {r['title']}")
        for issue in r["nesting_issues"]:
            print(f"    NESTED: {issue}")

if failing_entries:
    print(f"\n{'=' * 100}")
    print(f"FAILING ENTRIES (community word count < 250)")
    print(f"{'=' * 100}")
    for r in sorted(failing_entries, key=lambda x: len(x["failing"])):
        print(f"\n  [{r['id']}] {r['date']} - {r['title']}")
        print(f"    Communities in c[]: {r['communities_in_c']}, Wrappers in I: {r['communities_in_I']}")
        if r["failing"]:
            print(f"    FAILING communities:")
            for comm, wc in r["failing"]:
                print(f"      - {comm}: {wc} words (need {250 - wc} more)")
        if r["passing"]:
            print(f"    Passing communities:")
            for comm, wc in r["passing"]:
                print(f"      - {comm}: {wc} words")

print(f"\n{'=' * 100}")
print(f"DETAILED WORD COUNTS FOR ALL ENTRIES")
print(f"{'=' * 100}")
for category, entry in all_entries:
    result = analyze_entry(entry)
    if result is None:
        continue

    status = "PASS" if not result["failing"] and not result["malformed"] and not result["nesting_issues"] else "FAIL"
    print(f"\n  [{status}] {result['id']} ({result['date']}) - {result['title']}")
    print(f"    c[]: {result['communities_in_c']} communities | I: {result['communities_in_I']} wrappers")

    for comm, wc in result["passing"]:
        print(f"      [OK] {comm}: {wc}w")
    for comm, wc in result["failing"]:
        print(f"      [!!] {comm}: {wc}w (need {250 - wc} more)")
    if result["malformed"]:
        print(f"      [MAL] Top-level fields without community wrapper")
    for issue in result["nesting_issues"]:
        print(f"      [NEST] {issue}")
