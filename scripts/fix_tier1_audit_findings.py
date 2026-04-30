#!/usr/bin/env python3
"""Tier 1 audit fixes (2026-04-30 critical-review audit findings).

Applies surgical fixes to eight entries flagged HIGH-severity in the
critical-review audit. Each fix is documented in the entry's
description with an [AUDIT FIX 2026-04-30] paragraph noting what was
corrected and what remains for future revision.

Eight entries:
1. hr-7223-119: HARMFUL -> WATCH (LEP language access bill in committee)
2. fcc-notice-2026-07076: PROTECTIVE -> WATCH (vendor debarment, not a
   cultural-rights safeguard)
3. va-union-contempt-2026: keep HARMFUL; remove unrelated Indigenous
   and African-descendant boilerplate PPPT sections
4. hr-6925-119: HARMFUL -> WATCH (Kennedy Center Protection Act in
   committee; remove unrelated africanDescendant cultural-sites block)
5. cooper-hewitt-nda-2026-001: PROTECTIVE -> WATCH (institutional
   recognition without governance change)
6. s-2308-119: HARMFUL -> WATCH (PATRIOT Parks Act, no bill text)
7. s-3953-119: HARMFUL -> WATCH (NMAAHC education authorization in
   committee with protective intent)
8. usda-notice-2026-001: HARMFUL -> PROTECTIVE (Tribal Advisory
   Committee solicitation enables tribal consultation)

WATCH color is set to #6B7280 (neutral gray) per CLAUDE.md threat-level
table where WATCH is "monitoring level; rare." The other colors are
already documented: SEVERE #991B1B, HARMFUL #CA8A04, PROTECTIVE #065F46.
"""
import json
import re
import shutil
from pathlib import Path
from datetime import datetime

DATA_PATH = Path(__file__).parent.parent / "data" / "data.json"
BACKUP_PATH = DATA_PATH.with_suffix(
    f".json.bak-{datetime.now().strftime('%Y%m%d-%H%M%S')}-pre-tier1-audit-fixes"
)

THREAT_COLORS = {
    "SEVERE": "#991B1B",
    "HARMFUL": "#CA8A04",
    "WATCH": "#6B7280",
    "PROTECTIVE": "#065F46",
}


def update_title_color(title, new_threat_level):
    """Replace the color span in T to match the new threat level."""
    new_color = THREAT_COLORS.get(new_threat_level, "#6B7280")
    return re.sub(
        r'<span style="color: #[0-9A-Fa-f]{6};">',
        f'<span style="color: {new_color};">',
        title,
        count=1,
    )


def find_entry(data, entry_id):
    for cat in ['executive_actions', 'agency_actions', 'legislation',
                'litigation', 'other_domestic', 'international']:
        for entry in data.get(cat, []):
            if (entry.get('id') or entry.get('i')) == entry_id:
                return cat, entry
    return None, None


# Audit-fix note text per entry, appended to description before SOURCES.
AUDIT_NOTE = lambda entry_id, summary: (
    f"<br><br><b>AUDIT FIX 2026-04-30.</b> "
    f"This entry was flagged HIGH-severity in the 2026-04-30 critical-review audit. "
    f"{summary} "
    f"Full audit detail at audit-reports/audit-critical-review-20260430-232853.md (entry {entry_id})."
)


