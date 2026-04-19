#!/usr/bin/env python3
"""
TCKC Threat Tracker — African Descendant Peoples Enrichment Script
Batch-enriches existing entries with specific African-descendant community
names, cultural resources, practices, and Afro-Indigenous cross-references
drawn from the reference database in comprehensive_update.py.

Usage:
    python enrich_african_descendant.py --dry-run     # Preview changes
    python enrich_african_descendant.py --all          # Run enrichment
    python enrich_african_descendant.py --report       # Report-only
"""

import json
import sys
import os
import argparse
from pathlib import Path
from datetime import datetime

TRACKER_DIR = Path(__file__).parent.parent
DATA_FILE = TRACKER_DIR / "data" / "data.json"

sys.path.insert(0, str(Path(__file__).parent))
from comprehensive_update import (
    AFRICAN_DESCENDANT_PEOPLES_BY_JURISDICTION,
    AFRICAN_DESCENDANT_SIGNAL_KEYWORDS,
    AFRICAN_DESCENDANT_CULTURAL_CONCEPTS,
    GEOGRAPHIC_AFRICAN_DESCENDANT_INDEX,
)

# Reuse jurisdiction keyword detection from the indigenous enrichment script
from enrich_indigenous import JURISDICTION_KEYWORDS, detect_jurisdictions


def load_data():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)


def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def get_entry_text(entry):
    parts = [entry.get('n', ''), entry.get('s', ''), entry.get('D', ''), entry.get('S', '')]
    impact = entry.get('I', {})
    for block in impact.values():
        if isinstance(block, dict):
            for v in block.values():
                if isinstance(v, str):
                    parts.append(v)
        elif isinstance(block, str):
            parts.append(block)
    return ' '.join(parts)


def build_community_sentence(jurisdiction, communities, max_items=5):
    """Build a concise sentence naming specific communities."""
    names = []
    for c in communities[:max_items]:
        name = c.split('—')[0].strip()
        if len(name) > 80:
            name = name.split(',')[0].strip()
        names.append(name)
    if not names:
        return ''
    return f'African-descendant communities in {jurisdiction} include {"; ".join(names)}.'


def build_afro_indigenous_sentence(afro_indigenous):
    """Build a sentence about Afro-Indigenous cross-references."""
    if not afro_indigenous:
        return ''
    items = []
    for ai in afro_indigenous[:3]:
        name = ai.split('—')[0].strip()
        context = ai.split('—')[1].strip()[:100] if '—' in ai else ''
        if context:
            items.append(f'{name} ({context})')
        else:
            items.append(name)
    return f'Afro-Indigenous communities in this region include: {"; ".join(items)}.'


