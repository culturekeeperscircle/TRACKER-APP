#!/usr/bin/env python3
"""
TCKC Threat Tracker — Unified Enrichment Script
================================================
Consolidates the functionality of four former scripts:
  - enrich_indigenous.py        → --community indigenous
  - enrich_african_descendant.py → --community african-descendant
  - enrich_targeted_gaps.py      → --community targeted-gaps
  - fix_impact_analyses.py       → --community fix-impacts

Usage:
    python enrich_entries.py --community indigenous --dry-run
    python enrich_entries.py --community african-descendant --all
    python enrich_entries.py --community targeted-gaps --all
    python enrich_entries.py --community fix-impacts --all
    python enrich_entries.py --community all --dry-run          # Run all enrichments
    python enrich_entries.py --report                            # Report-only across all
"""

import json
import sys
import argparse
from pathlib import Path
from datetime import datetime

TRACKER_DIR = Path(__file__).parent.parent
DATA_FILE = TRACKER_DIR / "data" / "data.json"
LOGS_DIR = TRACKER_DIR / "pipeline" / "logs" / "enrichment"

CATEGORIES = ['executive_actions', 'legislation', 'litigation',
              'agency_actions', 'international']


# ── SHARED UTILITIES ─────────────────────────────────────────────────────────

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


def ensure_pppt(block):
    """Ensure a block has all 4P keys."""
    for pppt in ('people', 'places', 'practices', 'treasures'):
        block.setdefault(pppt, '')
    return block


def save_log(community_type, stats):
    """Save enrichment change log."""
    if not stats.get('changes'):
        return
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    log_file = LOGS_DIR / f'{community_type}_{datetime.now().strftime("%Y%m%d_%H%M")}.json'
    with open(log_file, 'w') as f:
        json.dump(stats['changes'], f, indent=2, ensure_ascii=False)
    print(f'Change log: {log_file.name}')


# ── JURISDICTION DETECTION ───────────────────────────────────────────────────
# Shared by indigenous and african-descendant enrichment

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


# ── REGION MAPPING (shared by indigenous + african-descendant treasures) ─────

SE_STATES = {'alabama', 'georgia', 'tennessee', 'mississippi', 'florida',
             'south carolina', 'north carolina', 'louisiana', 'arkansas', 'virginia'}
NE_STATES = {'new york', 'connecticut', 'massachusetts', 'maine', 'rhode island',
             'new hampshire', 'vermont', 'pennsylvania', 'new jersey', 'delaware',
             'maryland', 'district of columbia', 'west virginia'}
PLAINS_STATES = {'montana', 'north dakota', 'south dakota', 'nebraska', 'kansas',
                 'oklahoma', 'wyoming', 'colorado'}
SW_STATES = {'arizona', 'new mexico', 'utah'}
NW_STATES = {'washington', 'oregon', 'alaska', 'idaho'}
CA_STATES = {'california', 'nevada'}
MW_STATES = {'illinois', 'michigan', 'ohio', 'indiana', 'missouri', 'minnesota',
             'iowa', 'wisconsin', 'kansas'}
WEST_STATES = {'california', 'colorado', 'texas', 'oklahoma', 'arizona', 'nevada',
               'oregon', 'washington'}
PACIFIC_TERRITORIES = {'guam', 'american samoa', 'northern mariana islands (cnmi)',
                       'republic of the marshall islands', 'republic of palau (belau)',
                       'federated states of micronesia', 'hawaii', 'us virgin islands',
                       'puerto rico'}


def get_region(jurisdiction):
    """Map a jurisdiction to a cultural region."""
    jur_lower = jurisdiction.lower()
    if jur_lower in SE_STATES:
        return 'southeast'
    elif jur_lower in NE_STATES:
        return 'northeast'
    elif jur_lower in PLAINS_STATES:
        return 'plains'
    elif jur_lower in SW_STATES:
        return 'southwest'
    elif jur_lower in NW_STATES:
        return 'northwest'
    elif jur_lower in CA_STATES:
        return 'california'
    elif jur_lower in PACIFIC_TERRITORIES:
        return 'pacific'
    elif jur_lower in MW_STATES:
        return 'midwest'
    elif jur_lower in WEST_STATES:
        return 'west'
    return None


# ═══════════════════════════════════════════════════════════════════════════════
# INDIGENOUS ENRICHMENT
# ═══════════════════════════════════════════════════════════════════════════════

def _import_indigenous_refs():
    """Lazy import the reference databases from comprehensive_update."""
    sys.path.insert(0, str(Path(__file__).parent))
    from comprehensive_update import (
        INDIGENOUS_PEOPLES_BY_JURISDICTION,
        INDIGENOUS_CULTURAL_CONCEPTS,
        GEOGRAPHIC_INDIGENOUS_INDEX,
        INDIGENOUS_SIGNAL_KEYWORDS,
    )
    return {
        'peoples': INDIGENOUS_PEOPLES_BY_JURISDICTION,
        'concepts': INDIGENOUS_CULTURAL_CONCEPTS,
        'geo_index': GEOGRAPHIC_INDIGENOUS_INDEX,
        'signals': INDIGENOUS_SIGNAL_KEYWORDS,
    }


