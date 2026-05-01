#!/usr/bin/env python3
"""Tier 2.5 audit follow-up: Tribal sovereignty wins (3) + RMP/EIS revisions (3).

Adds 6 new tracker entries surfaced from the BIA+BLM+DOI HIGH-priority
audit items not covered by the Tier 2 batch.

PROTECTIVE entries demonstrating tribal sovereignty wins (3):
- bia-tribal-self-governance-fy2027-deadline-2026: Tribal Self-Governance
  Program FY2027 participation deadline notice
- doi-southern-ute-tera-2026: Southern Ute Tribal Energy Resource
  Agreement
- ancsa-conveyances-2026: Aggregate of three ANCSA land conveyances
  (Ahtna, Doyon, Eklutna/Cook Inlet)

RMP/EIS individual entries (3):
- blm-or-wa-rmp-revision-2026: BLM Notice of Intent to Revise NW and
  Coastal Oregon plus SW Oregon RMPs (timber and old-growth)
- castle-mountain-mine-phase-ii-eis-2025: Castle Mountain Mine Phase II
  Expansion EIS, San Bernardino County, California
- ntec-west-antelope-coal-lease-eis-2025: NTEC West Antelope coal lease
  EIS in the Powder River Basin (Navajo Transitional Energy Company)
"""
import json
import shutil
from pathlib import Path
from datetime import datetime

DATA_PATH = Path(__file__).parent.parent / "data" / "data.json"
BACKUP_PATH = DATA_PATH.with_suffix(
    f".json.bak-{datetime.now().strftime('%Y%m%d-%H%M%S')}-pre-tier25-entries"
)


# ============================================================
# ENTRY 1: TRIBAL SELF-GOVERNANCE FY2027 DEADLINE
# ============================================================
ENTRY_TSG = {
    "i": "bia-tribal-self-governance-fy2027-deadline-2026",
    "t": "Federal Register Notice",
    "n": "BIA Notice 2026-04582: Notice of Deadline for Submitting Completed Requests To Begin Participation in the Tribal Self-Governance Program in Fiscal Year 2027 or Calendar Year 2027 (March 9, 2026)",
    "T": '<span style="color: #065F46;">BIA Tribal Self-Governance Program FY2027:</span> Federal Register Notice Establishes Deadline for Tribal Participation Requests; Implements Title IV of P.L. 93-638 Self-Determination Framework',
    "s": "Tribal Self-Governance FY2027 deadline",
    "d": "2026-03-09",
    "a": "Trump II",
    "A": ["DOI", "BIA"],
    "S": "Active. Federal Register publication on March 9, 2026 (Notice 2026-04582). The Bureau of Indian Affairs establishes the deadline for federally recognized Tribes to submit requests to begin participation in the Tribal Self-Governance Program in Fiscal Year 2027 or Calendar Year 2027 under Title IV of the Indian Self-Determination and Education Assistance Act (P.L. 93-638, as amended).",
    "L": "PROTECTIVE",
    "D": (
        "<b>FEDERAL ACTION.</b> On March 9, 2026, the Bureau of Indian Affairs published in the Federal Register Notice 2026-04582, establishing the deadline for federally recognized Tribes to submit completed requests to begin participation in the Tribal Self-Governance Program in Fiscal Year 2027 or Calendar Year 2027. The notice operates under Title IV of the Indian Self-Determination and Education Assistance Act (Public Law 93-638, codified at 25 U.S.C. 5361 et seq.).<br><br>"
        "<b>SELF-GOVERNANCE PROGRAM CONTEXT.</b> The Tribal Self-Governance Program is the principal federal-statutory mechanism through which federally recognized Tribes assume direct administration of programs, functions, services, and activities (PFSAs) historically operated by the Bureau of Indian Affairs and other federal agencies. Self-governance compacts and annual funding agreements transfer programmatic authority and the associated funds to participating Tribes, who exercise that authority through their own governmental institutions.<br><br>"
        "<b>SOVEREIGNTY DIMENSION.</b> Self-Governance Program participation is a tangible expression of tribal self-determination as articulated in UNDRIP Article 3 (the right of all peoples to self-determination) and the federal Indian-trust responsibility articulated in Cherokee Nation v. Georgia, 30 U.S. 1 (1831) and subsequent doctrine. Tribes choose which PFSAs to assume and at what scope. The federal role is non-substantive: BIA reviews compact and funding-agreement compliance with statute and regulation, but does not direct programmatic content.<br><br>"
        "<b>2026-2027 STAKES.</b> The FY2027 participation cycle proceeds during a federal-policy environment in which other Trump II actions have constrained tribal sovereignty (tracked at koi-nation-shiloh-trust-reversal-2026, anwr-coastal-plain-oil-gas-lease-2026, blm-plo-7966-dalton-corridor-2026, npra-2025-rod-2026, blm-chaco-withdrawal-revocation-2026). The continuation of the Self-Governance Program demonstrates the operating-by-default federal-trust framework even as parallel federal actions have produced harm. The number of Tribes participating in the program has grown over time; FY2027 participation requests will be reported in subsequent Federal Register notices.<br><br>"
        "<b>CULTURAL RESOURCE THREAT ASSESSMENT.</b> The threat level is PROTECTIVE. The Self-Governance Program is a foundational federal-statutory protection for tribal sovereignty across all four PPPT dimensions. Tribes assuming Self-Governance authority carry forward cultural-continuity practices, sacred-site stewardship, language and ceremonial-practice support, and tribal-historic-preservation work that cannot be matched by federal-agency operation."
        "<br><br>"
        "<b>SOURCES.</b><br>"
        "Primary source: Federal Register, BIA Notice 2026-04582, March 9, 2026. <a href=\"https://www.federalregister.gov/documents/2026/03/09/2026-04582\">https://www.federalregister.gov/documents/2026/03/09/2026-04582</a><br>"
        "Underlying authority: Indian Self-Determination and Education Assistance Act, Title IV (P.L. 93-638, as amended; 25 U.S.C. 5361 et seq.).<br>"
        "Related tracker entries: doi-southern-ute-tera-2026 (parallel tribal-sovereignty federal-action protective entry); ancsa-conveyances-2026 (parallel ANCSA implementation); v2026-indigenous-cultural-threat-analysis."
    ),
    "I": {
        "indigenous": {
            "people": "Federally recognized Tribes seeking Self-Governance Program participation in FY2027 are at the center of the action. Each participating Tribe assumes direct administrative authority over BIA-administered programs, redirecting decision-making authority from federal personnel to tribal personnel. Tribal governmental institutions, tribal employees, tribal-program beneficiaries, and tribal citizens directly benefit. As of recent reporting, approximately 350 federally recognized Tribes participate in some form of Self-Governance compacting, with the count expected to grow under the FY2027 cycle.",
            "places": "Self-Governance compacts cover programs, services, and activities at tribal lands, BIA agencies, and federal facilities serving tribal populations. Tribal cultural-resource sites, sacred sites, traditional-territory landscapes, and ceremonial places benefit from tribal Self-Governance authority over BIA programs that touch those places (cultural-resource management, NHPA Section 106 consultation, NAGPRA implementation, fire management, range management).",
            "practices": "Tribal cultural practices including language transmission, ceremonial-practice support, traditional-knowledge preservation, and tribal-historic-preservation-officer (THPO) work benefit when Tribes administer BIA programs directly. Tribal governmental practice is strengthened by the program's transfer of authority. The Self-Governance Program is itself a practice of federal-tribal government-to-government engagement under treaty-equivalent terms.",
            "treasures": "The Self-Governance Program institutional framework, accumulated through Title I (1975), Title III (1988), Title IV (1994), and Title V (2000) of P.L. 93-638, is itself a federal-statutory cultural-policy treasure that protects tribal sovereignty. Tribal-government records, tribal-historic-preservation databases, and tribal-cultural-resource inventories produced under Self-Governance compacts constitute cultural treasures whose stewardship remains with the Tribe rather than with federal agencies."
        }
    },
    "c": ["Indigenous", "All Communities"],
    "U": "https://www.federalregister.gov/documents/2026/03/09/2026-04582",
    "_source": "manual",
}


