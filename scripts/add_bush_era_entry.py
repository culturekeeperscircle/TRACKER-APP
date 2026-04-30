#!/usr/bin/env python3
"""Two atomic operations with one backup.

1. Create a discrete `international` entry capturing the pattern in
   which Bush-era Republican-built international development programs,
   sustained on bipartisan footing across four prior administrations,
   have been dismantled by the Trump II administration. Covers PEPFAR
   (2003), the President's Malaria Initiative (2005), and the
   Millennium Challenge Corporation (2004).

2. Replace the GEORGE W. BUSH-ERA BIPARTISAN PROGRAMS DISMANTLED
   section that was added to enrich-wood-chipper-book-2026 with a
   one-line cross-reference to the new discrete entry. The Enrich
   entry remains the primary-source whistleblower record. The new
   entry is the cross-program pattern synthesis.
"""
import json
import shutil
from pathlib import Path
from datetime import datetime

DATA_PATH = Path(__file__).parent.parent / "data" / "data.json"
BACKUP_PATH = DATA_PATH.with_suffix(
    f".json.bak-{datetime.now().strftime('%Y%m%d-%H%M%S')}-pre-bush-era-entry"
)

ENRICH_ID = "enrich-wood-chipper-book-2026"
NEW_ID = "bush-era-bipartisan-programs-dismantled-2026"


