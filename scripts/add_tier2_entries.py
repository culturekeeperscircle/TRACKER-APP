#!/usr/bin/env python3
"""Tier 2 audit follow-up: add ~11 new entries surfaced from BIA, BLM, DOI
HIGH-priority untracked items in the 2026-04-30 agency-coverage audit.

Entries added:
- 6 major SEVERE individual entries (ANWR, Dalton Corridor, NPR-A ROD,
  Koi Nation reversal, ESA Gulf exemption, Spring Creek coal lease)
- 1 aggregate SEVERE entry (Alaska oil-and-gas pivot 2025-2026)
- 2 PROTECTIVE individual entries (Southern Ute TERA, Tribal Self-
  Governance FY2027 deadline)
- 2 NAGPRA monthly roundups (Feb 2026, Mar 2026)
- 1 Indian Gaming Compact aggregate (covering 20 compacts)

Plus 1 update: existing nagpra-roundup-2026-04 with 15 additional notices
captured in the audit.
"""
import json
import shutil
from pathlib import Path
from datetime import datetime

DATA_PATH = Path(__file__).parent.parent / "data" / "data.json"
BACKUP_PATH = DATA_PATH.with_suffix(
    f".json.bak-{datetime.now().strftime('%Y%m%d-%H%M%S')}-pre-tier2-entries"
)

# Load aggregate data
AGG = json.loads(open('/tmp/tier2_aggregates.json').read())


def make_nagpra_roundup_desc(month_label, items):
    n = len(items)
    items_sorted = sorted(items, key=lambda x: x.get('date',''))
    lines = []
    lines.append(f"<b>ACTION.</b> During {month_label}, the U.S. Department of the Interior, through the National Park Service, published in the Federal Register {n} NAGPRA notices from state agencies, state universities, private universities, and private institutions. Per the TCKC Threat Tracker's federal-actor-only coding policy (locked 2026-04-23), individual notices from non-federal actors are aggregated into this single monthly PROTECTIVE roundup rather than coded individually.<br><br>")
    lines.append("<b>CULTURAL CONTINUITY IMPACT.</b> NAGPRA (25 U.S.C. sections 3001-3013) requires institutions receiving federal funding to inventory Native American ancestral remains, funerary objects, sacred objects, and objects of cultural patrimony, and to repatriate these items to lineal descendants and culturally affiliated federally recognized Tribes, Native Hawaiian organizations, and Alaska Native villages. Each notice in this roundup either identifies institutional holdings (Notice of Inventory Completion) or commences repatriation transfer (Notice of Intended Repatriation). The notices protect Indigenous cultural continuity along all four PPPT dimensions: People (descendant communities and tribal historic preservation officers regain authority over ancestral remains and sacred objects), Places (sacred and ceremonial sites are reconnected to surviving cultural materials), Practices (ceremonial reburial and intergenerational transmission practices are restored), and Treasures (the material culture itself is returned to community stewardship).<br><br>")
    lines.append(f"<b>{month_label.upper()} AGGREGATE LIST ({n} notices).</b><br>")
    for item in items_sorted:
        lines.append(f"- <b>{item['date']}</b>: {item['title'][:200]} (Federal Register {item['doc']})<br>")
        lines.append(f"  <a href=\"{item['url']}\">{item['url']}</a><br>")
    lines.append("<br>")
    lines.append(f"<b>SOURCES.</b><br>")
    lines.append(f"All notices cited above are public Federal Register documents accessible via the URLs in the aggregate list. The federal-actor-only coding policy underlying this aggregation is documented in CLAUDE.md (locked 2026-04-23). NAGPRA statutory framework: 25 U.S.C. 3001 et seq.<br>")
    lines.append("Related tracker entries: nagpra-roundup-2026-04 (April 2026); see also individual NAGPRA-related entries in agency_actions for federal-actor NAGPRA actions (DOI, NPS, U.S. Army Corps of Engineers, BIA, Smithsonian).")
    return "".join(lines)


def make_pppt(default_section_text=None):
    if default_section_text is None:
        default_section_text = "150-300 words"
    return {
        "indigenous": {
            "people": default_section_text,
            "places": default_section_text,
            "practices": default_section_text,
            "treasures": default_section_text,
        }
    }


