#!/usr/bin/env python3
"""
TCKC Threat Tracker — Indigenous Peoples Enrichment Script
Batch-enriches existing entries with specific tribal nation names, cultural
practices, places, and concepts drawn from the reference database in
comprehensive_update.py.

Operates in three batches:
  Batch 1: Virginia/DC/Maryland/Southeastern parks — most critical geographic gaps
  Batch 2: 119 entries with generic-only Indigenous impact text
  Batch 3: Missing major nations (Comanche, Kiowa, Caddo, Ohlone, Powhatan, etc.)

Usage:
    python enrich_indigenous.py --dry-run          # Preview changes
    python enrich_indigenous.py --batch 1          # Run batch 1 only
    python enrich_indigenous.py --all              # Run all batches
    python enrich_indigenous.py --report           # Report-only, no changes
"""

import json
import sys
import os
import argparse
from pathlib import Path
from datetime import datetime

TRACKER_DIR = Path(__file__).parent.parent
DATA_FILE = TRACKER_DIR / "data" / "data.json"
AUDIT_FILE = TRACKER_DIR / "data" / "indigenous_audit_results.json"

# Import the reference database from comprehensive_update
sys.path.insert(0, str(Path(__file__).parent))
from comprehensive_update import (
    INDIGENOUS_PEOPLES_BY_JURISDICTION,
    INDIGENOUS_CULTURAL_CONCEPTS,
    GEOGRAPHIC_INDIGENOUS_INDEX,
)