def enrich_african_descendant_impact(entry, jurisdictions):
    """Add specific African-descendant community names and cultural details."""
    changes = []
    impact = entry.get('I', {})

    # Find the African-descendant impact key
    ad_key = None
    for k in ('africanDescendant', 'africanAmerican', 'african', 'black'):
        if k in impact:
            ad_key = k
            break

    if not ad_key:
        ad_key = 'africanDescendant'
        impact[ad_key] = {'people': '', 'places': '', 'practices': '', 'treasures': ''}
        entry['I'] = impact
        changes.append('Created new africanDescendant impact section')

    block = impact[ad_key]
    if not isinstance(block, dict):
        block = {'people': str(block), 'places': '', 'practices': '', 'treasures': ''}
        impact[ad_key] = block

    for pppt in ('people', 'places', 'practices', 'treasures'):
        if pppt not in block:
            block[pppt] = ''

    existing_text = ' '.join(v for v in block.values() if isinstance(v, str)).lower()

    for jur in jurisdictions:
        if jur not in AFRICAN_DESCENDANT_PEOPLES_BY_JURISDICTION:
            continue
        jur_data = AFRICAN_DESCENDANT_PEOPLES_BY_JURISDICTION[jur]

        # --- PEOPLE: communities + afro-indigenous ---
        communities = jur_data.get('communities', [])
        communities_to_add = []
        for c in communities:
            primary = c.split('—')[0].split('(')[0].strip().split(',')[0].strip()
            if primary.lower() not in existing_text and len(primary) > 3:
                communities_to_add.append(c)

        if communities_to_add:
            addition = ' ' + build_community_sentence(jur, communities_to_add)
            block['people'] = (block['people'].rstrip() + addition).strip()
            changes.append(f'Added {len(communities_to_add)} communities for {jur}')

        afro_indigenous = jur_data.get('afro_indigenous', [])
        ai_to_add = []
        for ai in afro_indigenous:
            primary = ai.split('—')[0].strip()
            if primary.lower() not in existing_text and len(primary) > 3:
                ai_to_add.append(ai)
        if ai_to_add:
            addition = ' ' + build_afro_indigenous_sentence(ai_to_add)
            block['people'] = (block['people'].rstrip() + addition).strip()
            changes.append(f'Added {len(ai_to_add)} Afro-Indigenous references for {jur}')

        # --- PLACES: cultural resources ---
        resources = jur_data.get('cultural_resources', [])
        resources_to_add = []
        for r in resources:
            name = r.split('—')[0].split('(')[0].strip()
            if name.lower() not in existing_text and len(name) > 3:
                resources_to_add.append(r)
        if resources_to_add:
            resource_text = '; '.join(resources_to_add[:5])
            addition = f' African-descendant cultural resources in {jur}: {resource_text}.'
            block['places'] = (block['places'].rstrip() + addition).strip()
            changes.append(f'Added {len(resources_to_add[:5])} cultural resources for {jur}')

        # --- PRACTICES ---
        practices = jur_data.get('cultural_practices', [])
        practices_to_add = []
        for p in practices:
            name = p.split('—')[0].strip()
            if name.lower() not in existing_text and len(name) > 3:
                practices_to_add.append(p)
        if practices_to_add:
            practice_text = '; '.join(practices_to_add[:4])
            addition = f' Cultural practices in {jur}: {practice_text}.'
            block['practices'] = (block['practices'].rstrip() + addition).strip()
            changes.append(f'Added {len(practices_to_add[:4])} cultural practices for {jur}')

        # --- TREASURES: material culture items by region ---
        treasures_to_add = []
        jur_lower = jur.lower()
        se_states = {'alabama', 'georgia', 'mississippi', 'louisiana', 'south carolina',
                     'north carolina', 'tennessee', 'florida', 'arkansas', 'virginia'}
        ne_states = {'new york', 'pennsylvania', 'massachusetts', 'connecticut', 'maryland',
                     'delaware', 'new jersey', 'district of columbia'}
        mw_states = {'illinois', 'michigan', 'ohio', 'indiana', 'missouri', 'minnesota',
                     'iowa', 'wisconsin', 'kansas'}
        west_states = {'california', 'colorado', 'texas', 'oklahoma', 'arizona', 'nevada',
                      'oregon', 'washington'}
        territories = {'puerto rico', 'us virgin islands', 'guam', 'american samoa',
                      'northern mariana islands (cnmi)'}

        if jur_lower in se_states:
            items = ['Gullah/Geechee sweetgrass baskets', 'quilts (Gee\'s Bend tradition)',
                    'wrought ironwork (West African metalworking)', 'indigo-dyed textiles',
                    'enslaved persons\' pottery (Edgefield/Colonoware)', 'shotgun house architecture']
        elif jur_lower in ne_states:
            items = ['African Burial Ground artifacts', 'Schomburg Center collections',
                    'AME church institutional records', 'Harlem Renaissance artworks and manuscripts',
                    'Underground Railroad safe house documentation']
        elif jur_lower in mw_states:
            items = ['Motown recordings and memorabilia', 'Chicago Blues recordings',
                    'Great Migration oral histories and photographs',
                    'HBCU institutional archives']
        elif jur_lower in west_states:
            items = ['Black Panther Party archives and ephemera', 'Freedmen\'s town artifacts',
                    'Buffalo Soldiers military artifacts', 'Black cowboy and rodeo heritage materials',
                    'Juneteenth historical documentation']
        elif jur_lower in territories:
            items = ['Vejigante masks and costumes (Loíza)', 'Bomba drums (barriles)',
                    'Quelbe instruments', 'Mocko jumbie stilts and costumes',
                    'Plantation-era archaeological artifacts']
        else:
            items = []

        for item in items:
            if item.lower() not in existing_text:
                treasures_to_add.append(item)

        if treasures_to_add:
            treasure_text = ', '.join(treasures_to_add[:5])
            addition = f' African-descendant cultural treasures of this region include {treasure_text}.'
            block['treasures'] = (block['treasures'].rstrip() + addition).strip()
            changes.append(f'Added {len(treasures_to_add[:5])} cultural treasures for {jur}')

    return entry, changes