# ============================================================
# ENTRY 2: SOUTHERN UTE TERA
# ============================================================
ENTRY_TERA = {
    "i": "doi-southern-ute-tera-2026",
    "t": "Federal Register Notice",
    "n": "BIA Notice 2026-03309: Indian Energy Service Center; Receipt of Tribal Energy Resource Agreement for the Southern Ute Indian Tribe (February 19, 2026)",
    "T": '<span style="color: #065F46;">DOI/BIA Southern Ute Tribal Energy Resource Agreement:</span> Notice of TERA Approval Grants Southern Ute Indian Tribe Autonomous Authority Over Energy Development on Tribal Lands',
    "s": "Southern Ute TERA approval",
    "d": "2026-02-19",
    "a": "Trump II",
    "A": ["DOI", "BIA"],
    "S": "Active. Federal Register publication on February 19, 2026 (Notice 2026-03309). The Bureau of Indian Affairs Indian Energy Service Center receives and processes the Southern Ute Indian Tribe of the Southern Ute Reservation's Tribal Energy Resource Agreement (TERA) under the Indian Tribal Energy Development and Self-Determination Act of 2005 (25 U.S.C. 3501 et seq.). A TERA grants the participating Tribe autonomous authority to enter into energy-related leases, business agreements, and rights-of-way without further Secretarial approval.",
    "L": "PROTECTIVE",
    "D": (
        "<b>FEDERAL ACTION.</b> On February 19, 2026, the Bureau of Indian Affairs Indian Energy Service Center published in the Federal Register Notice 2026-03309, documenting receipt of the Southern Ute Indian Tribe of the Southern Ute Reservation's Tribal Energy Resource Agreement (TERA) under the Indian Tribal Energy Development and Self-Determination Act of 2005 (Public Law 109-58, Title V, codified at 25 U.S.C. 3501 et seq.).<br><br>"
        "<b>WHAT A TERA DOES.</b> A Tribal Energy Resource Agreement is a federal-statutory instrument that grants the participating Tribe autonomous authority to enter into energy-related leases, business agreements, and rights-of-way for energy development on tribal lands without further Secretarial approval for each transaction. The TERA shifts the federal role from per-transaction approval to a one-time review of the agreement's compliance framework. The participating Tribe assumes the federal-trust-responsibility role for individual transactions through its own tribal-government framework.<br><br>"
        "<b>SOUTHERN UTE CONTEXT.</b> The Southern Ute Indian Tribe is a federally recognized Tribe whose reservation is located in southwestern Colorado. The Tribe is a major energy producer with substantial natural-gas operations on tribal lands. The Tribe has built tribal-government institutional capacity over decades, including the Southern Ute Indian Tribe Department of Energy and the tribally owned Red Willow Production Company. The TERA approval is consistent with the Tribe's long-term self-governance trajectory.<br><br>"
        "<b>TERA RARITY.</b> Few Tribes have completed TERAs. The 2005 statutory framework requires substantial tribal-government institutional capacity, environmental-protection capacity, and consultation infrastructure. Tribes that complete TERAs are typically those with established energy-development programs and significant federal-Indian-policy expertise. The Southern Ute TERA strengthens the federal-statutory precedent that tribal sovereignty over energy development can operate at the level of full per-transaction federal-approval bypass.<br><br>"
        "<b>RELATIONSHIP TO BROADER PATTERN.</b> The Southern Ute TERA approval operates alongside, and in tension with, the broader 2025-2026 federal energy-pivot pattern (tracked at alaska-oil-gas-leasing-pivot-2025-2026, eo-14154, so-3418, eo-14300-nrc-reform-2025). TERAs are a tribal-sovereignty mechanism that operates within the energy-development framework but on tribal terms. Southern Ute energy development pursued under the TERA is governed by tribal-government decisions rather than by federal-agency permitting timelines.<br><br>"
        "<b>CULTURAL RESOURCE THREAT ASSESSMENT.</b> The threat level is PROTECTIVE. The TERA is a federal-statutory instrument that strengthens Southern Ute tribal sovereignty over energy development on tribal lands and demonstrates the operating force of the Indian Tribal Energy Development and Self-Determination Act framework."
        "<br><br>"
        "<b>SOURCES.</b><br>"
        "Primary source: Federal Register, BIA Notice 2026-03309, February 19, 2026. <a href=\"https://www.federalregister.gov/documents/2026/02/19/2026-03309\">https://www.federalregister.gov/documents/2026/02/19/2026-03309</a><br>"
        "Underlying authority: Indian Tribal Energy Development and Self-Determination Act of 2005 (Public Law 109-58, Title V; 25 U.S.C. 3501 et seq.).<br>"
        "Related tracker entries: bia-tribal-self-governance-fy2027-deadline-2026; ancsa-conveyances-2026; v2026-indigenous-cultural-threat-analysis."
    ),
    "I": {
        "indigenous": {
            "people": "The Southern Ute Indian Tribe and its approximately 1,500 enrolled members benefit from increased tribal-government authority over energy development on tribal lands. Tribal-government departments including the Southern Ute Department of Energy gain operating authority. Tribal employees in energy operations, environmental review, and regulatory compliance assume responsibilities previously shared with BIA personnel. The TERA framework demonstrates a pathway that other federally recognized Tribes with substantial energy resources may pursue, including the Navajo Nation, the Mandan, Hidatsa, and Arikara Nation, the Ute Mountain Ute Tribe, and other tribal governments.",
            "places": "Southern Ute Indian Reservation lands in southwestern Colorado are subject to TERA-governed energy development. The reservation occupies approximately 681,000 acres of trust and fee land. Cultural-resource sites including sacred places, archaeological resources, and traditional-territory landscapes benefit from tribal-government cultural-resource-management authority over energy-development decisions on those lands.",
            "practices": "Southern Ute cultural practices including the Sun Dance, Bear Dance, traditional-language transmission, and ceremonial uses of tribal lands operate within the cultural-resource-management framework that the TERA strengthens. Tribal-government administrative practice expands as the Tribe assumes per-transaction approval authority. Energy-development practice on tribal lands proceeds under tribal-government environmental-review and consultation frameworks.",
            "treasures": "The federal-statutory TERA framework is itself a cultural-policy treasure that protects tribal sovereignty. The Indian Tribal Energy Development and Self-Determination Act of 2005, accumulating from earlier self-determination instruments since 1975, demonstrates federal-Indian-policy that respects tribal sovereignty in operative terms. Southern Ute traditional cultural knowledge of tribal lands, energy resources, and environmental stewardship constitutes intangible cultural heritage."
        }
    },
    "c": ["Indigenous", "All Communities"],
    "U": "https://www.federalregister.gov/documents/2026/02/19/2026-03309",
    "_source": "manual",
}


