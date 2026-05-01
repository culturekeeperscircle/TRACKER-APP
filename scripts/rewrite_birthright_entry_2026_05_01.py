#!/usr/bin/env python3
"""Rewrite birthright-citizenship entry as a clean federal record.

The previous entry described a Berkeley public forum about EO 14160
and the related litigation. Birthright citizenship is the federal
matter, so the rewrite recenters the record on the executive order
itself and the federal litigation that has followed it. The entry
moves from `other_domestic` to `executive_actions` because the
underlying action is presidential.

The PPPT impact analysis (`I` field) is preserved with a global
em-dash sweep so the prose conforms to the project writing-style
rules. The cultural-impact framing remains accurate because the
order's threat to AAPI, immigrant, Latine, African-descendant, and
all-communities cultural resources is independent of who held the
forum that originally prompted the entry.
"""
import json
import re
import shutil
from pathlib import Path
from datetime import datetime

DATA_PATH = Path(__file__).parent.parent / "data" / "data.json"
BACKUP_PATH = DATA_PATH.with_suffix(
    f".json.bak-{datetime.now().strftime('%Y%m%d-%H%M%S')}-pre-birthright-rewrite"
)

ENTRY_ID = "birthright-citizenship-attack-2026-001"
OLD_CAT = "other_domestic"
NEW_CAT = "executive_actions"

NEW_FIELDS = {
    "i": ENTRY_ID,
    "t": "Executive Order",
    "n": "EO 14160",
    "T": (
        '<span style="color: #991B1B;">Executive Order 14160:</span> '
        'Protecting the Meaning and Value of American Citizenship '
        '(Birthright Citizenship Restriction)'
    ),
    "s": "EO 14160 birthright citizenship and federal litigation",
    "d": "2025-01-20",
    "a": "Trump II",
    "A": ["White House", "DHS", "DOJ", "State", "SSA"],
    "S": (
        "Active and contested. Issued January 20, 2025. Multiple federal "
        "district courts have entered preliminary injunctions blocking "
        "enforcement. The Supreme Court decided Trump v. CASA, 606 U.S. "
        "___ (June 27, 2025), narrowing the use of universal injunctions "
        "without resolving the constitutional merits of the order. Merits "
        "litigation continues in the courts of appeals and on remand."
    ),
    "L": "SEVERE",
    "U": (
        "https://www.whitehouse.gov/presidential-actions/2025/01/"
        "protecting-the-meaning-and-value-of-american-citizenship/"
    ),
    "c": [
        "Asian American/Pacific Islander",
        "Immigrant/Refugee",
        "Latiné",
        "African-descendant",
        "All communities",
    ],
    "_source": "manual_2026_05_01_rewrite",
}

NEW_D = (
    "<b>EXECUTIVE ACTION.</b> On January 20, 2025, President Donald "
    "Trump issued Executive Order 14160, titled \"Protecting the Meaning "
    "and Value of American Citizenship.\" The order directs federal "
    "agencies to deny citizenship documents to children born in the "
    "United States when the mother is unlawfully present or holds a "
    "temporary visa and the father is neither a citizen nor a lawful "
    "permanent resident. Implementing agencies include the Department "
    "of State (passports), the Social Security Administration (Social "
    "Security numbers), the Department of Homeland Security "
    "(immigration documents), and the Department of Justice (litigation "
    "defense). The order purports to apply to births occurring thirty "
    "days or more after issuance."
    "<br><br>"
    "<b>CONSTITUTIONAL CONTEXT.</b> The Fourteenth Amendment Citizenship "
    "Clause provides that \"All persons born or naturalized in the "
    "United States, and subject to the jurisdiction thereof, are "
    "citizens of the United States.\" The clause was ratified in 1868 "
    "as the constitutional response to <i>Dred Scott v. Sandford</i> "
    "(1857) and the foundation of equal citizenship for formerly "
    "enslaved Black Americans. The Supreme Court applied the clause to "
    "the U.S.-born children of immigrant parents in <i>United States v. "
    "Wong Kim Ark</i>, 169 U.S. 649 (1898), holding that a child born "
    "in San Francisco to Chinese immigrant parents was a U.S. citizen "
    "at birth. EO 14160 directly contests the reading of the "
    "Citizenship Clause that has governed federal practice for more "
    "than 125 years."
    "<br><br>"
    "<b>FEDERAL LITIGATION.</b> Suits challenging EO 14160 were filed "
    "within hours of issuance. Federal district courts in Washington, "
    "Maryland, Massachusetts, and New Hampshire entered preliminary "
    "injunctions blocking enforcement. The lead cases include "
    "<i>State of Washington v. Trump</i> (W.D. Wash.), <i>CASA, Inc. v. "
    "Trump</i> (D. Md.), <i>New Hampshire Indonesian Community Support "
    "v. Trump</i> (D.N.H.), and <i>Doe v. Trump</i> (D. Mass.). The "
    "Trump administration sought emergency relief at the Supreme Court "
    "targeting the scope of the universal injunctions entered by the "
    "district courts. On June 27, 2025, the Supreme Court decided "
    "<i>Trump v. CASA, Inc.</i>, 606 U.S. ___ (2025), narrowing the "
    "availability of universal injunctions while leaving the "
    "constitutional merits of EO 14160 unresolved. Merits litigation "
    "continues in the courts of appeals and on remand at the district-"
    "court level."
    "<br><br>"
    "<b>OPERATIONAL POSTURE.</b> Implementation has been blocked by "
    "court order for the duration of the litigation. DHS, DOJ, State, "
    "and SSA have suspended formal rollout of denial procedures pending "
    "resolution. The administration continues to defend the order on "
    "the theory that the phrase \"subject to the jurisdiction thereof\" "
    "excludes the children of undocumented or temporary-status parents. "
    "Every federal court of appeals to consider that reading has "
    "rejected it."
    "<br><br>"
    "<b>CULTURAL STAKES.</b> Birthright citizenship is the legal "
    "predicate for the cultural and civic standing of communities whose "
    "members include U.S.-born children of immigrant parents. Asian "
    "American communities carry the most direct historical resonance "
    "with the order through the legacy of the Chinese Exclusion Act, "
    "Angel Island detention, and the <i>Wong Kim Ark</i> case itself. "
    "Latine communities face the broadest immediate exposure given the "
    "demographic distribution of mixed-status families and the policy's "
    "direct impact on millions of U.S.-born children. African-descendant "
    "communities, including African and Caribbean immigrants and their "
    "U.S.-born children, face cumulative effects compounding the "
    "Reconstruction-era purpose of the Fourteenth Amendment. The "
    "Cultural Impacts section below details concrete threats to People, "
    "Places, Practices, and Treasures across the affected communities."
    "<br><br>"
    "<b>SOURCES.</b><br>"
    '<a href="https://www.whitehouse.gov/presidential-actions/2025/01/'
    'protecting-the-meaning-and-value-of-american-citizenship/" '
    'target="_blank" rel="noopener">Executive Order 14160 '
    "(whitehouse.gov, January 20, 2025)</a>.<br>"
    '<a href="https://www.federalregister.gov/executive-order/14160" '
    'target="_blank" rel="noopener">EO 14160 (Federal Register)</a>.<br>"'
    '<a href="https://www.scotusblog.com/case-files/cases/trump-v-casa-inc/" '
    'target="_blank" rel="noopener"><i>Trump v. CASA, Inc.</i>, '
    "606 U.S. ___ (2025) (SCOTUSblog case page)</a>.<br>"
    '<a href="https://www.courtlistener.com/?q=birthright+citizenship+'
    'executive+order&type=r" target="_blank" rel="noopener">CourtListener '
    "docket search for the consolidated district-court litigation</a>."
)


