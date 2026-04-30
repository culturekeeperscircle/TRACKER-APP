#!/usr/bin/env python3
"""Three atomic additions, one backup.

A. Truth in National Parks Act (Davids and Goldman, introduced April 28,
   2026). PROTECTIVE legislation requiring reinstatement of NPS
   materials removed since January 20, 2025, prohibiting future erasure,
   and mandating tribal consultation before exhibit changes.
   Category: legislation. Threat: PROTECTIVE.

B. Burgum FY2027 Interior Budget Hearing (Senate Energy and Natural
   Resources Committee, April 29, 2026). Documents the Interior
   Secretary's defense of the proposed FY2027 budget cutting Interior
   13 percent and the NPS maintenance budget 40 percent.
   Category: other_domestic. Threat: SEVERE.

C. Markey and Blunt Rochester FY2027 appropriations letter (April 20,
   2026). 17 senators (Markey, Blunt Rochester, plus 15 cosigners)
   request that FY2027 appropriations include language prohibiting the
   use of taxpayer funds to implement or enforce SO 3431 (which
   implements EO 14253 Restoring Truth and Sanity to American History).
   Category: legislation. Threat: PROTECTIVE.
"""
import json
import shutil
from pathlib import Path
from datetime import datetime

DATA_PATH = Path(__file__).parent.parent / "data" / "data.json"
BACKUP_PATH = DATA_PATH.with_suffix(
    f".json.bak-{datetime.now().strftime('%Y%m%d-%H%M%S')}-pre-truth-npark-burgum-markey"
)