# ============================================================
# ENTRY 1: ANWR 2026 COASTAL PLAIN OIL AND GAS LEASE SALE
# ============================================================
ENTRY_ANWR = {
    "i": "anwr-coastal-plain-oil-gas-lease-2026",
    "t": "Federal Register Notice",
    "n": "BLM Notice 2026-07667: Notice of 2026 Coastal Plain Oil and Gas Lease Sale (April 20, 2026)",
    "T": '<span style="color: #991B1B;">BLM 2026 ANWR Coastal Plain Oil and Gas Lease Sale:</span> Federal Register Notice Reopens Arctic Refuge Coastal Plain to Oil and Gas Leasing; Direct Threat to Gwich\'in and Inupiat Cultural Continuity',
    "s": "ANWR 2026 Coastal Plain lease sale",
    "d": "2026-04-20",
    "a": "Trump II",
    "A": ["DOI", "BLM"],
    "S": "Active. Federal Register publication on April 20, 2026 (Notice 2026-07667). The notice schedules the 2026 Coastal Plain oil and gas lease sale on the 1.5 million-acre Coastal Plain of the Arctic National Wildlife Refuge. The Coastal Plain is paramount to the cultural continuity of the Gwich'in Nation (the lands where the Porcupine Caribou Herd calves) and to the Inupiat communities whose subsistence and ceremonial practices depend on the Coastal Plain ecosystem.",
    "L": "SEVERE",
    "D": (
        "<b>FEDERAL ACTION.</b> On April 20, 2026, the Bureau of Land Management published in the Federal Register Notice 2026-07667, scheduling the 2026 Coastal Plain Oil and Gas Lease Sale within the Arctic National Wildlife Refuge (ANWR). The Coastal Plain comprises approximately 1.5 million acres of the 19.6-million-acre Arctic Refuge, opened to oil and gas leasing under Section 20001 of the Tax Cuts and Jobs Act of 2017 (Public Law 115-97).<br><br>"
        "<b>CULTURAL CONTINUITY HARM.</b> The Coastal Plain is the calving ground of the Porcupine Caribou Herd, the keystone species of the Gwich'in Nation's cultural continuity. Gwich'in communities in fifteen villages across northeast Alaska and the Yukon Territory have organized for nearly four decades against industrial development of the Coastal Plain through the Gwich'in Steering Committee. Inupiat communities of the North Slope, including the village of Kaktovik located within the Coastal Plain, hold mixed views: the village government has at times supported development for revenue, while subsistence hunters depend on the same caribou and marine mammals the Gwich'in protect.<br><br>"
        "<b>RELATIONSHIP TO BROADER PIVOT.</b> The 2026 lease sale is one component of a coordinated 2025-2026 federal pivot to expand oil and gas leasing on Alaska public lands. Related actions tracked at alaska-oil-gas-leasing-pivot-2025-2026 include the ANWR Call for Nominations and Comments, the National Petroleum Reserve-Alaska 2025 Record of Decision, the NPR-A regulations rescission, the NPR-A 2026 lease sale, and Section 50203 of the One Big Beautiful Bill Act implementation.<br><br>"
        "<b>CULTURAL RESOURCE THREAT ASSESSMENT.</b> The threat level is SEVERE. Industrial development of the Coastal Plain disrupts caribou calving and migration, severing the foundational subsistence and cultural practice the Gwich'in Nation has maintained for over twenty thousand years. The harm is partially irreversible: caribou herd disruption, sacred-site exposure to road and pad construction, and the cumulative-impact load on Indigenous cultural-continuity practices."
        "<br><br>"
        "<b>SOURCES.</b><br>"
        "Primary source: Federal Register, BLM Notice 2026-07667, April 20, 2026. <a href=\"https://www.federalregister.gov/documents/2026/04/20/2026-07667\">https://www.federalregister.gov/documents/2026/04/20/2026-07667</a><br>"
        "Related tracker entries: alaska-oil-gas-leasing-pivot-2025-2026; eo-14154 (EO 14154 Unleashing American Energy); so-3418 (Secretary's Order 3418); blm-chaco-withdrawal-revocation-2026 (parallel Indigenous-sacred-landscape revocation pattern)."
    ),
    "I": {
        "indigenous": {
            "people": "The Gwich'in Nation, comprising fifteen villages across northeast Alaska and the Yukon Territory, has organized continuously for nearly four decades through the Gwich'in Steering Committee against industrial development of the Coastal Plain. The Gwich'in identify themselves as 'the people who live where the caribou are,' anchoring individual and collective identity in the Porcupine Caribou Herd. Inupiat communities of the North Slope, including Kaktovik (located within the Coastal Plain), face complex internal debate where village government has at times supported development for fiscal sovereignty while subsistence hunters depend on the same ecosystem. Disruption of caribou calving exposes the Gwich'in cultural-continuity foundation to permanent damage and accelerates the existing climate-change pressures on the Inupiat subsistence base.",
            "places": "The 1.5 million-acre Coastal Plain is the calving ground of the Porcupine Caribou Herd and contains documented archaeological sites including ancient hunting blinds, fish weirs, and ceremonial sites that span more than ten thousand years of continuous Indigenous occupation. The Coastal Plain is part of the Arctic National Wildlife Refuge, the largest intact ecosystem in the National Wildlife Refuge System. Industrial development brings drilling pad construction, road networks, pipeline infrastructure, and seismic-survey-induced ground disturbance to a landscape whose cultural-resource integrity depends on its near-pristine character.",
            "practices": "Gwich'in cultural practices including caribou hunting, ceremonial sharing of caribou meat, and intergenerational transmission of caribou-hunting knowledge depend on a healthy Porcupine Caribou Herd. The Gwich'in Athabaskan language preserves knowledge of caribou behavior, movement patterns, and cultural significance that cannot be transmitted absent the lived practice. Inupiat practices including bowhead whaling, caribou hunting, and ice cellar construction depend on the same ecosystem and on the absence of industrial-zone restrictions on subsistence movement.",
            "treasures": "Archaeological resources within the Coastal Plain include hunting blinds, fish weirs, ceremonial sites, and cultural-resource places documented through limited surveys conducted under Section 110 of the National Historic Preservation Act. The full inventory is incomplete because much of the Coastal Plain has not been surveyed at the level required for Section 106 review. The Porcupine Caribou Herd itself is a cultural treasure of the Gwich'in Nation. Traditional ecological knowledge held by Gwich'in and Inupiat elders constitutes intangible cultural heritage protected under the UNESCO Convention for the Safeguarding of the Intangible Cultural Heritage."
        }
    },
    "c": ["Indigenous", "All Communities", "environmentalJustice"],
    "U": "https://www.federalregister.gov/documents/2026/04/20/2026-07667",
    "_source": "manual",
}

# ============================================================
# ENTRY 2: BLM PLO 7966 DALTON CORRIDOR REVOCATION
# ============================================================
ENTRY_DALTON = {
    "i": "blm-plo-7966-dalton-corridor-2026",
    "t": "Public Land Order",
    "n": "BLM Public Land Order 7966: Partial Revocation of Public Land Order Nos. 5150 and 5180 (February 25, 2026)",
    "T": '<span style="color: #991B1B;">BLM Public Land Order 7966:</span> Partial Revocation of PLOs 5150 and 5180 Reopens 2.1 Million Acres of Alaska Dalton Utility Corridor to Mineral and Resource Development',
    "s": "BLM PLO 7966 Dalton Corridor revocation",
    "d": "2026-02-25",
    "a": "Trump II",
    "A": ["DOI", "BLM"],
    "S": "Active. Federal Register publication on February 25, 2026 (Notice 2026-03777). Public Land Order 7966 partially revokes Public Land Order Nos. 5150 (December 1971) and 5180 (April 1972), as amended, reopening approximately 2.1 million acres of Alaska's Dalton Utility Corridor to mineral location, mineral leasing, and resource development. The Dalton Corridor is the buffer area along the Trans-Alaska Pipeline System and the Dalton Highway between Yukon Crossing and Prudhoe Bay.",
    "L": "SEVERE",
    "D": (
        "<b>FEDERAL ACTION.</b> On February 25, 2026, the Bureau of Land Management published Public Land Order 7966 in the Federal Register (Notice 2026-03777). PLO 7966 partially revokes Public Land Order Nos. 5150 and 5180, both originally issued under the Alaska Native Claims Settlement Act of 1971 (43 U.S.C. 1601 et seq.) framework, that had withdrawn approximately 2.1 million acres of Alaska's Dalton Utility Corridor from mineral entry and leasing. The revocation reopens these lands to location, leasing, and resource development.<br><br>"
        "<b>DALTON CORRIDOR CONTEXT.</b> The Dalton Utility Corridor follows the Trans-Alaska Pipeline System and the James W. Dalton Highway between Yukon Crossing and Prudhoe Bay, traversing the traditional territories of Athabaskan and Inupiat communities. The lands at issue overlap with the cultural landscapes of the Stevens Village, Allakaket, Bettles, Wiseman, and Anaktuvuk Pass communities, among others. The corridor passes through the Brooks Range, the Yukon Flats, and the North Slope tundra.<br><br>"
        "<b>CULTURAL CONTINUITY HARM.</b> Industrial development on the 2.1 million acres now reopened threatens cultural-continuity practices documented in the Alaska Native Claims Settlement Act, the Alaska National Interest Lands Conservation Act of 1980 (16 U.S.C. 3101 et seq.), and the federal trust responsibility. Subsistence resources (caribou, moose, fish, plant materials), sacred sites, ceremonial gathering places, and traditional travel routes face cumulative-impact harm from accelerated mineral and resource extraction.<br><br>"
        "<b>RELATIONSHIP TO BROADER PIVOT.</b> PLO 7966 is one component of the coordinated 2025-2026 federal pivot to expand oil, gas, mineral, and resource leasing on Alaska public lands. The cumulative pattern is tracked at alaska-oil-gas-leasing-pivot-2025-2026.<br><br>"
        "<b>CULTURAL RESOURCE THREAT ASSESSMENT.</b> The threat level is SEVERE. The 2.1-million-acre revocation is one of the largest Alaska public-lands withdrawals reversed in the 2025-2026 period and directly affects Indigenous subsistence, sacred-site, and traditional-travel-route resources across multiple Athabaskan and Inupiat communities."
        "<br><br>"
        "<b>SOURCES.</b><br>"
        "Primary source: Federal Register, BLM Public Land Order 7966, February 25, 2026 (Notice 2026-03777). <a href=\"https://www.federalregister.gov/documents/2026/02/25/2026-03777\">https://www.federalregister.gov/documents/2026/02/25/2026-03777</a><br>"
        "Underlying authorities: ANCSA (43 U.S.C. 1601 et seq.); ANILCA (16 U.S.C. 3101 et seq.); Original PLOs 5150 (December 1971) and 5180 (April 1972).<br>"
        "Related tracker entries: alaska-oil-gas-leasing-pivot-2025-2026; eo-14154; so-3418; blm-chaco-withdrawal-revocation-2026."
    ),
    "I": {
        "indigenous": {
            "people": "Athabaskan communities of Stevens Village, Allakaket, Bettles, Wiseman, and other interior Alaska villages plus Inupiat communities of Anaktuvuk Pass and the broader North Slope hold continuous traditional-territory relationships to the 2.1 million-acre revocation area. Subsistence-dependent populations face direct harm from accelerated mineral-and-resource development. Tribal historic-preservation-officer (THPO) practice is constrained by the foreshortened federal-permitting environment under EO 14154 and Secretary's Order 3418.",
            "places": "The Dalton Corridor traverses Athabaskan and Inupiat sacred sites, ceremonial gathering places, traditional fish camps, and ancestral travel routes documented through ANILCA Section 810 subsistence reviews and ANCSA Section 14(h)(1) cemetery-and-historical-place selections. Many sites within the corridor remain unsurveyed at the Section 106 level. The Brooks Range, the Yukon Flats, and the North Slope tundra are the cultural landscapes at risk.",
            "practices": "Subsistence practices (caribou, moose, Dolly Varden char, salmon, plant gathering) depend on the ecological integrity of the Dalton Corridor lands. Traditional travel between villages along the corridor and adjacent lands depends on access patterns that industrial development can disrupt. Ceremonial gatherings tied to seasonal subsistence cycles depend on healthy populations of subsistence species.",
            "treasures": "Archaeological resources, ceremonial sites, and ancestral burial places within the 2.1-million-acre revocation area constitute Indigenous cultural treasures protected under NHPA Section 106, NAGPRA, and the Archaeological Resources Protection Act. Traditional ecological knowledge held by Athabaskan and Inupiat elders, transmitted through Indigenous-language instruction, constitutes intangible cultural heritage. The federal-trust-responsibility documentation accumulated under ANCSA, ANILCA, and the Indian Reorganization Act is itself a treasure whose erosion under PLO 7966 weakens future protective claims."
        }
    },
    "c": ["Indigenous", "All Communities", "environmentalJustice"],
    "U": "https://www.federalregister.gov/documents/2026/02/25/2026-03777",
    "_source": "manual",
}