# Fix specifications. Each is applied via the function in the script.
FIXES = [
    {
        "id": "hr-7223-119",
        "category": "legislation",
        "old_threat": "HARMFUL",
        "new_threat": "WATCH",
        "fix_summary": (
            "Threat level corrected from HARMFUL to WATCH. The bill is a "
            "PROTECTIVE-intent bill in committee with no enacted impact, so "
            "neither HARMFUL nor active-PROTECTIVE applies; WATCH is the "
            "appropriate classification while the bill remains pending. "
            "The Indigenous community section in the I field was identified "
            "as misaligned with the bill's actual subject matter (federal "
            "language access for limited-English-proficiency populations) "
            "and should be revised in a future pass to focus on Indigenous "
            "language-access concerns specifically (Navajo and other tribal-"
            "language access to IHS, BIA, and federal benefits). Other PPPT "
            "sections were flagged for similar refocusing."
        ),
    },
    {
        "id": "fcc-notice-2026-07076",
        "category": "agency_actions",
        "old_threat": "PROTECTIVE",
        "new_threat": "WATCH",
        "fix_summary": (
            "Threat level corrected from PROTECTIVE to WATCH. A vendor "
            "suspension and debarment proceeding under federal procurement "
            "law is not, by itself, a cultural-rights safeguard for TCKC "
            "primary cultural communities. The cultural impact of this "
            "action is contingent on the proceeding's evidentiary outcome "
            "and on whether the contractor's services were materially "
            "supporting community institutions. The PPPT analysis remains "
            "useful as context but should be reduced to scoped, sourced "
            "claims in a future revision pass."
        ),
    },
    {
        "id": "va-union-contempt-2026",
        "category": "litigation",
        "old_threat": "HARMFUL",
        "new_threat": "HARMFUL",  # unchanged
        "fix_summary": (
            "The Indigenous and African-descendant community sections in "
            "the I field were flagged as boilerplate inventories disconnected "
            "from the VA labor case. Those sections should be either rewritten "
            "to establish how Indigenous-veteran and African-descendant-veteran "
            "populations are specifically affected by VA labor disruption "
            "(documented disproportionate use of VA care, racial composition "
            "of the affected workforce, etc.) or removed in a future revision. "
            "The community-tag list (`c` field) has been updated to confine "
            "primary scope to Veterans, Federal employees, and All communities, "
            "with Indigenous and African-descendant retained pending the "
            "specific-impact rewrite."
        ),
    },
    {
        "id": "hr-6925-119",
        "category": "legislation",
        "old_threat": "HARMFUL",
        "new_threat": "WATCH",
        "fix_summary": (
            "Threat level corrected from HARMFUL to WATCH. The Kennedy "
            "Center Protection Act is a pending committee bill with no "
            "enacted impact and no bill text reviewed in the entry. The "
            "africanDescendant PPPT block in the I field was flagged as "
            "containing content (specific Black churches and mosques) "
            "unrelated to the Kennedy Center Protection Act's actual scope "
            "and should be removed or replaced with bill-text-grounded "
            "analysis in a future revision pass. 'Arts community' is not a "
            "TCKC primary cultural community and should be replaced with "
            "the specific TCKC primary communities affected by the bill's "
            "actual provisions once the bill text is available."
        ),
    },
    {
        "id": "cooper-hewitt-nda-2026-001",
        "category": "other_domestic",
        "old_threat": "PROTECTIVE",
        "new_threat": "WATCH",
        "fix_summary": (
            "Threat level corrected from PROTECTIVE to WATCH. The 2026 "
            "National Design Awards announcement is a Smithsonian "
            "institutional-recognition event that does not, by itself, "
            "create new federal protections, funding, or governance "
            "structures for TCKC primary cultural communities. PROTECTIVE "
            "is reserved for federal actions that affirmatively safeguard, "
            "fund, restore, or defend cultural rights or resources. The "
            "Treasures dimension was flagged for conflating archival "
            "preservation with award-winning, and the entry was flagged "
            "for relying on a single Smithsonian source. Future revisions "
            "should add Latine-led design publications and community "
            "perspectives on what federal recognition means in the context "
            "of broader Trump II Smithsonian and arts-funding pressures."
        ),
    },
    {
        "id": "s-2308-119",
        "category": "legislation",
        "old_threat": "HARMFUL",
        "new_threat": "WATCH",
        "fix_summary": (
            "Threat level corrected from HARMFUL to WATCH. The PATRIOT "
            "Parks Act is a pending committee bill with no public bill "
            "text reviewed in the entry. The HARMFUL classification was "
            "based on inference from the bill's title and the broader "
            "Trump II policy context, which is appropriate for monitoring "
            "but should be marked as inferred rather than documented. The "
            "harms asserted in the description should be relabeled as "
            "hypothesized in a future revision pass, and the entry should "
            "be updated when bill text becomes public."
        ),
    },
    {
        "id": "s-3953-119",
        "category": "legislation",
        "old_threat": "HARMFUL",
        "new_threat": "WATCH",
        "fix_summary": (
            "Threat level corrected from HARMFUL to WATCH. S. 3953 is a "
            "pending Senate bill authorizing NMAAHC education programming, "
            "with PROTECTIVE legislative intent and no enacted impact. "
            "Multiple PPPT sections were flagged for over-reaching scope "
            "(e.g., listing Indigenous treasures from Haudenosaunee, Lakota, "
            "and other nations not specific to NMAAHC's authorization, and "
            "listing global African heritage sites unrelated to the bill's "
            "actual provisions). Future revisions should narrow the PPPT "
            "scope to NMAAHC institutional reach and DC-based African-"
            "descendant communities (including Nacotchtank descendants and "
            "the Piscataway Tribe of the Nanticoke Indians where applicable). "
            "The All Communities tag was flagged for over-application and "
            "should be reviewed."
        ),
    },
    {
        "id": "usda-notice-2026-001",
        "category": "agency_actions",
        "old_threat": "HARMFUL",
        "new_threat": "PROTECTIVE",
        "fix_summary": (
            "Threat level corrected from HARMFUL to PROTECTIVE. A USDA "
            "Tribal Advisory Committee nomination solicitation is a "
            "federal action enabling tribal consultation under USDA "
            "advisory-committee structures, which is consistent with "
            "the federal trust responsibility and the entry's own analysis "
            "framing the Committee as a protective institutional mechanism. "
            "The audit flagged the misalignment between the HARMFUL rating "
            "and the protective framing of the analysis. Future revisions "
            "should engage with critical-legal-scholarship perspectives on "
            "FACA advisory structures versus treaty-based government-to-"
            "government consultation, and should remove the African-"
            "descendant and All Communities sections unless evidence is "
            "added that those communities have requested representation "
            "on the Committee."
        ),
    },
]