# =================== ENTRY A: TRUTH IN NATIONAL PARKS ACT ===================
ENTRY_A = {
    "id": "truth-in-national-parks-act-2026",
    "t": "Bill",
    "n": "Truth in National Parks Act (H.R. number pending Congress.gov indexing; introduced April 28, 2026 by Reps. Sharice Davids and Dan Goldman)",
    "T": '<span style="color: #065F46;">Truth in National Parks Act:</span> Davids and Goldman Bill to Reinstate NPS Materials Removed Under EO 14253 and SO 3431, Prohibit Future Erasure, and Mandate Tribal Consultation Before Exhibit Changes',
    "s": "Truth in National Parks Act",
    "d": "2026-04-28",
    "a": "Trump II",
    "A": ["NPS", "DOI", "BIA"],
    "S": "Active. Introduced April 28, 2026 by Representative Sharice Davids (D-KS-03, Ho-Chunk; one of the first two Native American women elected to Congress) and Representative Dan Goldman (D-NY-10). Pending Congress.gov H.R. number indexing. Endorsements include the National Congress of American Indians (NCAI), the National Parks Conservation Association (NPCA), the Sierra Club, and other Indigenous and conservation organizations. Operative provisions: (1) require reinstatement of all NPS materials removed since January 20, 2025; (2) prohibit future erasure of historical and cultural signs at NPS sites; (3) mandate consultation with Tribal Nations and other relevant stakeholders before making changes to NPS exhibits.",
    "L": "PROTECTIVE",
    "D": (
        "<b>BILL.</b> On April 28, 2026, Representative Sharice Davids (D-KS-03) and Representative Dan Goldman (D-NY-10) introduced the Truth in National Parks Act in the U.S. House of Representatives. The bill is a direct legislative response to the National Park Service's ongoing implementation of Executive Order 14253 (Restoring Truth and Sanity to American History, March 27, 2025; tracked at eo-14253) and Secretarial Order 3431 (Department of Interior Implementation, May 20, 2025; tracked at so-3431-truth-sanity-doi), under which NPS has removed historical and cultural materials referencing African-descendant, Indigenous, Latiné, Asian, Pacific Islander, and LGBTQ+ communities at park sites nationwide.<br><br>"
        "<b>OPERATIVE PROVISIONS.</b> The bill includes three core directives. First, it requires the National Park Service to reinstate all NPS materials (interpretive signs, exhibit panels, brochures, audiovisual content, online materials) that have been removed from any NPS site since January 20, 2025. Second, it prohibits the future removal or alteration of historical and cultural materials at NPS sites except through formal NEPA-and-NHPA-compliant review processes. Third, it mandates consultation with Tribal Nations and other relevant cultural-community stakeholders before any future exhibit changes at NPS sites with material affecting those communities.<br><br>"
        "<b>SPONSORS.</b> Lead sponsors are Rep. Sharice Davids (D-KS-03), an enrolled member of the Ho-Chunk Nation and one of the first two Native American women elected to Congress, and Rep. Dan Goldman (D-NY-10). The bill carries cosponsors from the Congressional Native American Caucus, the Congressional Hispanic Caucus, the Congressional Black Caucus, the Congressional Asian Pacific American Caucus, and the Congressional Equality Caucus.<br><br>"
        "<b>NPS HARMS THE BILL ADDRESSES.</b> NPS implementation of EO 14253 and SO 3431 has produced documented removal and alteration actions across NPS sites since January 20, 2025. Tracked exemplars include: NPS removal of the Stonewall National Monument LGBTQ+ history materials (which substituted \"LGB\" for \"LGBTQ+\" and stripped trans-women references); NPS removal of climate change signs at Acadia, Jamaica Bay, and other parks (tracked at nps-climate-signs-removal-2025); NPS Presidents House slavery exhibit removal in Philadelphia (tracked at nps-presidents-house-exhibit-removal-2026 and at philadelphia-v-doi-presidents-house-2026); NPS fee-free-day-elimination affecting MLK Day and Juneteenth (tracked at nps-fee-free-days-changes-2025); Lowell National Historical Park (Massachusetts) removal of two historical films; Independence National Historical Park (Philadelphia) interpretive-content alteration; Muir Woods (California) interpretive-content alteration. The Markey/Blunt Rochester April 20, 2026 appropriations letter (tracked at markey-blunt-rochester-fy2027-appropriations-letter-2026) cites these examples as the basis for the parallel appropriations-rider request.<br><br>"
        "<b>ENDORSEMENTS.</b> The National Congress of American Indians (NCAI), the National Parks Conservation Association (NPCA), and the Sierra Club have publicly endorsed the bill. The Society of American Archivists (SAA) issued a parallel statement on changes being made at national parks and monuments. The bill's tribal-consultation provision aligns with Joint Secretary's Order 3403 on Trust Responsibility (tracked at so-3403-co-stewardship) and with the United Nations Declaration on the Rights of Indigenous Peoples Free, Prior, and Informed Consent standard (tracked at intl-undrip-implementation).<br><br>"
        "<b>RELATIONSHIP TO PARALLEL FEDERAL ACTIONS.</b> The bill is the principal House-side legislative response to EO 14253 and SO 3431. The Senate-side parallel actions are: S. 2385 Restoring Truth and Sanity to American History Act (tracked at leg-2026-008 and at s-2385-codify-smithsonian-senate, which would CODIFY rather than counter the executive-order policy); and the Markey/Blunt Rochester April 20, 2026 appropriations letter (tracked at markey-blunt-rochester-fy2027-appropriations-letter-2026, which seeks an appropriations rider prohibiting funds for SO 3431 implementation). The principal litigation is NPCA et al. v. DOI (tracked at lit-2026-npca-v-doi).<br><br>"
        "<b>LEGISLATIVE PROSPECTS.</b> With Republican control of the House in the 119th Congress, the bill faces an uphill path to floor consideration. The bill nonetheless functions as the principal legislative-document anchor for tribal-consultation and historical-accuracy advocacy by Indigenous and civil-rights organizations.<br><br>"
        "<b>CULTURAL RESOURCE THREAT ASSESSMENT.</b> The threat level is PROTECTIVE. The bill, if enacted, would reverse the documented NPS erasure pattern affecting all five TCKC primary cultural communities. Even if the bill does not advance to enactment in the 119th Congress, its introduction establishes the legislative-document anchor that civil-rights and tribal-consultation litigation can reference."
        "<br><br>"
        "<b>SOURCES.</b><br>"
        "Primary sponsor materials: Rep. Sharice Davids, \"Reps. Davids, Goldman Introduce Bill to Protect Native American Culture Amid Administration's Removal of Historical Content at National Parks.\" <a href=\"https://davids.house.gov/media/press-releases/reps-davids-goldman-introduce-bill-protect-native-american-culture-amid\">https://davids.house.gov/media/press-releases/reps-davids-goldman-introduce-bill-protect-native-american-culture-amid</a><br>"
        "Bill text draft (PDF, House office): <a href=\"https://davids.house.gov/sites/evo-subsites/davids.house.gov/files/evo-media-document/daviks_050_xml.pdf\">https://davids.house.gov/sites/evo-subsites/davids.house.gov/files/evo-media-document/daviks_050_xml.pdf</a><br>"
        "Endorsements and analysis: Sierra Club, \"Sierra Club Endorses Truth in National Parks Act,\" April 2026. <a href=\"https://www.sierraclub.org/press-releases/2026/04/sierra-club-endorses-truth-national-parks-act\">https://www.sierraclub.org/press-releases/2026/04/sierra-club-endorses-truth-national-parks-act</a>; "
        "National Parks Conservation Association, \"Parks Group Responds to Executive Order Targeting American History.\" <a href=\"https://www.npca.org/articles/7769-parks-group-responds-to-executive-order-targeting-american-history\">https://www.npca.org/articles/7769-parks-group-responds-to-executive-order-targeting-american-history</a>; "
        "Society of American Archivists, \"SAA Statement on Changes Being Made at National Parks and Monuments.\" <a href=\"https://www2.archivists.org/news/2026/saa-statement-on-changes-being-made-at-national-parks-and-monuments\">https://www2.archivists.org/news/2026/saa-statement-on-changes-being-made-at-national-parks-and-monuments</a><br>"
        "Coverage: Native News Online, \"Rep. Davids Introduces Truth in National Parks Act to Protect Accurate Native History.\" <a href=\"https://nativenewsonline.net/currents/rep-davids-introduces-truth-in-national-parks-act-to-protect-accurate-native-history/\">https://nativenewsonline.net/currents/rep-davids-introduces-truth-in-national-parks-act-to-protect-accurate-native-history/</a>; "
        "The Travel, \"Native American Politician's New National Park Rule Proposal Could Stop President Trump's Censorship Of U.S. History.\" <a href=\"https://www.thetravel.com/native-american-sharice-davids-truth-in-national-parks-act-could-stop-trump-censorship-us-history/\">https://www.thetravel.com/native-american-sharice-davids-truth-in-national-parks-act-could-stop-trump-censorship-us-history/</a><br>"
        "Related tracker entries: eo-14253 (EO 14253 Restoring Truth and Sanity, 2025-03-27); so-3431-truth-sanity-doi (SO 3431 DOI Implementation, 2025-05-20); leg-2026-008 (S. 2385 Restoring Truth and Sanity Codification Bill); markey-blunt-rochester-fy2027-appropriations-letter-2026 (Markey appropriations letter, 2026-04-20); burgum-fy2027-budget-hearing-2026-04-29 (Burgum FY2027 budget hearing, 2026-04-29); nps-presidents-house-exhibit-removal-2026 (NPS Presidents House exhibit removal); philadelphia-v-doi-presidents-house-2026 (Philadelphia v. DOI litigation); nps-climate-signs-removal-2025 (NPS climate signs removal); nps-fee-free-days-changes-2025 (NPS fee-free days policy change); lit-2026-npca-v-doi (NPCA v. DOI litigation); so-3403-co-stewardship (Joint SO 3403 trust responsibility)."
    ),
    "I": {
        "indigenous": {
            "people": "Indigenous nations whose history has been erased from NPS interpretive materials at sites including Stonewall (trans-women contributions), the Trail of Tears NHT, Sand Creek Massacre NHS, Bear Paw Battlefield (Nez Perce NHP), Trail of Death corridor markers, and other Indigenous-history sites would have those materials reinstated.",
            "places": "NPS sites at which Indigenous-history materials have been removed since January 20, 2025 face restoration of those materials. Tribal-consultation requirement applies to all future exhibit changes affecting tribal-cultural-resource interests.",
            "practices": "Tribal historic-preservation-officer (THPO) practice and federal-Indian-trust consultation practice are strengthened by the mandatory-consultation requirement.",
            "treasures": "Indigenous-history NPS interpretive materials and the underlying tribal-government documentation that informed them face restoration."
        },
        "africanDescendant": {
            "people": "African-descendant communities whose history has been erased from NPS interpretive materials at sites including Independence NHP (Philadelphia), the President's House Slavery Memorial, Frederick Douglass NHS, Tuskegee Institute NHS, African Burial Ground NM, and other Black-history sites would have those materials reinstated.",
            "places": "NPS sites with Black-history materials removed face restoration. The Lowell NHP two-films removal and the Philadelphia Independence NHP material alterations cited in the Markey letter would be reversed.",
            "practices": "Black-community history-keeping practice and Black scholarly-historical practice gain federal-statutory backing.",
            "treasures": "African-descendant historical interpretive materials face restoration."
        },
        "latine": {
            "people": "Latiné communities whose history has been erased face restoration. NPS sites with Spanish colonial, Mexican-American War, Bracero Program, Chicano civil rights, and other Latiné-history materials altered or removed face reversal.",
            "places": "NPS sites with Latiné-history materials face restoration.",
            "practices": "Latiné-community history-keeping practice gains federal-statutory backing.",
            "treasures": "Latiné historical interpretive materials face restoration."
        },
        "asianAmerican": {
            "people": "Asian American communities whose history has been erased face restoration. NPS sites covering Manzanar, Tule Lake, Minidoka, and other Japanese internment sites and broader Asian American history sites face material restoration.",
            "places": "Japanese American Confinement Sites and other Asian American history sites face restoration.",
            "practices": "Asian American history-keeping practice gains federal-statutory backing.",
            "treasures": "Asian American historical interpretive materials face restoration."
        },
        "pacificIslander": {
            "people": "Pacific Islander communities whose history has been erased face restoration. NPS sites covering the World War II in the Pacific NHP, Pearl Harbor NM, and other Pacific Islander history sites face material restoration.",
            "places": "Pacific Islander history sites face restoration.",
            "practices": "Pacific Islander history-keeping practice gains federal-statutory backing.",
            "treasures": "Pacific Islander historical interpretive materials face restoration."
        },
        "lgbtq": {
            "people": "LGBTQ+ communities whose history has been erased from Stonewall NM (LGB substitution for LGBTQ+, removal of trans-women references) and other LGBTQ+-history sites face material restoration.",
            "places": "Stonewall National Monument and other LGBTQ+-history sites face restoration.",
            "practices": "LGBTQ+ history-keeping practice gains federal-statutory backing.",
            "treasures": "LGBTQ+ historical interpretive materials face restoration."
        },
        "allCommunities": {
            "people": "All NPS visitors and the broader American public benefit from accurate historical interpretation at NPS sites.",
            "places": "All NPS sites benefit from a federal-statutory framework requiring transparent historical interpretation.",
            "practices": "NPS interpretive practice is strengthened by the consultation requirement.",
            "treasures": "The NPS interpretive-materials inheritance is preserved against politically motivated removal."
        }
    },
    "c": ["Indigenous", "African-descendant", "Latiné", "Asian", "Pacific Islander", "lgbtq", "All Communities"],
    "U": "https://davids.house.gov/media/press-releases/reps-davids-goldman-introduce-bill-protect-native-american-culture-amid",
    "_source": "manual",
}


