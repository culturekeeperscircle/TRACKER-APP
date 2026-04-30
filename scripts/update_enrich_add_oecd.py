#!/usr/bin/env python3
"""Two operations on data.json, atomic with one backup.

1. Update the Enrich book entry (enrich-wood-chipper-book-2026) to
   incorporate Democracy Now! interview material from April 16, 2026:
   correct/clarify Enrich's career titles, add the March 2, 2025
   administrative-leave date, add the 750,000-already-dead figure
   stated by Enrich, add the Sudan testimony, add the Uganda Ebola
   national-security incident, add the Marco Rubio reversal, add
   Trump's verbatim "obscene, con job" remarks, add Enrich's
   "cruel and buffoons" framing, and add the children-born-with-HIV
   resurgence claim. Append Democracy Now! to the sources block.

2. Add a new international entry (oecd-aid-decline-2026) capturing the
   OECD 2025 official-development-assistance data: 23.1% global ODA
   contraction (largest on record), U.S. ODA down 56.9% (largest
   single-provider reduction on record), Germany surpasses the U.S.
   as largest DAC provider for the first time ever, OECD projects
   further 5.8% decline in 2026.
"""
import json
import shutil
from pathlib import Path
from datetime import datetime

DATA_PATH = Path(__file__).parent.parent / "data" / "data.json"
BACKUP_PATH = DATA_PATH.with_suffix(
    f".json.bak-{datetime.now().strftime('%Y%m%d-%H%M%S')}-pre-enrich-oecd-update"
)

ENRICH_ID = "enrich-wood-chipper-book-2026"
OECD_ID = "oecd-aid-decline-2026"


# ============== ENRICH ENTRY UPDATE ==============
# This block is inserted into the Enrich entry's description, immediately
# before the "<b>SOURCES.</b>" section, to add the Democracy Now! interview
# material.
ENRICH_INSERT = (
    "<b>DEMOCRACY NOW! INTERVIEW (APRIL 16, 2026): ADDITIONAL TESTIMONY.</b> "
    "On April 16, 2026, Enrich appeared on Democracy Now! with hosts Amy Goodman and Nermeen Shaikh to discuss the book. The interview elaborated specific claims and added new ones not captured in the Handbasket excerpt.<br><br>"
    "<b>ENRICH'S CAREER TITLE.</b> Enrich identified himself in the Democracy Now! interview as the former \"Director of Policy, Programs, and Planning in the Bureau of Global Health\" at USAID, in office until January 2025. He had served at USAID through four administrations. Other reporting describes his concurrent or successor role as Acting Assistant Administrator for Global Health.<br><br>"
    "<b>ADMINISTRATIVE LEAVE DATE.</b> Enrich stated he was placed on administrative leave on March 2, 2025 for exposing what he characterizes as the Trump administration's \"illegitimate and dangerous dismantling of the agency.\"<br><br>"
    "<b>UPDATED MORTALITY FIGURES.</b> Enrich stated that 750,000 people, most of them children, have already died as a result of the cuts, by conservative estimate. He projected up to 14 million additional unnecessary deaths over the next five years if the cuts are not rectified. He warned of a particular forward-looking harm: \"the next generation of children who are unable to get immunizations, with children being born with HIV at high rates when just a year ago those numbers were near zero.\"<br><br>"
    "<b>ENRICH'S TWO-CATEGORY FRAMING.</b> Enrich classified the Trump appointees who arrived to dismantle USAID as falling into two categories: \"those who were cruel and those who were buffoons.\" He placed most of the DOGE team in the second category and described them as \"uninformed, unqualified, and truly knew nothing about the agency that they had been tasked with dismantling.\"<br><br>"
    "<b>UGANDA EBOLA NATIONAL SECURITY INCIDENT.</b> During the early dismantling, an Ebola outbreak was active in Uganda. Enrich states that USAID could not mount its standard outbreak response because the agency was being dismantled, but a few key activities remained urgent. The political appointees and DOGE staff refused to allow USAID even to screen passengers at airports for Ebola symptoms before they boarded international flights onward to the United States. Enrich characterizes this as a direct national-security risk that the Trump appointees \"laughed off and ignored.\"<br><br>"
    "<b>MARCO RUBIO REVERSAL.</b> When Marco Rubio was named Secretary of State, USAID staff \"breathed a collective sigh of relief\" because Rubio had been one of the agency's strongest Senate-era champions. Enrich states that Rubio subsequently made false public claims that USAID staff were insubordinate and that no one has died because of the cuts. Enrich states both claims are untrue. Programs Rubio had previously championed have been dissolved.<br><br>"
    "<b>TRUMP'S OPERATIVE STATEMENT.</b> Speaking to reporters in February 2025, President Trump said USAID was \"absolutely obscene, dangerous, bad, very costly. I mean, virtually every investment made is a con job.\" Enrich frames this statement as the operative justification for a decision made by personnel \"who really knew nothing about the agency.\"<br><br>"
    "<b>SUDAN TESTIMONY.</b> Enrich identified Sudan, in its fourth year of war and currently bearing the world's worst humanitarian crisis, as \"one of the most glaring examples of what happens when the world's richest man is killing the world's poorest children.\" He testified that displaced Sudanese families and refugees, whose only access to health care and nutrition was through USAID services, walked all day to reach USAID-marked clinics only to find them shuttered. They could not access food supplements. Families returned home and made what Enrich called \"the harrowing decision of which of their children to feed.\"<br><br>"
    "<b>STRATEGIC GEOPOLITICAL CONSEQUENCE.</b> Enrich quoted President Obama's observation that \"for most people around the world, USAID is the United States.\" He warned that the dismantling of USAID will turn countries that were once U.S. partners toward Russia and China for support and will eliminate decades of U.S. soft-power infrastructure. Tracked separately at oecd-aid-decline-2026 is the OECD 2025 data showing U.S. ODA down 56.9% and Germany surpassing the United States as the largest provider of official development assistance for the first time in history.<br><br>"
    "<b>ENRICH'S CIVIC CALL.</b> The book's secondary purpose, Enrich states, is to remind readers \"that normal people can make important choices every day. And when people see things that they truly believe are not okay, they're being asked to do things that are illegal, and this is inside the government or in everyday life, whether you're working at a university or working at a law firm or just a neighbor who sees neighbors getting picked up on the streets by masked ICE agents, it's up to you to stand up and speak out when you see something wrong.\"<br><br>"
)