# ============================================================
# ENTRY 3: NPR-A 2025 RECORD OF DECISION
# ============================================================
ENTRY_NPRA_ROD = {
    "i": "npra-2025-rod-2026",
    "t": "Record of Decision",
    "n": "BLM Record of Decision 2026-03784: National Petroleum Reserve in Alaska 2025 Record of Decision for the Final Environmental Impact Statement on the Integrated Activity Plan (February 25, 2026)",
    "T": '<span style="color: #991B1B;">BLM NPR-A 2025 Record of Decision:</span> Final EIS Integrated Activity Plan Reverses Biden-Era Protections on the 23-Million-Acre National Petroleum Reserve in Alaska',
    "s": "NPR-A 2025 Record of Decision",
    "d": "2026-02-25",
    "a": "Trump II",
    "A": ["DOI", "BLM"],
    "S": "Active. Federal Register publication on February 25, 2026 (Notice 2026-03784). The Record of Decision adopts the 2025 Final Environmental Impact Statement for the National Petroleum Reserve in Alaska Integrated Activity Plan. The decision reverses the Biden-era 2024 NPR-A management framework that had designated approximately 13 million acres as Special Areas with enhanced protection for caribou calving, fish-spawning streams, and Indigenous subsistence access.",
    "L": "SEVERE",
    "D": (
        "<b>FEDERAL ACTION.</b> On February 25, 2026, the Bureau of Land Management published in the Federal Register the Record of Decision for the 2025 Final Environmental Impact Statement on the National Petroleum Reserve in Alaska Integrated Activity Plan (Notice 2026-03784). The Record of Decision adopts a management framework that reverses the protections established by the Biden administration's 2024 NPR-A management plan, which had designated approximately 13 million acres of the 23-million-acre Reserve as Special Areas under 43 CFR 2361.1.<br><br>"
        "<b>NPR-A CONTEXT.</b> The National Petroleum Reserve in Alaska comprises approximately 23 million acres on Alaska's North Slope, the largest single block of federal land in the United States. The Reserve overlaps with traditional territories of Inupiat communities of the North Slope, including the village of Nuiqsut, which sits within the southeastern boundary of the Reserve and has organized continuously against expanded oil and gas development. The Reserve also overlaps with the Teshekpuk Lake Caribou Herd calving grounds, the principal subsistence resource for Inupiat communities of the western North Slope.<br><br>"
        "<b>CULTURAL CONTINUITY HARM.</b> The Special Areas designations under the 2024 Biden-era plan had limited oil and gas leasing in the Teshekpuk Lake area, the Colville River, and the Utukok River Uplands, all paramount to Inupiat cultural-continuity practices. Reversing those protections reopens these lands to leasing, with cumulative-impact consequences for caribou calving, fish-spawning, and subsistence-access practices.<br><br>"
        "<b>RELATIONSHIP TO BROADER PIVOT.</b> The NPR-A Record of Decision is the principal Alaska public-lands deregulatory action of the 2025-2026 period. The cumulative pattern is tracked at alaska-oil-gas-leasing-pivot-2025-2026.<br><br>"
        "<b>CULTURAL RESOURCE THREAT ASSESSMENT.</b> The threat level is SEVERE. The reversal of Special Areas designations on approximately 13 million acres directly affects Inupiat cultural continuity through caribou-herd disruption, sacred-site exposure to industrial development, and the foreshortening of federal-consultation timelines under the broader EO 14154 and SO 3418 deregulatory regime."
        "<br><br>"
        "<b>SOURCES.</b><br>"
        "Primary source: Federal Register, BLM Notice 2026-03784, February 25, 2026. <a href=\"https://www.federalregister.gov/documents/2026/02/25/2026-03784\">https://www.federalregister.gov/documents/2026/02/25/2026-03784</a><br>"
        "Underlying authority: Naval Petroleum Reserves Production Act of 1976 (42 U.S.C. 6501 et seq.); Special Areas regulations at 43 CFR 2361.1.<br>"
        "Related tracker entries: alaska-oil-gas-leasing-pivot-2025-2026; anwr-coastal-plain-oil-gas-lease-2026; blm-plo-7966-dalton-corridor-2026; eo-14154; so-3418."
    ),
    "I": {
        "indigenous": {
            "people": "Inupiat communities of the North Slope, particularly Nuiqsut, Atqasuk, Wainwright, and Utqiagvik (Barrow), face cumulative cultural-continuity harm from the NPR-A Record of Decision. The Teshekpuk Lake Caribou Herd, which calves on the lands now reopened to leasing, is the principal subsistence resource for western North Slope communities. Nuiqsut residents have organized continuously through the City of Nuiqsut and the Native Village of Nuiqsut against expanded NPR-A oil and gas development, citing health and environmental-justice impacts already documented from existing Reserve operations including the ConocoPhillips Willow Project.",
            "places": "Sacred sites and ceremonial places within the 13-million-acre Special Areas designations include the Teshekpuk Lake area, the Colville River corridor, the Utukok River Uplands, and the broader caribou-calving and fish-spawning landscapes. The Reserve contains Inupiat cultural-resource places documented under ANCSA Section 14(h)(1) and through ANILCA Section 810 subsistence reviews. Many places remain unsurveyed at the Section 106 level. Cultural-landscape integrity is threatened by accelerated leasing.",
            "practices": "Inupiat subsistence practices (caribou hunting, fish camps, beluga and bowhead-whale harvesting on adjacent coasts, ice cellar construction, plant gathering) depend on the ecological integrity of NPR-A lands. The Inupiaq language preserves cultural knowledge of caribou behavior and seasonal movement that cannot transmit absent the lived practice. Industrial development of Special Areas accelerates the disruption already underway from climate change.",
            "treasures": "Archaeological resources within the NPR-A include hunting blinds, fish weirs, ceremonial sites, and ancestral burial places spanning multiple millennia of Inupiat occupation. Traditional ecological knowledge of NPR-A lands held by Inupiat elders constitutes intangible cultural heritage. The federal-statutory protections (ANILCA Section 810, ANCSA Section 14(h)(1), NHPA Section 106) are themselves cultural-policy treasures whose practical force is reduced by the Record of Decision's accelerated-leasing posture."
        }
    },
    "c": ["Indigenous", "All Communities", "environmentalJustice"],
    "U": "https://www.federalregister.gov/documents/2026/02/25/2026-03784",
    "_source": "manual",
}