INDIGENOUS_REGION_TREASURES = {
    'southeast': ['Stomp Dance regalia', 'rivercane baskets', 'shell gorgets', 'chunkey stones', 'copper plates from Mississippian era'],
    'northeast': ['Wampum belts', 'birch bark scrolls', 'Haudenosaunee false face masks', 'moose hair embroidery'],
    'plains': ['Star quilts', 'parfleche containers', 'porcupine quillwork', 'Sun Dance lodges', 'tipi covers with winter counts'],
    'southwest': ['Katsina/Kachina carvings', 'Navajo weavings', 'Pueblo pottery', 'turquoise and silver jewelry', 'sand paintings'],
    'northwest': ['Totem poles', 'bentwood boxes', 'button blankets', 'cedar bark textiles', 'formline art'],
    'california': ['Coiled baskets', 'abalone shell regalia', 'tule boats', 'acorn granaries', 'obsidian blades'],
    'pacific': ['Siapo/tapa cloth', '\'Ie Tōga fine mats', 'carved storyboards', 'latte stones', 'stick navigation charts'],
}


def build_people_sentence(jurisdiction, peoples_list, max_names=8):
    names = []
    for p in peoples_list:
        primary = p.split('—')[0].strip()
        if '(' in primary:
            base = primary.split('(')[0].strip()
            if '/' in primary and len(primary.split('(')[1].split(')')[0].strip()) < 30:
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


def enrich_indigenous_impact(entry, jurisdictions, peoples_by_jur, refs):
    """Add specific tribal nation names and cultural details to indigenous impact."""
    changes = []
    impact = entry.get('I', {})

    indigenous_key = None
    for k in ('indigenous', 'Indigenous', 'Indigenous/Tribal', 'indigenousTribal'):
        if k in impact:
            indigenous_key = k
            break

    if not indigenous_key:
        indigenous_key = 'indigenous'
        impact[indigenous_key] = {'people': '', 'places': '', 'practices': '', 'treasures': ''}
        entry['I'] = impact
        changes.append('Created new indigenous impact section')

    block = impact[indigenous_key]
    if not isinstance(block, dict):
        block = {'people': str(block), 'places': '', 'practices': '', 'treasures': ''}
        impact[indigenous_key] = block

    ensure_pppt(block)
    existing_text = ' '.join(v for v in block.values() if isinstance(v, str)).lower()

    for jur, jur_info in peoples_by_jur.items():
        jur_data = refs['peoples'].get(jur, {})

        # PEOPLE
        peoples_to_add = [p for p in jur_info['peoples']
                         if p.split('—')[0].split('(')[0].strip().lower() not in existing_text
                         and len(p.split('—')[0].split('(')[0].strip()) > 2]
        if peoples_to_add:
            people_text = build_people_sentence(jur, peoples_to_add)
            displaced_text = build_displaced_sentence(jur, jur_data.get('displaced_peoples', []))
            addition = ''
            if people_text:
                addition += f' This action affects the ancestral and contemporary territories of {people_text}.'
            if displaced_text and displaced_text.split('—')[0].split('(')[0].strip().lower() not in existing_text:
                addition += f' {displaced_text}'
            if addition:
                block['people'] = (block['people'].rstrip() + addition).strip()
                changes.append(f'Added {len(peoples_to_add)} named peoples for {jur}')

        # PLACES
        resources_to_add = [r for r in jur_info.get('resources', [])
                           if r.split('—')[0].split('(')[0].strip().lower() not in existing_text
                           and len(r.split('—')[0].split('(')[0].strip()) > 3]
        if resources_to_add:
            resource_text = '; '.join(resources_to_add[:5])
            addition = f' Cultural resources in {jur} include: {resource_text}.'
            block['places'] = (block['places'].rstrip() + addition).strip()
            changes.append(f'Added {len(resources_to_add[:5])} cultural resources for {jur}')

        # PRACTICES
        concepts_to_add = [c for c in jur_info.get('concepts', [])
                          if c.split('—')[0].split('(')[0].strip().lower() not in existing_text
                          and len(c.split('—')[0].split('(')[0].strip()) > 3]
        if concepts_to_add:
            concept_text = '; '.join(concepts_to_add[:4])
            addition = f' Indigenous cultural practices and concepts relevant to {jur}: {concept_text}.'
            block['practices'] = (block['practices'].rstrip() + addition).strip()
            changes.append(f'Added {len(concepts_to_add[:4])} cultural concepts for {jur}')

        # TREASURES
        region = get_region(jur)
        if region and region in INDIGENOUS_REGION_TREASURES:
            treasures_to_add = [item for item in INDIGENOUS_REGION_TREASURES[region]
                               if item.lower() not in existing_text]
            if treasures_to_add:
                treasure_text = ', '.join(treasures_to_add[:5])
                addition = f' Indigenous cultural treasures of this region include {treasure_text}.'
                block['treasures'] = (block['treasures'].rstrip() + addition).strip()
                changes.append(f'Added {len(treasures_to_add[:5])} cultural treasures for {jur}')

    return entry, changes