# Sources-block additions for the Enrich entry. Inserted immediately
# after the existing Simon & Schuster line in the SOURCES block.
ENRICH_SOURCES_INSERT = (
    "Author interview (full transcript reviewed): Democracy Now!, \"'Into the Wood Chipper': Whistleblower's Inside Story of DOGE Shredding USAID, 14 Million May Die,\" April 16, 2026. Hosts Amy Goodman and Nermeen Shaikh. <a href=\"https://www.democracynow.org/2026/4/16/usaid_whistleblower\">https://www.democracynow.org/2026/4/16/usaid_whistleblower</a><br>"
)


# ============== NEW OECD ENTRY ==============
OECD_ENTRY = {
    "i": OECD_ID,
    "t": "Advisory Report",
    "n": "OECD Official Development Assistance 2025 Preliminary Data: U.S. ODA Down 56.9%, Germany Surpasses U.S. as Largest DAC Provider for the First Time",
    "T": '<span style="color: #991B1B;">OECD ODA 2025:</span> Largest Annual Contraction in Recorded History; U.S. Drives Three-Quarters of the Decline; Germany Becomes Largest DAC Provider for First Time',
    "s": "OECD ODA collapse 2025",
    "d": "2026-04-10",
    "a": "Trump II",
    "A": ["State", "USAID", "OECD"],
    "S": "Active. OECD preliminary 2025 ODA data released April 2026. U.S. official development assistance fell 56.9% in 2025 compared to 2024, the largest reduction in volume by any provider in any year on record. Global ODA contracted 23.1%, the largest annual contraction on record and the second consecutive annual decline. Germany surpassed the U.S. as the largest DAC provider for the first time, at $29.1 billion. OECD projects a further 5.8% global decline in 2026.",
    "L": "SEVERE",
    "D": (
        "<b>OECD ODA DATA.</b> The Organisation for Economic Co-operation and Development (OECD) released preliminary 2025 official development assistance (ODA) data in April 2026. The data document the largest annual contraction in global development assistance on record and a structural shift in the global aid landscape directly attributable to U.S. policy decisions under the Trump II administration.<br><br>"
        "<b>U.S. ODA COLLAPSE.</b> U.S. ODA fell 56.9 percent in 2025 compared to 2024. This represents the largest reduction in ODA volume by any single provider in any year on record. The U.S. alone drove three-quarters of the global ODA decline. The reduction tracks directly to the dismantling of USAID (tracked at intl-2026-usaid-shutdown-001), the cuts to PEPFAR (tracked at intl-2026-pepfar-cuts-001), and the broader DOGE-led federal workforce purges (tracked at eo-2026-doge-anniversary).<br><br>"
        "<b>GERMANY SURPASSES THE UNITED STATES.</b> For the first time in the history of the Development Assistance Committee (DAC), Germany was the largest DAC provider of ODA in 2025, at $29.1 billion. The United States, which had been the largest DAC provider through every previous year of DAC reporting, ceded the position. The shift represents a structural realignment of the global aid system away from U.S. leadership.<br><br>"
        "<b>GLOBAL CONTRACTION.</b> Global ODA contracted 23.1 percent in 2025. This is the largest annual contraction on record and the second consecutive annual decline. Global ODA is now at its lowest level in ten years. The OECD projects a further 5.8 percent fall in ODA budgets in 2026.<br><br>"
        "<b>RELATIONSHIP TO ENRICH'S TESTIMONY.</b> Nicholas Enrich's whistleblower memoir (tracked at enrich-wood-chipper-book-2026) and his April 16, 2026 Democracy Now! interview directly anticipated this OECD data point. Enrich warned that the dismantling of USAID would precipitate broader retrenchment by other wealthy donors and would turn countries that were once U.S. partners toward Russia and China for support. The OECD's preliminary 2025 data confirms the magnitude of the U.S. retrenchment and the scale of the consequent global decline. Enrich quoted President Obama's observation that \"for most people around the world, USAID is the United States.\" The OECD data shows a world in which that statement is no longer operatively true.<br><br>"
        "<b>RELATIONSHIP TO PEER-REVIEWED MORTALITY ANALYSIS.</b> The Lancet's analysis (\"Evaluating the impact of two decades of USAID interventions and projecting the effects of defunding on mortality up to 2030\") projected more than 14 million avoidable deaths by 2030 from USAID cuts alone, including more than 4.5 million children under five. The OECD data on broader global ODA contraction implies additional avoidable mortality beyond the USAID-only figure, since wealthy-country aid serves overlapping but not identical populations. Health Policy Watch reported a separate Lancet-cited figure of 2.4 million additional deaths per year from USAID closure alone.<br><br>"
        "<b>STRATEGIC CONSEQUENCES.</b> The OECD data document a structural shift in the global aid system. The U.S. withdrawal opens a strategic vacuum that other donor states (notably China through its Belt and Road and Global Development Initiative programs, and Russia through its bilateral aid and security partnerships) can fill. The OECD projection of a further 5.8 percent global ODA decline in 2026 indicates that the contraction is not a one-time correction.<br><br>"
        "<b>CULTURAL RESOURCE THREAT ASSESSMENT.</b> The threat level is SEVERE. The OECD data document a structural decline in global development assistance directly attributable to U.S. policy under the Trump II administration. The decline reduces the resources available to communities with deep diaspora ties to all five TCKC primary cultural communities. Programs serving sub-Saharan Africa (African-descendant diaspora ties), Latin America and the Caribbean (Latiné and African-descendant diaspora ties), South and Southeast Asia (Asian diaspora ties), and the Pacific (Pacific Islander diaspora ties) are all reduced or eliminated."
        "<br><br>"
        "<b>SOURCES.</b><br>"
        "Primary source: OECD, ODA Trends and Statistics, preliminary 2025 data released April 2026. <a href=\"https://www.oecd.org/en/topics/oda-trends-and-statistics.html\">https://www.oecd.org/en/topics/oda-trends-and-statistics.html</a><br>"
        "OECD Development Co-operation Profile (Germany): <a href=\"https://www.oecd.org/en/publications/development-co-operation-profiles_04b376d7-en/germany_460a37b1-en.html\">https://www.oecd.org/en/publications/development-co-operation-profiles_04b376d7-en/germany_460a37b1-en.html</a><br>"
        "Coverage and analysis: The New Humanitarian, \"What the latest OECD numbers tell us about the future of aid,\" April 10, 2026. <a href=\"https://www.thenewhumanitarian.org/maps-and-graphics/2026/04/10/what-latest-oecd-numbers-tell-us-about-future-aid\">https://www.thenewhumanitarian.org/maps-and-graphics/2026/04/10/what-latest-oecd-numbers-tell-us-about-future-aid</a>; "
        "African Business, \"OECD data shows brutal drop in development assistance,\" April 2026. <a href=\"https://african.business/2026/04/politics/oecd-data-shows-brutal-drop-in-development-assistance\">https://african.business/2026/04/politics/oecd-data-shows-brutal-drop-in-development-assistance</a>; "
        "FactRefuge, \"International Development Aid Plummets in 2025.\" <a href=\"https://www.factrefuge.com/report/international-development-aid-plummets-in-2025/\">https://www.factrefuge.com/report/international-development-aid-plummets-in-2025/</a>; "
        "Visual Capitalist, \"Ranked: OECD Countries Giving the Most Foreign Aid.\" <a href=\"https://www.visualcapitalist.com/cp/ranked-oecd-countries-giving-the-most-foreign-aid/\">https://www.visualcapitalist.com/cp/ranked-oecd-countries-giving-the-most-foreign-aid/</a>; "
        "Our World in Data, \"Foreign aid given.\" <a href=\"https://ourworldindata.org/grapher/foreign-aid-given-grant-equivalents\">https://ourworldindata.org/grapher/foreign-aid-given-grant-equivalents</a><br>"
        "Author and book context: Democracy Now!, \"'Into the Wood Chipper': Whistleblower's Inside Story of DOGE Shredding USAID, 14 Million May Die,\" April 16, 2026 (Enrich identified the Germany-surpasses-U.S. fact in this interview). <a href=\"https://www.democracynow.org/2026/4/16/usaid_whistleblower\">https://www.democracynow.org/2026/4/16/usaid_whistleblower</a><br>"
        "Related tracker entries: enrich-wood-chipper-book-2026 (Enrich whistleblower memoir, 2026-04-14); intl-2026-usaid-shutdown-001 (USAID Shutdown Anniversary, 2026-03-18); intl-2026-pepfar-cuts-001 (PEPFAR cuts, 2026-03-01); eo-2026-doge-anniversary (DOGE one-year report, 2026-01-20)."
    ),
    "I": {
        "africanDescendant": {
            "people": "Sub-Saharan Africa, the largest single regional recipient of ODA in recent decades, faces the steepest absolute reductions. Populations served by HIV/AIDS, malaria, tuberculosis, and maternal-and-child-health programs face direct mortality and morbidity consequences. African-descendant diaspora communities in the United States have direct kinship ties to those populations.",
            "places": "Health-system, food-security, and education infrastructure across sub-Saharan Africa face collapse following the U.S. retrenchment.",
            "practices": "Cross-Atlantic public-health solidarity practice loses its primary federal-funding infrastructure.",
            "treasures": "Decades of U.S.-Africa partnership institutional knowledge and partner-government relationships are lost."
        },
        "latine": {
            "people": "Latin America and the Caribbean face reduced ODA across multiple sectors. Latiné diaspora communities in the United States have direct kinship ties to affected populations.",
            "places": "USAID-supported clinics, food-distribution networks, and disaster-response infrastructure across the hemisphere face closure.",
            "practices": "Hemispheric public-health and development practice loses U.S. operational support.",
            "treasures": "Decades of U.S.-Latin-American partnership institutional knowledge are lost."
        },
        "asianAmerican": {
            "people": "South Asia, Southeast Asia, and East Asia face reduced ODA across multiple sectors. Asian American diaspora communities have direct kinship ties to affected populations.",
            "places": "Health and education infrastructure across Asia faces reduced support.",
            "practices": "Trans-Pacific public-health and development practice loses U.S. operational support.",
            "treasures": "Decades of U.S.-Asia partnership institutional knowledge are lost."
        },
        "pacificIslander": {
            "people": "Pacific Islander populations, including those in COFA states, face reduced ODA. Pacific Islander diaspora communities in the United States have direct kinship ties to affected populations.",
            "places": "Climate-adaptation and public-health infrastructure across the Pacific faces reduced support.",
            "practices": "Pacific public-health and climate-resilience partnerships lose U.S. operational support.",
            "treasures": "Decades of U.S.-Pacific partnership institutional knowledge are lost."
        },
        "indigenous": {
            "people": "Indigenous communities globally, including in the Amazon basin, Mesoamerica, and elsewhere, face reduced support from U.S.-funded Indigenous-rights and Indigenous-health programs.",
            "places": "Indigenous-led land-rights, forest-protection, and health-clinic networks lose U.S. funding.",
            "practices": "International Indigenous-rights solidarity practice loses U.S. infrastructure.",
            "treasures": "Indigenous-led documentation and language-preservation programs that received U.S. funding lose support."
        },
        "allCommunities": {
            "people": "All populations served by U.S. official development assistance face reduced services. The OECD projection of a further 5.8 percent decline in 2026 indicates the harm compounds.",
            "places": "Aid-funded infrastructure globally faces reduced operational support.",
            "practices": "U.S. development practice as an instrument of soft power and partnership-building loses its operational base.",
            "treasures": "U.S. institutional knowledge in international development, accumulated since 1961, is lost as USAID is dismantled and ODA collapses."
        }
    },
    "c": ["African-descendant", "Latiné", "Asian", "Pacific Islander", "Indigenous", "All Communities"],
    "U": "https://www.oecd.org/en/topics/oda-trends-and-statistics.html",
    "_source": "manual",
}