# ============== NEW DISCRETE ENTRY ==============
NEW_ENTRY = {
    "i": NEW_ID,
    "t": "Aggregate Analysis",
    "n": "Pattern Analysis: George W. Bush-Era Bipartisan International Development Programs Dismantled by the Trump II Administration",
    "T": '<span style="color: #991B1B;">Aggregate Analysis:</span> Bush-Era Bipartisan International Development Programs Dismantled by Trump II (PEPFAR, PMI, MCC)',
    "s": "Bush-era bipartisan programs dismantled",
    "d": "2026-04-16",
    "a": "Trump II",
    "A": ["State", "USAID", "PEPFAR", "PMI", "MCC", "DOGE"],
    "S": "Active. Three signature international-development programs established under President George W. Bush and sustained on bipartisan footing across the Bush, Obama, first Trump, and Biden administrations have been dismantled, deeply cut, or operationally crippled by the Trump II administration during 2025 and 2026. The dismantling is therefore a departure from prior Republican policy. The pattern is independent of any one Bush-era program and constitutes a structural realignment of U.S. international development.",
    "L": "SEVERE",
    "D": (
        "<b>PATTERN.</b> Three signature international-development programs were established under President George W. Bush and have been sustained on bipartisan footing across four prior administrations of both parties. All three have been dismantled, deeply cut, or operationally crippled by the Trump II administration during 2025 and 2026. The dismantling is therefore a departure from prior Republican policy, not the continuation of one. Whistleblower Nicholas Enrich, former Director of Policy, Programs, and Planning in the USAID Bureau of Global Health (tracked at enrich-wood-chipper-book-2026), made this pattern explicit in his April 16, 2026 Democracy Now! interview and in his memoir \"Into the Wood Chipper\" (Summit Books / Simon & Schuster, April 14, 2026). This entry synthesizes the cross-program pattern and ties it to its Bush-era bipartisan origins.<br><br>"
        "<b>PROGRAM 1: PEPFAR (BUSH, 2003).</b> The President's Emergency Plan for AIDS Relief was announced by President Bush in his 2003 State of the Union and signed into law that year. By 2026 PEPFAR had saved approximately 26 million lives and had enabled nearly 8 million babies to be born without HIV infection. The program was reauthorized under the Tom Lantos and Henry J. Hyde United States Global Leadership Against HIV/AIDS, Tuberculosis, and Malaria Reauthorization Act and renewed across the Obama, first Trump, and Biden administrations. The Trump II administration's FY2026 budget proposes reducing PEPFAR from $7.1 billion to $2.9 billion (a 59 percent cut). The Center for Global Development projects more than 600,000 additional HIV-related deaths from the proposed cuts. The Lancet HIV projects 565,000 new HIV infections in sub-Saharan Africa over ten years from elimination of pre-exposure prophylaxis funding alone. Survey data shows 71 percent of PEPFAR implementing partners have cancelled at least one category of activities and 50 percent report staff reductions. When questioned publicly about the disruption, Elon Musk said, \"Oh, we made a little mistake, but we fixed that.\" Tracked separately at intl-2026-pepfar-cuts-001.<br><br>"
        "<b>PROGRAM 2: PRESIDENT'S MALARIA INITIATIVE (BUSH, 2005).</b> PMI was launched by President Bush in 2005 as a five-year, $1.2 billion commitment to halve malaria mortality in 15 high-burden African countries. PMI subsequently expanded to additional countries and was reauthorized across the Obama, first Trump, and Biden administrations. USAID served as PMI's principal implementing agency, obligating approximately 96 percent of bilateral malaria assistance in FY 2023. Under the Trump II administration's foreign-aid review, of 770 global-health awards identified, 157 included malaria activities, and 80 percent of those were terminated. KFF analysis estimates that approximately 47 percent of USAID funding for PMI was cut. A limited \"life-saving services\" waiver issued February 4, 2025 allowed some bed-net distribution and indoor residual spraying to continue, but implementing partners reported difficulty securing approvals and payments and continued operational disruption. The dismantling of USAID itself eliminates the staff and partner relationships through which PMI operated.<br><br>"
        "<b>PROGRAM 3: MILLENNIUM CHALLENGE CORPORATION (BUSH, 2004).</b> MCC was authorized by Congress in 2004 at the urging of President Bush as an independent U.S. foreign-aid agency that delivers performance-based development assistance to lower-income countries that meet eligibility criteria on governance, economic freedom, and investment in citizens. MCC's signature instrument is the Compact, a multi-year grant agreement with a partner country. Under the Trump II administration, DOGE moved to shut MCC down. Agency leaders told employees that staff would be cut to a small residual team to run legally mandated programs and that contracts would be terminated. MCC ultimately survived as a legal entity. More than half of MCC's programs are slated for cancellation. Compacts in development for African and other partner-country governments have been terminated or paused. The Center for Global Development analysis of the program terminations finds no consistent rationale for which compacts were preserved versus cancelled.<br><br>"
        "<b>BIPARTISAN-FIREWALL FRAMING.</b> Each of these three programs was established under a Republican administration and was sustained across two Democratic administrations and one prior Republican administration. PEPFAR, PMI, and MCC were not partisan compromises; they were pillars of George W. Bush's claim that compassionate conservatism could deliver durable international results. Marco Rubio, in his Senate career, was among the most prominent Republican champions of this Bush legacy. Enrich states that USAID staff \"breathed a collective sigh of relief\" upon Rubio's appointment as Secretary of State because Rubio had been one of the agency's strongest Senate-era champions. Rubio subsequently presided over the dismantling of the very programs he had once defended and made false public statements that no one had died because of the cuts. The bipartisan firewall around these programs has been broken from inside the Republican coalition that built it.<br><br>"
        "<b>WHISTLEBLOWER-DOCUMENTED HARM.</b> The harms attributable to the dismantling of these Bush-era programs are documented and present-tense, not hypothetical. Enrich testified that 750,000 people, most of them children, had already died from the cuts by the time of his April 16, 2026 Democracy Now! interview, by his conservative estimate. He testified that children are again being born with HIV at high rates, after a year in which those numbers had been near zero. He testified that USAID-supported drug-resistant tuberculosis clinical trials were abandoned mid-treatment. He testified that displaced Sudanese families walked all day to reach USAID-marked clinics only to find them shuttered. The Lancet projects more than 14 million additional avoidable deaths by 2030 from the cumulative cuts to USAID, PEPFAR, PMI, and adjacent programs, including more than 4.5 million children under age five (tracked at enrich-wood-chipper-book-2026, intl-2026-usaid-shutdown-001, intl-2026-pepfar-cuts-001).<br><br>"
        "<b>RELATIONSHIP TO GLOBAL ODA COLLAPSE.</b> The OECD reported in April 2026 that U.S. official development assistance fell 56.9 percent in 2025, the largest single-provider reduction in any year on record, and that Germany surpassed the United States as the largest DAC provider for the first time in history. The Bush-era bipartisan-program dismantling is the principal driver of that historic U.S. retrenchment (tracked at oecd-aid-decline-2026).<br><br>"
        "<b>CULTURAL RESOURCE THREAT ASSESSMENT.</b> The threat level is SEVERE. The dismantling of PEPFAR, PMI, and MCC eliminates programs that have served populations with deep diaspora ties to all five TCKC primary cultural communities, with sub-Saharan Africa bearing the largest share of program-served populations and the largest documented mortality consequences. The harm is not partisan. The dismantling represents the abandonment of a Republican-built bipartisan international-development infrastructure that operated across four prior administrations and produced measurable life-saving results."
        "<br><br>"
        "<b>SOURCES.</b><br>"
        "Whistleblower memoir: Nicholas Enrich, \"Into the Wood Chipper: A Whistleblower's Account of How the Trump Administration Shredded USAID,\" Summit Books / Simon & Schuster, April 14, 2026. <a href=\"https://www.simonandschuster.com/books/Into-the-Wood-Chipper/Nicholas-Enrich/9781668226957\">https://www.simonandschuster.com/books/Into-the-Wood-Chipper/Nicholas-Enrich/9781668226957</a><br>"
        "Whistleblower interview: Democracy Now!, April 16, 2026. <a href=\"https://www.democracynow.org/2026/4/16/usaid_whistleblower\">https://www.democracynow.org/2026/4/16/usaid_whistleblower</a><br>"
        "PEPFAR primary policy analysis: KFF, \"The Status of President Trump's Pause of Foreign Aid and Implications for PEPFAR and other Global Health Programs.\" <a href=\"https://www.kff.org/policy-watch/the-status-of-president-trumps-pause-of-foreign-aid-and-implications-for-pepfar-and-other-global-health-programs/\">https://www.kff.org/policy-watch/the-status-of-president-trumps-pause-of-foreign-aid-and-implications-for-pepfar-and-other-global-health-programs/</a><br>"
        "PMI primary policy analysis: KFF, \"The Trump Administration's Foreign Aid Review: Status of the President's Malaria Initiative (PMI).\" <a href=\"https://www.kff.org/global-health-policy/the-trump-administrations-foreign-aid-review-status-of-the-presidents-malaria-initiative-pmi/\">https://www.kff.org/global-health-policy/the-trump-administrations-foreign-aid-review-status-of-the-presidents-malaria-initiative-pmi/</a>; "
        "KFF Fact Sheet (PDF): <a href=\"https://files.kff.org/attachment/fact-sheet-the-trump-administrations-foreign-aid-review-status-of-the-presidents-malaria-initiative-pmi.pdf\">https://files.kff.org/attachment/fact-sheet-the-trump-administrations-foreign-aid-review-status-of-the-presidents-malaria-initiative-pmi.pdf</a>; "
        "STAT News, \"Trump administration allows some global aid to restart, but concerns remain on impact of USAID shutdown,\" February 7, 2025. <a href=\"https://www.statnews.com/2025/02/07/trump-usaid-malaria-tuberculosis-funding-restored-waiver-granted-foreign-aid-freeze/\">https://www.statnews.com/2025/02/07/trump-usaid-malaria-tuberculosis-funding-restored-waiver-granted-foreign-aid-freeze/</a>; "
        "PMI program reference: <a href=\"https://en.wikipedia.org/wiki/President's_Malaria_Initiative\">https://en.wikipedia.org/wiki/President's_Malaria_Initiative</a><br>"
        "MCC primary policy analysis: Federal News Network, \"Millennium Challenge Corporation 'shutting down' in latest cut to foreign aid,\" April 2025. <a href=\"https://federalnewsnetwork.com/agency-oversight/2025/04/millennium-challenge-corporation-shutting-down-in-latest-cut-to-foreign-aid/\">https://federalnewsnetwork.com/agency-oversight/2025/04/millennium-challenge-corporation-shutting-down-in-latest-cut-to-foreign-aid/</a>; "
        "Devex, \"MCC board approves projects, terminates others at much-anticipated meeting.\" <a href=\"https://www.devex.com/news/mcc-board-approves-projects-terminates-others-at-much-anticipated-meeting-110711\">https://www.devex.com/news/mcc-board-approves-projects-terminates-others-at-much-anticipated-meeting-110711</a>; "
        "Devex, \"Millennium Challenge Corporation will survive, but many programs might not.\" <a href=\"https://www.devex.com/news/millennium-challenge-corporation-will-survive-but-many-programs-might-not-110602\">https://www.devex.com/news/millennium-challenge-corporation-will-survive-but-many-programs-might-not-110602</a>; "
        "Center for Global Development, \"What Are They Thinking: Is There a Rationale for the Proposed MCC Program Terminations?\" <a href=\"https://www.cgdev.org/blog/what-are-they-thinking-there-rationale-proposed-mcc-program-terminations\">https://www.cgdev.org/blog/what-are-they-thinking-there-rationale-proposed-mcc-program-terminations</a>; "
        "Center for Global Development, \"The Impact of Shuttering the Millennium Challenge Corporation.\" <a href=\"https://www.cgdev.org/blog/impact-shuttering-millennium-challenge-corporation\">https://www.cgdev.org/blog/impact-shuttering-millennium-challenge-corporation</a><br>"
        "Related tracker entries: enrich-wood-chipper-book-2026 (Enrich whistleblower memoir, 2026-04-14); intl-2026-usaid-shutdown-001 (USAID Shutdown Anniversary, 2026-03-18); intl-2026-pepfar-cuts-001 (PEPFAR Funding Crisis, 2026-03-01); oecd-aid-decline-2026 (OECD ODA collapse, 2026-04-10); eo-2026-doge-anniversary (DOGE one-year report, 2026-01-20)."
    ),
    "I": {
        "africanDescendant": {
            "people": "Sub-Saharan Africa, the principal recipient region of PEPFAR, PMI, and a substantial share of MCC compacts, faces the largest documented mortality and morbidity consequences. African-descendant diaspora communities in the United States have direct kinship ties to the populations served by these Bush-era Republican-built programs.",
            "places": "Health-system, malaria-control, and infrastructure investments built across sub-Saharan Africa over two decades of bipartisan U.S. commitment face collapse.",
            "practices": "U.S.-Africa public-health partnership practice across HIV/AIDS, malaria, and infrastructure, sustained across four administrations of both parties, is being severed.",
            "treasures": "Two decades of partner-government relationships, clinical-trial data, malaria-surveillance systems, and infrastructure investments tied to Bush-era programs are lost."
        },
        "latine": {
            "people": "Latin America and the Caribbean, principal recipients of MCC compacts and significant PEPFAR programming, face reduced services. Latiné diaspora communities in the United States have direct kinship ties to affected populations.",
            "places": "MCC-funded infrastructure projects across the Americas face termination.",
            "practices": "Hemispheric development practice loses bipartisan U.S. infrastructure.",
            "treasures": "Latin American MCC compacts and partnership institutional knowledge are lost."
        },
        "asianAmerican": {
            "people": "South Asia, Southeast Asia, and Pacific Asia, recipients of PEPFAR and MCC programming, face reduced services. Asian American diaspora communities have direct kinship ties to affected populations.",
            "places": "Asian MCC compacts and PEPFAR programming sites face reduced operational support.",
            "practices": "Trans-Pacific public-health and development practice loses bipartisan U.S. infrastructure.",
            "treasures": "Asian MCC compacts and partner-institution relationships are lost."
        },
        "pacificIslander": {
            "people": "Pacific Islander populations, including those in COFA states, lose programming through the broader retrenchment of which the Bush-era program dismantling is the principal driver.",
            "places": "Pacific public-health and infrastructure programs lose support.",
            "practices": "Pacific public-health partnership practice is being severed.",
            "treasures": "Pacific partnership institutional knowledge is lost."
        },
        "indigenous": {
            "people": "Indigenous communities globally, served by USAID Indigenous-rights and Indigenous-health programs and by some MCC compact components, lose programming.",
            "places": "Indigenous-served clinics and land-rights programs lose support.",
            "practices": "International Indigenous-rights solidarity practice loses U.S. infrastructure.",
            "treasures": "Indigenous-led partnerships and documentation funded by U.S. development programs are lost."
        },
        "allCommunities": {
            "people": "All populations served by Bush-era bipartisan international-development programs face reduced services. The bipartisan firewall that protected the programs across four administrations has been broken.",
            "places": "Health and infrastructure investments built across two decades face collapse.",
            "practices": "U.S. compassionate-conservatism development practice as a bipartisan operational tradition has been abandoned.",
            "treasures": "Two decades of bipartisan U.S. development institutional knowledge are being lost."
        }
    },
    "c": ["African-descendant", "Latiné", "Asian", "Pacific Islander", "Indigenous", "All Communities"],
    "U": "https://www.kff.org/policy-watch/the-status-of-president-trumps-pause-of-foreign-aid-and-implications-for-pepfar-and-other-global-health-programs/",
    "_source": "manual",
}