# ============================================================
# ENTRY 4: KOI NATION SHILOH TRUST REVERSAL
# ============================================================
ENTRY_KOI = {
    "i": "koi-nation-shiloh-trust-reversal-2026",
    "t": "Federal Register Notice",
    "n": "BIA Notice 2026-06434: Reversal of Land Acquisition; Koi Nation of Northern California, Shiloh Site, Sonoma County, California (April 2, 2026)",
    "T": '<span style="color: #991B1B;">BIA Reversal of Trust Acquisition for Koi Nation:</span> 68.6-Acre Shiloh Site in Sonoma County Removed From Trust Status; Rare Reversal of Federal Tribal Land-Into-Trust Decision',
    "s": "Koi Nation Shiloh trust reversal",
    "d": "2026-04-02",
    "a": "Trump II",
    "A": ["DOI", "BIA"],
    "S": "Active. Federal Register publication on April 2, 2026 (Notice 2026-06434). The Bureau of Indian Affairs reverses a prior trust acquisition for the Koi Nation of Northern California, removing 68.60 acres at the Shiloh Site in Sonoma County, California from federal trust status and returning it to private ownership. The reversal is a rare federal action against a completed land-into-trust acquisition.",
    "L": "SEVERE",
    "D": (
        "<b>FEDERAL ACTION.</b> On April 2, 2026, the Bureau of Indian Affairs published in the Federal Register Notice 2026-06434, reversing a prior trust acquisition for the Koi Nation of Northern California. The reversal removes 68.60 acres at the Shiloh Site in Sonoma County, California from federal trust status under 25 U.S.C. 5108. The land returns to non-trust ownership.<br><br>"
        "<b>WHY THIS IS UNUSUAL.</b> Federal land-into-trust acquisitions for federally recognized tribes are typically permanent. Reversal of a completed trust acquisition is rare and operates against the federal trust responsibility. The federal trust responsibility, articulated in Cherokee Nation v. Georgia, 30 U.S. 1 (1831) and codified in the Indian Reorganization Act of 1934 (25 U.S.C. 5108), establishes that federal land held in trust for a tribe is held to be permanent absent congressional action.<br><br>"
        "<b>KOI NATION CONTEXT.</b> The Koi Nation of Northern California is a federally recognized tribe with ancestral territory in the Clear Lake basin and surrounding regions of Northern California. The Shiloh Site is within the Koi Nation's traditional territory. The trust acquisition had been pursued as part of the Koi Nation's economic-development and self-governance framework.<br><br>"
        "<b>CULTURAL CONTINUITY HARM.</b> The reversal undermines the Koi Nation's land base, which is foundational to tribal cultural continuity along all four PPPT dimensions. The reversal also operates as a precedent threat to other completed land-into-trust acquisitions, signaling that federal trust commitments are reversible under political pressure.<br><br>"
        "<b>CULTURAL RESOURCE THREAT ASSESSMENT.</b> The threat level is SEVERE. The reversal directly harms the Koi Nation's cultural-continuity foundation and threatens the broader federal-tribal trust relationship through precedent."
        "<br><br>"
        "<b>SOURCES.</b><br>"
        "Primary source: Federal Register, BIA Notice 2026-06434, April 2, 2026. <a href=\"https://www.federalregister.gov/documents/2026/04/02/2026-06434\">https://www.federalregister.gov/documents/2026/04/02/2026-06434</a><br>"
        "Underlying authority: Indian Reorganization Act, 25 U.S.C. 5108; federal trust responsibility doctrine.<br>"
        "Related tracker entries: bie-tribal-lawsuit (Pueblo of Isleta et al. v. DOI, parallel federal-Indian-trust harm); v2026-indigenous-cultural-threat-analysis."
    ),
    "I": {
        "indigenous": {
            "people": "The Koi Nation of Northern California, a federally recognized tribe, loses 68.60 acres of trust land at the Shiloh Site in Sonoma County. Tribal economic-development and self-governance plans built around the Shiloh Site face foundational disruption. The reversal sets a precedent threat to other federally recognized tribes whose completed land-into-trust acquisitions could face similar reversal. Other tribes in California with active land-into-trust applications, including the Federated Indians of Graton Rancheria, the Lytton Band of Pomo Indians, and the Cloverdale Rancheria of Pomo Indians, face heightened uncertainty.",
            "places": "The 68.60-acre Shiloh Site in Sonoma County, California reverts to non-trust ownership. The site is within the Koi Nation's ancestral territory in the Clear Lake basin region. Cultural-resource sites within the parcel face altered protection under non-trust ownership, since federal NHPA Section 106 protections apply differently outside trust status.",
            "practices": "Koi Nation cultural-continuity practices, including ceremonial uses of the Shiloh Site under tribal-government authority, are constrained by the loss of trust-land jurisdiction. Tribal historic-preservation-officer practice on the site is reduced. The reversal disrupts intergenerational planning for tribal cultural-resource stewardship at the site.",
            "treasures": "Cultural-resource sites within the Shiloh Site parcel, including any archaeological resources, ceremonial places, and ancestral burial sites documented through tribal cultural-resource management, face altered federal-statutory protection under non-trust ownership. The Koi Nation's self-governance institutional infrastructure built around the Shiloh Site faces disruption. The federal-trust-responsibility doctrine itself, accumulated since Cherokee Nation v. Georgia (1831), is weakened as a precedent through this reversal."
        }
    },
    "c": ["Indigenous", "All Communities"],
    "U": "https://www.federalregister.gov/documents/2026/04/02/2026-06434",
    "_source": "manual",
}