# ============================================================
# ENTRY 3: ANCSA CONVEYANCES AGGREGATE
# ============================================================
ENTRY_ANCSA = {
    "i": "ancsa-conveyances-2026",
    "t": "Aggregate Analysis",
    "n": "Aggregate: BLM ANCSA Land Conveyances to Alaska Native Corporations, February-March 2026 (Ahtna, Eklutna/Cook Inlet, Doyon)",
    "T": '<span style="color: #065F46;">Aggregate Analysis:</span> BLM ANCSA Land Conveyances to Alaska Native Corporations, February-March 2026. Implementation of Foundational Alaska Native Land-Settlement Framework',
    "s": "ANCSA conveyances Feb-Mar 2026",
    "d": "2026-03-25",
    "a": "Trump II",
    "A": ["DOI", "BLM"],
    "S": "Active aggregate. Three Federal Register notices in February and March 2026 documenting BLM Alaska Native Claims Settlement Act land conveyances to Alaska Native regional and village corporations: Ahtna, Incorporated (March 25, Notice 2026-05823); Eklutna, Inc. and Cook Inlet Region, Inc. (February 26, Notice 2026-03804); Doyon, Limited (February 18, Notice 2026-03149).",
    "L": "PROTECTIVE",
    "D": (
        "<b>AGGREGATE PATTERN.</b> Between February 18 and March 25, 2026, the Bureau of Land Management published three Federal Register notices documenting Alaska Native Claims Settlement Act land conveyances to Alaska Native regional corporations and village corporations. The notices implement statutory obligations under the Alaska Native Claims Settlement Act of 1971 (43 U.S.C. 1601 et seq.).<br><br>"
        "<b>COMPONENT CONVEYANCES.</b><br>"
        "(1) <b>Ahtna conveyance (March 25, 2026; Federal Register 2026-05823).</b> BLM publishes notice of land conveyance to Ahtna, Incorporated, the Alaska Native regional corporation for the Copper River basin region of southeastern interior Alaska. Ahtna serves approximately 2,000 Ahtna Athabaskan shareholders.<br>"
        "(2) <b>Eklutna and Cook Inlet conveyance (February 26, 2026; Federal Register 2026-03804).</b> BLM publishes notice of surface and subsurface estate land conveyance to Eklutna, Inc. (the village corporation for Eklutna) and Cook Inlet Region, Inc. (CIRI, the regional corporation for the Cook Inlet area). Cook Inlet Region serves approximately 9,000 shareholders of Athabaskan, Yup'ik, Inupiat, Aleut, and Alutiiq descent.<br>"
        "(3) <b>Doyon conveyance (February 18, 2026; Federal Register 2026-03149).</b> BLM publishes notice of land conveyance to Doyon, Limited, the Alaska Native regional corporation for interior Alaska. Doyon is the largest private landowner in Alaska, with approximately 12.5 million acres of land entitlement. Doyon serves approximately 20,000 Athabaskan shareholders.<br><br>"
        "<b>ANCSA CONTEXT.</b> The Alaska Native Claims Settlement Act of 1971 (Public Law 92-203) settled aboriginal land claims in Alaska through the conveyance of approximately 44 million acres of land and a $962.5 million payment to twelve regional Alaska Native corporations and 200-plus village corporations. ANCSA was a foundational federal-Indigenous land-settlement framework, although it remains contested for substituting corporate land ownership for traditional sovereignty and for the conditions it imposed on Alaska Native cultural-continuity claims.<br><br>"
        "<b>2026 CONTINUITY.</b> The continuation of routine ANCSA conveyances during the 2025-2026 period demonstrates the operating-by-default federal-statutory framework even as other federal-Indigenous-policy actions during the same period have produced harm (tracked at koi-nation-shiloh-trust-reversal-2026, anwr-coastal-plain-oil-gas-lease-2026, blm-plo-7966-dalton-corridor-2026, npra-2025-rod-2026). ANCSA conveyances are PROTECTIVE because they transfer land, surface estate, and subsurface estate to Alaska Native corporations whose tribal-shareholder governance frameworks support cultural-continuity practice, traditional-territory stewardship, and intergenerational Alaska Native asset accumulation.<br><br>"
        "<b>CULTURAL RESOURCE THREAT ASSESSMENT.</b> The threat level is PROTECTIVE. ANCSA conveyances are foundational to Alaska Native cultural-continuity by securing the corporate land base that supports tribal-shareholder governance, subsistence practice, and cultural-resource stewardship across interior, coastal, and Arctic Alaska."
        "<br><br>"
        "<b>SOURCES.</b><br>"
        "Component federal sources: Federal Register, BLM Notice 2026-05823, March 25, 2026 (Ahtna). <a href=\"https://www.federalregister.gov/documents/2026/03/25/2026-05823\">https://www.federalregister.gov/documents/2026/03/25/2026-05823</a><br>"
        "Federal Register, BLM Notice 2026-03804, February 26, 2026 (Eklutna/Cook Inlet). <a href=\"https://www.federalregister.gov/documents/2026/02/26/2026-03804\">https://www.federalregister.gov/documents/2026/02/26/2026-03804</a><br>"
        "Federal Register, BLM Notice 2026-03149, February 18, 2026 (Doyon). <a href=\"https://www.federalregister.gov/documents/2026/02/18/2026-03149\">https://www.federalregister.gov/documents/2026/02/18/2026-03149</a><br>"
        "Underlying authority: Alaska Native Claims Settlement Act of 1971 (Public Law 92-203; 43 U.S.C. 1601 et seq.).<br>"
        "Related tracker entries: bia-tribal-self-governance-fy2027-deadline-2026; doi-southern-ute-tera-2026; alaska-oil-gas-leasing-pivot-2025-2026 (parallel-and-tension Alaska federal-action context)."
    ),
    "I": {
        "indigenous": {
            "people": "Ahtna Athabaskan shareholders (approximately 2,000), Eklutna village shareholders, Cook Inlet Region shareholders (approximately 9,000 of Athabaskan, Yup'ik, Inupiat, Aleut, and Alutiiq descent), and Doyon Athabaskan shareholders (approximately 20,000) benefit directly from the conveyances. Each corporation's tribal-shareholder governance framework supports cultural-continuity practice and intergenerational asset accumulation. Beyond the immediate corporations, the broader Alaska Native population benefits from the demonstrated operating force of the ANCSA framework during a period when federal Indigenous-policy harm patterns (tracked elsewhere) might otherwise undermine confidence in federal-statutory commitments.",
            "places": "Ahtna conveyances cover lands in the Copper River basin region of southeastern interior Alaska. Eklutna and Cook Inlet conveyances cover lands in the Cook Inlet basin and adjacent areas. Doyon conveyances cover lands in interior Alaska. The conveyed lands include cultural-resource sites, sacred places, traditional-territory landscapes, and ceremonial areas covered by ANCSA Section 14(h)(1) cemetery-and-historical-place selections and broader corporate-land entitlements.",
            "practices": "Subsistence practice (caribou and moose hunting, salmon fishing, plant gathering, traditional travel) on conveyed lands operates under corporate-shareholder governance frameworks that include tribal-government and Native-organization advisory structures. Cultural-resource-management practice on corporate lands proceeds under corporate-government cultural-resource policies. Heritage-language transmission and ceremonial practices benefit from secure land tenure.",
            "treasures": "ANCSA-conveyed lands constitute material cultural treasures of Alaska Native shareholders and broader Alaska Native communities. Cultural-resource sites within conveyed lands face protective tenure under corporate-shareholder governance. The ANCSA framework itself, while contested for its corporate-substitute-for-sovereignty design, is a federal-statutory cultural-policy treasure whose continued operation demonstrates federal commitment to Alaska Native land settlement."
        }
    },
    "c": ["Indigenous", "All Communities"],
    "U": "https://www.federalregister.gov/documents/2026/03/25/2026-05823",
    "_source": "manual",
    "_isAggregate": True,
}