def run_enrichment(data, dry_run=True, report_only=False):
    stats = {'entries_checked': 0, 'entries_enriched': 0, 'changes': []}
    categories = ['executive_actions', 'legislation', 'litigation',
                  'agency_actions', 'international']

    for cat in categories:
        if cat not in data or not isinstance(data[cat], list):
            continue
        for i, entry in enumerate(data[cat]):
            stats['entries_checked'] += 1
            entry_id = entry.get('i', entry.get('id', f'{cat}[{i}]'))
            text = get_entry_text(entry)
            text_lower = text.lower()

            # Check if entry involves African-descendant communities
            signal_count = sum(1 for kw in AFRICAN_DESCENDANT_SIGNAL_KEYWORDS
                              if kw.lower() in text_lower)
            if signal_count == 0:
                continue

            # Detect jurisdictions
            jurisdictions = detect_jurisdictions(text)
            if not jurisdictions:
                continue

            # Filter to jurisdictions that have African-descendant data
            relevant_jurs = [j for j in jurisdictions
                           if j in AFRICAN_DESCENDANT_PEOPLES_BY_JURISDICTION
                           and AFRICAN_DESCENDANT_PEOPLES_BY_JURISDICTION[j].get('communities')]
            if not relevant_jurs:
                continue

            if report_only:
                print(f'  [{cat}] {entry_id}: jurisdictions={relevant_jurs[:5]}, signals={signal_count}')
                continue

            entry, changes = enrich_african_descendant_impact(entry, relevant_jurs)
            if changes:
                stats['entries_enriched'] += 1
                stats['changes'].append({
                    'id': entry_id, 'category': cat,
                    'jurisdictions': relevant_jurs[:5],
                    'changes': changes,
                })
                if not dry_run:
                    data[cat][i] = entry
                print(f'  [{cat}] {entry_id}: {len(changes)} changes — {"; ".join(changes[:3])}')

    return data, stats


def main():
    parser = argparse.ArgumentParser(
        description='TCKC Threat Tracker — African Descendant Enrichment',
    )
    parser.add_argument('--all', action='store_true', help='Run full enrichment')
    parser.add_argument('--dry-run', action='store_true', help='Preview without saving')
    parser.add_argument('--report', action='store_true', help='Report-only')
    args = parser.parse_args()

    if not args.all and not args.report and not args.dry_run:
        parser.print_help()
        sys.exit(1)

    print(f'=== TCKC African Descendant Enrichment — {datetime.now().strftime("%Y-%m-%d %H:%M")} ===')

    data = load_data()
    total = sum(len(v) for v in data.values() if isinstance(v, list))
    print(f'Loaded {total} entries')

    if args.report:
        _, stats = run_enrichment(data, report_only=True)
        print(f'\nEntries checked: {stats["entries_checked"]}')
        sys.exit(0)

    data, stats = run_enrichment(data, dry_run=args.dry_run)
    print(f'\nChecked: {stats["entries_checked"]}, Enriched: {stats["entries_enriched"]}')

    if stats['changes']:
        log_file = TRACKER_DIR / f'ad_enrichment_log_{datetime.now().strftime("%Y%m%d_%H%M")}.json'
        with open(log_file, 'w') as f:
            json.dump(stats['changes'], f, indent=2, ensure_ascii=False)
        print(f'Change log: {log_file.name}')

    if not args.dry_run and stats['entries_enriched'] > 0:
        save_data(data)
        print(f'Saved data.json — {stats["entries_enriched"]} entries enriched')
    elif args.dry_run:
        print(f'DRY RUN — {stats["entries_enriched"]} entries would be enriched')


if __name__ == '__main__':
    main()