def run_indigenous_enrichment(data, batch_num=None, dry_run=True, report_only=False):
    refs = _import_indigenous_refs()
    stats = {'entries_checked': 0, 'entries_enriched': 0, 'changes': []}

    for cat in CATEGORIES:
        if cat not in data or not isinstance(data[cat], list):
            continue
        for i, entry in enumerate(data[cat]):
            stats['entries_checked'] += 1
            entry_id = entry.get('i', f'{cat}[{i}]')
            text = get_entry_text(entry)
            jurisdictions = detect_jurisdictions(text)
            if not jurisdictions:
                continue

            text_lower = text.lower()
            signal_count = sum(1 for kw in refs['signals'] if kw.lower() in text_lower)
            if signal_count == 0:
                continue

            # Get peoples for detected jurisdictions
            peoples_by_jur = {}
            for jur in jurisdictions:
                if jur in refs['peoples']:
                    jur_data = refs['peoples'][jur]
                    jur_peoples = []
                    for key in ('federally_recognized', 'state_recognized', 'displaced_peoples',
                               'indigenous_peoples', 'unrecognized_with_presence'):
                        if key in jur_data:
                            jur_peoples.extend(jur_data[key])
                    peoples_by_jur[jur] = {
                        'peoples': jur_peoples,
                        'concepts': jur_data.get('cultural_concepts', []),
                        'resources': jur_data.get('cultural_resources', []),
                    }
            if not peoples_by_jur:
                continue

            # Batch filtering
            if batch_num:
                has_indigenous_section = any(
                    k in entry.get('I', {})
                    for k in ('indigenous', 'Indigenous', 'Indigenous/Tribal', 'indigenousTribal')
                )
                se_va_dc_jurs = {'Virginia', 'District of Columbia', 'Maryland', 'Georgia',
                                 'Tennessee', 'South Carolina', 'Alabama', 'North Carolina',
                                 'Florida', 'Mississippi', 'Louisiana'}
                is_se_va_dc = any(j in jurisdictions for j in se_va_dc_jurs)

                if batch_num == 1 and not is_se_va_dc:
                    continue
                elif batch_num == 2 and not has_indigenous_section:
                    continue

            if report_only:
                print(f'  [{cat}] {entry_id}: jurisdictions={jurisdictions}')
                continue

            entry, changes = enrich_indigenous_impact(entry, jurisdictions, peoples_by_jur, refs)
            if changes:
                stats['entries_enriched'] += 1
                stats['changes'].append({
                    'id': entry_id, 'category': cat,
                    'jurisdictions': jurisdictions, 'changes': changes,
                })
                if not dry_run:
                    data[cat][i] = entry
                print(f'  [{cat}] {entry_id}: {len(changes)} changes — {"; ".join(changes[:3])}')

    return data, stats


# ═══════════════════════════════════════════════════════════════════════════════
# AFRICAN DESCENDANT ENRICHMENT
# ═══════════════════════════════════════════════════════════════════════════════

def _import_african_descendant_refs():
    sys.path.insert(0, str(Path(__file__).parent))
    from comprehensive_update import (
        AFRICAN_DESCENDANT_PEOPLES_BY_JURISDICTION,
        AFRICAN_DESCENDANT_SIGNAL_KEYWORDS,
        AFRICAN_DESCENDANT_CULTURAL_CONCEPTS,
        GEOGRAPHIC_AFRICAN_DESCENDANT_INDEX,
    )
    return {
        'peoples': AFRICAN_DESCENDANT_PEOPLES_BY_JURISDICTION,
        'signals': AFRICAN_DESCENDANT_SIGNAL_KEYWORDS,
        'concepts': AFRICAN_DESCENDANT_CULTURAL_CONCEPTS,
        'geo_index': GEOGRAPHIC_AFRICAN_DESCENDANT_INDEX,
    }


AD_REGION_TREASURES = {
    'southeast': ['Gullah/Geechee sweetgrass baskets', 'quilts (Gee\'s Bend tradition)',
                  'wrought ironwork (West African metalworking)', 'indigo-dyed textiles',
                  'enslaved persons\' pottery (Edgefield/Colonoware)', 'shotgun house architecture'],
    'northeast': ['African Burial Ground artifacts', 'Schomburg Center collections',
                  'AME church institutional records', 'Harlem Renaissance artworks and manuscripts',
                  'Underground Railroad safe house documentation'],
    'midwest': ['Motown recordings and memorabilia', 'Chicago Blues recordings',
                'Great Migration oral histories and photographs', 'HBCU institutional archives'],
    'west': ['Black Panther Party archives and ephemera', 'Freedmen\'s town artifacts',
             'Buffalo Soldiers military artifacts', 'Black cowboy and rodeo heritage materials',
             'Juneteenth historical documentation'],
    'pacific': ['Vejigante masks and costumes (Loíza)', 'Bomba drums (barriles)',
                'Quelbe instruments', 'Mocko jumbie stilts and costumes',
                'Plantation-era archaeological artifacts'],
}


def build_community_sentence(jurisdiction, communities, max_items=5):
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