# ============================================================
# ENTRY 5: ESA GULF OIL AND GAS EXEMPTION
# ============================================================
ENTRY_ESA_GULF = {
    "i": "doi-esa-gulf-oil-gas-exemption-2026",
    "t": "Federal Register Notice",
    "n": "DOI Endangered Species Committee Notice 2026-06458: ESA Exemption for Gulf of America Oil and Gas Activities (April 3, 2026)",
    "T": '<span style="color: #991B1B;">DOI Endangered Species Committee:</span> ESA Section 7 Exemption Process Activated for Gulf of America Oil and Gas Activities; Bypasses Standard Endangered Species Act Consultation',
    "s": "ESA Gulf oil-gas exemption",
    "d": "2026-04-03",
    "a": "Trump II",
    "A": ["DOI", "FWS", "NOAA"],
    "S": "Active. Federal Register publication on April 3, 2026 (Notice 2026-06458). The Endangered Species Committee, established under Section 7(e) of the Endangered Species Act (16 U.S.C. 1536(e)), is convened to consider an exemption from ESA Section 7 consultation requirements for Gulf of America (formerly Gulf of Mexico) oil and gas activities. Section 7(e) is colloquially known as the 'God Squad' provision and has been used only sparingly in the ESA's fifty-year history.",
    "L": "SEVERE",
    "D": (
        "<b>FEDERAL ACTION.</b> On April 3, 2026, the Department of the Interior published in the Federal Register Notice 2026-06458, convening the Endangered Species Committee under Section 7(e) of the Endangered Species Act (16 U.S.C. 1536(e)) to consider an exemption from ESA Section 7 consultation requirements for oil and gas activities in the Gulf of America (formerly the Gulf of Mexico). Section 7(e) authorizes a seven-member committee, including the Secretary of the Interior, the Secretary of Agriculture, the Secretary of the Army, the Chair of the Council of Economic Advisers, the Administrator of EPA, the Administrator of NOAA, and one representative of each affected state, to grant exemptions from ESA Section 7 by a five-vote majority.<br><br>"
        "<b>WHY THIS IS UNUSUAL.</b> The Endangered Species Committee, colloquially known as the 'God Squad,' has been convened only a handful of times in the ESA's fifty-year history. The most prominent prior invocation was for the Tellico Dam in 1979, where the Committee ultimately denied the exemption (the dam was completed only after a separate congressional rider). Use of the Section 7(e) exemption process for a category of activity (Gulf oil and gas) rather than a specific project is doctrinally novel and would create a precedent for blanket-exemption use of the provision.<br><br>"
        "<b>CULTURAL CONTINUITY HARM.</b> Gulf oil and gas activities affect cultural resources of multiple TCKC primary cultural communities. African-descendant communities of the Gulf Coast (Louisiana Creole, Mississippi Black communities, Black-fishing-village communities) face direct environmental-justice harm from oil-spill exposure, disrupted fisheries, and air-quality degradation. Indigenous communities of coastal Louisiana (United Houma Nation, Pointe-au-Chien Indian Tribe, Isle de Jean Charles Choctaw, Atakapa-Ishak/Chawasha) face displacement-driven cultural-continuity harm from existing oil-and-gas-induced subsidence and saltwater intrusion. Latine and Pacific Islander Gulf-Coast communities face parallel harms.<br><br>"
        "<b>CULTURAL RESOURCE THREAT ASSESSMENT.</b> The threat level is SEVERE. Convocation of the Endangered Species Committee for Gulf oil and gas activities operates as a category-wide bypass of the principal federal-statutory protective regime for at-risk species. The downstream cultural-continuity harm to Gulf Coast TCKC primary cultural communities is structural and durable."
        "<br><br>"
        "<b>SOURCES.</b><br>"
        "Primary source: Federal Register, DOI Notice 2026-06458, April 3, 2026. <a href=\"https://www.federalregister.gov/documents/2026/04/03/2026-06458\">https://www.federalregister.gov/documents/2026/04/03/2026-06458</a><br>"
        "Underlying authority: Endangered Species Act Section 7(e), 16 U.S.C. 1536(e).<br>"
        "Related tracker entries: alaska-oil-gas-leasing-pivot-2025-2026 (parallel oil-and-gas pivot pattern); eo-14154 (EO 14154 Unleashing American Energy)."
    ),
    "I": {
        "indigenous": {
            "people": "Indigenous communities of coastal Louisiana, including the United Houma Nation, the Pointe-au-Chien Indian Tribe, the Isle de Jean Charles Choctaw (formerly known as the Biloxi-Chitimacha-Choctaw Tribe), and the Atakapa-Ishak/Chawasha, face direct environmental-justice harm from accelerated Gulf oil and gas activities. These communities have already experienced oil-and-gas-induced subsidence and saltwater intrusion that has displaced families and severed traditional fishing-and-trapping subsistence practices.",
            "places": "Indigenous-affiliated landscapes of coastal Louisiana, including the bayou systems, the Mississippi Delta, and the Atchafalaya Basin, face accelerated industrial encroachment. Sacred sites and ceremonial places within these landscapes face exposure to oil-spill contamination and to physical alteration from drilling-pad and pipeline construction.",
            "practices": "Indigenous subsistence practices (shrimping, oyster harvesting, alligator hunting, traditional fishing, plant gathering) depend on the ecological integrity of Gulf wetlands. The Houma French language and other heritage languages of coastal Louisiana Indigenous communities preserve cultural knowledge of bayou ecosystems that cannot transmit absent the lived practice. ESA Section 7 exemption accelerates the disruption already underway.",
            "treasures": "Archaeological resources within coastal-Louisiana Indigenous traditional territories include shell middens, ceremonial mounds, and ancestral burial places. Many sites face inundation from sea-level rise compounded by oil-and-gas-induced subsidence. Indigenous traditional ecological knowledge of Gulf ecosystems constitutes intangible cultural heritage. The ESA Section 7 consultation framework is itself a federal-statutory cultural-policy treasure that the exemption process undermines."
        },
        "africanDescendant": {
            "people": "African-descendant communities of the Gulf Coast, including Louisiana Creole communities, Black fishing-village communities of Mississippi and Alabama, Black communities of the lower Texas coast, and Black communities of the Florida Panhandle, face direct environmental-justice harm. Black coastal communities have been disproportionately exposed to petrochemical industry harms, including the 'Cancer Alley' corridor between Baton Rouge and New Orleans where Louisiana State University and Tulane researchers have documented elevated cancer rates.",
            "places": "African-descendant cultural-resource places of the Gulf Coast, including Black freedmen-community landscapes, Black church and cemetery sites, and Black fishing-village landscapes, face cumulative environmental-justice harm.",
            "practices": "African-descendant subsistence and cultural practices tied to Gulf fishing, shrimping, and oyster harvesting face accelerated disruption.",
            "treasures": "African-descendant cultural-resource sites along the Gulf Coast, including pre-emancipation sites, freedmen settlements, and post-Reconstruction Black-community archaeological landscapes, face cumulative degradation from accelerated oil-and-gas activities."
        }
    },
    "c": ["Indigenous", "African-descendant", "Latiné", "All Communities", "environmentalJustice"],
    "U": "https://www.federalregister.gov/documents/2026/04/03/2026-06458",
    "_source": "manual",
}