# ============================================================
# ENTRY 4: BLM OR/WA RMP REVISION
# ============================================================
ENTRY_OR_WA_RMP = {
    "i": "blm-or-wa-rmp-revision-timber-2026",
    "t": "Federal Register Notice",
    "n": "BLM Notice 2026-03290: Notice of Intent To Revise Resource Management Plans for Northwestern and Coastal Oregon and Southwestern Oregon in Oregon/Washington (February 19, 2026)",
    "T": '<span style="color: #6B7280;">BLM Oregon/Washington RMP Revision:</span> Notice of Intent To Revise Resource Management Plans for Northwestern and Coastal Oregon and Southwestern Oregon; Affects Indigenous Treaty Rights and Old-Growth Forest Stewardship',
    "s": "BLM OR-WA RMP revision",
    "d": "2026-02-19",
    "a": "Trump II",
    "A": ["DOI", "BLM"],
    "S": "Active. Federal Register publication on February 19, 2026 (Notice 2026-03290). The Bureau of Land Management initiates revision of Resource Management Plans for Northwestern and Coastal Oregon and for Southwestern Oregon, plus a parallel BLM Oregon/Washington Forest Resource Management Plan amendment. The current RMPs were adopted in 2016 under the Western Oregon Resource Management Plan amendments. Revision is anticipated to increase timber harvest from BLM Oregon and Washington lands and to alter old-growth-forest reserve designations.",
    "L": "WATCH",
    "D": (
        "<b>FEDERAL ACTION.</b> On February 19, 2026, the Bureau of Land Management published in the Federal Register Notice 2026-03290, initiating the formal revision of three Resource Management Plans governing approximately 2.5 million acres of BLM-administered lands in western Oregon: the Northwestern and Coastal Oregon RMP, the Southwestern Oregon RMP, and an amendment to the BLM Oregon/Washington Forest Resource Management Plan.<br><br>"
        "<b>O AND C LANDS CONTEXT.</b> The lands subject to the RMP revisions include the Oregon and California Railroad Revested Lands (O and C Lands), which under the O and C Lands Act of 1937 (43 U.S.C. 2601 et seq.) are managed for sustained-yield timber production while balancing other uses. The 2016 Western Oregon RMP framework established Late Successional Reserves and other special designations to balance timber harvest with old-growth-forest conservation, threatened-species habitat (including the Northern Spotted Owl and Marbled Murrelet), and watershed protection.<br><br>"
        "<b>INDIGENOUS DIMENSIONS.</b> The lands subject to revision overlap with traditional territories and treaty-reserved rights of multiple federally recognized Tribes, including the Confederated Tribes of Grand Ronde, the Confederated Tribes of Siletz Indians, the Confederated Tribes of the Coos, Lower Umpqua and Siuslaw Indians, the Cow Creek Band of Umpqua Tribe of Indians, the Coquille Indian Tribe, the Klamath Tribes, and the Confederated Tribes of the Umatilla Indian Reservation. Tribal cultural-resource interests include sacred sites, ceremonial places, ancestral burial sites, traditional plant-gathering areas (camas, huckleberry, beargrass, cedar), traditional fishing and lamprey harvest sites, and old-growth-forest cultural practice.<br><br>"
        "<b>TIMBER-INDUSTRY DIMENSION.</b> The revision is anticipated to increase timber-harvest authorizations from BLM lands. Industry stakeholders have advocated for reduced Late Successional Reserve designations, expanded harvest blocks, and shorter rotation cycles. Conservation organizations have advocated against rollback of 2016 RMP protections, citing climate-mitigation values of old-growth-forest carbon sequestration and biodiversity conservation needs.<br><br>"
        "<b>CONSULTATION POSTURE.</b> The Notice of Intent commences NEPA scoping and federal-Indian consultation under NHPA Section 106 and Joint Secretary's Order 3403 on Trust Responsibility. The compressed federal-permitting environment under EO 14154 (Unleashing American Energy) and Secretary's Order 3418 may foreshorten consultation timelines.<br><br>"
        "<b>CULTURAL RESOURCE THREAT ASSESSMENT.</b> The threat level is WATCH. The RMP revisions are at the scoping stage; the final direction will depend on Draft Environmental Impact Statement and Record of Decision content. The audit will reclassify when the substantive content is published. The classification reflects the likely direction (increased timber harvest, reduced old-growth-forest reserves, foreshortened consultation) without prejudging the final decision."
        "<br><br>"
        "<b>SOURCES.</b><br>"
        "Primary source: Federal Register, BLM Notice 2026-03290, February 19, 2026. <a href=\"https://www.federalregister.gov/documents/2026/02/19/2026-03290\">https://www.federalregister.gov/documents/2026/02/19/2026-03290</a><br>"
        "Underlying authority: O and C Lands Act of 1937 (43 U.S.C. 2601 et seq.); FLPMA (43 U.S.C. 1701 et seq.); NEPA (42 U.S.C. 4321 et seq.); NHPA Section 106 (54 U.S.C. 306108).<br>"
        "Related tracker entries: alaska-oil-gas-leasing-pivot-2025-2026; blm-chaco-withdrawal-revocation-2026; eo-14154; so-3418; so-3403-co-stewardship."
    ),
    "I": {
        "indigenous": {
            "people": "Multiple federally recognized Tribes with traditional-territory and treaty-reserved-rights relationships to the affected lands face cumulative cultural-continuity pressure: the Confederated Tribes of Grand Ronde, the Confederated Tribes of Siletz Indians, the Confederated Tribes of the Coos, Lower Umpqua and Siuslaw Indians, the Cow Creek Band of Umpqua Tribe of Indians, the Coquille Indian Tribe, the Klamath Tribes, and the Confederated Tribes of the Umatilla Indian Reservation. Tribal members who depend on traditional plant gathering, fishing, hunting, and ceremonial uses of forested landscapes face direct impact.",
            "places": "Approximately 2.5 million acres of BLM Oregon lands face revised management. Sacred sites, ceremonial places, ancestral burial sites, traditional plant-gathering areas (camas, huckleberry, beargrass, cedar), traditional fishing and lamprey harvest sites, and old-growth-forest cultural-resource places are within the affected footprint. Cultural-landscape integrity depends on the protective designations the revision may alter.",
            "practices": "Indigenous traditional practices on the affected lands include first-foods gathering, lamprey harvest, salmon fishing on adjacent rivers, ceremonial use of old-growth forests, and intergenerational transmission of forest-and-river knowledge. Heritage-language traditions in Sahaptin, Salish, Penutian, and other language families preserve knowledge tied to the affected landscapes that cannot transmit absent the lived practice.",
            "treasures": "Old-growth-forest cultural sites, ceremonial places, and traditional-territory landscapes within the affected RMP areas constitute cultural treasures protected under NHPA Section 106 and the federal Indian-trust responsibility. Tribal traditional ecological knowledge of these landscapes, held by tribal elders, constitutes intangible cultural heritage."
        }
    },
    "c": ["Indigenous", "All Communities", "environmentalJustice"],
    "U": "https://www.federalregister.gov/documents/2026/02/19/2026-03290",
    "_source": "manual",
}