# =================== ENTRY B: BURGUM FY2027 BUDGET HEARING ===================
ENTRY_B = {
    "i": "burgum-fy2027-budget-hearing-2026-04-29",
    "t": "Senate Hearing on Federal Budget Proposal",
    "n": "Burgum FY2027 Interior Budget Hearing: Senate Energy and Natural Resources Committee, April 29, 2026. Interior Secretary Defends FY2027 Budget Request Cutting Interior 13 Percent and NPS Maintenance 40 Percent",
    "T": '<span style="color: #991B1B;">Burgum FY2027 Interior Budget Hearing:</span> Senate Energy and Natural Resources Committee. Interior Secretary Defends Proposed 13 Percent Interior Cut and 40 Percent NPS Maintenance Budget Cut as More "Efficient"',
    "s": "Burgum FY2027 budget hearing",
    "d": "2026-04-29",
    "a": "Trump II",
    "A": ["DOI", "NPS", "OMB"],
    "S": "Active. Senate Energy and Natural Resources Committee hearing held April 29, 2026 with Interior Secretary Doug Burgum testifying in defense of the Trump administration's FY2027 budget request. The FY2027 budget proposes a 13 percent cut to the Department of the Interior and a 40 percent cut to the National Park Service maintenance budget. Burgum defended the cuts by claiming the government can perform maintenance more \"efficiently.\" The National Parks Conservation Association (NPCA) issued a public rebuke of Burgum's misrepresentation of NPS staffing.",
    "L": "SEVERE",
    "D": (
        "<b>HEARING.</b> On April 29, 2026, the U.S. Senate Committee on Energy and Natural Resources held a hearing at which Interior Secretary Doug Burgum testified in defense of the Trump administration's Fiscal Year 2027 budget request for the Department of the Interior. The hearing's principal subject was the proposed budget cuts to the Interior Department and the National Park Service.<br><br>"
        "<b>BUDGET CUTS DEFENDED.</b> The FY2027 budget request proposes a 13 percent cut to the Department of the Interior overall and a 40 percent cut to the National Park Service maintenance budget. Burgum defended the cuts by asserting that the government can perform maintenance more efficiently than current operating practices reflect. Committee members questioned the basis for the efficiency claim and challenged Burgum's representations about NPS staffing levels.<br><br>"
        "<b>STAFFING CONTEXT.</b> The proposed FY2027 cuts would compound the documented 24 percent NPS permanent-staff reduction already in effect (tracked at v2025-doi-001), the 100-plus NARA staff reductions documented separately (tracked at v2025-nara-005), and the broader DOGE-mediated federal-workforce reductions (tracked at eo-2026-doge-anniversary). The cumulative reduction in NPS operational capacity is substantial. NPCA characterized Burgum's testimony as misrepresenting NPS staffing realities.<br><br>"
        "<b>MAINTENANCE BACKLOG IMPLICATIONS.</b> The NPS deferred-maintenance backlog has been a longstanding bipartisan concern. Senator Angus King (I-Maine) had previously secured commitments from the Burgum-led Interior Department to address the maintenance backlog. The proposed 40 percent cut to NPS maintenance is materially inconsistent with those commitments. The Great American Outdoors Act (Pub. L. 116-152, 2020), which created the National Parks and Public Lands Legacy Restoration Fund, was a bipartisan response to the maintenance-backlog concern. The proposed FY2027 cut threatens the operational complement to the GAOA-funded restoration program.<br><br>"
        "<b>RELATIONSHIP TO BROADER PATTERN.</b> The FY2027 budget request operates within the broader Trump II administration pattern of cultural-institution defunding tracked at multiple entries: leg-2025-004 (FY2026 Interior Appropriations 35 percent NEA-and-NEH cuts); aa-2026-doge-neh-001 (DOGE-led NEH grant terminations); v2025-cpb-002 (Public Broadcasting Stations layoffs and closures); v2025-doi-001 (NPS 24 percent permanent-staff reduction); aa-2026-nara-leadership (NARA leadership change); and the broader DOGE workforce reduction (tracked at eo-2026-doge-anniversary). The April 29 hearing is the principal documentary record of the FY2027 phase of this pattern.<br><br>"
        "<b>RELATIONSHIP TO HISTORIC-EXHIBIT DESTRUCTION PATTERN.</b> The proposed cuts compound the cultural-resource harm produced by NPS implementation of EO 14253 and SO 3431, under which historical and cultural materials affecting TCKC primary cultural communities have been removed at NPS sites nationwide. Reduced NPS operational capacity will further compromise the agency's ability to defend interpretive materials against politically directed removal. The Truth in National Parks Act (tracked at truth-in-national-parks-act-2026) and the Markey/Blunt Rochester appropriations letter (tracked at markey-blunt-rochester-fy2027-appropriations-letter-2026) are the principal legislative responses to this combined budget-and-erasure pattern.<br><br>"
        "<b>CULTURAL RESOURCE THREAT ASSESSMENT.</b> The threat level is SEVERE. A 40 percent cut to NPS maintenance directly compromises the operational capacity required to maintain interpretive materials, archaeological sites, historic structures, and natural resources at NPS sites that hold significance for all five TCKC primary cultural communities. The cumulative pattern (staff reductions plus maintenance cuts plus politically directed exhibit removals) produces a structural attack on federal cultural-resource stewardship at scale."
        "<br><br>"
        "<b>SOURCES.</b><br>"
        "Primary coverage: National Parks Traveler, \"Burgum Defends Proposed Cuts To Park System Budget During Committee Hearing,\" April 2026. <a href=\"https://www.nationalparkstraveler.org/2026/04/burgum-defends-proposed-cuts-park-system-budget-during-committee-hearing\">https://www.nationalparkstraveler.org/2026/04/burgum-defends-proposed-cuts-park-system-budget-during-committee-hearing</a><br>"
        "NPCA rebuke: National Parks Conservation Association, \"Parks Group Rebukes Secretary Burgum's Misrepresentation of National Park Staffing.\" <a href=\"https://www.npca.org/articles/9221-parks-group-rebukes-secretary-burgum-s-misrepresentation-of-national-park\">https://www.npca.org/articles/9221-parks-group-rebukes-secretary-burgum-s-misrepresentation-of-national-park</a><br>"
        "Senate committee record: U.S. Senate Committee on Energy and Natural Resources, National Parks portfolio. <a href=\"https://www.energy.senate.gov/national-parks\">https://www.energy.senate.gov/national-parks</a><br>"
        "Senate floor record: <a href=\"https://www.congress.gov/on-senate-floor-today\">https://www.congress.gov/on-senate-floor-today</a><br>"
        "Senate executive calendar: <a href=\"https://www.senate.gov/legislative/LIS/executive_calendar/xcalv.pdf\">https://www.senate.gov/legislative/LIS/executive_calendar/xcalv.pdf</a><br>"
        "Related tracker entries: v2025-doi-001 (NPS 24 percent permanent-staff reduction); v2025-doi-008 (43-day government shutdown furloughs); leg-2025-004 (FY2026 Interior Appropriations cuts to NEA and NEH); eo-2026-doge-anniversary (DOGE one-year report); eo-14253 (EO 14253 Restoring Truth and Sanity); so-3431-truth-sanity-doi (SO 3431 DOI Implementation); truth-in-national-parks-act-2026 (Truth in National Parks Act); markey-blunt-rochester-fy2027-appropriations-letter-2026 (Markey appropriations letter); lit-2026-npca-v-doi (NPCA v. DOI litigation)."
    ),
    "I": {
        "indigenous": {
            "people": "Indigenous communities whose tribal-cultural-resource interests are stewarded by NPS at parks including Mesa Verde, Chaco Culture, Navajo NM, Chickasaw NRA, and dozens of other tribal-affiliated sites face reduced NPS operational capacity to protect those resources.",
            "places": "Tribal-affiliated NPS sites face reduced maintenance, ranger presence, interpretive programming, and protective enforcement.",
            "practices": "Federal-Indian-trust stewardship practice operating through NPS is weakened.",
            "treasures": "Tribal-affiliated archaeological sites, sacred sites, and cultural-heritage properties under NPS stewardship face reduced protection."
        },
        "africanDescendant": {
            "people": "African-descendant communities whose history is stewarded by NPS at sites including Frederick Douglass NHS, Tuskegee Institute NHS, Tuskegee Airmen NHS, African Burial Ground NM, Birmingham Civil Rights NM, Selma to Montgomery NHT, and many others face reduced operational capacity at those sites.",
            "places": "Black-history NPS sites face reduced maintenance and programming.",
            "practices": "Federal Black-history stewardship practice is weakened.",
            "treasures": "Black-history archaeological and historic-structure resources face reduced protection."
        },
        "latine": {
            "people": "Latiné communities whose history is stewarded at sites including Cesar E. Chavez NM, San Antonio Missions NHP, Castillo de San Marcos NM, and El Camino Real de los Tejas NHT face reduced operational capacity.",
            "places": "Latiné-history NPS sites face reduced maintenance and programming.",
            "practices": "Federal Latiné-history stewardship practice is weakened.",
            "treasures": "Spanish colonial, Mexican-American, and Chicano-history resources face reduced protection."
        },
        "asianAmerican": {
            "people": "Asian American communities whose history is stewarded at Japanese American Confinement Sites (Manzanar, Tule Lake, Minidoka, Honouliuli) face reduced operational capacity at those sites.",
            "places": "Asian American confinement-history sites face reduced maintenance and programming.",
            "practices": "Federal Asian American history stewardship practice is weakened.",
            "treasures": "Japanese American confinement archaeological and structural resources face reduced protection."
        },
        "pacificIslander": {
            "people": "Pacific Islander communities whose history is stewarded at War in the Pacific NHP (Guam), Pearl Harbor NM, and other Pacific NPS sites face reduced operational capacity.",
            "places": "Pacific Islander history sites face reduced maintenance and programming.",
            "practices": "Federal Pacific Islander history stewardship practice is weakened.",
            "treasures": "Pacific Islander historic and ecological resources face reduced protection."
        },
        "allCommunities": {
            "people": "All NPS visitors face reduced ranger presence, interpretive programming, maintenance of facilities, and protective enforcement at all 433 NPS units.",
            "places": "All 433 NPS units face cumulative degradation under sustained budget contraction.",
            "practices": "Federal cultural-resource stewardship practice is weakened across the agency.",
            "treasures": "The federal-cultural-resource inheritance held in trust by NPS faces cumulative degradation."
        }
    },
    "c": ["Indigenous", "African-descendant", "Latiné", "Asian", "Pacific Islander", "All Communities"],
    "U": "https://www.nationalparkstraveler.org/2026/04/burgum-defends-proposed-cuts-park-system-budget-during-committee-hearing",
    "_source": "manual",
}


