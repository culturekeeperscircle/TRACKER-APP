#!/usr/bin/env python3
"""Two atomic updates with one backup.

1. Update enrich-wood-chipper-book-2026 to add:
   (a) An explicit "ALREADY-OCCURRED HARMS" section that consolidates
       documented (not projected) consequences from Enrich's testimony.
   (b) A "GEORGE W. BUSH-ERA BIPARTISAN PROGRAMS DISMANTLED" section
       on PEPFAR (26M lives saved; 8M babies born HIV-negative; Musk's
       'we made a little mistake, but we fixed that' admission).

2. Update intl-2026-pepfar-cuts-001 to add:
   (a) The 8-million-babies-born-HIV-negative figure.
   (b) Musk's "little mistake" admission.
   (c) Cross-reference to Enrich's testimony.
"""
import json
import shutil
from pathlib import Path
from datetime import datetime

DATA_PATH = Path(__file__).parent.parent / "data" / "data.json"
BACKUP_PATH = DATA_PATH.with_suffix(
    f".json.bak-{datetime.now().strftime('%Y%m%d-%H%M%S')}-pre-concrete-harms-bush"
)

ENRICH_ID = "enrich-wood-chipper-book-2026"
PEPFAR_ID = "intl-2026-pepfar-cuts-001"


# ============== ENRICH ENTRY: NEW SECTIONS ==============
ENRICH_NEW_BLOCK = (
    "<b>ALREADY-OCCURRED HARMS (DOCUMENTED, NOT PROJECTED).</b> "
    "Enrich draws an explicit line in his Democracy Now! testimony between harms that have already happened and harms that are projected. The harms in this section are documented, present-tense, and concrete. They are not hypothetical model outputs.<br>"
    "(1) <i>Deaths.</i> 750,000 people have already died from the cuts, most of them children, by Enrich's conservative estimate.<br>"
    "(2) <i>Children born with HIV.</i> Children are being born with HIV at high rates. One year before the dismantling, that number was near zero. The reversal is documented and present-tense.<br>"
    "(3) <i>Uganda Ebola, U.S. national-security exposure.</i> During an active Ebola outbreak in Uganda, USAID political appointees and DOGE staff refused to allow USAID to screen passengers at airports for Ebola symptoms before they boarded international flights to the United States. The refusal occurred. It is not a projection.<br>"
    "(4) <i>Sudan, fourth year of war.</i> Displaced Sudanese families and refugees walked all day to USAID-marked clinics and found them shuttered. Families could not access food supplements. They returned home and made what Enrich called \"the harrowing decision of which of their children to feed.\" These events occurred during the dismantling.<br>"
    "(5) <i>Drug-resistant TB clinical trials abandoned mid-treatment.</i> Patients enrolled in USAID-supported clinical trials for drug-resistant tuberculosis were left mid-protocol when the agency was dismantled. Mid-trial abandonment of TB patients is a documented harm with both individual mortality consequences and population-level consequences for resistance emergence.<br>"
    "(6) <i>Workforce purge.</i> USAID was reduced from more than 10,000 employees globally to 611 retained essential staff during the initial DOGE action and ultimately to 15 employees working under the State Department.<br><br>"
    "<b>GEORGE W. BUSH-ERA BIPARTISAN PROGRAMS DISMANTLED.</b> "
    "Several of the programs Enrich documents being gutted are programs established under previous Republican administrations and sustained on bipartisan footing for two decades. The dismantling is therefore a departure from prior Republican policy, not the continuation of one. PEPFAR (the President's Emergency Plan for AIDS Relief) is the most prominent example. PEPFAR was established by President George W. Bush in 2003. By 2026 PEPFAR had saved approximately 26 million lives and had enabled nearly 8 million babies to be born without HIV infection. The Trump II administration's FY2026 budget proposed reducing PEPFAR from $7.1 billion to $2.9 billion (a 59 percent cut). When questioned about the consequences of the PEPFAR disruption, Elon Musk said publicly, \"Oh, we made a little mistake, but we fixed that.\" Enrich states that the dissolution affected the very programs Marco Rubio had championed during his Senate career. The Bureau of Global Health, where Enrich served, administered PEPFAR alongside USAID's malaria, tuberculosis, maternal-and-child-health, and pandemic-preparedness portfolios. The cuts crossed the bipartisan firewall that had protected these programs through three previous administrations of both parties. (PEPFAR-specific entry: intl-2026-pepfar-cuts-001.)<br><br>"
    "<b>BUREAUS, AGENCIES, AND PROGRAMS AFFECTED.</b> "
    "Per Enrich's testimony, the dismantling reached across the entire global-health portfolio: PEPFAR (HIV/AIDS), malaria control (indoor residual spraying, bed-net distribution), tuberculosis (including the abandoned drug-resistant TB clinical trials), maternal health (postpartum hemorrhage, eclampsia treatment), childhood immunization, infectious-disease preparation and pandemic response (including the Uganda Ebola response), and health-systems strengthening. Beyond the Bureau of Global Health, the dismantling also reached USAID's food-security, education, disaster-response, and democracy-and-governance portfolios. The State Department absorbed a residual fraction of USAID functions. Congress's $50 billion February 2026 foreign-aid allocation has been distributed slowly and fragmentedly through the State Department rather than the disbanded USAID (tracked at intl-2026-usaid-shutdown-001).<br><br>"
)


