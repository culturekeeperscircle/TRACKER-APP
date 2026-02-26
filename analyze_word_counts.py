#!/usr/bin/env python3
"""
Analyze database entries from October 2025 onward to find community impact sections
with fewer than 250 words total across all 4P fields.
"""

import json
import re
from datetime import datetime

def count_words(text):
    """Count words in a text string."""
    if not text or not isinstance(text, str):
        return 0
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    # Split on whitespace and count
    words = text.split()
    return len(words)

def analyze_entry(entry):
    """
    Analyze a single entry and return communities with < 250 words.
    Returns dict with entry info and flagged communities.
    """
    entry_id = entry.get('i', 'UNKNOWN')
    entry_date = entry.get('d', 'UNKNOWN')
    entry_title = entry.get('T', entry.get('n', 'UNKNOWN'))

    # Remove HTML tags from title for readability
    entry_title_clean = re.sub(r'<[^>]+>', '', entry_title)

    impact_data = entry.get('I', {})

    flagged_communities = []

    for community_key, community_data in impact_data.items():
        if not isinstance(community_data, dict):
            continue

        # Count words across all 4P fields
        people_words = count_words(community_data.get('people', ''))
        places_words = count_words(community_data.get('places', ''))
        practices_words = count_words(community_data.get('practices', ''))
        treasures_words = count_words(community_data.get('treasures', ''))

        total_words = people_words + places_words + practices_words + treasures_words

        if total_words < 250:
            flagged_communities.append({
                'community': community_key,
                'total_words': total_words,
                'people': people_words,
                'places': places_words,
                'practices': practices_words,
                'treasures': treasures_words
            })

    if flagged_communities:
        return {
            'id': entry_id,
            'title': entry_title_clean,
            'date': entry_date,
            'flagged_communities': flagged_communities
        }

    return None

def is_date_in_range(date_str):
    """Check if date is October 2025 or later."""
    try:
        date = datetime.strptime(date_str, '%Y-%m-%d')
        cutoff = datetime(2025, 10, 1)
        return date >= cutoff
    except:
        return False

def main():
    # Read the HTML file
    with open('/Users/a.princealbert3/Desktop/TRACKER APP/tckc-threat-tracker-v10-Jan30final.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the database object - look for const DATA = {...}
    # The database appears to be in a JavaScript variable
    match = re.search(r'const\s+DATA\s*=\s*({.*?});', content, re.DOTALL)

    if not match:
        print("Could not find database object in file")
        return

    db_json = match.group(1)

    try:
        db = json.loads(db_json)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        return

    # Analyze all categories
    all_flagged = []

    categories = ['executive_orders', 'agency_actions', 'legislation', 'litigation', 'international']

    for category in categories:
        if category not in db:
            continue

        entries = db[category]
        for entry in entries:
            date = entry.get('d', '')
            if is_date_in_range(date):
                result = analyze_entry(entry)
                if result:
                    result['category'] = category
                    all_flagged.append(result)

    # Sort by date
    all_flagged.sort(key=lambda x: x['date'])

    # Print results
    print(f"\n{'='*80}")
    print(f"ENTRIES FROM OCTOBER 2025 ONWARD WITH COMMUNITY SECTIONS < 250 WORDS")
    print(f"{'='*80}\n")
    print(f"Total entries flagged: {len(all_flagged)}\n")

    for idx, entry in enumerate(all_flagged, 1):
        print(f"{idx}. ID: {entry['id']}")
        print(f"   Category: {entry['category']}")
        print(f"   Date: {entry['date']}")
        print(f"   Title: {entry['title'][:100]}{'...' if len(entry['title']) > 100 else ''}")
        print(f"   Flagged communities:")

        for comm in entry['flagged_communities']:
            print(f"      - {comm['community']}: {comm['total_words']} words total")
            print(f"        (people: {comm['people']}, places: {comm['places']}, " +
                  f"practices: {comm['practices']}, treasures: {comm['treasures']})")
        print()

    print(f"{'='*80}")
    print(f"ANALYSIS COMPLETE - {len(all_flagged)} entries flagged")
    print(f"{'='*80}\n")

if __name__ == '__main__':
    main()