# ============================================================
# ENTRY 5: CASTLE MOUNTAIN MINE PHASE II
# ============================================================
ENTRY_CASTLE_MTN = {
    "i": "castle-mountain-mine-phase-ii-eis-2025",
    "t": "Federal Register Notice",
    "n": "BLM Notice 2025-19593: Notice of Intent To Prepare an Environmental Impact Statement for the Proposed Castle Mountain Mine Phase II Expansion, San Bernardino County, California (October 20, 2025)",
    "T": '<span style="color: #6B7280;">BLM Castle Mountain Mine Phase II Expansion EIS:</span> Notice of Intent To Prepare EIS for Mining Expansion in San Bernardino County, California; Indigenous Sacred-Site and Mojave Cultural-Landscape Implications',
    "s": "Castle Mountain Mine Phase II EIS",
    "d": "2025-10-20",
    "a": "Trump II",
    "A": ["DOI", "BLM"],
    "S": "Active. Federal Register publication on October 20, 2025 (Notice 2025-19593). The Bureau of Land Management initiates preparation of an Environmental Impact Statement for the proposed Castle Mountain Mine Phase II Expansion in San Bernardino County, California, near the boundary of Mojave National Preserve. The mine is operated by Equinox Gold's subsidiary Castle Mountain Venture; Phase II would expand existing operations on a property where mining has occurred since the 1990s.",
    "L": "WATCH",
    "D": (
        "<b>FEDERAL ACTION.</b> On October 20, 2025, the Bureau of Land Management published in the Federal Register Notice 2025-19593, initiating preparation of an Environmental Impact Statement for the proposed Castle Mountain Mine Phase II Expansion in San Bernardino County, California. The proposed expansion would extend gold mining operations on a property near the eastern boundary of Mojave National Preserve.<br><br>"
        "<b>SITE CONTEXT.</b> The Castle Mountain area is within the cultural-territory and traditional-use lands of multiple Indigenous nations, including the Mojave (Aha Macav), the Chemehuevi, the Fort Mojave Indian Tribe, the Colorado River Indian Tribes, and broader Mojave Desert tribal interests. The Mojave Desert landscape contains numerous Indigenous sacred sites, ceremonial places, ancestral burial sites, prehistoric trail networks, and culturally significant flora and fauna. Adjacent Mojave National Preserve protects approximately 1.6 million acres of related Mojave Desert ecosystem.<br><br>"
        "<b>INDIGENOUS CULTURAL-RESOURCE DIMENSIONS.</b> Mojave Desert cultural-resource places include the Mojave Trail (the prehistoric east-west trade route), Spirit Mountain (Avi Kwa Ame, sacred to the Mojave), and numerous archaeological sites documented through Section 110 NHPA surveys. The Castle Mountain expansion area requires Section 106 NHPA tribal consultation. The Mojave Desert is also home to multiple Threatened and Endangered Species under ESA, including the desert tortoise, whose continued protection depends on habitat-connectivity conservation.<br><br>"
        "<b>WATER AND ECOLOGICAL DIMENSIONS.</b> Mojave Desert mining operations consume significant water resources in an arid region with documented over-allocation of groundwater and surface water. The Castle Mountain expansion will require water-supply analysis under NEPA and California state water-rights frameworks. Water-resource stress affects Indigenous cultural-continuity practices including ceremonial uses of springs, traditional plant cultivation, and wildlife dependent on desert water sources.<br><br>"
        "<b>CONSULTATION POSTURE.</b> The Notice of Intent commences formal NEPA scoping and Section 106 NHPA tribal consultation. Consultation timelines are subject to the broader EO 14154 and SO 3418 federal-permitting environment.<br><br>"
        "<b>CULTURAL RESOURCE THREAT ASSESSMENT.</b> The threat level is WATCH. The EIS process is in its scoping phase. The final direction will depend on the Draft EIS, Section 106 consultation outcomes, and the Record of Decision. The classification reflects the project's potential cultural-resource impact while preserving the analytical posture pending substantive record development."
        "<br><br>"
        "<b>SOURCES.</b><br>"
        "Primary source: Federal Register, BLM Notice 2025-19593, October 20, 2025. <a href=\"https://www.federalregister.gov/documents/2025/10/20/2025-19593\">https://www.federalregister.gov/documents/2025/10/20/2025-19593</a><br>"
        "Underlying authority: NEPA (42 U.S.C. 4321 et seq.); NHPA Section 106 (54 U.S.C. 306108); FLPMA (43 U.S.C. 1701 et seq.); General Mining Act of 1872 (30 U.S.C. 22 et seq.).<br>"
        "Related tracker entries: blm-chaco-withdrawal-revocation-2026 (parallel Indigenous sacred-landscape mining-pressure entry); usgs-critical-minerals-list-2025 (federal critical-minerals framework driving mining acceleration); ntec-west-antelope-coal-lease-eis-2025 (parallel coal lease EIS)."
    ),
    "I": {
        "indigenous": {
            "people": "Mojave Desert Indigenous nations face direct cultural-continuity pressure from the Castle Mountain expansion: the Fort Mojave Indian Tribe, the Colorado River Indian Tribes (Mojave, Chemehuevi, Hopi, Navajo), the Chemehuevi Indian Tribe, the Twenty-Nine Palms Band of Mission Indians, and the broader Mojave Desert tribal community. Tribal cultural-affiliation interests in the expansion area include ancestral connections, ceremonial-practice sites, and traditional-resource use.",
            "places": "Castle Mountain area cultural-resource sites include archaeological sites documented through Section 110 NHPA surveys, the Mojave Trail prehistoric trade route, sacred sites within and adjacent to the proposed expansion footprint, and broader Mojave Desert cultural-landscape places. The proximity to Mojave National Preserve raises additional cultural-landscape integrity concerns. Spirit Mountain (Avi Kwa Ame), sacred to the Mojave, lies within the broader regional context though outside the immediate expansion footprint.",
            "practices": "Mojave Desert Indigenous practices including pilgrimage along traditional trail networks, ceremonial use of desert springs, traditional plant cultivation (mesquite, agave, screwbean), and intergenerational transmission of desert ecological knowledge depend on the cultural-landscape integrity of the broader region. Industrial mining expansion threatens these practices through habitat fragmentation and noise-and-light pollution at adjacent ceremonial sites.",
            "treasures": "Cultural-resource sites within the expansion area, including unsurveyed archaeological resources requiring Section 106 review, constitute cultural treasures protected under NHPA, NAGPRA, and the Archaeological Resources Protection Act. Mojave Desert traditional ecological knowledge constitutes intangible cultural heritage. Critical minerals and gold resources at the site, while economically significant, do not justify foreshortened cultural-resource review."
        }
    },
    "c": ["Indigenous", "Latiné", "All Communities", "environmentalJustice"],
    "U": "https://www.federalregister.gov/documents/2025/10/20/2025-19593",
    "_source": "manual",
}


