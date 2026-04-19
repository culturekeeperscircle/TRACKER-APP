#!/usr/bin/env python3
"""
Clean topic-mismatched boilerplate leaked into entry descriptions by a prior
enrichment pass. Follow-up to the 2026-04-19 sub-federal audit.

Two cleanup passes:

1. IMMIGRATION block — strip from entries whose topic is NOT immigration.
   Fingerprint: three verbatim sentences citing "Migration Policy Institute",
   "mixed-status families, DACA recipients", and "Urban Institute and
   National Immigration Law Center". Appears in ~183 entries.

2. CONGRESS-GOV block — strip from state-level or placeholder legislation
   entries where federal congressional procedural language is nonsense.
   Applies to entries where `_origin == "state"` or the ID contains "xxx".

Run:  python3 scripts/clean_boilerplate.py [--dry-run]
"""
import json, re, sys, shutil, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data' / 'data.json'

# ----- Immigration block fingerprints (strip exactly these sentences) -----
IMMIGRATION_SENTENCES = [
    "Immigration enforcement actions disproportionately affect mixed-status "
    "families, DACA recipients, and long-established immigrant communities.",
    "According to the Migration Policy Institute, approximately 11 million "
    "undocumented individuals reside in the United States, with 4.4 million "
    "living with U.S. citizen family members.",
    "Enforcement escalation creates chilling effects on access to healthcare, "
    "education, and social services, even for lawfully present individuals, "
    "as documented by the Urban Institute and National Immigration Law Center.",
    # Variant seen in 61 entries
    "Immigration policy changes create chilling effects on mixed-status "
    "families, DACA recipients, and long-established immigrant communities, "
    "reducing access to healthcare, education, and social services.",
]

# ----- Congress-gov/state-bill mismatch fingerprints -----
CONGRESS_GOV_SENTENCES = [
    "Sponsor and committee referral details for this measure are tracked via "
    "Congress.gov. The bill has been referred to the relevant committee(s) "
    "of jurisdiction for consideration under standard congressional procedure.",
    "This measure, 119th Congress.",
    "Legislative session: 119th Congress (2025-2027).",
    "CRS Report RS20856 explains the legislative process in detail.",
    "The legislative process for this measure follows standard congressional "
    "procedure: introduction, committee referral, potential hearings and "
    "markup, floor consideration, and conference if both chambers act.",
    "The committee may hold hearings, markups, and vote to report the bill "
    "to the full chamber.",
    "Most legislation does not advance past committee stage.",
]

IMMIGRATION_AGENCIES = {'DHS','ICE','CBP','USCIS','EOIR','DOS','DOJ'}
IMMIGRATION_COMMUNITY_MARKERS = ('immigrant', 'latiné', 'latine', 'asian american')
IMMIGRATION_KEYWORDS = [
    'immigra','deport','undocument','asylum','refugee','daca','tps',
    'visa','border','sanctuary','naturalization','citizenship',
    'travel ban','muslim ban','ice enforcement','cbp','uscis',
]


def strip_html(s):
    return re.sub(r'<[^>]+>', ' ', s or '')


def is_immigration_topic(entry):
    """Return True if this entry is actually about immigration.

    Uses ONLY title/summary/number/agencies — not the description, because
    the description itself contains the boilerplate we're trying to detect.
    """
    agencies = {str(a).upper() for a in (entry.get('A') or [])}
    # Strong agency signal (excluding DOJ, which spans many topics).
    if agencies & (IMMIGRATION_AGENCIES - {'DOJ'}):
        return True
    communities_raw = entry.get('c') or []
    communities_blob = ' '.join(str(c).lower() for c in communities_raw)
    if 'immigrant' in communities_blob:
        return True
    blob = (
        (entry.get('T') or '') + ' ' + (entry.get('s') or '') + ' ' +
        (entry.get('n') or '')
    ).lower()
    return any(kw in blob for kw in IMMIGRATION_KEYWORDS)


def is_state_or_placeholder(entry):
    if entry.get('_origin') == 'state':
        return True
    eid = entry.get('i') or entry.get('id') or ''
    if 'xxx' in eid.lower():
        return True
    return False


def strip_sentences_from_html(html, sentences):
    """Remove exact sentence matches from an HTML string; collapse whitespace."""
    if not html:
        return html, 0
    out = html
    removed = 0
    for s in sentences:
        # Case-sensitive exact match; strip one trailing space if present.
        patterns = [
            s + ' ',
            ' ' + s,
            s,
        ]
        for p in patterns:
            while p in out:
                out = out.replace(p, '', 1)
                removed += 1
                break  # move to next sentence after one hit per pattern-form
        # Keep looping if multiple occurrences of bare form
        while s in out:
            out = out.replace(s, '', 1)
            removed += 1
    # Collapse whitespace/<br> artifacts
    out = re.sub(r'(<br\s*/?>\s*){3,}', '<br><br>', out)
    out = re.sub(r' {2,}', ' ', out)
    out = re.sub(r'\s+([.,;:])', r'\1', out)
    return out, removed


def main():
    dry = '--dry-run' in sys.argv
    with DATA.open() as f:
        data = json.load(f)

    imm_cleaned = []  # (cat, id, hits)
    imm_kept = []     # kept because entry IS immigration topic
    cg_cleaned = []

    for cat in ('executive_actions','agency_actions','legislation',
                'litigation','other_domestic','international'):
        for entry in data.get(cat, []):
            eid = entry.get('i') or entry.get('id')
            desc = entry.get('D') or ''

            # Pass 1: immigration boilerplate
            if any(s in desc for s in IMMIGRATION_SENTENCES):
                if is_immigration_topic(entry):
                    imm_kept.append((cat, eid))
                else:
                    new_desc, n = strip_sentences_from_html(desc, IMMIGRATION_SENTENCES)
                    if n:
                        entry['D'] = new_desc
                        imm_cleaned.append((cat, eid, n))
                        desc = new_desc  # for downstream pass

            # Pass 2: congress-gov boilerplate — only for state/placeholder
            if is_state_or_placeholder(entry):
                if any(s in desc for s in CONGRESS_GOV_SENTENCES):
                    new_desc, n = strip_sentences_from_html(desc, CONGRESS_GOV_SENTENCES)
                    if n:
                        entry['D'] = new_desc
                        cg_cleaned.append((cat, eid, n))

    print(f'Immigration boilerplate stripped from: {len(imm_cleaned)} entries')
    for cat, eid, n in imm_cleaned[:10]:
        print(f'  [{cat}] {eid} ({n} sentence-hits)')
    if len(imm_cleaned) > 10:
        print(f'  ... and {len(imm_cleaned)-10} more')

    print(f'\nImmigration boilerplate PRESERVED in: {len(imm_kept)} on-topic entries')
    for cat, eid in imm_kept[:10]:
        print(f'  [{cat}] {eid}')
    if len(imm_kept) > 10:
        print(f'  ... and {len(imm_kept)-10} more')

    print(f'\nCongress-gov boilerplate stripped from: {len(cg_cleaned)} state/placeholder entries')
    for cat, eid, n in cg_cleaned:
        print(f'  [{cat}] {eid} ({n} sentence-hits)')

    if dry:
        print('\n(dry run — no file written)')
        return

    backup = DATA.with_suffix(
        f'.json.bak-{datetime.datetime.now().strftime("%Y%m%d-%H%M%S")}'
    )
    shutil.copy2(DATA, backup)
    with DATA.open('w') as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    print(f'\nBackup: {backup.name}')
    print(f'Wrote:  {DATA}')


if __name__ == '__main__':
    main()