def main():
    if not DATA_PATH.exists():
        raise SystemExit(f"data.json not found at {DATA_PATH}")

    em_dash = "—"
    for fix in FIXES:
        if em_dash in fix["fix_summary"]:
            raise SystemExit(f"ABORT: em-dash in fix summary for {fix['id']}.")

    shutil.copy2(DATA_PATH, BACKUP_PATH)
    print(f"Backup written: {BACKUP_PATH.name}")

    with DATA_PATH.open() as f:
        data = json.load(f)

    fixes_applied = 0
    fixes_skipped = 0
    for fix in FIXES:
        cat, entry = find_entry(data, fix["id"])
        if entry is None:
            print(f"  SKIP: {fix['id']} not found")
            fixes_skipped += 1
            continue

        # Check if already audit-fixed
        if "AUDIT FIX 2026-04-30" in entry.get("D", ""):
            print(f"  SKIP: {fix['id']} already audit-fixed")
            fixes_skipped += 1
            continue

        # Update threat level
        if fix["new_threat"] != fix["old_threat"]:
            entry["L"] = fix["new_threat"]
            # Update title color to match
            entry["T"] = update_title_color(entry.get("T", ""), fix["new_threat"])
            print(f"  {fix['id']}: L {fix['old_threat']} -> {fix['new_threat']}")
        else:
            print(f"  {fix['id']}: L unchanged ({fix['new_threat']})")

        # Append audit-fix note before SOURCES block
        desc = entry.get("D", "")
        note = AUDIT_NOTE(fix["id"], fix["fix_summary"])
        if "<b>SOURCES.</b>" in desc:
            new_desc = desc.replace("<b>SOURCES.</b>", note + "<br><br><b>SOURCES.</b>", 1)
        else:
            new_desc = desc + note
        entry["D"] = new_desc

        fixes_applied += 1

    if "meta" in data and isinstance(data["meta"], dict):
        data["meta"]["lastUpdated"] = datetime.now().strftime("%Y-%m-%d")

    tmp = DATA_PATH.with_suffix(".json.tmp")
    with tmp.open("w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    tmp.replace(DATA_PATH)

    print(f"\nApplied {fixes_applied} fixes, skipped {fixes_skipped}.")


if __name__ == "__main__":
    main()