def enrich_african_descendant_impact(entry, jurisdictions, refs):
    changes = []
    impact = entry.get('I', {})

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

    ensure_pppt(block)
    existing_text = ' '.join(v for v in block.values() if isinstance(v, str)).lower()

    for jur in jurisdictions:
        if jur not in refs['peoples']:
            continue
        jur_data = refs['peoples'][jur]

        # PEOPLE
        communities = jur_data.get('communities', [])
        communities_to_add = [c for c in communities
                             if c.split('—')[0].split('(')[0].strip().split(',')[0].strip().lower() not in existing_text
                             and len(c.split('—')[0].split('(')[0].strip()) > 3]
        if communities_to_add:
            addition = ' ' + build_community_sentence(jur, communities_to_add)
            block['people'] = (block['people'].rstrip() + addition).strip()
            changes.append(f'Added {len(communities_to_add)} communities for {jur}')

        afro_indigenous = jur_data.get('afro_indigenous', [])
        ai_to_add = [ai for ai in afro_indigenous
                    if ai.split('—')[0].strip().lower() not in existing_text
                    and len(ai.split('—')[0].strip()) > 3]
        if ai_to_add:
            addition = ' ' + build_afro_indigenous_sentence(ai_to_add)
            block['people'] = (block['people'].rstrip() + addition).strip()
            changes.append(f'Added {len(ai_to_add)} Afro-Indigenous references for {jur}')

        # PLACES
        resources = jur_data.get('cultural_resources', [])
        resources_to_add = [r for r in resources
                           if r.split('—')[0].split('(')[0].strip().lower() not in existing_text
                           and len(r.split('—')[0].split('(')[0].strip()) > 3]
        if resources_to_add:
            resource_text = '; '.join(resources_to_add[:5])
            addition = f' African-descendant cultural resources in {jur}: {resource_text}.'
            block['places'] = (block['places'].rstrip() + addition).strip()
            changes.append(f'Added {len(resources_to_add[:5])} cultural resources for {jur}')

        # PRACTICES
        practices = jur_data.get('cultural_practices', [])
        practices_to_add = [p for p in practices
                           if p.split('—')[0].strip().lower() not in existing_text
                           and len(p.split('—')[0].strip()) > 3]
        if practices_to_add:
            practice_text = '; '.join(practices_to_add[:4])
            addition = f' Cultural practices in {jur}: {practice_text}.'
            block['practices'] = (block['practices'].rstrip() + addition).strip()
            changes.append(f'Added {len(practices_to_add[:4])} cultural practices for {jur}')

        # TREASURES
        region = get_region(jur)
        if region and region in AD_REGION_TREASURES:
            treasures_to_add = [item for item in AD_REGION_TREASURES[region]
                               if item.lower() not in existing_text]
            if treasures_to_add:
                treasure_text = ', '.join(treasures_to_add[:5])
                addition = f' African-descendant cultural treasures of this region include {treasure_text}.'
                block['treasures'] = (block['treasures'].rstrip() + addition).strip()
                changes.append(f'Added {len(treasures_to_add[:5])} cultural treasures for {jur}')

    return entry, changes


def run_african_descendant_enrichment(data, dry_run=True, report_only=False):
    refs = _import_african_descendant_refs()
    stats = {'entries_checked': 0, 'entries_enriched': 0, 'changes': []}

    for cat in CATEGORIES:
        if cat not in data or not isinstance(data[cat], list):
            continue
        for i, entry in enumerate(data[cat]):
            stats['entries_checked'] += 1
            entry_id = entry.get('i', entry.get('id', f'{cat}[{i}]'))
            text = get_entry_text(entry)
            text_lower = text.lower()

            signal_count = sum(1 for kw in refs['signals'] if kw.lower() in text_lower)
            if signal_count == 0:
                continue

            jurisdictions = detect_jurisdictions(text)
            if not jurisdictions:
                continue

            relevant_jurs = [j for j in jurisdictions
                           if j in refs['peoples']
                           and refs['peoples'][j].get('communities')]
            if not relevant_jurs:
                continue

            if report_only:
                print(f'  [{cat}] {entry_id}: jurisdictions={relevant_jurs[:5]}, signals={signal_count}')
                continue

            entry, changes = enrich_african_descendant_impact(entry, relevant_jurs, refs)
            if changes:
                stats['entries_enriched'] += 1
                stats['changes'].append({
                    'id': entry_id, 'category': cat,
                    'jurisdictions': relevant_jurs[:5], 'changes': changes,
                })
                if not dry_run:
                    data[cat][i] = entry
                print(f'  [{cat}] {entry_id}: {len(changes)} changes — {"; ".join(changes[:3])}')

    return data, stats


# ═══════════════════════════════════════════════════════════════════════════════
# TARGETED GAP ENRICHMENT
# ═══════════════════════════════════════════════════════════════════════════════

MIGRATION_ROUTES_TEXT = (
    ' The Great Migration moved 6 million African Americans from the South to '
    'northern, midwestern, and western cities in two waves (1910–1940, 1940–1970). '
    'Key routes: the Illinois Central Railroad ("the Chickenbone Express," $11.10 '
    'from Mississippi to Chicago) carried migrants from the Mississippi Delta, '
    'Arkansas, Tennessee, and Louisiana to Chicago, St. Louis, and Milwaukee; '
    'the Pennsylvania Railroad and Atlantic Coast Line carried migrants from '
    'South Carolina, Georgia, Virginia, and North Carolina to New York/Harlem, '
    'Philadelphia, Newark, Baltimore, Washington DC, and Boston; the Louisville '
    '& Nashville Railroad carried migrants from Alabama and Mississippi to '
    'Detroit, Cleveland, Cincinnati, and Indianapolis; and the Southern Pacific '
    'Railroad and Route 66 carried Second Wave migrants from Louisiana, Texas, '
    'Oklahoma, and Arkansas to Los Angeles, Oakland, Portland, Seattle, and '
    'Phoenix. These migration corridors transformed American culture: Delta Blues '
    'became Chicago Blues, southern gospel became Motown, and the Harlem '
    'Renaissance emerged from the convergence of southern Black migrants in New York.'
)