# ---------------------------------------------------------------------------
# JURISDICTION DETECTION — map text keywords to jurisdictions
# ---------------------------------------------------------------------------
JURISDICTION_KEYWORDS = {
    'Alabama': ['alabama', 'moundville', 'russell cave', 'mobile bay', 'huntsville'],
    'Alaska': ['alaska', 'tongass', 'denali', 'kodiak', 'aleutian', 'north slope', 'fairbanks', 'anchorage', 'juneau'],
    'Arizona': ['arizona', 'grand canyon', 'canyon de chelly', 'navajo', 'monument valley', 'casa grande', 'phoenix', 'tucson', 'oak flat'],
    'Arkansas': ['arkansas', 'toltec mounds', 'ozarks', 'hot springs'],
    'California': ['california', 'los angeles', 'san francisco', 'oakland', 'bay area', 'yosemite', 'channel islands', 'joshua tree', 'death valley', 'sequoia', 'point reyes', 'lava beds', 'alcatraz', 'sacramento', 'san diego'],
    'Colorado': ['colorado', 'mesa verde', 'sand creek', 'chimney rock', 'canyons of the ancients', 'hovenweep', 'denver', 'great sand dunes'],
    'Connecticut': ['connecticut', 'mashantucket', 'mohegan', 'mystic', 'pequot'],
    'Delaware': ['delaware state', 'delmarva'],
    'District of Columbia': ['washington, d.c.', 'washington dc', 'washington d.c', 'district of columbia', 'national mall', 'smithsonian', 'anacostia', 'capitol hill', 'potomac', 'national museum of the american indian', 'nmai'],
    'Florida': ['florida', 'everglades', 'big cypress', 'seminole', 'st. augustine', 'castillo de san marcos', 'cape canaveral', 'crystal river', 'key marco', 'miami', 'tampa', 'jacksonville'],
    'Georgia': ['georgia', 'ocmulgee', 'etowah', 'savannah', 'atlanta', 'new echota', 'sapelo', 'jekyll island', 'fort frederica'],
    'Hawaii': ['hawaii', 'hawai\'i', 'hawaiʻi', 'maui', 'oahu', 'o\'ahu', 'kauai', 'kaua\'i', 'mauna kea', 'maunakea', 'haleakala', 'kilauea', 'honolulu', 'pearl harbor', 'iolani'],
    'Idaho': ['idaho', 'nez perce', 'craters of the moon', 'boise', 'camas prairie', 'bear river massacre'],
    'Illinois': ['illinois', 'cahokia', 'chicago', 'starved rock', 'dickson mounds'],
    'Indiana': ['indiana', 'angel mounds', 'tippecanoe', 'prophetstown', 'indiana dunes'],
    'Iowa': ['iowa', 'effigy mounds', 'blood run', 'meskwaki', 'des moines'],
    'Kansas': ['kansas', 'council grove', 'fort larned', 'el quartelejo', 'pawnee indian museum'],
    'Kentucky': ['kentucky', 'mammoth cave', 'wickliffe', 'cumberland gap'],
    'Louisiana': ['louisiana', 'poverty point', 'new orleans', 'natchitoches', 'baton rouge', 'isle de jean charles'],
    'Maine': ['maine', 'acadia', 'katahdin', 'penobscot', 'passamaquoddy', 'wabanaki'],
    'Maryland': ['maryland', 'chesapeake', 'annapolis', 'baltimore', 'piscataway park', 'st. mary\'s city'],
    'Massachusetts': ['massachusetts', 'plymouth', 'cape cod', 'martha\'s vineyard', 'boston', 'wampanoag', 'deerfield'],
    'Michigan': ['michigan', 'isle royale', 'sleeping bear', 'pictured rocks', 'detroit', 'keweenaw', 'mackinac'],
    'Minnesota': ['minnesota', 'pipestone', 'grand portage', 'voyageurs', 'bdote', 'minneapolis', 'st. paul', 'mankato'],
    'Mississippi': ['mississippi state', 'nanih waiya', 'natchez trace', 'vicksburg', 'tupelo', 'winterville'],
    'Missouri': ['missouri', 'gateway arch', 'st. louis', 'osage village', 'towosahgy', 'trail of tears state park'],
    'Montana': ['montana', 'glacier national', 'little bighorn', 'big hole', 'bear paw', 'billings', 'missoula'],
    'Nebraska': ['nebraska', 'agate fossil', 'scotts bluff', 'chimney rock', 'homestead', 'omaha', 'lincoln'],
    'Nevada': ['nevada', 'great basin', 'pyramid lake', 'las vegas', 'reno', 'spirit cave'],
    'New Hampshire': ['new hampshire', 'mount washington', 'lake winnipesaukee'],
    'New Jersey': ['new jersey', 'ramapough', 'lenape', 'delaware water gap'],
    'New Mexico': ['new mexico', 'chaco', 'bandelier', 'gila cliff', 'aztec ruins', 'petroglyph', 'taos pueblo', 'acoma', 'santa fe', 'albuquerque', 'white sands'],
    'New York': ['new york', 'manhattan', 'ganondagan', 'fort stanwix', 'onondaga lake', 'finger lakes', 'long island', 'brooklyn', 'buffalo', 'albany'],
    'North Carolina': ['north carolina', 'blue ridge', 'great smoky', 'qualla', 'cherokee, nc', 'town creek', 'raleigh', 'charlotte', 'asheville', 'outer banks'],
    'North Dakota': ['north dakota', 'theodore roosevelt national', 'knife river', 'fort union', 'bismarck', 'fargo'],
    'Ohio': ['ohio', 'hopewell', 'serpent mound', 'newark earthworks', 'fort ancient', 'flint ridge', 'gnadenhutten', 'columbus', 'cleveland', 'cincinnati'],
    'Oklahoma': ['oklahoma', 'washita', 'spiro mounds', 'chickasaw national recreation', 'tahlequah', 'tulsa', 'oklahoma city', 'indian territory'],
    'Oregon': ['oregon', 'crater lake', 'john day', 'oregon caves', 'portland', 'salem', 'columbia river', 'celilo'],
    'Pennsylvania': ['pennsylvania', 'valley forge', 'philadelphia', 'gettysburg', 'meadowcroft', 'delaware water gap', 'pittsburgh', 'harrisburg'],
    'Puerto Rico': ['puerto rico', 'borikén', 'borinquen', 'boricua', 'caguana', 'tibes', 'san juan', 'ponce', 'arecibo'],
    'Rhode Island': ['rhode island', 'narragansett', 'providence', 'newport'],
    'South Carolina': ['south carolina', 'congaree', 'fort sumter', 'charleston', 'columbia, sc'],
    'South Dakota': ['south dakota', 'badlands', 'wind cave', 'mount rushmore', 'crazy horse memorial', 'pine ridge', 'wounded knee', 'bear butte', 'rapid city', 'black hills'],
    'Tennessee': ['tennessee', 'great smoky', 'shiloh', 'stones river', 'nashville', 'memphis', 'pinson mounds', 'red clay'],
    'Texas': ['texas', 'big bend', 'guadalupe mountains', 'alibates', 'palo duro', 'san antonio missions', 'houston', 'austin', 'dallas', 'el paso'],
    'US Virgin Islands': ['virgin islands', 'usvi', 'st. croix', 'st. thomas', 'st. john', 'salt river bay'],
    'Utah': ['utah', 'bears ears', 'canyonlands', 'arches', 'capitol reef', 'natural bridges', 'grand staircase', 'salt lake', 'zion'],
    'Vermont': ['vermont', 'green mountains', 'lake champlain', 'burlington', 'abenaki'],
    'Virginia': ['virginia', 'jamestown', 'shenandoah', 'williamsburg', 'yorktown', 'colonial national', 'werowocomoco', 'richmond', 'norfolk', 'natural bridge'],
    'Washington': ['washington state', 'olympic national', 'mount rainier', 'tahoma', 'north cascades', 'san juan island', 'seattle', 'tacoma', 'spokane', 'makah', 'ozette'],
    'West Virginia': ['west virginia', 'new river gorge', 'grave creek mound', 'charleston, wv'],
    'Wisconsin': ['wisconsin', 'apostle islands', 'aztalan', 'milwaukee', 'madison', 'green bay', 'menominee forest'],
    'Wyoming': ['wyoming', 'yellowstone', 'grand teton', 'devils tower', 'bear lodge', 'medicine wheel', 'fort laramie', 'wind river', 'cheyenne'],
    'Guam': ['guam', 'guåhan', 'chamorro', 'chamoru'],
    'American Samoa': ['american samoa', 'pago pago', 'tutuila'],
    'Northern Mariana Islands (CNMI)': ['northern mariana', 'cnmi', 'saipan', 'tinian', 'rota'],
    'Republic of the Marshall Islands': ['marshall islands', 'marshallese', 'bikini atoll', 'enewetak', 'majuro', 'kwajalein'],
    'Republic of Palau (Belau)': ['palau', 'belau', 'palauan'],
    'Federated States of Micronesia': ['micronesia', 'chuuk', 'pohnpei', 'kosrae', 'yap', 'nan madol'],
}