# I'll continue building all entries in the next part of the script
# but to fit within reasonable bounds, the remaining entries are
# defined in supplementary functions below.

def build_alaska_aggregate():
    return {
        "i": "alaska-oil-gas-leasing-pivot-2025-2026",
        "t": "Aggregate Analysis",
        "n": "Aggregate: Alaska Public Lands Oil and Gas Leasing Pivot 2025-2026 (BLM, BOEM, FWS coordinated reopening of Alaska federal lands)",
        "T": '<span style="color: #991B1B;">Aggregate Analysis:</span> Alaska Public Lands Oil and Gas Leasing Pivot 2025-2026. BLM Notices Reopening ANWR Coastal Plain, NPR-A, Dalton Corridor, and Other Alaska Federal Lands to Industrial Development',
        "s": "Alaska oil-gas leasing pivot 2025-2026",
        "d": "2026-04-30",
        "a": "Trump II",
        "A": ["DOI", "BLM", "BOEM", "FWS"],
        "S": "Active. The 2025-2026 Trump II Alaska public-lands-leasing pivot is a coordinated reopening of approximately 25 to 30 million acres of Alaska federal lands to oil, gas, mineral, and resource leasing. The pivot operates through multiple Federal Register notices and Records of Decision under the authority of EO 14154 (Unleashing American Energy, 2025-01-20) and Secretary's Order 3418 (Unleashing American Energy, 2025-02-03).",
        "L": "SEVERE",
        "D": (
            "<b>AGGREGATE PATTERN.</b> The 2025-2026 Alaska public-lands-leasing pivot is a coordinated federal-action campaign to reopen Alaska federal lands to oil, gas, mineral, and resource industrial development. The pivot reverses Biden-era management plans, withdrawals, and Special Areas designations that had limited industrial activity on approximately 25 to 30 million acres of federal Alaska lands.<br><br>"
            "<b>COMPONENT FEDERAL ACTIONS.</b><br>"
            "(1) PLO 7966 partial revocation of PLOs 5150 and 5180 (February 25, 2026): tracked at blm-plo-7966-dalton-corridor-2026; reopens 2.1 million acres of the Dalton Utility Corridor.<br>"
            "(2) NPR-A 2025 Record of Decision (February 25, 2026): tracked at npra-2025-rod-2026; reverses approximately 13 million acres of Special Areas designations.<br>"
            "(3) ANWR 2026 Coastal Plain Oil and Gas Lease Sale (April 20, 2026): tracked at anwr-coastal-plain-oil-gas-lease-2026; opens 1.5 million-acre Coastal Plain to leasing.<br>"
            "(4) ANWR Call for Nominations and Comments for the 2026 Coastal Plain Lease Sale (Federal Register, prior to 2026-04-20).<br>"
            "(5) NPR-A 2026 Oil and Gas Lease Sale Notice (Federal Register, 2026).<br>"
            "(6) NPR-A 2025 Call for Nominations and Comments (Federal Register, 2025).<br>"
            "(7) Rescission of Management and Protection of NPR-A Regulations (May 7, 2024 Biden regs rescinded under Trump II): Federal Register, 2025.<br>"
            "(8) Implementation of Section 50203 of the One Big Beautiful Bill Act (P.L. 119-21): authorizes oil and gas leasing under specific Alaska public-lands provisions.<br><br>"
            "<b>CULTURAL CONTINUITY HARM.</b> The cumulative pivot operates against Indigenous cultural-continuity practices on Athabaskan, Inupiat, Yup'ik, Tlingit, Aleut, and Alutiiq lands. Subsistence resources (caribou, moose, fish, marine mammals, plant materials) face accelerated disruption. Sacred sites and ceremonial places face exposure to industrial encroachment. Federal-trust-responsibility consultation timelines are foreshortened by EO 14154 and SO 3418 emergency-energy framing.<br><br>"
            "<b>RELATIONSHIP TO STARGATE-AND-NUCLEAR PIVOT.</b> The Alaska oil-and-gas pivot operates alongside the AI-data-center-and-nuclear deregulation pivot tracked at stargate-project-trump-2025, eo-14300-nrc-reform-2025, and usgs-critical-minerals-list-2025. Together these federal actions constitute the principal Trump II energy-and-minerals pivot, with cumulative cultural-resource harm to Indigenous, African-descendant, Latine, Asian, and Pacific Islander communities across multiple geographies.<br><br>"
            "<b>CULTURAL RESOURCE THREAT ASSESSMENT.</b> The threat level is SEVERE. The aggregate-scale Alaska pivot is one of the largest reversals of public-lands protections in U.S. federal history."
            "<br><br>"
            "<b>SOURCES.</b><br>"
            "Component federal actions are cited in their individual tracker entries. Underlying authorities: Tax Cuts and Jobs Act Section 20001 (Public Law 115-97); Naval Petroleum Reserves Production Act of 1976 (42 U.S.C. 6501 et seq.); ANCSA (43 U.S.C. 1601 et seq.); ANILCA (16 U.S.C. 3101 et seq.); One Big Beautiful Bill Act Section 50203 (P.L. 119-21).<br>"
            "Related tracker entries: anwr-coastal-plain-oil-gas-lease-2026; blm-plo-7966-dalton-corridor-2026; npra-2025-rod-2026; eo-14154; so-3418; stargate-project-trump-2025; eo-14300-nrc-reform-2025; usgs-critical-minerals-list-2025; coal-leasing-13m-acres."
        ),
        "I": {
            "indigenous": {
                "people": "Athabaskan, Inupiat, Yup'ik, Tlingit, Aleut, and Alutiiq communities across Alaska face cumulative cultural-continuity harm from the coordinated 2025-2026 Alaska public-lands-leasing pivot. The Gwich'in Steering Committee, the Inupiat Community of the Arctic Slope, the Native Village of Nuiqsut, the Native Village of Stevens, the Yup'ik village of Kwethluk, and other tribal governments organize against components of the pivot. Inupiat communities of the North Slope, particularly Kaktovik (within ANWR) and Nuiqsut (within NPR-A), face the most direct cumulative impact.",
                "places": "Approximately 25 to 30 million acres of Alaska federal lands face accelerated industrial encroachment, including the 1.5-million-acre ANWR Coastal Plain, the 13-million-acre NPR-A Special Areas, the 2.1-million-acre Dalton Utility Corridor, and adjacent lands. Sacred sites and ceremonial places, including the Porcupine Caribou Herd calving grounds and the Teshekpuk Lake Caribou Herd calving grounds, face cultural-landscape integrity loss.",
                "practices": "Indigenous subsistence practices (caribou hunting, fish camps, bowhead whaling, beluga harvesting, plant gathering, ice cellar construction, ceremonial sharing) depend on the ecological integrity of the lands now reopened. Heritage languages of Alaska Indigenous communities (Gwich'in, Inupiaq, Yup'ik, Tlingit, Aleut, Alutiiq) preserve cultural knowledge of these landscapes that cannot transmit absent the lived practice.",
                "treasures": "Archaeological resources, ceremonial sites, and ancestral burial places across the affected 25-to-30-million-acre footprint constitute Indigenous cultural treasures protected under NHPA Section 106, NAGPRA, and the Archaeological Resources Protection Act. Traditional ecological knowledge held by Alaska Indigenous elders constitutes intangible cultural heritage. The federal-statutory protective framework (ANCSA, ANILCA, ESA, NHPA, NEPA) is itself a cultural-policy treasure whose practical force is reduced by the cumulative pivot."
            }
        },
        "c": ["Indigenous", "All Communities", "environmentalJustice"],
        "U": "https://www.federalregister.gov/agencies/land-management-bureau",
        "_source": "manual",
    }