# ============================================================
# ENTRY 6: NTEC WEST ANTELOPE COAL LEASE EIS
# ============================================================
ENTRY_NTEC = {
    "i": "ntec-west-antelope-coal-lease-eis-2025",
    "t": "Federal Register Notice",
    "n": "BLM Notice 2025-16096: Environmental Impact Statement for NTEC West Antelope Coal Lease Application Maximum Economic Recovery and Fair Market Value Determination, Powder River Basin, Wyoming (August 22, 2025)",
    "T": '<span style="color: #CA8A04;">BLM NTEC West Antelope Coal Lease EIS:</span> Powder River Basin Coal Lease Application by Navajo Transitional Energy Company; Cumulative Cultural-Resource Pressure Across Plains and Southwestern Indigenous Communities',
    "s": "NTEC West Antelope coal EIS",
    "d": "2025-08-22",
    "a": "Trump II",
    "A": ["DOI", "BLM"],
    "S": "Active. Federal Register publication on August 22, 2025 (Notice 2025-16096). The Bureau of Land Management publishes notice of an Environmental Impact Statement, public hearing, and request for comment on Maximum Economic Recovery and Fair Market Value determinations for the proposed NTEC West Antelope coal lease application in the Powder River Basin, Wyoming. The coal lease applicant is the Navajo Transitional Energy Company (NTEC), the wholly-owned energy company of the Navajo Nation.",
    "L": "HARMFUL",
    "D": (
        "<b>FEDERAL ACTION.</b> On August 22, 2025, the Bureau of Land Management published in the Federal Register Notice 2025-16096, opening public comment on the Environmental Impact Statement for the NTEC West Antelope coal lease application in the Powder River Basin, Wyoming. The notice covers Maximum Economic Recovery and Fair Market Value determinations under the Mineral Leasing Act of 1920 (30 U.S.C. 181 et seq.).<br><br>"
        "<b>NTEC AND NAVAJO NATION CONTEXT.</b> The Navajo Transitional Energy Company is the wholly-owned energy-development company of the Navajo Nation, established under Navajo Nation law. NTEC operates the Spring Creek Mine in Montana (also subject to a parallel Federal coal lease-by-application tracked separately) and pursues coal leases in the Powder River Basin to support the Navajo Nation's revenue base during the transition from the closed Navajo Generating Station and the Four Corners Power Plant. The Navajo Nation faces a complex sovereignty-and-energy-policy tension: maintaining tribal-revenue continuity from coal operations while addressing the documented public-health, sacred-site, and climate harms of coal extraction within and adjacent to the Navajo Nation Reservation.<br><br>"
        "<b>POWDER RIVER BASIN CONTEXT.</b> The Powder River Basin is the largest coal-producing region in the United States and supplies approximately 40 percent of U.S. coal production. The basin spans Wyoming and Montana and overlaps with traditional territories of the Northern Cheyenne, the Crow, and other Plains Indigenous nations. Cultural-resource sites within the basin include archaeological resources, ceremonial places, and traditional-territory landscapes. Air-quality, water-quality, and climate-impact concerns affect both Plains and downwind Southwestern Indigenous communities.<br><ml>"
        "<b>CULTURAL CONTINUITY HARM.</b> Coal-lease expansion in the Powder River Basin operates against multiple Indigenous cultural-continuity interests simultaneously: Northern Cheyenne and Crow traditional-territory protections in the basin; Navajo Nation traditional-territory protections in the Four Corners region affected by coal-power-plant emissions and water consumption; Hopi traditional-territory protections in the Black Mesa region affected by coal-mining and water-extraction history; and broader Plains and Southwestern Indigenous-community air-quality and climate concerns.<br><br>"
        "<b>SOVEREIGNTY DIMENSION.</b> NTEC's pursuit of the West Antelope coal lease is a tribal-sovereignty exercise of the Navajo Nation's authority over its energy-revenue base. The Navajo Nation Council and tribal members hold diverse views: continued coal-revenue dependency funds tribal-government operations and cultural-program support, but also perpetuates cultural-resource harm to other Indigenous nations and to Navajo communities downwind of coal-power emissions. The federal action is HARMFUL on the cumulative cultural-resource analysis but operates within a framework that respects Navajo Nation sovereignty.<br><br>"
        "<b>CULTURAL RESOURCE THREAT ASSESSMENT.</b> The threat level is HARMFUL. Coal-lease expansion in the Powder River Basin produces cumulative cultural-resource harm across Plains and Southwestern Indigenous communities. The Navajo Nation's sovereign decision to pursue the lease through NTEC is respected, but the federal-action assessment captures the cumulative cultural-resource impact regardless of the applicant's tribal-government status."
        "<br><br>"
        "<b>SOURCES.</b><br>"
        "Primary source: Federal Register, BLM Notice 2025-16096, August 22, 2025. <a href=\"https://www.federalregister.gov/documents/2025/08/22/2025-16096\">https://www.federalregister.gov/documents/2025/08/22/2025-16096</a><br>"
        "Underlying authority: Mineral Leasing Act of 1920 (30 U.S.C. 181 et seq.); NEPA (42 U.S.C. 4321 et seq.); NHPA Section 106 (54 U.S.C. 306108); Federal Coal Leasing Amendments Act of 1976.<br>"
        "Related tracker entries: coal-leasing-13m-acres (broader Powder River Basin coal-leasing pattern); usgs-critical-minerals-list-2025 (metallurgical-coal critical-minerals listing); castle-mountain-mine-phase-ii-eis-2025; alaska-oil-gas-leasing-pivot-2025-2026."
    ),
    "I": {
        "indigenous": {
            "people": "The Navajo Nation, through NTEC, is the lease applicant and would receive the revenue benefit. Navajo Nation Council members and Navajo citizens hold diverse views on continued coal-revenue dependency. Northern Cheyenne and Crow tribal members in the immediate Powder River Basin face direct cultural-continuity impact from expanded coal operations. Hopi tribal members face indirect cultural-continuity impact from cumulative coal-and-energy pressure on the broader Four Corners region. Plains and Southwestern Indigenous communities downwind of coal-power emissions face cumulative public-health pressure.",
            "places": "The Powder River Basin coal-lease tracts overlap with cultural-resource sites including ceremonial places, ancestral burial sites, archaeological resources, and traditional-territory landscapes of Northern Cheyenne and Crow significance. Navajo Nation lands and the broader Four Corners region face cumulative pressure from coal-power-plant emissions, despite the closure of Navajo Generating Station, due to ongoing operations elsewhere.",
            "practices": "Indigenous subsistence and ceremonial practices in the Powder River Basin (sacred-site visitation, traditional-plant gathering, hunting) face accelerated disruption from expanded coal operations. Navajo Nation cultural practices benefit from continued tribal-revenue support but face cumulative climate-and-health pressure from the energy-policy framework that sustains those revenues.",
            "treasures": "Cultural-resource sites within the West Antelope tract footprint, including unsurveyed archaeological resources and ceremonial places, face exposure under coal-lease development. Northern Cheyenne and Crow traditional ecological knowledge of the basin constitutes intangible cultural heritage. Navajo Nation institutional infrastructure built around coal-revenue, including tribal-government operations, language programs, and cultural institutions, faces complex tradeoffs between continued operation and cultural-resource protection."
        }
    },
    "c": ["Indigenous", "All Communities", "environmentalJustice"],
    "U": "https://www.federalregister.gov/documents/2025/08/22/2025-16096",
    "_source": "manual",
}