def load_data():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)


def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def get_entry_text(entry):
    """Collect all searchable text from an entry."""
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


def detect_jurisdictions(text):
    """Detect which US jurisdictions are referenced in text."""
    text_lower = text.lower()
    found = []
    for jurisdiction, keywords in JURISDICTION_KEYWORDS.items():
        for kw in keywords:
            if kw.lower() in text_lower:
                found.append(jurisdiction)
                break
    return found


def get_peoples_for_jurisdictions(jurisdictions):
    """Get all Indigenous peoples associated with a set of jurisdictions."""
    peoples = {}
    for jur in jurisdictions:
        if jur in INDIGENOUS_PEOPLES_BY_JURISDICTION:
            jur_data = INDIGENOUS_PEOPLES_BY_JURISDICTION[jur]
            jur_peoples = []
            for key in ('federally_recognized', 'state_recognized', 'displaced_peoples',
                       'indigenous_peoples', 'unrecognized_with_presence'):
                if key in jur_data:
                    jur_peoples.extend(jur_data[key])
            peoples[jur] = {
                'peoples': jur_peoples,
                'concepts': jur_data.get('cultural_concepts', []),
                'resources': jur_data.get('cultural_resources', []),
            }
    return peoples


def build_people_sentence(jurisdiction, peoples_list, max_names=8):
    """Build a concise sentence naming specific peoples for a jurisdiction."""
    names = []
    for p in peoples_list:
        primary = p.split('—')[0].strip()
        # Clean parentheticals for brevity but keep alternate names
        if '(' in primary:
            base = primary.split('(')[0].strip()
            alt = primary.split('(')[1].split(')')[0].strip()
            # Only include alt if it's a self-designation
            if len(alt) < 30 and '/' in primary:
                names.append(primary)
            else:
                names.append(base)
        else:
            names.append(primary)
        if len(names) >= max_names:
            break

    if not names:
        return ''

    if len(names) == 1:
        return f'the {names[0]} of {jurisdiction}'
    elif len(names) == 2:
        return f'the {names[0]} and {names[1]} of {jurisdiction}'
    else:
        return f'the {", ".join(names[:-1])}, and {names[-1]} of {jurisdiction}'