def clean_em_dashes(text):
    """Remove em-dashes from existing prose without altering meaning.

    Patterns:
    - ' — ' (em-dash with surrounding spaces) becomes '. ' and the
      following letter is uppercased so the result is a clean sentence
      break. This handles the common parenthetical-aside use.
    - '—' (em-dash without spaces) becomes '-' (hyphen) so compound
      modifiers and ranges keep their typographic intent.
    """
    if not isinstance(text, str):
        return text

    def break_to_sentence(match):
        return ". "

    out = re.sub(r"\s—\s", break_to_sentence, text)

    def cap_after_period(m):
        return m.group(1) + m.group(2).upper()

    out = re.sub(r"(\.\s)([a-z])", cap_after_period, out)
    out = out.replace("—", "-")
    return out


def deep_clean(obj):
    if isinstance(obj, dict):
        return {k: deep_clean(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [deep_clean(x) for x in obj]
    if isinstance(obj, str):
        return clean_em_dashes(obj)
    return obj


def main():
    if not DATA_PATH.exists():
        raise SystemExit(f"data.json not found at {DATA_PATH}")

    if "—" in NEW_D:
        raise SystemExit("ABORT: em-dash in new description.")
    for v in NEW_FIELDS.values():
        if isinstance(v, str) and "—" in v:
            raise SystemExit("ABORT: em-dash in new field.")

    shutil.copy2(DATA_PATH, BACKUP_PATH)
    print(f"Backup written: {BACKUP_PATH.name}")

    with DATA_PATH.open() as f:
        data = json.load(f)

    found_index = None
    found_cat = None
    for cat in [
        "executive_actions",
        "agency_actions",
        "legislation",
        "litigation",
        "other_domestic",
        "international",
    ]:
        for i, entry in enumerate(data.get(cat, [])):
            if (entry.get("i") or entry.get("id")) == ENTRY_ID:
                found_index = i
                found_cat = cat
                break
        if found_index is not None:
            break

    if found_index is None:
        raise SystemExit(f"ABORT: entry {ENTRY_ID} not found")

    print(f"Found {ENTRY_ID} in {found_cat} at index {found_index}")

    entry = data[found_cat].pop(found_index)

    cleaned_I = deep_clean(entry.get("I"))

    new_entry = {
        "i": NEW_FIELDS["i"],
        "t": NEW_FIELDS["t"],
        "n": NEW_FIELDS["n"],
        "T": NEW_FIELDS["T"],
        "s": NEW_FIELDS["s"],
        "d": NEW_FIELDS["d"],
        "a": NEW_FIELDS["a"],
        "A": NEW_FIELDS["A"],
        "S": NEW_FIELDS["S"],
        "L": NEW_FIELDS["L"],
        "D": NEW_D,
        "I": cleaned_I,
        "c": NEW_FIELDS["c"],
        "U": NEW_FIELDS["U"],
        "_source": NEW_FIELDS["_source"],
    }

    if NEW_CAT not in data:
        data[NEW_CAT] = []
    data[NEW_CAT].append(new_entry)
    print(f"Reinserted into {NEW_CAT} (now {len(data[NEW_CAT])} entries)")

    if "meta" in data and isinstance(data["meta"], dict):
        data["meta"]["lastUpdated"] = datetime.now().strftime("%Y-%m-%d")

    tmp = DATA_PATH.with_suffix(".json.tmp")
    with tmp.open("w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    tmp.replace(DATA_PATH)

    print("Rewrite complete.")


if __name__ == "__main__":
    main()