# ============== ENRICH ENTRY: REPLACE BUSH SECTION WITH CROSS-REFERENCE ==============
ENRICH_OLD_SECTION_START = "<b>GEORGE W. BUSH-ERA BIPARTISAN PROGRAMS DISMANTLED.</b>"
ENRICH_OLD_SECTION_END_MARKER = "(PEPFAR-specific entry: intl-2026-pepfar-cuts-001.)<br><br>"

ENRICH_REPLACEMENT = (
    "<b>BUSH-ERA BIPARTISAN PROGRAMS DISMANTLED (CROSS-REFERENCE).</b> "
    "Several of the programs Enrich documents being gutted were established under President George W. Bush and sustained on bipartisan footing across the Bush, Obama, first Trump, and Biden administrations. PEPFAR (2003), the President's Malaria Initiative (2005), and the Millennium Challenge Corporation (2004) have all been dismantled, deeply cut, or operationally crippled by the Trump II administration during 2025 and 2026. The cross-program pattern is captured in a discrete tracker entry at bush-era-bipartisan-programs-dismantled-2026. The PEPFAR-specific entry is at intl-2026-pepfar-cuts-001.<br><br>"
)


def main():
    if not DATA_PATH.exists():
        raise SystemExit(f"data.json not found at {DATA_PATH}")

    em_dash = "—"
    if em_dash in json.dumps(NEW_ENTRY, ensure_ascii=False):
        raise SystemExit("ABORT: em-dash detected in new entry.")
    if em_dash in ENRICH_REPLACEMENT:
        raise SystemExit("ABORT: em-dash detected in Enrich replacement block.")

    shutil.copy2(DATA_PATH, BACKUP_PATH)
    print(f"Backup written: {BACKUP_PATH.name}")

    with DATA_PATH.open() as f:
        data = json.load(f)

    # ---- Insert new discrete entry ----
    intl = data.get("international", [])
    if any((e.get("id") or e.get("i")) == NEW_ID for e in intl):
        print(f"Entry {NEW_ID} already exists. Skipping insert.")
    else:
        intl.append(NEW_ENTRY)
        data["international"] = intl
        print(f"Inserted {NEW_ID} into international.")

    # ---- Replace Bush section in Enrich entry with cross-reference ----
    enrich_target = None
    for e in data.get("international", []):
        if (e.get("id") or e.get("i")) == ENRICH_ID:
            enrich_target = e
            break
    if enrich_target is None:
        raise SystemExit(f"Enrich entry {ENRICH_ID} not found.")

    desc = enrich_target["D"]
    start_idx = desc.find(ENRICH_OLD_SECTION_START)
    if start_idx == -1:
        print("Old GEORGE W. BUSH section not found in Enrich entry. Skipping replacement.")
    else:
        end_marker_idx = desc.find(ENRICH_OLD_SECTION_END_MARKER, start_idx)
        if end_marker_idx == -1:
            raise SystemExit("End marker for old Bush section not found. Aborting.")
        end_idx = end_marker_idx + len(ENRICH_OLD_SECTION_END_MARKER)
        new_desc = desc[:start_idx] + ENRICH_REPLACEMENT + desc[end_idx:]
        enrich_target["D"] = new_desc
        print("Replaced Bush section in Enrich entry with cross-reference block.")

    if "meta" in data and isinstance(data["meta"], dict):
        data["meta"]["lastUpdated"] = datetime.now().strftime("%Y-%m-%d")

    tmp = DATA_PATH.with_suffix(".json.tmp")
    with tmp.open("w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    tmp.replace(DATA_PATH)

    print(f"Done. Total international: {len(data['international'])}.")


if __name__ == "__main__":
    main()