SPIRITUAL_SITES_TEXT = (
    ' African-derived spiritual and cultural sites in the US include: '
    'Oyotunji African Village (Sheldon, SC), the only Yoruba village in North '
    'America, founded 1970 by Oba Adefunmi I, maintaining Ogun, Oshun, Shango, '
    'and Obatala shrines and traditional Yoruba governance; Congo Square (New '
    'Orleans), where enslaved Africans gathered on Sundays to drum, dance, and '
    'maintain West African cultural traditions — the birthplace of American '
    'musical culture; the African Burial Ground National Monument (NYC), where '
    '15,000+ enslaved and free Africans were buried with African spiritual '
    'objects (1690s–1790s); the Church of Lukumi Babalu Aye (Hialeah, FL), '
    'which won the 1993 Supreme Court case establishing Santería/Lukumí animal '
    'sacrifice as protected religious practice; Gullah/Geechee praise houses '
    'on the Sea Islands (SC/GA), small wooden buildings where ring shout — '
    'the most direct West African worship survival in the Americas — is still '
    'practiced; and the canopied bottle tree tradition visible across the rural '
    'South (Mississippi, Alabama, South Carolina), a Kongo/BaKongo cosmological '
    'practice of trapping harmful spirits in blue bottles. These sites connect '
    'to the African continent\'s heritage sites: Goree Island/Door of No Return '
    '(Senegal), Cape Coast Castle and Elmina Castle (Ghana), Ouidah (Benin), '
    'and the Osun-Osogbo Sacred Grove (Nigeria, UNESCO World Heritage Site) — '
    'the spiritual source of Yoruba/Orisha traditions practiced in the diaspora.'
)

DELTA_SPECIFICITY_TEXT = (
    ' The Mississippi Delta — the alluvial floodplain between Memphis and '
    'Vicksburg — is the most culturally significant African-descendant region '
    'in the US. Specific communities and cultural landmarks: Clarksdale '
    '(crossroads of Highways 61 and 49; Muddy Waters, Son House, John Lee '
    'Hooker connections); Indianola (B.B. King\'s hometown); Ruleville (Fannie '
    'Lou Hamer\'s home — "I\'m sick and tired of being sick and tired"); Money '
    '(Bryant\'s Grocery, where 14-year-old Emmett Till was accused, 1955); '
    'Mound Bayou (all-Black town founded 1887, "Jewel of the Delta"); Dockery '
    'Plantation (birthplace of the Delta Blues — Charley Patton, Howlin\' Wolf, '
    'Roebuck Staples); Parchman Farm/Mississippi State Penitentiary (prison '
    'blues documented by John and Alan Lomax; Freedom Riders imprisoned 1961); '
    'Rolling Fork (Muddy Waters\'s birthplace); Greenwood (SNCC voter '
    'registration headquarters 1962–64); and the Hill Country Blues territory '
    'of Tate/Panola County (R.L. Burnside, Junior Kimbrough, Fred McDowell). '
    'The Delta\'s cultural practices include field hollers, juke joints, fife '
    'and drum (direct West African musical survival), river baptisms, Decoration '
    'Day/graveyard cleaning (ancestor veneration), and the hot tamale tradition '
    '(Afro-Latino culinary convergence).'
)

WORSHIP_SITES_TEXT = (
    ' Historic Black places of worship central to the African-descendant '
    'experience include: 16th Street Baptist Church (Birmingham — 1963 bombing '
    'killed four girls); Ebenezer Baptist Church (Atlanta — MLK Sr. and Jr. '
    'pastored); Mother Bethel AME Church (Philadelphia — founded 1794 by '
    'Richard Allen, birthplace of the AME denomination, Underground Railroad '
    'site); Emanuel AME Church (Charleston — "Mother Emanuel," founded 1816, '
    '2015 massacre killed 9); Abyssinian Baptist Church (Harlem — Adam Clayton '
    'Powell Jr., founded 1808); Mason Temple (Memphis — MLK delivered "I\'ve '
    'Been to the Mountaintop" April 3, 1968); Dexter Avenue King Memorial '
    'Baptist Church (Montgomery — bus boycott organized here); First African '
    'Baptist Church (Savannah — 1773, one of oldest Black churches; breathing '
    'holes in floor for Underground Railroad); Masjid Muhammad/The Nation\'s '
    'Mosque (DC — first mosque in America established for Islam, 1945); Mosque '
    'Maryam (Chicago — Nation of Islam HQ); Masjid Malcolm Shabazz (Harlem — '
    'formerly Malcolm X\'s mosque); and Beth Shalom B\'nai Zaken Ethiopian '
    'Hebrew Congregation (Chicago — oldest historically Black synagogue, 1918).'
)

HBCU_SPECIFICITY_TEXT = (
    ' The 107 HBCUs (Historically Black Colleges and Universities) are the most '
    'significant educational infrastructure in Black America. Key institutions: '
    'Howard University (DC, 1867 — preeminent HBCU, Moorland-Spingarn Research '
    'Center); Morehouse College (Atlanta — MLK Jr. alma mater); Spelman College '
    '(Atlanta — premier women\'s HBCU); Fisk University (Nashville — Jubilee '
    'Singers, W.E.B. Du Bois); Tuskegee University (Booker T. Washington, '
    'George Washington Carver); Hampton University (1868 — oldest African '
    'American museum); FAMU/Florida A&M (Marching 100); Xavier University of '
    'Louisiana (only historically Black Catholic university, #1 in placing '
    'Black students in medical school); Meharry Medical College (Nashville — '
    'first Black medical school in the South); Cheyney University (PA — oldest '
    'HBCU, 1837); Lincoln University (PA — Thurgood Marshall attended); Alcorn '
    'State (MS — oldest public HBCU); and Shaw University (Raleigh — SNCC '
    'founded here 1960).'
)