def build_displaced_sentence(jurisdiction, peoples_list):
    """Build a sentence specifically about displaced/removed peoples."""
    displaced = []
    for p in peoples_list:
        if '—' in p and any(word in p.lower() for word in
                           ['removed', 'displaced', 'destroyed', 'forced', 'massacre',
                            'relocated', 'fled', 'ancestral', 'trail of tears']):
            displaced.append(p)

    if not displaced:
        return ''

    names = []
    for d in displaced[:5]:
        name = d.split('—')[0].strip()
        if '(' in name:
            name = name.split('(')[0].strip()
        context = d.split('—')[1].strip() if '—' in d else ''
        if context:
            names.append(f'{name} ({context[:80]})')
        else:
            names.append(name)

    return (f'The ancestral homelands of {jurisdiction} belong to peoples who were forcibly '
            f'displaced, including {"; ".join(names)}. '
            f'Their cultural resources — burial sites, ceremonial grounds, village sites, '
            f'and sacred places — remain on these lands under federal management.')


def enrich_indigenous_impact(entry, jurisdictions, peoples_by_jur):
    """Add specific tribal nation names and cultural details to an entry's
    indigenous impact section. Returns (modified_entry, changes_made_list)."""
    changes = []
    impact = entry.get('I', {})

    # Find the indigenous impact key
    indigenous_key = None
    for k in ('indigenous', 'Indigenous', 'Indigenous/Tribal', 'indigenousTribal'):
        if k in impact:
            indigenous_key = k
            break

    if not indigenous_key:
        # Create a new indigenous impact section
        indigenous_key = 'indigenous'
        impact[indigenous_key] = {
            'people': '', 'places': '', 'practices': '', 'treasures': ''
        }
        entry['I'] = impact
        changes.append(f'Created new indigenous impact section')

    block = impact[indigenous_key]
    if not isinstance(block, dict):
        block = {'people': str(block), 'places': '', 'practices': '', 'treasures': ''}
        impact[indigenous_key] = block

    # Ensure PPPT keys exist
    for pppt in ('people', 'places', 'practices', 'treasures'):
        if pppt not in block:
            block[pppt] = ''

    # Check what's already named
    existing_text = ' '.join(v for v in block.values() if isinstance(v, str)).lower()

    # Build enrichment for each jurisdiction
    for jur, jur_info in peoples_by_jur.items():
        jur_data = INDIGENOUS_PEOPLES_BY_JURISDICTION.get(jur, {})

        # --- PEOPLE ---
        peoples_to_add = []
        for p in jur_info['peoples']:
            primary = p.split('—')[0].split('(')[0].strip()
            if primary.lower() not in existing_text and len(primary) > 2:
                peoples_to_add.append(p)

        if peoples_to_add:
            people_text = build_people_sentence(jur, peoples_to_add)
            displaced_text = build_displaced_sentence(
                jur,
                jur_data.get('displaced_peoples', [])
            )
            addition = ''
            if people_text:
                addition += f' This action affects the ancestral and contemporary territories of {people_text}.'
            if displaced_text and displaced_text.split('—')[0].split('(')[0].strip().lower() not in existing_text:
                addition += f' {displaced_text}'

            if addition:
                block['people'] = (block['people'].rstrip() + addition).strip()
                changes.append(f'Added {len(peoples_to_add)} named peoples for {jur}')

        # --- PLACES ---
        resources_to_add = []
        for r in jur_info.get('resources', []):
            resource_name = r.split('—')[0].split('(')[0].strip()
            if resource_name.lower() not in existing_text and len(resource_name) > 3:
                resources_to_add.append(r)

        if resources_to_add:
            resource_text = '; '.join(resources_to_add[:5])
            addition = f' Cultural resources in {jur} include: {resource_text}.'
            block['places'] = (block['places'].rstrip() + addition).strip()
            changes.append(f'Added {len(resources_to_add[:5])} cultural resources for {jur}')

        # --- PRACTICES ---
        concepts_to_add = []
        for c in jur_info.get('concepts', []):
            concept_name = c.split('—')[0].split('(')[0].strip()
            if concept_name.lower() not in existing_text and len(concept_name) > 3:
                concepts_to_add.append(c)

        if concepts_to_add:
            concept_text = '; '.join(concepts_to_add[:4])
            addition = f' Indigenous cultural practices and concepts relevant to {jur}: {concept_text}.'
            block['practices'] = (block['practices'].rstrip() + addition).strip()
            changes.append(f'Added {len(concepts_to_add[:4])} cultural concepts for {jur}')

        # --- TREASURES ---
        # Add cultural items relevant to the region's peoples
        treasures_to_add = []
        jur_lower = jur.lower()
        # Map jurisdictions to cultural item categories
        region_items = {
            'southeast': ['Stomp Dance regalia', 'rivercane baskets', 'shell gorgets', 'chunkey stones', 'copper plates from Mississippian era'],
            'northeast': ['Wampum belts', 'birch bark scrolls', 'Haudenosaunee false face masks', 'moose hair embroidery'],
            'plains': ['Star quilts', 'parfleche containers', 'porcupine quillwork', 'Sun Dance lodges', 'tipi covers with winter counts'],
            'southwest': ['Katsina/Kachina carvings', 'Navajo weavings', 'Pueblo pottery', 'turquoise and silver jewelry', 'sand paintings'],
            'northwest': ['Totem poles', 'bentwood boxes', 'button blankets', 'cedar bark textiles', 'formline art'],
            'california': ['Coiled baskets', 'abalone shell regalia', 'tule boats', 'acorn granaries', 'obsidian blades'],
            'pacific': ['Siapo/tapa cloth', '\'Ie Tōga fine mats', 'carved storyboards', 'latte stones', 'stick navigation charts'],
        }
        se_states = {'alabama', 'georgia', 'tennessee', 'mississippi', 'florida',
                     'south carolina', 'north carolina', 'louisiana'}
        ne_states = {'new york', 'connecticut', 'massachusetts', 'maine', 'rhode island',
                     'new hampshire', 'vermont', 'pennsylvania', 'new jersey', 'delaware',
                     'maryland', 'district of columbia', 'virginia', 'west virginia'}
        plains_states = {'montana', 'north dakota', 'south dakota', 'nebraska', 'kansas',
                        'oklahoma', 'wyoming', 'colorado'}
        sw_states = {'arizona', 'new mexico', 'utah'}
        nw_states = {'washington', 'oregon', 'alaska', 'idaho'}
        ca_states = {'california', 'nevada'}
        pacific_territories = {'guam', 'american samoa', 'northern mariana islands (cnmi)',
                              'republic of the marshall islands', 'republic of palau (belau)',
                              'federated states of micronesia', 'hawaii', 'us virgin islands',
                              'puerto rico'}

        region = None
        if jur_lower in se_states:
            region = 'southeast'
        elif jur_lower in ne_states:
            region = 'northeast'
        elif jur_lower in plains_states:
            region = 'plains'
        elif jur_lower in sw_states:
            region = 'southwest'
        elif jur_lower in nw_states:
            region = 'northwest'
        elif jur_lower in ca_states:
            region = 'california'
        elif jur_lower in pacific_territories:
            region = 'pacific'

        if region and region in region_items:
            for item in region_items[region]:
                if item.lower() not in existing_text:
                    treasures_to_add.append(item)

        if treasures_to_add:
            treasure_text = ', '.join(treasures_to_add[:5])
            addition = f' Indigenous cultural treasures of this region include {treasure_text}.'
            block['treasures'] = (block['treasures'].rstrip() + addition).strip()
            changes.append(f'Added {len(treasures_to_add[:5])} cultural treasures for {jur}')

    return entry, changes