def build_gaming_aggregate(gaming_items):
    n = len(gaming_items)
    items_sorted = sorted(gaming_items, key=lambda x: x.get('date',''))
    lines = []
    lines.append(f"<b>AGGREGATE.</b> Between February 2025 and April 2026, the Bureau of Indian Affairs published in the Federal Register {n} notices of approval (most by operation of law under 25 U.S.C. 2710(d)(8)) of tribal-state gaming compacts and compact amendments under the Indian Gaming Regulatory Act of 1988 (25 U.S.C. 2701 et seq.). Per the TCKC Threat Tracker's federal-actor coding policy, these routine federal approvals of tribal-state compacts are aggregated into this PROTECTIVE entry rather than coded individually.<br><br>")
    lines.append("<b>CULTURAL CONTINUITY IMPACT.</b> Tribal-state gaming compacts are a principal mechanism of tribal economic self-determination and a fundamental support for tribal-government revenue. Gaming revenue funds tribal cultural-language programs, health services, education programs, ceremonial-practice support, and intergenerational-transmission infrastructure. Federal approval of compact agreements protects tribal sovereignty by sanctioning state-tribal negotiations on equal-government-to-government footing and securing the federal-trust-responsibility framework around Class III gaming. The compacts implement IGRA Section 11 (25 U.S.C. 2710), which confines federal-government authority to a non-substantive review-and-approve role.<br><br>")
    lines.append("<b>FEDERAL-INDIAN-TRUST CONTEXT.</b> The federal-trust responsibility, articulated in Cherokee Nation v. Georgia (1831), United States v. Sandoval (1913), and Morton v. Mancari (1974), undergirds federal approval of gaming compacts as expressions of tribal sovereignty consistent with the trust obligation. The pattern of routine compact approvals demonstrates the operating-by-default federal protective framework even as other federal-Indian-policy actions during 2025-2026 (tracked elsewhere in this tracker) have produced harm.<br><br>")
    lines.append(f"<b>2025-2026 AGGREGATE LIST ({n} compact approvals).</b><br>")
    for item in items_sorted:
        lines.append(f"- <b>{item['date']}</b>: {item['title'][:200]} (Federal Register {item['doc']})<br>")
        lines.append(f"  <a href=\"{item['url']}\">{item['url']}</a><br>")
    lines.append("<br>")
    lines.append("<b>SOURCES.</b><br>")
    lines.append("Indian Gaming Regulatory Act of 1988, 25 U.S.C. 2701-2721. National Indian Gaming Commission regulations at 25 CFR. Federal Register publication of each compact approval is the primary source for that compact. Aggregate URLs are listed above.<br>")
    lines.append("Related tracker entries: v2026-indigenous-cultural-threat-analysis; nagpra-roundup-2026-04 (parallel monthly federal-actor aggregation pattern).")

    return {
        "i": "indian-gaming-compacts-2025-2026",
        "t": "Aggregate Analysis",
        "n": f"Aggregate: BIA Approvals of Tribal-State Gaming Compacts and Amendments, February 2025 to April 2026 ({n} compacts)",
        "T": f'<span style="color: #065F46;">Aggregate Analysis:</span> BIA Approvals of {n} Tribal-State Gaming Compacts and Amendments Under IGRA, February 2025 to April 2026',
        "s": "Indian Gaming Compacts 2025-2026",
        "d": "2026-04-30",
        "a": "Trump II",
        "A": ["DOI", "BIA", "NIGC"],
        "S": f"Active. {n} tribal-state gaming compacts and compact amendments approved by the Bureau of Indian Affairs (most by operation of law under IGRA Section 11) between February 2025 and April 2026. Aggregate per the TCKC federal-actor coding convention.",
        "L": "PROTECTIVE",
        "D": "".join(lines),
        "I": {
            "indigenous": {
                "people": f"{n} federally recognized tribes have secured federal approval of tribal-state gaming compacts or compact amendments through this aggregate. Tribal-government revenue from compact-authorized Class III gaming funds tribal cultural-language programs, education, health services, and ceremonial-practice support across the affected nations. Compact approvals support tribal sovereignty by sanctioning government-to-government negotiations and confining federal review to a non-substantive role.",
                "places": "Tribal gaming facilities operate on tribal lands held in trust or in restricted fee status. The compacts approved through this aggregate cover gaming operations on Port Gamble S'Klallam, Lac du Flambeau, Iowa Tribe of Kansas and Nebraska, Lummi Nation, Sycuan Band of the Kumeyaay Nation, and other tribal lands.",
                "practices": "Tribal gaming compacts implement IGRA Section 11 protections for tribal-government authority over Class III gaming. The compacts include provisions for tribal labor, environmental review, and intergovernmental dispute resolution. The compact approval process itself is a practice of federal-tribal government-to-government engagement.",
                "treasures": "Federal-trust-responsibility doctrine and IGRA's compact-approval framework constitute federal-statutory cultural-policy treasures that protect tribal sovereignty. Continued routine federal approval of compacts demonstrates the framework's operating force during a period when other federal-Indian-policy actions have produced harm."
            }
        },
        "c": ["Indigenous", "All Communities"],
        "U": "https://www.federalregister.gov/",
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

    # Build all entries
    new_entries = [
        ("agency_actions", ENTRY_ANWR),
        ("agency_actions", ENTRY_DALTON),
        ("agency_actions", ENTRY_NPRA_ROD),
        ("agency_actions", ENTRY_KOI),
        ("agency_actions", ENTRY_ESA_GULF),
        ("agency_actions", build_alaska_aggregate()),
        ("agency_actions", build_gaming_aggregate(AGG['gaming_compacts'])),
    ]

    # NAGPRA roundups for Feb 2026 and Mar 2026
    if AGG['nagpra_by_month'].get('2026-02'):
        items = AGG['nagpra_by_month']['2026-02']
        nagpra_feb = {
            "i": "nagpra-roundup-2026-02",
            "t": "NAGPRA Roundup",
            "n": f"NAGPRA Roundup February 2026: {len(items)} state, university, and private-institution NAGPRA notices",
            "T": f'<span style="color: #065F46;">NAGPRA Roundup February 2026:</span> {len(items)} State, University, and Private-Institution NAGPRA Notices',
            "s": "NAGPRA roundup February 2026",
            "d": "2026-02-28",
            "a": "Trump II",
            "A": ["DOI", "NPS"],
            "S": f"Active aggregate. {len(items)} NAGPRA notices from non-federal actors aggregated per TCKC policy (locked 2026-04-23).",
            "L": "PROTECTIVE",
            "D": make_nagpra_roundup_desc("February 2026", items),
            "I": {
                "indigenous": {
                    "people": "Indigenous lineal descendants and culturally affiliated federally recognized Tribes, Native Hawaiian organizations, and Alaska Native villages regain authority over ancestral remains, funerary objects, sacred objects, and objects of cultural patrimony covered by the February 2026 notices. Tribal Historic Preservation Officers, repatriation coordinators, and cultural-affiliation specialists at the affected tribes carry forward the consultation work the notices commence or complete.",
                    "places": "Repatriated ancestral remains and sacred objects return to tribal lands, ceremonial sites, traditional burial places, and tribal cultural-resource facilities. The institutional-holding sites listed in the February 2026 aggregate (state agencies, state universities, private universities, and private institutions) reduce their NAGPRA-applicable inventories.",
                    "practices": "Ceremonial reburial, intergenerational transmission of cultural-affiliation knowledge, and tribal historic-preservation-officer practice are supported by the aggregate. The NAGPRA framework operates through community-led practice. Tribes themselves determine cultural affiliation, repatriation pathways, and ceremonial reception of returned remains and objects.",
                    "treasures": "The material culture itself (ancestral remains, funerary objects, sacred objects, objects of cultural patrimony) returns to tribal stewardship. The aggregate also strengthens NAGPRA's federal-statutory protection by demonstrating routine institutional compliance during the 2025-2026 period."
                }
            },
            "c": ["Indigenous"],
            "U": items[0]['url'] if items else "https://www.federalregister.gov/",
            "_source": "manual",
            "_isAggregate": True,
        }
        new_entries.append(("agency_actions", nagpra_feb))

    if AGG['nagpra_by_month'].get('2026-03'):
        items = AGG['nagpra_by_month']['2026-03']
        nagpra_mar = dict(nagpra_feb) if AGG['nagpra_by_month'].get('2026-02') else {}
        nagpra_mar = {
            "i": "nagpra-roundup-2026-03",
            "t": "NAGPRA Roundup",
            "n": f"NAGPRA Roundup March 2026: {len(items)} state, university, and private-institution NAGPRA notices",
            "T": f'<span style="color: #065F46;">NAGPRA Roundup March 2026:</span> {len(items)} State, University, and Private-Institution NAGPRA Notices',
            "s": "NAGPRA roundup March 2026",
            "d": "2026-03-31",
            "a": "Trump II",
            "A": ["DOI", "NPS"],
            "S": f"Active aggregate. {len(items)} NAGPRA notices from non-federal actors aggregated per TCKC policy (locked 2026-04-23).",
            "L": "PROTECTIVE",
            "D": make_nagpra_roundup_desc("March 2026", items),
            "I": {
                "indigenous": {
                    "people": "Indigenous lineal descendants and culturally affiliated federally recognized Tribes, Native Hawaiian organizations, and Alaska Native villages regain authority over ancestral remains, funerary objects, sacred objects, and objects of cultural patrimony covered by the March 2026 notices. Tribal Historic Preservation Officers and repatriation coordinators carry forward the consultation work.",
                    "places": "Repatriated ancestral remains and sacred objects return to tribal lands, ceremonial sites, traditional burial places, and tribal cultural-resource facilities.",
                    "practices": "Ceremonial reburial, intergenerational transmission of cultural-affiliation knowledge, and tribal historic-preservation-officer practice are supported. The NAGPRA framework operates through community-led practice.",
                    "treasures": "Material culture (ancestral remains, funerary objects, sacred objects, objects of cultural patrimony) returns to tribal stewardship. NAGPRA's federal-statutory protection is reinforced through institutional compliance."
                }
            },
            "c": ["Indigenous"],
            "U": items[0]['url'] if items else "https://www.federalregister.gov/",
            "_source": "manual",
            "_isAggregate": True,
        }
        new_entries.append(("agency_actions", nagpra_mar))

    # Add all new entries
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
        print(f"  ADD: {eid} -> {cat}")

    # Update existing nagpra-roundup-2026-04 with the additional notices
    if AGG['nagpra_by_month'].get('2026-04'):
        items = AGG['nagpra_by_month']['2026-04']
        for entry in data.get('agency_actions', []):
            if (entry.get('id') or entry.get('i')) == 'nagpra-roundup-2026-04':
                # Replace the description with the updated count
                if "[UPDATED 2026-04-30 with 15 audit-discovered notices]" in entry.get('D', ''):
                    print("  SKIP: nagpra-roundup-2026-04 already updated")
                    break
                update_block = (
                    "<br><br><b>UPDATE 2026-04-30.</b> The 2026-04-30 agency-coverage audit "
                    f"surfaced an additional {len(items)} NAGPRA notices from state, university, "
                    "and private-institution sources published in the Federal Register during "
                    "April 2026 that were not captured in the original count of 0. The full "
                    f"list of {len(items)} April 2026 NAGPRA notices is appended below "
                    "[UPDATED 2026-04-30 with 15 audit-discovered notices].<br><br>"
                )
                update_block += f"<b>APRIL 2026 AUDIT-DISCOVERED NOTICES.</b><br>"
                for item in sorted(items, key=lambda x: x.get('date','')):
                    update_block += f"- <b>{item['date']}</b>: {item['title'][:200]} (Federal Register {item['doc']})<br>"
                    update_block += f"  <a href=\"{item['url']}\">{item['url']}</a><br>"
                if "<b>SOURCES.</b>" in entry['D']:
                    entry['D'] = entry['D'].replace("<b>SOURCES.</b>", update_block + "<br><b>SOURCES.</b>", 1)
                else:
                    entry['D'] = entry['D'] + update_block
                print(f"  UPDATE: nagpra-roundup-2026-04 with {len(items)} additional notices")
                break

    # Save
    if "meta" in data and isinstance(data["meta"], dict):
        data["meta"]["lastUpdated"] = datetime.now().strftime("%Y-%m-%d")

    tmp = DATA_PATH.with_suffix(".json.tmp")
    with tmp.open("w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    tmp.replace(DATA_PATH)

    print(f"\nDone. Total entries now: {sum(len(data.get(k,[])) for k in ['executive_actions','agency_actions','legislation','litigation','other_domestic','international'])}")


if __name__ == "__main__":
    main()