# =================== ENTRY C: MARKEY/BLUNT ROCHESTER LETTER ===================
ENTRY_C = {
    "id": "markey-blunt-rochester-fy2027-appropriations-letter-2026",
    "t": "Senate Appropriations Letter",
    "n": "Senators Markey and Blunt Rochester FY2027 Appropriations Letter (April 20, 2026): 17 Senators Request Appropriations Rider Prohibiting Funds for SO 3431 Implementation of EO 14253",
    "T": '<span style="color: #065F46;">Markey and Blunt Rochester FY2027 Appropriations Letter:</span> 17 Senators Request Appropriations Rider Prohibiting Use of Taxpayer Funds to Implement or Enforce SO 3431 (Which Implements EO 14253 Restoring Truth and Sanity to American History)',
    "s": "Markey Blunt Rochester FY2027 letter",
    "d": "2026-04-20",
    "a": "Trump II",
    "A": ["DOI", "NPS"],
    "S": "Active. Letter sent April 20, 2026 by Senator Edward J. Markey (D-MA) and Senator Lisa Blunt Rochester (D-DE), members of the Environment and Public Works Committee, leading 15 colleagues. Addressed to the chair and ranking member of the Senate Appropriations Subcommittee on Interior, Environment, and Related Agencies. Requests that FY2027 appropriations legislation include language prohibiting the use of taxpayer funds to implement or enforce Department of the Interior Secretarial Order 3431, which implements Executive Order 14253 (Restoring Truth and Sanity to American History). Cosigners: Ben Ray Lujan, Bernie Sanders, Andy Kim, Richard Blumenthal, Chris Van Hollen, Tammy Duckworth, Angela D. Alsobrooks, Mazie K. Hirono, Catherine Cortez Masto, Ron Wyden, Jack Reed, Angus S. King Jr., Cory Booker, Martin Heinrich, Jeanne Shaheen.",
    "L": "PROTECTIVE",
    "D": (
        "<b>LETTER.</b> On April 20, 2026, Senator Edward J. Markey (D-MA) and Senator Lisa Blunt Rochester (D-DE), both members of the Environment and Public Works Committee, sent a letter to the chair and ranking member of the Senate Appropriations Subcommittee on Interior, Environment, and Related Agencies. The letter was joined by 15 cosigners. The letter requests that Fiscal Year 2027 appropriations legislation for the Department of the Interior include statutory language prohibiting the use of taxpayer funds to implement or enforce Department of the Interior Secretarial Order 3431.<br><br>"
        "<b>SECRETARIAL ORDER 3431 BACKGROUND.</b> Secretarial Order 3431 (May 20, 2025) is the Department of the Interior's implementing instrument for Executive Order 14253, \"Restoring Truth and Sanity to American History\" (March 27, 2025; tracked at eo-14253). SO 3431 (tracked at so-3431-truth-sanity-doi) directs the Department of the Interior to review all public monuments, memorials, statues, markers, or similar properties under DOI jurisdiction and to remove content deemed to inappropriately disparage Americans past or living. The order has resulted in the arbitrary flagging of thousands of interpretive signs and educational materials across NPS sites, with documented removal and alteration of historic exhibits in multiple parks.<br><br>"
        "<b>NPS HARMS THE LETTER CITES.</b> The Markey letter cites three specific examples of NPS exhibits that have been altered or removed under SO 3431. First, Lowell National Historical Park (Massachusetts) had two historical films removed. Second, Independence National Historical Park (Philadelphia) experienced material alteration including changes to the President's House Slavery Memorial (tracked separately at nps-presidents-house-exhibit-removal-2026 and at philadelphia-v-doi-presidents-house-2026). Third, Muir Woods (California) experienced interpretive-content alteration. The letter characterizes the SO 3431 implementation as \"censorship of historical National Park exhibits.\"<br><br>"
        "<b>SEVENTEEN SIGNATORIES.</b> The letter is led by Senator Markey and Senator Blunt Rochester and joined by 15 cosigners: Senator Ben Ray Lujan (D-NM), Senator Bernie Sanders (I-VT), Senator Andy Kim (D-NJ), Senator Richard Blumenthal (D-CT), Senator Chris Van Hollen (D-MD), Senator Tammy Duckworth (D-IL), Senator Angela D. Alsobrooks (D-MD), Senator Mazie K. Hirono (D-HI), Senator Catherine Cortez Masto (D-NV), Senator Ron Wyden (D-OR), Senator Jack Reed (D-RI), Senator Angus S. King Jr. (I-ME), Senator Cory Booker (D-NJ), Senator Martin Heinrich (D-NM), and Senator Jeanne Shaheen (D-NH). The 17-senator coalition includes Environment and Public Works Committee members, Energy and Natural Resources Committee members, Native American senators (Hirono, Cortez Masto), and senators representing states with prominent NPS sites affected by SO 3431 implementation.<br><br>"
        "<b>APPROPRIATIONS-RIDER MECHANISM.</b> The requested rider operates as a Hyde-style funding restriction, prohibiting the executive branch from spending appropriated funds on a specific category of activity. The rider mechanism has historical precedent in cultural and civil-rights appropriations contexts. If included in the FY2027 Interior, Environment, and Related Agencies appropriations bill, the rider would have the practical effect of halting SO 3431 implementation while leaving the executive order itself in legal force. The rider would persist for the duration of the appropriated-funds period and would require renewal in subsequent appropriations cycles.<br><br>"
        "<b>RELATIONSHIP TO PARALLEL ACTIONS.</b> The Markey letter is the Senate-side appropriations counterpart to the House-side Truth in National Parks Act introduced April 28, 2026 by Reps. Davids and Goldman (tracked at truth-in-national-parks-act-2026). Together, the two actions represent the principal legislative response to EO 14253 and SO 3431 in the 119th Congress. The Burgum FY2027 budget hearing of April 29, 2026 (tracked at burgum-fy2027-budget-hearing-2026-04-29) is the Senate-committee oversight context within which the appropriations-rider request will be evaluated. The principal litigation is NPCA et al. v. DOI (tracked at lit-2026-npca-v-doi).<br><br>"
        "<b>LEGISLATIVE PROSPECTS.</b> Appropriations riders require negotiation with House Republican appropriations leadership and acceptance by the President in conference or as part of an omnibus appropriations vehicle. The 17-senator letter establishes the documentary anchor for the appropriations-rider request and creates negotiating leverage for the Senate Appropriations Subcommittee on Interior, Environment, and Related Agencies during FY2027 markup.<br><br>"
        "<b>CULTURAL RESOURCE THREAT ASSESSMENT.</b> The threat level is PROTECTIVE. The letter, if its requested appropriations rider is enacted, would halt the SO 3431 implementation pattern that has produced documented removal and alteration of NPS interpretive materials affecting all five TCKC primary cultural communities. Even absent enactment, the letter establishes the documentary anchor for civil-rights and tribal-consultation advocacy by establishing 17 Senate signatories on the record opposing SO 3431 implementation."
        "<br><br>"
        "<b>SOURCES.</b><br>"
        "Primary letter: Senator Edward J. Markey, \"Senators Markey, Blunt Rochester Lead Colleagues in Demanding a Stop to the Use of Taxpayer Funds for Censorship of Historical National Park Exhibits.\" <a href=\"https://www.markey.senate.gov/news/press-releases/senators-markey-blunt-rochester-lead-colleagues-in-demanding-a-stop-to-the-use-of-taxpayer-funds-for-censorship-of-historical-national-park-exhibits\">https://www.markey.senate.gov/news/press-releases/senators-markey-blunt-rochester-lead-colleagues-in-demanding-a-stop-to-the-use-of-taxpayer-funds-for-censorship-of-historical-national-park-exhibits</a><br>"
        "Underlying federal action: \"Executive Order 14253: Restoring Truth and Sanity to American History,\" March 27, 2025 (American Presidency Project). <a href=\"https://www.presidency.ucsb.edu/documents/executive-order-14253-restoring-truth-and-sanity-american-history\">https://www.presidency.ucsb.edu/documents/executive-order-14253-restoring-truth-and-sanity-american-history</a>; "
        "Federal Register publication of EO 14253: <a href=\"https://www.federalregister.gov/documents/2025/04/03/2025-05838/restoring-truth-and-sanity-to-american-history\">https://www.federalregister.gov/documents/2025/04/03/2025-05838/restoring-truth-and-sanity-to-american-history</a><br>"
        "Congressional Research Service: \"Smithsonian Institution: Potential Effects of Executive Order 14253\" (CRS IF12975). <a href=\"https://www.congress.gov/crs-product/IF12975\">https://www.congress.gov/crs-product/IF12975</a><br>"
        "Reference: Wikipedia, \"Executive Order 14253.\" <a href=\"https://en.wikipedia.org/wiki/Executive_Order_14253\">https://en.wikipedia.org/wiki/Executive_Order_14253</a>; "
        "Health Equity Policy Hub, \"Restoring Truth and Sanity to American History.\" <a href=\"https://www.healthequitypolicyhub.org/policies/restoring-truth-and-sanity-to-american-history\">https://www.healthequitypolicyhub.org/policies/restoring-truth-and-sanity-to-american-history</a><br>"
        "Related tracker entries: eo-14253 (EO 14253 Restoring Truth and Sanity, 2025-03-27); so-3431-truth-sanity-doi (SO 3431 DOI Implementation, 2025-05-20); leg-2026-008 (S. 2385 Restoring Truth and Sanity Codification Bill); truth-in-national-parks-act-2026 (Truth in National Parks Act, House response); burgum-fy2027-budget-hearing-2026-04-29 (Burgum FY2027 budget hearing); nps-presidents-house-exhibit-removal-2026 (NPS Presidents House exhibit removal); philadelphia-v-doi-presidents-house-2026 (Philadelphia v. DOI litigation); nps-climate-signs-removal-2025 (NPS climate signs removal); nps-fee-free-days-changes-2025 (NPS fee-free days policy change); lit-2026-npca-v-doi (NPCA v. DOI litigation); ea-2026-columbus-statue (Columbus Statue White House installation); aa-2026-imls-political-grants (IMLS political-alignment grant guidelines); v2025-003 (Smithsonian divisive-narratives review)."
    ),
    "I": {
        "indigenous": {
            "people": "Indigenous communities whose history is at stake under SO 3431 at NPS sites benefit from the appropriations-rider request that would halt SO 3431 implementation.",
            "places": "Tribal-affiliated NPS sites face protection from further SO 3431-driven material removal if the rider is enacted.",
            "practices": "Tribal historic-preservation-officer (THPO) practice and tribal-consultation practice are protected.",
            "treasures": "Tribal historical interpretive materials face protection from further removal."
        },
        "africanDescendant": {
            "people": "African-descendant communities whose history is at stake at NPS sites including the Lowell NHP films, Independence NHP and the President's House Slavery Memorial, Frederick Douglass NHS, Tuskegee Institute NHS, and other Black-history sites benefit directly.",
            "places": "Black-history NPS sites face protection from further removal of material.",
            "practices": "Federal Black-history stewardship practice is protected.",
            "treasures": "Black-history interpretive materials face protection from further removal."
        },
        "latine": {
            "people": "Latiné communities whose history is at stake at NPS sites including San Antonio Missions NHP, Cesar E. Chavez NM, and Spanish colonial NPS sites benefit directly.",
            "places": "Latiné-history NPS sites face protection.",
            "practices": "Federal Latiné-history stewardship practice is protected.",
            "treasures": "Latiné historical interpretive materials face protection."
        },
        "asianAmerican": {
            "people": "Asian American communities whose history is at stake at Japanese American Confinement Sites and other Asian American history sites benefit directly.",
            "places": "Asian American history NPS sites face protection.",
            "practices": "Federal Asian American history stewardship practice is protected.",
            "treasures": "Asian American historical interpretive materials face protection."
        },
        "pacificIslander": {
            "people": "Pacific Islander communities whose history is at stake at War in the Pacific NHP, Pearl Harbor NM, and other Pacific NPS sites benefit directly.",
            "places": "Pacific Islander history NPS sites face protection.",
            "practices": "Federal Pacific Islander history stewardship practice is protected.",
            "treasures": "Pacific Islander historical interpretive materials face protection."
        },
        "lgbtq": {
            "people": "LGBTQ+ communities whose history is at stake at Stonewall NM and other LGBTQ+-history NPS sites (where SO 3431 has produced documented removal of trans-women references and substitution of LGB for LGBTQ+) benefit directly.",
            "places": "Stonewall National Monument and other LGBTQ+-history sites face protection.",
            "practices": "LGBTQ+ history-keeping practice is protected.",
            "treasures": "LGBTQ+ historical interpretive materials face protection."
        },
        "allCommunities": {
            "people": "All NPS visitors and the broader American public benefit from accurate historical interpretation.",
            "places": "All NPS sites benefit from a federal-statutory funding restriction halting SO 3431 implementation.",
            "practices": "NPS interpretive practice is protected from politically directed material removal.",
            "treasures": "The NPS interpretive-materials inheritance is protected."
        }
    },
    "c": ["Indigenous", "African-descendant", "Latiné", "Asian", "Pacific Islander", "lgbtq", "All Communities"],
    "U": "https://www.markey.senate.gov/news/press-releases/senators-markey-blunt-rochester-lead-colleagues-in-demanding-a-stop-to-the-use-of-taxpayer-funds-for-censorship-of-historical-national-park-exhibits",
    "_source": "manual",
}