# ============== PEPFAR ENTRY: NEW BLOCK ==============
PEPFAR_NEW_BLOCK = (
    "<br><br><b>ENRICH WHISTLEBLOWER TESTIMONY AND MUSK ADMISSION (added 2026-04-30).</b> "
    "Former USAID Bureau of Global Health Director of Policy, Programs, and Planning Nicholas Enrich (tracked at enrich-wood-chipper-book-2026) testified on Democracy Now! on April 16, 2026 that the cuts had already produced 750,000 deaths, most of them children, by conservative estimate, and that children are being born with HIV \"at high rates when just a year ago those numbers were near zero.\" Enrich's testimony confirms that PEPFAR's harm is no longer prospective. PEPFAR was established by President George W. Bush in 2003 and by 2026 had saved approximately 26 million lives and enabled nearly 8 million babies to be born without HIV infection. The dismantling crossed the bipartisan firewall that had protected the program across the Bush, Obama, first Trump, and Biden administrations. When questioned publicly about the PEPFAR disruption, Elon Musk said, \"Oh, we made a little mistake, but we fixed that.\" Enrich states that programs Marco Rubio had championed during his Senate career, including PEPFAR, were dissolved in the very period during which Rubio publicly claimed that no one had died because of the USAID cuts. The 8-million-babies-born-HIV-negative figure quantifies the cumulative pediatric impact of PEPFAR's mother-to-child-transmission-prevention component. That component is among the program functions disrupted by the cuts.<br><br>"
    "<b>ADDITIONAL SOURCES (added 2026-04-30).</b><br>"
    "Whistleblower testimony: Democracy Now!, \"'Into the Wood Chipper': Whistleblower's Inside Story of DOGE Shredding USAID, 14 Million May Die,\" April 16, 2026. <a href=\"https://www.democracynow.org/2026/4/16/usaid_whistleblower\">https://www.democracynow.org/2026/4/16/usaid_whistleblower</a><br>"
    "Whistleblower memoir: Nicholas Enrich, \"Into the Wood Chipper: A Whistleblower's Account of How the Trump Administration Shredded USAID,\" Summit Books / Simon & Schuster, April 14, 2026. <a href=\"https://www.simonandschuster.com/books/Into-the-Wood-Chipper/Nicholas-Enrich/9781668226957\">https://www.simonandschuster.com/books/Into-the-Wood-Chipper/Nicholas-Enrich/9781668226957</a><br>"
    "Cross-reference: enrich-wood-chipper-book-2026 (Enrich whistleblower memoir, 2026-04-14); oecd-aid-decline-2026 (OECD ODA collapse, 2026-04-10)."
)


def main():
    if not DATA_PATH.exists():
        raise SystemExit(f"data.json not found at {DATA_PATH}")

    em_dash = "—"
    if em_dash in ENRICH_NEW_BLOCK or em_dash in PEPFAR_NEW_BLOCK:
        raise SystemExit("ABORT: em-dash detected in update blocks.")

    shutil.copy2(DATA_PATH, BACKUP_PATH)
    print(f"Backup written: {BACKUP_PATH.name}")

    with DATA_PATH.open() as f:
        data = json.load(f)

    # ---- Update Enrich entry ----
    enrich_target = None
    for e in data.get("international", []):
        if (e.get("id") or e.get("i")) == ENRICH_ID:
            enrich_target = e
            break
    if enrich_target is None:
        raise SystemExit(f"Enrich entry {ENRICH_ID} not found.")

    desc = enrich_target["D"]
    if "ALREADY-OCCURRED HARMS" in desc:
        print("Enrich entry already updated with ALREADY-OCCURRED HARMS block. Skipping.")
    else:
        anchor = "<b>SOURCES.</b><br>"
        if anchor not in desc:
            raise SystemExit("SOURCES anchor not found in Enrich description.")
        new_desc = desc.replace(anchor, ENRICH_NEW_BLOCK + anchor, 1)
        enrich_target["D"] = new_desc
        print("Updated Enrich entry: inserted ALREADY-OCCURRED HARMS and BUSH-ERA PROGRAMS sections.")

    # ---- Update PEPFAR entry ----
    pepfar_target = None
    for e in data.get("international", []):
        if (e.get("id") or e.get("i")) == PEPFAR_ID:
            pepfar_target = e
            break
    if pepfar_target is None:
        raise SystemExit(f"PEPFAR entry {PEPFAR_ID} not found.")

    if "ENRICH WHISTLEBLOWER TESTIMONY" in pepfar_target["D"]:
        print("PEPFAR entry already updated. Skipping.")
    else:
        pepfar_target["D"] = pepfar_target["D"] + PEPFAR_NEW_BLOCK
        print("Updated PEPFAR entry: appended Enrich testimony block + Musk admission + 8M babies figure.")

    if "meta" in data and isinstance(data["meta"], dict):
        data["meta"]["lastUpdated"] = datetime.now().strftime("%Y-%m-%d")

    tmp = DATA_PATH.with_suffix(".json.tmp")
    with tmp.open("w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    tmp.replace(DATA_PATH)

    print("Done.")


if __name__ == "__main__":
    main()