def run_enrichment(data, batch_num=None, dry_run=True, report_only=False):
    """Run enrichment across all categories in data."""
    stats = {'entries_checked': 0, 'entries_enriched': 0, 'changes': []}
    categories = ['executive_actions', 'legislation', 'litigation',
                  'agency_actions', 'international']

    for cat in categories:
        if cat not in data or not isinstance(data[cat], list):
            continue

        for i, entry in enumerate(data[cat]):
            stats['entries_checked'] += 1
            entry_id = entry.get('i', f'{cat}[{i}]')
            text = get_entry_text(entry)

            # Detect jurisdictions
            jurisdictions = detect_jurisdictions(text)
            if not jurisdictions:
                continue

            # Check if entry involves Indigenous cultural resources
            text_lower = text.lower()
            from comprehensive_update import INDIGENOUS_SIGNAL_KEYWORDS
            signal_count = sum(1 for kw in INDIGENOUS_SIGNAL_KEYWORDS
                              if kw.lower() in text_lower)
            if signal_count == 0:
                continue

            # Get peoples for detected jurisdictions
            peoples_by_jur = get_peoples_for_jurisdictions(jurisdictions)
            if not peoples_by_jur:
                continue

            # Apply batch filtering
            has_indigenous_section = any(
                k in entry.get('I', {})
                for k in ('indigenous', 'Indigenous', 'Indigenous/Tribal', 'indigenousTribal')
            )
            is_se_va_dc = any(
                j in jurisdictions
                for j in ('Virginia', 'District of Columbia', 'Maryland',
                         'Georgia', 'Tennessee', 'South Carolina', 'Alabama',
                         'North Carolina', 'Florida', 'Mississippi', 'Louisiana')
            )

            if batch_num == 1 and not is_se_va_dc:
                continue
            elif batch_num == 2 and not has_indigenous_section:
                continue
            elif batch_num == 3:
                # Only entries that mention places with missing nations
                pass  # Process all that match

            if report_only:
                print(f'  [{cat}] {entry_id}: jurisdictions={jurisdictions}, '
                      f'has_indigenous={has_indigenous_section}')
                continue

            # Enrich
            entry, changes = enrich_indigenous_impact(entry, jurisdictions, peoples_by_jur)
            if changes:
                stats['entries_enriched'] += 1
                stats['changes'].append({
                    'id': entry_id,
                    'category': cat,
                    'jurisdictions': jurisdictions,
                    'changes': changes,
                })
                if not dry_run:
                    data[cat][i] = entry
                print(f'  [{cat}] {entry_id}: {len(changes)} changes — {"; ".join(changes[:3])}')

    return data, stats