def main():
    if not DATA_PATH.exists():
        raise SystemExit(f"data.json not found at {DATA_PATH}")

    em_dash = "—"
    shutil.copy2(DATA_PATH, BACKUP_PATH)
    print(f"Backup written: {BACKUP_PATH.name}")

    with DATA_PATH.open() as f:
        data = json.load(f)

    new_entries = [
        ("agency_actions", ENTRY_TSG),
        ("agency_actions", ENTRY_TERA),
        ("agency_actions", ENTRY_ANCSA),
        ("agency_actions", ENTRY_OR_WA_RMP),
        ("agency_actions", ENTRY_CASTLE_MTN),
        ("agency_actions", ENTRY_NTEC),
    ]

    for cat, entry in new_entries:
        eid = entry.get('id') or entry.get('i')
        existing = data.get(cat, [])
        if any((e.get('id') or e.get('i')) == eid for e in existing):
            print(f"  SKIP: {eid} already exists")
            continue
        if em_dash in json.dumps(entry, ensure_ascii=False):
            raise SystemExit(f"ABORT: em-dash in {eid}")
        existing.append(entry)
        data[cat] = existing
        print(f"  ADD: {eid} ({entry['L']}) -> {cat}")

    if "meta" in data and isinstance(data["meta"], dict):
        data["meta"]["lastUpdated"] = datetime.now().strftime("%Y-%m-%d")

    tmp = DATA_PATH.with_suffix(".json.tmp")
    with tmp.open("w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    tmp.replace(DATA_PATH)

    print(f"\nDone. Total entries: {sum(len(data.get(k,[])) for k in ['executive_actions','agency_actions','legislation','litigation','other_domestic','international'])}")


if __name__ == "__main__":
    main()