def main():
    if not DATA_PATH.exists():
        raise SystemExit(f"data.json not found at {DATA_PATH}")

    em_dash = "—"
    for label, e in [("A", ENTRY_A), ("B", ENTRY_B), ("C", ENTRY_C)]:
        if em_dash in json.dumps(e, ensure_ascii=False):
            raise SystemExit(f"ABORT: em-dash detected in entry {label} ({e.get('id') or e.get('i')}).")

    shutil.copy2(DATA_PATH, BACKUP_PATH)
    print(f"Backup written: {BACKUP_PATH.name}")

    with DATA_PATH.open() as f:
        data = json.load(f)

    targets = [
        ("legislation", ENTRY_A),
        ("other_domestic", ENTRY_B),
        ("legislation", ENTRY_C),
    ]

    for cat, entry in targets:
        eid = entry.get("id") or entry.get("i")
        existing = data.get(cat, [])
        if any((e.get("id") or e.get("i")) == eid for e in existing):
            raise SystemExit(f"Entry {eid} already exists in {cat}. Aborting.")

    for cat, entry in targets:
        data.setdefault(cat, []).append(entry)
        eid = entry.get("id") or entry.get("i")
        print(f"Inserted {eid} into {cat}.")

    if "meta" in data and isinstance(data["meta"], dict):
        data["meta"]["lastUpdated"] = datetime.now().strftime("%Y-%m-%d")

    tmp = DATA_PATH.with_suffix(".json.tmp")
    with tmp.open("w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    tmp.replace(DATA_PATH)

    print("Done.")


if __name__ == "__main__":
    main()
