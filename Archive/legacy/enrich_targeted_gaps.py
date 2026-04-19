#!/usr/bin/env python3
"""
TCKC Threat Tracker — Targeted Gap Enrichment
Fixes the 5 structural gaps identified in the audit:
  1. Migration routes (railroads/highways) — 533 entries
  2. African spiritual sites (Oyotunji, etc.) — 126 entries
  3. Mississippi Delta specificity — 58 entries
  4. Black Places of Worship — 29 entries
  5. Small gaps: HBCU (8), Afro-Indigenous (11), Diaspora (12)

Usage:
    python enrich_targeted_gaps.py --dry-run
    python enrich_targeted_gaps.py --all
"""

import json
import sys
import argparse
from pathlib import Path
from datetime import datetime

TRACKER_DIR = Path(__file__).parent.parent
DATA_FILE = TRACKER_DIR / "data" / "data.json"


def load_data():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)


def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def get_all_text(entry):
    parts = [entry.get('n', ''), entry.get('s', ''), entry.get('D', ''), entry.get('S', '')]
    for block in entry.get('I', {}).values():
        if isinstance(block, dict):
            for v in block.values():
                if isinstance(v, str):
                    parts.append(v)
        elif isinstance(block, str):
            parts.append(block)
    return ' '.join(parts)


def get_ad_text(entry):
    """Get the africanDescendant impact text specifically."""
    impact = entry.get('I', {})
    for k in ('africanDescendant', 'africanAmerican', 'african', 'black'):
        if k in impact and isinstance(impact[k], dict):
            return ' '.join(v for v in impact[k].values() if isinstance(v, str)), k
    return '', None


def ensure_ad_block(entry):
    """Ensure entry has an africanDescendant impact section with PPPT."""
    impact = entry.setdefault('I', {})
    for k in ('africanDescendant', 'africanAmerican', 'african', 'black'):
        if k in impact:
            block = impact[k]
            if isinstance(block, dict):
                for pppt in ('people', 'places', 'practices', 'treasures'):
                    block.setdefault(pppt, '')
                return k
    # Create new
    impact['africanDescendant'] = {'people': '', 'places': '', 'practices': '', 'treasures': ''}
    return 'africanDescendant'


# ── ENRICHMENT TEXT FRAGMENTS ──────────────────────────────────────────────

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