AFRO_INDIGENOUS_TEXT = (
    ' Afro-Indigenous communities represent the intersection of African-descendant '
    'and Indigenous histories: Freedmen of the Five Tribes (Cherokee, Chickasaw, '
    'Choctaw, Creek/Muscogee, Seminole — descendants of people enslaved by '
    'these nations, brought on the Trail of Tears, who fought for and in many '
    'cases won citizenship rights); Black Seminoles/Seminole Maroons (African-'
    'descended people who escaped enslavement and allied with Seminole, fought '
    'in all three Seminole Wars — "the largest slave rebellion in US history"; '
    'John Horse/Juan Caballo was a key leader; descendants persist in '
    'Brackettville, TX and Oklahoma); Mardi Gras Indians of New Orleans '
    '(African-descendant communities who honor relationships with Indigenous '
    'peoples through elaborate hand-beaded suits; tribes include Wild Magnolias, '
    'Guardians of the Flame — 200+ year tradition); and Gullah/Geechee-'
    'Indigenous connections along the Sea Islands coast.'
)

DIASPORA_TEXT = (
    ' African diaspora communities in the US include: Haitian (largest community '
    'in Little Haiti/Miami, also Flatbush/Brooklyn, Mattapan/Boston — Haitian '
    'Vodou, Rara, Compas/Konpa traditions; the Haitian Revolution of 1791–1804 '
    'was the only successful slave revolution in history); Somali (largest '
    'diaspora in Cedar-Riverside/Minneapolis "Little Mogadishu," also Columbus '
    'OH, San Diego; rich oral poetry tradition); Ethiopian/Eritrean (largest '
    'diaspora in Silver Spring/DC metro area, also LA, Dallas; coffee ceremony/'
    'jebena buna, Ge\'ez script, Orthodox Christian and Islamic traditions); '
    'Nigerian (Houston, NYC, Chicago — one of most educated immigrant groups in '
    'US); Jamaican (NYC, South Florida — dancehall, reggae, Carnival traditions); '
    'Cape Verdean (New Bedford/Brockton MA — oldest African diaspora in US, '
    'whaling industry connection; morna, coladeira music); Ghanaian (NYC, DC '
    'area); and Trinidadian/Tobagonian (Brooklyn — West Indian Day Parade/Carnival, '
    'soca, calypso, steel pan).'
)


def _get_ad_text(entry):
    impact = entry.get('I', {})
    for k in ('africanDescendant', 'africanAmerican', 'african', 'black'):
        if k in impact and isinstance(impact[k], dict):
            return ' '.join(v for v in impact[k].values() if isinstance(v, str)), k
    return '', None


def _ensure_ad_block(entry):
    impact = entry.setdefault('I', {})
    for k in ('africanDescendant', 'africanAmerican', 'african', 'black'):
        if k in impact:
            block = impact[k]
            if isinstance(block, dict):
                ensure_pppt(block)
                return k
    impact['africanDescendant'] = {'people': '', 'places': '', 'practices': '', 'treasures': ''}
    return 'africanDescendant'


