#!/usr/bin/env python3
"""
One-off remediation for sub-federal entries surfaced by the 2026-04-19 audit.

- Tags 7 state-level entries with `_origin: "state"` and `_federalHook`
  describing the federal-court or federal-policy nexus.
- Demotes `lit-2026-greenpeace-dapl` (ND state court, no federal hook,
  plus corrupted enrichment field) with `_origin: "state"` and
  `_outOfScope: true` so the UI can filter it out without data loss.
- Prepends a <b>Federal implication:</b> note to the HTML description
  so the hook is visible to readers of each entry.

Run:  python3 scripts/remediate_subfederal.py [--dry-run]
"""
import json, sys, shutil, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data' / 'data.json'

REMEDIATIONS = {
    'lit-2026-ks-sb244-001': {
        '_origin': 'state',
        '_federalHook': (
            "ACLU challenge proceeds on U.S. Constitution Equal Protection and "
            "Due Process grounds; federal-court review inevitable. Note: this "
            "entry's description previously stated Kansas-Constitution-only "
            "claims, which conflicts with the companion entry "
            "kansas-trans-license-invalidation-2026."
        ),
    },
    'kansas-trans-license-invalidation-2026': {
        '_origin': 'state',
        '_federalHook': (
            "ACLU filed suit March 2026 invoking the U.S. Constitution's Equal "
            "Protection and Due Process Clauses; federal REAL ID Act "
            "coordination implicated by retroactive license invalidation."
        ),
    },
    's-tennessee-immigrant-school-ban-2026': {
        '_origin': 'state',
        '_federalHook': (
            "Any enacted version is squarely controlled by Plyler v. Doe, 457 "
            "U.S. 202 (1982); enactment triggers federal Equal Protection "
            "challenge."
        ),
    },
    's-pending-ny-119': {
        '_origin': 'state',
        '_federalHook': (
            "Sanctuary-style limits on cooperation with federal ICE invite "
            "federal preemption litigation under Arizona v. United States, 567 "
            "U.S. 387 (2012)."
        ),
    },
    'indiana-fairness-act-2026': {
        '_origin': 'state',
        '_federalHook': (
            "Mandates state and local cooperation with federal ICE enforcement; "
            "interfaces directly with federal immigration policy and raises "
            "Tenth Amendment anti-commandeering questions (cf. Murphy v. NCAA, "
            "584 U.S. 453 (2018))."
        ),
    },
    'ohio-drag-ban-hb249-2026': {
        '_origin': 'state',
        '_federalHook': (
            "First Amendment challenges go to federal court; the nearly "
            "identical Tennessee Adult Entertainment Act was enjoined in "
            "Friends of Georges v. Mulroy, 675 F. Supp. 3d 831 (W.D. Tenn. 2023)."
        ),
    },
    'idaho-trans-bathroom-criminal-2026': {
        '_origin': 'state',
        '_federalHook': (
            "Expected federal challenges under the Fourteenth Amendment and "
            "potentially the ADA; the Ninth Circuit previously enjoined "
            "Idaho's transgender-sports ban in Hecox v. Little, 79 F.4th 1009 "
            "(9th Cir. 2023)."
        ),
    },
}

DEMOTIONS = {
    'lit-2026-greenpeace-dapl': {
        '_origin': 'state',
        '_outOfScope': True,
        '_outOfScopeReason': (
            "North Dakota state court, state tort claims, appeals to North "
            "Dakota Supreme Court; no federal-court hook. Flagged for review "
            "2026-04-19. The entry's LEGAL MECHANISM field also contained "
            "template leakage citing the Immigration and Nationality Act, "
            "unrelated to the case."
        ),
    },
}


def idkey(entry):
    return entry.get('i') or entry.get('id')


def apply_remediation(entry, patch, federal_hook=None):
    for k, v in patch.items():
        entry[k] = v
    if federal_hook:
        note = (
            f"<p><b>Federal implication:</b> {federal_hook}</p>"
        )
        existing = entry.get('D') or ''
        # Avoid duplicate insertion on re-runs.
        if '<b>Federal implication:</b>' not in existing:
            entry['D'] = note + existing


def main():
    dry = '--dry-run' in sys.argv
    with DATA.open() as f:
        data = json.load(f)

    changes = []
    for cat in ('executive_actions', 'agency_actions', 'legislation',
                'litigation', 'other_domestic'):
        for entry in data.get(cat, []):
            eid = idkey(entry)
            if eid in REMEDIATIONS:
                patch = REMEDIATIONS[eid]
                apply_remediation(entry, patch,
                                  federal_hook=patch['_federalHook'])
                changes.append((cat, eid, 'retag+hook'))
            elif eid in DEMOTIONS:
                apply_remediation(entry, DEMOTIONS[eid])
                changes.append((cat, eid, 'demote out-of-scope'))

    for (cat, eid, action) in changes:
        print(f'  [{cat}] {eid} — {action}')
    print(f'\nTotal entries modified: {len(changes)}')
    expected = len(REMEDIATIONS) + len(DEMOTIONS)
    if len(changes) != expected:
        print(f'WARNING: expected {expected} matches, got {len(changes)}')

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