def run_enrichment(data, dry_run=True):
    stats = {
        'migration_routes': 0, 'spiritual_sites': 0, 'delta': 0,
        'worship': 0, 'hbcu': 0, 'afro_indigenous': 0, 'diaspora': 0,
        'total_entries_modified': 0,
    }
    modified_ids = set()
    categories = ['executive_actions', 'legislation', 'litigation',
                  'agency_actions', 'international']

    for cat in categories:
        if cat not in data or not isinstance(data[cat], list):
            continue
        for i, entry in enumerate(data[cat]):
            entry_id = entry.get('i', entry.get('id', f'{cat}[{i}]'))
            full_text = get_all_text(entry)
            full_lower = full_text.lower()
            ad_text, ad_key = get_ad_text(entry)
            ad_lower = ad_text.lower()

            changes = []

            # Common context checks used by multiple enrichments
            ad_context = any(t in full_lower for t in
                           ['african', 'black', 'enslaved', 'civil rights', 'negro',
                            'hbcu', 'segregation', 'dei', 'diversity'])

            # ── 1. MIGRATION ROUTES ────────────────────────────────────
            if 'great migration' in full_lower:
                # Check if any route is named
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

            # ── 2. AFRICAN SPIRITUAL SITES ─────────────────────────────
            spiritual_terms = ['vodou', 'voodoo', 'santería', 'santeria',
                             'yoruba', 'orisha', 'hoodoo', 'rootwork',
                             'conjure', 'african spiritual', 'african-derived',
                             'ring shout', 'spiritual tradition', 'sacred',
                             'ceremony', 'ancestor', 'spirit']
            if any(t in full_lower for t in spiritual_terms) and ad_context:
                # Require Oyotunji specifically — the biggest gap
                oyotunji_and_heritage = ['oyotunji', 'goree island', 'door of no return',
                                        'cape coast castle', 'elmina castle',
                                        'osun-osogbo', 'church of lukumi']
                if not any(t in full_lower for t in oyotunji_and_heritage):
                    ad_key_used = ad_key or ensure_ad_block(entry)
                    block = entry['I'][ad_key_used]
                    block['places'] = (block['places'].rstrip() + SPIRITUAL_SITES_TEXT).strip()
                    changes.append('spiritual_sites')
                    stats['spiritual_sites'] += 1

            # ── 3. MISSISSIPPI DELTA SPECIFICITY ───────────────────────
            if 'mississippi' in full_lower or 'delta' in full_lower:
                delta_specifics = ['clarksdale', 'indianola', 'ruleville',
                                 'fannie lou hamer', 'emmett till', 'dockery',
                                 'parchman', 'mound bayou', 'greenwood, ms',
                                 'rolling fork', 'b.b. king museum',
                                 'muddy waters', 'robert johnson',
                                 'charley patton', 'hill country blues']
                if not any(t in full_lower for t in delta_specifics):
                    # Only enrich if entry has AD relevance
                    ad_signal = any(t in full_lower for t in
                                   ['african', 'black', 'enslaved', 'civil rights',
                                    'blues', 'hbcu', 'segregation', 'voting'])
                    if ad_signal:
                        ad_key_used = ad_key or ensure_ad_block(entry)
                        block = entry['I'][ad_key_used]
                        block['places'] = (block['places'].rstrip() + DELTA_SPECIFICITY_TEXT).strip()
                        changes.append('delta')
                        stats['delta'] += 1

            # ── 4. BLACK PLACES OF WORSHIP ─────────────────────────────
            worship_context = any(t in full_lower for t in
                                ['church', 'baptist', ' ame ', 'mosque', 'synagogue',
                                 'worship', 'congregation', 'temple', 'spiritual'])
            if worship_context and ad_context:
                specific_worship = ['16th street baptist', 'ebenezer baptist',
                                  'mother bethel', 'abyssinian', 'emanuel ame',
                                  'mason temple', 'dexter avenue', 'pilgrim baptist',
                                  'mosque maryam', 'masjid malcolm', 'masjid muhammad',
                                  'first african baptist', 'beth shalom']
                if not any(t in full_lower for t in specific_worship):
                    ad_key_used = ad_key or ensure_ad_block(entry)
                    block = entry['I'][ad_key_used]
                    block['treasures'] = (block['treasures'].rstrip() + WORSHIP_SITES_TEXT).strip()
                    changes.append('worship')
                    stats['worship'] += 1

            # ── 5a. HBCU SPECIFICITY ───────────────────────────────────
            if 'hbcu' in full_lower or 'historically black' in full_lower:
                specific_hbcus = ['howard university', 'morehouse', 'spelman',
                                'fisk', 'tuskegee', 'hampton university',
                                'famu', 'florida a&m', 'xavier university',
                                'meharry', 'alcorn', 'jackson state',
                                'cheyney', 'lincoln university', 'shaw university']
                if not any(t in full_lower for t in specific_hbcus):
                    ad_key_used = ad_key or ensure_ad_block(entry)
                    block = entry['I'][ad_key_used]
                    block['places'] = (block['places'].rstrip() + HBCU_SPECIFICITY_TEXT).strip()
                    changes.append('hbcu')
                    stats['hbcu'] += 1

            # ── 5b. AFRO-INDIGENOUS ────────────────────────────────────
            has_indigenous = any(t in full_lower for t in
                               ['indigenous', 'tribal', 'native american', 'indian'])
            has_ad = any(t in full_lower for t in
                        ['african', 'black', 'enslaved', 'hbcu'])
            if has_indigenous and has_ad:
                afro_indig_terms = ['freedmen', 'black seminole', 'mardi gras indian',
                                  'afro-indigenous', 'afro indigenous',
                                  'seminole maroon', 'buffalo soldier']
                if not any(t in full_lower for t in afro_indig_terms):
                    ad_key_used = ad_key or ensure_ad_block(entry)
                    block = entry['I'][ad_key_used]
                    block['people'] = (block['people'].rstrip() + AFRO_INDIGENOUS_TEXT).strip()
                    changes.append('afro_indigenous')
                    stats['afro_indigenous'] += 1

            # ── 5c. DIASPORA ───────────────────────────────────────────
            diaspora_context = any(t in full_lower for t in
                                  ['immigration', 'immigrant', 'diaspora', 'refugee',
                                   'asylum', 'deportation', 'tps', 'visa'])
            if diaspora_context and ad_context:
                specific_diaspora = ['haitian', 'somali', 'ethiopian', 'nigerian',
                                   'jamaican', 'cape verdean', 'eritrean',
                                   'ghanaian', 'trinidadian', 'congolese']
                if not any(t in full_lower for t in specific_diaspora):
                    ad_key_used = ad_key or ensure_ad_block(entry)
                    block = entry['I'][ad_key_used]
                    block['people'] = (block['people'].rstrip() + DIASPORA_TEXT).strip()
                    changes.append('diaspora')
                    stats['diaspora'] += 1

            # Apply changes
            if changes:
                modified_ids.add(entry_id)
                if not dry_run:
                    data[cat][i] = entry

    stats['total_entries_modified'] = len(modified_ids)
    return data, stats


def main():
    parser = argparse.ArgumentParser(description='TCKC — Targeted Gap Enrichment')
    parser.add_argument('--all', action='store_true', help='Run all enrichments')
    parser.add_argument('--dry-run', action='store_true', help='Preview without saving')
    args = parser.parse_args()

    if not args.all and not args.dry_run:
        parser.print_help()
        sys.exit(1)

    print(f'=== TCKC Targeted Gap Enrichment — {datetime.now().strftime("%Y-%m-%d %H:%M")} ===')
    data = load_data()
    total = sum(len(v) for v in data.values() if isinstance(v, list))
    print(f'Loaded {total} entries')

    data, stats = run_enrichment(data, dry_run=args.dry_run)

    print(f'\n--- Results ---')
    print(f'Migration routes added: {stats["migration_routes"]}')
    print(f'Spiritual sites added: {stats["spiritual_sites"]}')
    print(f'Delta specificity added: {stats["delta"]}')
    print(f'Worship sites added: {stats["worship"]}')
    print(f'HBCU specificity added: {stats["hbcu"]}')
    print(f'Afro-Indigenous added: {stats["afro_indigenous"]}')
    print(f'Diaspora communities added: {stats["diaspora"]}')
    print(f'Total unique entries modified: {stats["total_entries_modified"]}')

    if not args.dry_run and stats['total_entries_modified'] > 0:
        save_data(data)
        print(f'\nSaved data.json')
    elif args.dry_run:
        print(f'\nDRY RUN — no changes saved')


if __name__ == '__main__':
    main()