def main():
    if not DATA_PATH.exists():
        raise SystemExit(f"data.json not found at {DATA_PATH}")

    em_dash = "—"
    if em_dash in ENRICH_INSERT or em_dash in ENRICH_SOURCES_INSERT:
        raise SystemExit("ABORT: em-dash detected in Enrich insert blocks.")
    if em_dash in json.dumps(OECD_ENTRY, ensure_ascii=False):
        raise SystemExit("ABORT: em-dash detected in OECD entry.")

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
    if "<b>DEMOCRACY NOW! INTERVIEW" in desc:
        print(f"Enrich entry already updated. Skipping description insert.")
    else:
        anchor = "<b>SOURCES.</b><br>"
        if anchor not in desc:
            raise SystemExit("SOURCES anchor not found in Enrich description.")
        new_desc = desc.replace(anchor, ENRICH_INSERT + anchor, 1)
        # Also insert Democracy Now! into sources block, after the Simon & Schuster page line
        ss_anchor = "9781668226957</a><br>"
        if ss_anchor not in new_desc:
            raise SystemExit("Simon & Schuster anchor not found in Enrich SOURCES.")
        new_desc = new_desc.replace(
            ss_anchor,
            ss_anchor + ENRICH_SOURCES_INSERT,
            1,
        )
        enrich_target["D"] = new_desc
        print(f"Updated Enrich entry: inserted Democracy Now! testimony block and source citation.")

    # ---- Add OECD entry ----
    intl = data.get("international", [])
    if any((e.get("id") or e.get("i")) == OECD_ID for e in intl):
        print(f"OECD entry {OECD_ID} already exists. Skipping insert.")
    else:
        intl.append(OECD_ENTRY)
        data["international"] = intl
        print(f"Inserted {OECD_ID} into international.")

    if "meta" in data and isinstance(data["meta"], dict):
        data["meta"]["lastUpdated"] = datetime.now().strftime("%Y-%m-%d")

    tmp = DATA_PATH.with_suffix(".json.tmp")
    with tmp.open("w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    tmp.replace(DATA_PATH)

    print(f"Done. Total international: {len(data['international'])}.")


if __name__ == "__main__":
    main()