def run_targeted_gaps_enrichment(data, dry_run=True):
    stats = {
        'migration_routes': 0, 'spiritual_sites': 0, 'delta': 0,
        'worship': 0, 'hbcu': 0, 'afro_indigenous': 0, 'diaspora': 0,
        'total_entries_modified': 0, 'changes': [],
    }
    modified_ids = set()

    for cat in CATEGORIES:
        if cat not in data or not isinstance(data[cat], list):
            continue
        for i, entry in enumerate(data[cat]):
            entry_id = entry.get('i', entry.get('id', f'{cat}[{i}]'))
            full_text = get_entry_text(entry)
            full_lower = full_text.lower()
            ad_text, ad_key = _get_ad_text(entry)
            changes = []

            ad_context = any(t in full_lower for t in
                           ['african', 'black', 'enslaved', 'civil rights', 'negro',
                            'hbcu', 'segregation', 'dei', 'diversity'])

            # 1. MIGRATION ROUTES
            if 'great migration' in full_lower:
                route_terms = ['illinois central', 'pennsylvania railroad',
                              'atlantic coast line', 'route 66',
                              'southern pacific', 'louisville & nashville',
                              'chickenbone express']
                if not any(t in full_lower for t in route_terms):
                    if ad_key:
                        block = entry['I'][ad_key]
                        block['places'] = (block['places'].rstrip() + MIGRATION_ROUTES_TEXT).strip()
                        changes.append('migration_routes')
                        stats['migration_routes'] += 1

            # 2. AFRICAN SPIRITUAL SITES
            spiritual_terms = ['vodou', 'voodoo', 'santería', 'santeria', 'yoruba', 'orisha',
                             'hoodoo', 'rootwork', 'conjure', 'african spiritual', 'african-derived',
                             'ring shout', 'spiritual tradition', 'sacred', 'ceremony', 'ancestor', 'spirit']
            if any(t in full_lower for t in spiritual_terms) and ad_context:
                heritage_checks = ['oyotunji', 'goree island', 'door of no return',
                                  'cape coast castle', 'elmina castle', 'osun-osogbo', 'church of lukumi']
                if not any(t in full_lower for t in heritage_checks):
                    ad_key_used = ad_key or _ensure_ad_block(entry)
                    block = entry['I'][ad_key_used]
                    block['places'] = (block['places'].rstrip() + SPIRITUAL_SITES_TEXT).strip()
                    changes.append('spiritual_sites')
                    stats['spiritual_sites'] += 1

            # 3. MISSISSIPPI DELTA SPECIFICITY
            if 'mississippi' in full_lower or 'delta' in full_lower:
                delta_specifics = ['clarksdale', 'indianola', 'ruleville', 'fannie lou hamer',
                                 'emmett till', 'dockery', 'parchman', 'mound bayou',
                                 'greenwood, ms', 'rolling fork', 'b.b. king museum',
                                 'muddy waters', 'robert johnson', 'charley patton', 'hill country blues']
                if not any(t in full_lower for t in delta_specifics):
                    ad_signal = any(t in full_lower for t in
                                   ['african', 'black', 'enslaved', 'civil rights', 'blues',
                                    'hbcu', 'segregation', 'voting'])
                    if ad_signal:
                        ad_key_used = ad_key or _ensure_ad_block(entry)
                        block = entry['I'][ad_key_used]
                        block['places'] = (block['places'].rstrip() + DELTA_SPECIFICITY_TEXT).strip()
                        changes.append('delta')
                        stats['delta'] += 1

            # 4. BLACK PLACES OF WORSHIP
            worship_context = any(t in full_lower for t in
                                ['church', 'baptist', ' ame ', 'mosque', 'synagogue',
                                 'worship', 'congregation', 'temple', 'spiritual'])
            if worship_context and ad_context:
                specific_worship = ['16th street baptist', 'ebenezer baptist', 'mother bethel',
                                  'abyssinian', 'emanuel ame', 'mason temple', 'dexter avenue',
                                  'pilgrim baptist', 'mosque maryam', 'masjid malcolm',
                                  'masjid muhammad', 'first african baptist', 'beth shalom']
                if not any(t in full_lower for t in specific_worship):
                    ad_key_used = ad_key or _ensure_ad_block(entry)
                    block = entry['I'][ad_key_used]
                    block['treasures'] = (block['treasures'].rstrip() + WORSHIP_SITES_TEXT).strip()
                    changes.append('worship')
                    stats['worship'] += 1

            # 5a. HBCU SPECIFICITY
            if 'hbcu' in full_lower or 'historically black' in full_lower:
                specific_hbcus = ['howard university', 'morehouse', 'spelman', 'fisk',
                                'tuskegee', 'hampton university', 'famu', 'florida a&m',
                                'xavier university', 'meharry', 'alcorn', 'jackson state',
                                'cheyney', 'lincoln university', 'shaw university']
                if not any(t in full_lower for t in specific_hbcus):
                    ad_key_used = ad_key or _ensure_ad_block(entry)
                    block = entry['I'][ad_key_used]
                    block['places'] = (block['places'].rstrip() + HBCU_SPECIFICITY_TEXT).strip()
                    changes.append('hbcu')
                    stats['hbcu'] += 1

            # 5b. AFRO-INDIGENOUS
            has_indigenous = any(t in full_lower for t in ['indigenous', 'tribal', 'native american', 'indian'])
            has_ad = any(t in full_lower for t in ['african', 'black', 'enslaved', 'hbcu'])
            if has_indigenous and has_ad:
                afro_indig_terms = ['freedmen', 'black seminole', 'mardi gras indian',
                                  'afro-indigenous', 'afro indigenous', 'seminole maroon', 'buffalo soldier']
                if not any(t in full_lower for t in afro_indig_terms):
                    ad_key_used = ad_key or _ensure_ad_block(entry)
                    block = entry['I'][ad_key_used]
                    block['people'] = (block['people'].rstrip() + AFRO_INDIGENOUS_TEXT).strip()
                    changes.append('afro_indigenous')
                    stats['afro_indigenous'] += 1

            # 5c. DIASPORA
            diaspora_context = any(t in full_lower for t in
                                  ['immigration', 'immigrant', 'diaspora', 'refugee',
                                   'asylum', 'deportation', 'tps', 'visa'])
            if diaspora_context and ad_context:
                specific_diaspora = ['haitian', 'somali', 'ethiopian', 'nigerian', 'jamaican',
                                   'cape verdean', 'eritrean', 'ghanaian', 'trinidadian', 'congolese']
                if not any(t in full_lower for t in specific_diaspora):
                    ad_key_used = ad_key or _ensure_ad_block(entry)
                    block = entry['I'][ad_key_used]
                    block['people'] = (block['people'].rstrip() + DIASPORA_TEXT).strip()
                    changes.append('diaspora')
                    stats['diaspora'] += 1

            if changes:
                modified_ids.add(entry_id)
                stats['changes'].append({'id': entry_id, 'category': cat, 'changes': changes})
                if not dry_run:
                    data[cat][i] = entry

    stats['total_entries_modified'] = len(modified_ids)
    return data, stats


# ═══════════════════════════════════════════════════════════════════════════════
# FIX IMPACT ANALYSES (hardcoded entries from fix_impact_analyses.py)
# ═══════════════════════════════════════════════════════════════════════════════