def main():
    parser = argparse.ArgumentParser(
        description='TCKC Threat Tracker — Indigenous Peoples Enrichment',
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument('--batch', type=int, choices=[1, 2, 3],
                       help='Run specific batch (1=SE/VA/DC, 2=generic-only, 3=missing nations)')
    parser.add_argument('--all', action='store_true', help='Run all batches')
    parser.add_argument('--dry-run', action='store_true', help='Preview without saving')
    parser.add_argument('--report', action='store_true', help='Report-only, no changes')

    args = parser.parse_args()

    if not args.batch and not args.all and not args.report:
        parser.print_help()
        sys.exit(1)

    print(f'=== TCKC Indigenous Enrichment — {datetime.now().strftime("%Y-%m-%d %H:%M")} ===')

    data = load_data()
    total_entries = sum(len(v) for v in data.values() if isinstance(v, list))
    print(f'Loaded {total_entries} entries from data.json')

    if args.report:
        print('\n--- REPORT MODE ---')
        _, stats = run_enrichment(data, report_only=True)
        print(f'\nEntries checked: {stats["entries_checked"]}')
        sys.exit(0)

    batches = [args.batch] if args.batch else [1, 2, 3]
    total_enriched = 0

    for batch in batches:
        print(f'\n--- BATCH {batch} ---')
        data, stats = run_enrichment(data, batch_num=batch, dry_run=args.dry_run)
        print(f'Checked: {stats["entries_checked"]}, Enriched: {stats["entries_enriched"]}')
        total_enriched += stats['entries_enriched']

        # Save change log
        if stats['changes']:
            log_file = TRACKER_DIR / f'enrichment_log_batch{batch}_{datetime.now().strftime("%Y%m%d_%H%M")}.json'
            with open(log_file, 'w') as f:
                json.dump(stats['changes'], f, indent=2, ensure_ascii=False)
            print(f'Change log: {log_file.name}')

    if not args.dry_run and total_enriched > 0:
        save_data(data)
        print(f'\nSaved data.json — {total_enriched} entries enriched across {len(batches)} batch(es)')
    elif args.dry_run:
        print(f'\nDRY RUN — {total_enriched} entries would be enriched (no changes saved)')
    else:
        print(f'\nNo entries needed enrichment')


if __name__ == '__main__':
    main()