def run_fix_impacts(data, dry_run=True):
    """Locate entries by ID and apply hardcoded comprehensive impact analyses.
    This imports the IMPACT_ANALYSES dict from the archived script if available,
    or runs as a no-op if the archive is not present."""
    archive_script = TRACKER_DIR / "Archive" / "legacy" / "fix_impact_analyses_data.json"
    script_path = Path(__file__).parent / "fix_impact_analyses.py"

    stats = {'entries_checked': 0, 'entries_fixed': 0, 'changes': []}

    # Try to import from the original script
    if script_path.exists():
        sys.path.insert(0, str(script_path.parent))
        try:
            from fix_impact_analyses import IMPACT_ANALYSES
        except ImportError:
            print('  fix_impact_analyses.py found but could not import IMPACT_ANALYSES')
            return data, stats
    else:
        print('  fix_impact_analyses.py not found — skipping fix-impacts')
        return data, stats

    entry_ids = list(IMPACT_ANALYSES.keys())
    for category_key, category_list in data.items():
        if not isinstance(category_list, list):
            continue
        for i, entry in enumerate(category_list):
            if not isinstance(entry, dict):
                continue
            stats['entries_checked'] += 1
            eid = entry.get('i')
            if eid in entry_ids:
                if not dry_run:
                    entry['I'] = IMPACT_ANALYSES[eid]
                    data[category_key][i] = entry
                stats['entries_fixed'] += 1
                stats['changes'].append({'id': eid, 'category': category_key})
                print(f'  [{category_key}] {eid}: impact analysis {"applied" if not dry_run else "would be applied"}')

    return data, stats


# ═══════════════════════════════════════════════════════════════════════════════
# MAIN CLI
# ═══════════════════════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(
        description='TCKC Threat Tracker — Unified Enrichment Tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Communities:
  indigenous          Enrich with tribal nation names, cultural details
  african-descendant  Enrich with African-descendant community data
  targeted-gaps       Fill structural gaps (migration routes, HBCUs, etc.)
  fix-impacts         Apply hardcoded impact analysis fixes
  all                 Run all enrichments sequentially
        """
    )
    parser.add_argument('--community', '-c', required=True,
                       choices=['indigenous', 'african-descendant', 'targeted-gaps',
                               'fix-impacts', 'all'],
                       help='Which enrichment to run')
    parser.add_argument('--batch', type=int, choices=[1, 2, 3],
                       help='Batch number (indigenous only: 1=SE/VA/DC, 2=generic, 3=missing)')
    parser.add_argument('--all', action='store_true', help='Run all batches (indigenous)')
    parser.add_argument('--dry-run', action='store_true', help='Preview without saving')
    parser.add_argument('--report', action='store_true', help='Report-only, no changes')

    args = parser.parse_args()
    community = args.community

    if community not in ('all', 'fix-impacts') and not args.all and not args.report and not args.dry_run and not args.batch:
        parser.print_help()
        sys.exit(1)

    print(f'=== TCKC Enrichment [{community}] — {datetime.now().strftime("%Y-%m-%d %H:%M")} ===')

    data = load_data()
    total = sum(len(v) for v in data.values() if isinstance(v, list))
    print(f'Loaded {total} entries')

    communities_to_run = (['indigenous', 'african-descendant', 'targeted-gaps', 'fix-impacts']
                          if community == 'all' else [community])

    total_enriched = 0
    for comm in communities_to_run:
        print(f'\n--- {comm.upper()} ---')

        if comm == 'indigenous':
            if args.report:
                run_indigenous_enrichment(data, report_only=True)
                continue
            batches = [args.batch] if args.batch else [1, 2, 3]
            for batch in batches:
                print(f'  Batch {batch}:')
                data, stats = run_indigenous_enrichment(data, batch_num=batch, dry_run=args.dry_run)
                print(f'  Checked: {stats["entries_checked"]}, Enriched: {stats["entries_enriched"]}')
                total_enriched += stats['entries_enriched']
                save_log(f'indigenous_batch{batch}', stats)

        elif comm == 'african-descendant':
            if args.report:
                run_african_descendant_enrichment(data, report_only=True)
                continue
            data, stats = run_african_descendant_enrichment(data, dry_run=args.dry_run)
            print(f'Checked: {stats["entries_checked"]}, Enriched: {stats["entries_enriched"]}')
            total_enriched += stats['entries_enriched']
            save_log('african_descendant', stats)

        elif comm == 'targeted-gaps':
            data, stats = run_targeted_gaps_enrichment(data, dry_run=args.dry_run)
            print(f'Migration routes: {stats["migration_routes"]}')
            print(f'Spiritual sites: {stats["spiritual_sites"]}')
            print(f'Delta specificity: {stats["delta"]}')
            print(f'Worship sites: {stats["worship"]}')
            print(f'HBCU specificity: {stats["hbcu"]}')
            print(f'Afro-Indigenous: {stats["afro_indigenous"]}')
            print(f'Diaspora: {stats["diaspora"]}')
            print(f'Total modified: {stats["total_entries_modified"]}')
            total_enriched += stats['total_entries_modified']
            save_log('targeted_gaps', stats)

        elif comm == 'fix-impacts':
            data, stats = run_fix_impacts(data, dry_run=args.dry_run)
            print(f'Fixed: {stats["entries_fixed"]}')
            total_enriched += stats['entries_fixed']

    if not args.dry_run and not args.report and total_enriched > 0:
        save_data(data)
        print(f'\nSaved data.json — {total_enriched} entries enriched')
    elif args.dry_run:
        print(f'\nDRY RUN — {total_enriched} entries would be enriched (no changes saved)')
    elif not args.report:
        print(f'\nNo entries needed enrichment')


if __name__ == '__main__':
    main()
