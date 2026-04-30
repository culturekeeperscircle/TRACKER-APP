#!/usr/bin/env python3
"""Add three approved AI-infrastructure entries atomically with one backup.

Entry A. xAI Colossus / 35 unlicensed methane gas turbines polluting Memphis.
  Category: agency_actions. Threat: SEVERE.
  Federal nexus: Clean Air Act enforcement, EPA non-enforcement, NAACP and
  SELC and Earthjustice civil-rights and CAA lawsuit.

Entry B. Meta Los Lunas / Greater Kudu LLC AI-data-center expansion (NM).
  Category: agency_actions. Threat: HARMFUL.
  Federal nexus: Industrial Revenue Bond private-activity-bond tax exemption
  (IRC sec. 142), federally adjudicated Rio Grande Compact water draw,
  shell-LLC land-acquisition pattern.

Entry C. Stargate Project announcement (January 21, 2025).
  Category: executive_actions. Threat: SEVERE.
  Federal nexus: Presidential White House announcement, Trump-promised
  executive orders and emergency declarations to enable infrastructure
  siting, federal permitting, NEPA waiver implications, MGX (UAE sovereign
  wealth) partner.
"""
import json
import shutil
from pathlib import Path
from datetime import datetime

DATA_PATH = Path(__file__).parent.parent / "data" / "data.json"
BACKUP_PATH = DATA_PATH.with_suffix(
    f".json.bak-{datetime.now().strftime('%Y%m%d-%H%M%S')}-pre-ai-infra-package"
)


# =================== ENTRY A: xAI MEMPHIS ===================
ENTRY_A = {
    "i": "xai-colossus-memphis-cleanair-2026",
    "t": "Civil Rights and Clean Air Act Violation",
    "n": "xAI Colossus 1 (South Memphis, Tennessee) and Colossus 2 (Southaven, Mississippi): Unpermitted Methane Gas Turbines, Federal Clean Air Act Violations, NAACP and SELC and Earthjustice Litigation",
    "T": '<span style="color: #991B1B;">xAI Colossus, Memphis and Southaven:</span> 35 Unpermitted Methane Gas Turbines Pollute Predominantly Black Communities; NAACP and SELC and Earthjustice Sue Under Clean Air Act',
    "s": "xAI Colossus methane turbines Memphis",
    "d": "2026-04-01",
    "a": "Trump II",
    "A": ["EPA", "TDEC", "MDEQ"],
    "S": "Active. Colossus 1 has operated approximately 35 unpermitted methane gas turbines in South Memphis (Shelby County, Tennessee) since June 2024 to power xAI's Grok-training supercomputer. Colossus 2 (Southaven, DeSoto County, Mississippi) follows the same unpermitted-turbine strategy. NAACP, SELC, and Earthjustice filed a 60-day Clean Air Act notice of intent to sue in February 2026 and filed suit against xAI and subsidiary MZX Tech in 2026 over Clean Air Act violations and civil-rights harms in predominantly Black Memphis-area communities. Mississippi regulators have approved the Southaven plant over public objection.",
    "L": "SEVERE",
    "D": (
        "<b>FACILITY AND OPERATIONS.</b> Elon Musk's xAI built and operates Colossus, a supercomputer training the Grok large-language model accessible through X. Colossus 1 began operating in South Memphis (Shelby County, Tennessee) in June 2024. To power the facility, xAI installed and operated approximately 35 methane gas turbines without obtaining the air-quality permits required under the federal Clean Air Act and the Tennessee State Implementation Plan. Colossus 2, a planned expansion sited in Southaven (DeSoto County, Mississippi), follows the same unpermitted-turbine approach. xAI officials described the strategy publicly as \"copying and pasting\" the Memphis operation across the state line.<br><br>"
        "<b>EMISSIONS.</b> The Southaven facility alone has the potential to emit more than 1,700 tons of nitrogen oxides (NOx) per year. NOx is a smog-forming and respiratory-disease-driving pollutant. The Southaven plant would likely become the largest industrial source of NOx in the greater Memphis metropolitan area. The Memphis area is already in nonattainment of the National Ambient Air Quality Standards for ozone. The American Lung Association has assigned both Shelby County (Tennessee) and DeSoto County (Mississippi) failing grades for ozone pollution.<br><br>"
        "<b>ENVIRONMENTAL-JUSTICE COMMUNITY CONTEXT.</b> South Memphis is a historically Black community. Memphis was recently designated an asthma capital of the United States. The siting of an unpermitted high-NOx industrial source in this community follows the documented pattern of environmental-justice harm to African-descendant communities in the U.S. South under which industrial polluters are sited in Black neighborhoods with reduced regulatory enforcement. Boxtown and adjacent South Memphis neighborhoods have organized against the facility through Memphis Community Against Pollution (MCAP) and allied organizations.<br><br>"
        "<b>LITIGATION.</b> In February 2026, the NAACP, the Southern Environmental Law Center (SELC), and Earthjustice issued a 60-day notice of intent to sue under the citizen-suit provision of the Clean Air Act (42 U.S.C. sec. 7604). Following expiration of the notice period, the NAACP filed suit against xAI and its subsidiary MZX Tech for ongoing Clean Air Act violations. The lawsuit seeks injunctive relief halting unpermitted operations, civil penalties, and remedial relief for affected communities. SELC and Earthjustice are litigating in parallel proceedings. Public hearings on the Southaven permit took place in early 2026; Mississippi state regulators approved the permit over public objection.<br><br>"
        "<b>FEDERAL NEXUS.</b> The Clean Air Act is federal law (42 U.S.C. sec. 7401 et seq.). EPA has primary enforcement authority and shares it with state agencies through SIP delegations. EPA's failure to enforce the Act against an obvious unpermitted major-source operation is the operative federal-action gap that this entry tracks. The NAACP citizen suit is the principal vehicle through which the federal-statutory protection is being enforced in the absence of EPA action. The case sits within the broader Trump II pattern of EPA enforcement retreat and environmental-justice rollback.<br><br>"
        "<b>RELATIONSHIP TO STARGATE AND THE BROADER AI-INFRASTRUCTURE BUILDOUT.</b> Colossus is a Musk/xAI project rather than a Stargate Project node, but the underlying federal posture (the Trump administration's willingness to fast-track AI-infrastructure siting through executive orders and emergency declarations, tracked at stargate-project-trump-2025) supplies the political cover under which environmental and air-quality permitting requirements are being bypassed. The pattern is documented in Karen Hao's reporting (Library reference, *Empire of AI*, 2025) and in Hao's Democracy Now! interview of May 2025.<br><br>"
        "<b>CULTURAL RESOURCE THREAT ASSESSMENT.</b> The threat level is SEVERE. The harms are present-tense and documented. Boxtown and South Memphis residents are exposed to elevated NOx, particulate matter, and other combustion byproducts produced by 35 unpermitted turbines. Asthma rates, cardiovascular morbidity, and pediatric respiratory disease in the affected airshed will rise on documented exposure-response curves. The harm tracks the People dimension of cultural-resource analysis directly. Boxtown's place-based identity as a historically Black freedmen-founded community is harmed by industrial siting that the community had no opportunity to consent to (Places dimension). Community health-keeping practices passed across generations, including church-based mutual-aid health networks, face increased burden from preventable disease (Practices dimension). Environmental health is a precondition of cultural continuity (Treasures dimension)."
        "<br><br>"
        "<b>SOURCES.</b><br>"
        "Primary litigation: NAACP, \"NAACP Sues xAI for Illegal Pollution from Data Center Power Plant.\" <a href=\"https://naacp.org/articles/naacp-sues-xai-illegal-pollution-data-center-power-plant\">https://naacp.org/articles/naacp-sues-xai-illegal-pollution-data-center-power-plant</a>; "
        "Earthjustice, \"NAACP Sues xAI for Illegal Pollution from Data Center Power Plant,\" 2026. <a href=\"https://earthjustice.org/press/2026/xai-sued-for-illegal-power-plant\">https://earthjustice.org/press/2026/xai-sued-for-illegal-power-plant</a><br>"
        "Primary advocacy and case documentation: Southern Environmental Law Center, \"xAI built an illegal power plant to power its data center.\" <a href=\"https://www.selc.org/news/xai-built-an-illegal-power-plant-to-power-its-data-center/\">https://www.selc.org/news/xai-built-an-illegal-power-plant-to-power-its-data-center/</a>; "
        "SELC, \"Civil rights group sues xAI for illegal pollution from data center power plant.\" <a href=\"https://www.selc.org/press-release/civil-rights-group-sues-xai-for-illegal-pollution-from-data-center-power-plant/\">https://www.selc.org/press-release/civil-rights-group-sues-xai-for-illegal-pollution-from-data-center-power-plant/</a>; "
        "SELC, \"Resistance against Elon Musk's xAI facility in South Memphis gets stronger.\" <a href=\"https://www.selc.org/news/resistance-against-elon-musks-xai-facility-in-south-memphis-gets-stronger/\">https://www.selc.org/news/resistance-against-elon-musks-xai-facility-in-south-memphis-gets-stronger/</a>; "
        "SELC, \"Groups appeal permit for xAI's South Memphis data center, decisions around unpermitted methane gas turbines.\" <a href=\"https://www.selc.org/press-release/groups-appeal-permit-for-xais-south-memphis-data-center-decisions-around-unpermitted-methane-gas-turbines/\">https://www.selc.org/press-release/groups-appeal-permit-for-xais-south-memphis-data-center-decisions-around-unpermitted-methane-gas-turbines/</a>; "
        "SELC, \"Groups threaten lawsuit over xAI's unpermitted gas turbines in Mississippi.\" <a href=\"https://www.selc.org/press-release/groups-threaten-lawsuit-over-xais-unpermitted-gas-turbines-in-mississippi/\">https://www.selc.org/press-release/groups-threaten-lawsuit-over-xais-unpermitted-gas-turbines-in-mississippi/</a>; "
        "NAACP, \"NAACP, SELC, Earthjustice threaten Lawsuit over xAI's Unpermitted Gas Turbines in Mississippi.\" <a href=\"https://naacp.org/articles/naacp-selc-earthjustice-threaten-lawsuit-over-xais-unpermitted-gas-turbines-mississippi\">https://naacp.org/articles/naacp-selc-earthjustice-threaten-lawsuit-over-xais-unpermitted-gas-turbines-mississippi</a>; "
        "NAACP, \"NAACP, SELC Condemn Mississippi Approval of xAI Power Plant, Regulators Ignore Public Disapproval.\" <a href=\"https://naacp.org/articles/naacp-selc-condemns-mississippi-approval-xai-power-plant-regulators-ignore-public\">https://naacp.org/articles/naacp-selc-condemns-mississippi-approval-xai-power-plant-regulators-ignore-public</a><br>"
        "Local news: Local Memphis (WATN), \"NAACP files lawsuit against Elon Musk's xAI over gas turbines in Southaven.\" <a href=\"https://www.localmemphis.com/article/news/local/naacp-lawsuit-elon-musk-gas-turbines-southaven/522-41e40836-0bf4-4919-9d47-596d5d02f633\">https://www.localmemphis.com/article/news/local/naacp-lawsuit-elon-musk-gas-turbines-southaven/522-41e40836-0bf4-4919-9d47-596d5d02f633</a><br>"
        "Karen Hao testimony reference: Democracy Now!, May 2025 interview rebroadcast as holiday special. <a href=\"https://www.youtube.com/watch?v=s4hZz9Vd0lY\">https://www.youtube.com/watch?v=s4hZz9Vd0lY</a> (Library reference: [INTERVIEW] Karen Hao on Sam Altman OpenAI and the Quasi-Religious Push for Artificial Intelligence - Democracy Now! (2025) [EN].md).<br>"
        "Related tracker entries: stargate-project-trump-2025 (Stargate Project, 2025-01-21); meta-los-lunas-greater-kudu-2024 (Meta NM expansion, 2024-12); v2026-african-descendant-cultural-threat-analysis (African-descendant aggregate analysis)."
    ),
    "I": {
        "africanDescendant": {
            "people": "South Memphis residents (a historically Black community), DeSoto County Mississippi residents (substantial Black population), and the broader greater Memphis Black community face elevated exposure to nitrogen oxides, particulate matter, and other combustion byproducts. Asthma rates, cardiovascular morbidity, and pediatric respiratory-disease prevalence are projected to rise. Memphis is already designated an asthma capital. The harms compound an existing environmental-justice burden documented across decades.",
            "places": "Boxtown and adjacent South Memphis neighborhoods, founded by formerly enslaved people after the Civil War, are place-based African-descendant cultural sites whose airshed has been industrialized without community consent. The historical Mississippi Delta African-descendant communities surrounding Southaven face the same harm vector.",
            "practices": "Church-based mutual-aid health networks, intergenerational caregiving practices, and community-organized environmental-health advocacy (Memphis Community Against Pollution and allied organizations) are being burdened by a preventable industrial harm that the federal Clean Air Act was enacted to forestall.",
            "treasures": "Community health, intergenerational continuity, and place-based cultural identity are cultural treasures whose preservation requires breathable air. The xAI operation degrades each."
        },
        "allCommunities": {
            "people": "All Memphis-area residents are exposed to the elevated regional smog burden the unpermitted turbines produce. Vulnerable populations (children, elderly, asthmatics, cardiac patients) bear disproportionate harm.",
            "places": "The Memphis metropolitan area's airshed is degraded across racial and geographic lines.",
            "practices": "Federal Clean Air Act enforcement practice is undermined by a high-profile permitless major-source operation proceeding without EPA intervention.",
            "treasures": "The federal Clean Air Act regime is itself a cultural-policy treasure of the post-1970 environmental settlement that the unpermitted operation undermines."
        },
        "environmentalJustice": {
            "people": "The classic environmental-justice pattern (industrial siting in Black, Brown, and low-income communities under reduced regulatory enforcement) is here reproduced in a 21st-century AI-infrastructure context.",
            "places": "Boxtown, South Memphis, Southaven and the wider DeSoto County Mississippi region.",
            "practices": "Environmental-justice organizing practice (MCAP and allied organizations) is burdened by the need to litigate what the regulatory state should have prevented.",
            "treasures": "The federal Environmental Justice mandate is undermined by the EPA's failure to act against the unpermitted source."
        }
    },
    "c": ["African-descendant", "All Communities", "environmentalJustice"],
    "U": "https://earthjustice.org/press/2026/xai-sued-for-illegal-power-plant",
    "_source": "manual",
}


# =================== ENTRY B: META LOS LUNAS / GREATER KUDU ===================
ENTRY_B = {
    "i": "meta-los-lunas-greater-kudu-2024",
    "t": "AI Data Center Expansion",
    "n": "Meta / Greater Kudu LLC AI Data Center Expansion at Los Lunas, New Mexico (December 2024 land acquisition; $7.5B Industrial Revenue Bond authorization)",
    "T": '<span style="color: #CA8A04;">Meta / Greater Kudu LLC AI Data Center Expansion:</span> 474-Acre Land Acquisition in Los Lunas, New Mexico, Backed by $7.5 Billion Industrial Revenue Bond, Drawing Up to 500 Acre-Feet of Water Annually',
    "s": "Meta Los Lunas Greater Kudu AI expansion",
    "d": "2024-12-01",
    "a": "Trump II",
    "A": ["IRS", "BIA"],
    "S": "Active. Greater Kudu LLC (Meta affiliate) closed acquisition of a 474-acre parcel adjacent to Meta's Los Lunas data center campus in December 2024. The Village of Los Lunas authorized issuance of up to six series of Industrial Revenue Bonds aggregating up to $7.5 billion in October 2024. Two new buildings dedicated to AI hardware are projected at $800 million construction cost; existing facility access to up to 500 acre-feet of water annually under New Mexico state law. Construction expected to take three years.",
    "L": "HARMFUL",
    "D": (
        "<b>FACILITY AND ENTITY.</b> Greater Kudu LLC is a Meta Platforms Inc. affiliate that owns and operates Meta's Los Lunas, New Mexico data center campus at 4250 Messenger Loop NW (Valencia County, New Mexico). The campus has expanded from a single $250 million 2016 facility to seven buildings. In December 2024, Greater Kudu LLC closed acquisition of an additional 474-acre parcel adjacent to the existing campus, brokered by CBRE. The acquisition supports a planned expansion of two additional buildings dedicated to AI hardware at an announced construction cost of approximately $800 million.<br><br>"
        "<b>FINANCING AND TAX MECHANISM.</b> In October 2024, the Village of Los Lunas approved an Industrial Revenue Bond (IRB) authorization for up to six series of bonds aggregating up to $7.5 billion in support of the expansion. This is the third series of IRBs Meta has obtained at Los Lunas; the first two prior series totaled up to $70 billion in authorized issuance capacity. IRBs are state and local instruments under New Mexico law (NMSA sec. 3-32-1 et seq.) but rely on federal tax-exemption mechanisms under the Internal Revenue Code (IRC sec. 142, private-activity bonds for exempt facilities) for investor demand and pricing. Federal tax-exemption status converts state and local IRBs into federally subsidized financial instruments.<br><br>"
        "<b>WATER DRAW.</b> The Los Lunas data center has access to up to 500 acre-feet of water annually under New Mexico state water law. New Mexico is among the most water-stressed states in the United States. Water rights in the Middle Rio Grande Basin are administered under New Mexico state law and are also subject to the federally adjudicated Rio Grande Compact (1938; codified at NMSA sec. 72-15-23 et seq.) governing interstate apportionment among Colorado, New Mexico, and Texas. Federal court oversight under Texas v. New Mexico and Colorado, No. 141, Original (U.S. Supreme Court) is the operative federal nexus.<br><br>"
        "<b>SHELL-LLC PATTERN.</b> Karen Hao reported in her May 2025 Democracy Now! interview that Meta entered New Mexico under the shell company name Greater Kudu LLC and that the Meta identity was revealed only after the deal closed and residents could not respond. Greater Kudu LLC has been registered with the New Mexico Secretary of State since the inception of the Los Lunas project in 2016 (NM corporate ID 5193818) and is publicly identified as a Meta affiliate in subsequent filings. The shell-LLC pattern Hao describes operates not by total concealment of the Meta identity but by use of an obscure LLC name during initial land-acquisition negotiations and IRB authorization, which can shape early community deliberation before the Meta brand surfaces in regulatory filings.<br><br>"
        "<b>FEDERAL NEXUS.</b> The federal-action angle in this entry is thinner than for xAI Memphis or Stargate. The federal mechanisms operative are: (1) IRC sec. 142 federal tax-exemption status converting state and local IRBs into federally subsidized debt instruments; (2) the federally adjudicated Rio Grande Compact governing water apportionment in the Middle Rio Grande Basin; (3) potential Federal Aviation Administration airspace coordination for any data-center hyperscale construction; and (4) potential federal tribal-consultation duties under the National Historic Preservation Act sec. 106 if any cultural-resource concerns are flagged through tribal historic preservation officers (THPOs) of nearby Pueblos.<br><br>"
        "<b>INDIGENOUS AND HISPANO COMMUNITY CONTEXT.</b> Los Lunas sits in Valencia County, in the Middle Rio Grande Basin, between the Pueblo of Isleta to the north (Bernalillo County) and the Pueblo of Laguna and Acoma Pueblo to the west. The Middle Rio Grande Basin is shared with the six middle-Rio-Grande Pueblos and with Hispano land-grant communities whose senior water rights predate territorial annexation. Industrial water draw at scale in the basin reduces the available margin for downstream Pueblo and acequia agricultural water use during drought years. The Rio Grande Compact's federally adjudicated delivery requirements concentrate the burden of any deficit on senior in-state users, including Pueblo and Hispano agricultural users.<br><br>"
        "<b>RELATIONSHIP TO BROADER PATTERN.</b> The Los Lunas expansion is one node in the broader AI-infrastructure-buildout pattern documented by Karen Hao and exemplified at xAI Memphis (tracked at xai-colossus-memphis-cleanair-2026) and at the Stargate Project (tracked at stargate-project-trump-2025). The pattern combines shell-LLC land acquisition, large IRB-financed construction, and water and energy draw at scale, in regions whose existing populations had no formal mechanism to consent to the cumulative load.<br><br>"
        "<b>CULTURAL RESOURCE THREAT ASSESSMENT.</b> The threat level is HARMFUL. The harms are structural rather than acute, and operate primarily through water-resource depletion, energy-grid load, and shaping of Middle Rio Grande Basin development trajectories that affect Pueblo and Hispano communities downstream and adjacent to the facility. The federal-action component is real (IRC sec. 142 tax exemption, Rio Grande Compact federal adjudication) but indirect. The Indigenous-consultation gap is the most consequential harm dimension: federal NHPA sec. 106 consultation duties have not, on the available record, been triggered for the Los Lunas expansion despite its proximity to the Middle Rio Grande Pueblos and their cultural-resource interests in the basin."
        "<br><br>"
        "<b>SOURCES.</b><br>"
        "Primary corporate filing: Greater Kudu LLC, New Mexico Secretary of State corporate registration. OpenCorporates: <a href=\"https://opencorporates.com/companies/us_nm/5193818\">https://opencorporates.com/companies/us_nm/5193818</a><br>"
        "Primary local-government action: Village of Los Lunas, Industrial Revenue Bond authorization (October 2024). Reported in Valencia County News-Bulletin: <a href=\"https://www.news-bulletin.com/news/tax-break-water-deal-for-meta-data-center/article_d4ff8540-163d-4c73-8a17-a5ec65209c42.html\">https://www.news-bulletin.com/news/tax-break-water-deal-for-meta-data-center/article_d4ff8540-163d-4c73-8a17-a5ec65209c42.html</a>; "
        "Valencia County News-Bulletin, \"Los Lunas Meta Data Center introduces expansion dedicated to Artificial Intelligence,\" January 2025. <a href=\"https://www.news-bulletin.com/news/los-lunas-meta-data-center-introduces-expansion-dedicated-to-artificial-intelligence/article_809a47fe-d366-11ef-b76e-470988820678.html\">https://www.news-bulletin.com/news/los-lunas-meta-data-center-introduces-expansion-dedicated-to-artificial-intelligence/article_809a47fe-d366-11ef-b76e-470988820678.html</a><br>"
        "Coverage of December 2024 land acquisition: Data Center Dynamics, \"Meta buys land adjacent to Los Lunas campus in New Mexico, possible expansion - report.\" <a href=\"https://www.datacenterdynamics.com/en/news/meta-buys-land-adjacent-to-los-lunas-campus-in-new-mexico-possible-expansion-report/\">https://www.datacenterdynamics.com/en/news/meta-buys-land-adjacent-to-los-lunas-campus-in-new-mexico-possible-expansion-report/</a>; "
        "Commercial Association of Realtors New Mexico, \"Meta acquires 474-acre parcel adjacent to Los Lunas data center.\" <a href=\"https://carnm.realtor/meta-acquires-474-acre-parcel-adjacent-to-los-lunas-data-center/\">https://carnm.realtor/meta-acquires-474-acre-parcel-adjacent-to-los-lunas-data-center/</a><br>"
        "Coverage of expansion plans and financing: Data Center Dynamics, \"Meta plans expansion of Los Lunas data center campus in New Mexico.\" <a href=\"https://www.datacenterdynamics.com/en/news/meta-planning-expansion-of-los-lunas-data-center-campus-in-new-mexico/\">https://www.datacenterdynamics.com/en/news/meta-planning-expansion-of-los-lunas-data-center-campus-in-new-mexico/</a>; "
        "BeBeez International, \"Meta plans expansion of Los Lunas data center campus in New Mexico,\" January 17, 2025. <a href=\"https://www.bebeez.eu/2025/01/17/meta-plans-expansion-of-los-lunas-data-center-campus-in-new-mexico/\">https://www.bebeez.eu/2025/01/17/meta-plans-expansion-of-los-lunas-data-center-campus-in-new-mexico/</a>; "
        "MMC Investments, \"The Desert Becomes a Data Center: Meta's $3.3 Billion Bet on Los Lunas, New Mexico.\" <a href=\"https://www.mmcginvest.com/post/the-desert-becomes-a-data-center-meta-s-3-3-billion-bet-on-los-lunas-new-mexico\">https://www.mmcginvest.com/post/the-desert-becomes-a-data-center-meta-s-3-3-billion-bet-on-los-lunas-new-mexico</a><br>"
        "Water-policy analysis: Water Education Colorado, \"Briefly: Facebook data center water use scrutinized.\" <a href=\"https://watereducationcolorado.org/fresh-water-news/briefly-facebook-data-center-water-use-scrutinized/\">https://watereducationcolorado.org/fresh-water-news/briefly-facebook-data-center-water-use-scrutinized/</a><br>"
        "Karen Hao testimony reference: Democracy Now!, May 2025. <a href=\"https://www.youtube.com/watch?v=s4hZz9Vd0lY\">https://www.youtube.com/watch?v=s4hZz9Vd0lY</a> (Library reference: [INTERVIEW] Karen Hao on Sam Altman OpenAI and the Quasi-Religious Push for Artificial Intelligence - Democracy Now! (2025) [EN].md).<br>"
        "Related tracker entries: stargate-project-trump-2025 (Stargate Project, 2025-01-21); xai-colossus-memphis-cleanair-2026 (xAI Memphis, 2026-04-01); v2026-indigenous-cultural-threat-analysis (Indigenous aggregate analysis); blm-chaco-withdrawal-revocation-2026 (Chaco mineral-withdrawal revocation, 2026-03-31, parallel water and consultation harm in NM)."
    ),
    "I": {
        "indigenous": {
            "people": "The six middle-Rio-Grande Pueblos (Cochiti, Santo Domingo, San Felipe, Santa Ana, Sandia, Isleta) hold senior cultural and water-rights interests in the Middle Rio Grande Basin. Pueblo of Laguna and Acoma Pueblo, located west of Los Lunas, hold cultural and ceremonial interests in the broader landscape. Industrial water draw at scale in the basin reduces the margin available for Pueblo agricultural water use, particularly during drought years.",
            "places": "The Middle Rio Grande Basin is a Pueblo cultural landscape. The Bosque (cottonwood riparian gallery) along the river is sacred and culturally significant. Industrial water draw and adjacent industrial development affect the place-based integrity of this landscape.",
            "practices": "Pueblo agricultural practices, including waffle-garden cultivation and acequia-irrigated farming, depend on reliable water deliveries that scale-industrial draw reduces. Ceremonial water-blessing practices that require flowing river water are degraded when basin flow is reduced.",
            "treasures": "The Middle Rio Grande and its Bosque are themselves cultural treasures of the Pueblos. Industrial draw at scale degrades these treasures. Archaeological sites in the 474-acre acquisition parcel and adjacent expansion area may be culturally significant; on the available record, NHPA sec. 106 tribal consultation has not been documented."
        },
        "latine": {
            "people": "Hispano land-grant communities of the Middle Rio Grande Basin (with senior water rights predating U.S. annexation under the Treaty of Guadalupe Hidalgo) face reduced water availability during drought years. Acequia farming communities along the Rio Grande share water-resource burden.",
            "places": "Hispano land-grant villages along the Rio Grande and its tributaries face cumulative water stress.",
            "practices": "Acequia practice (irrigation-cooperative governance dating to colonial Spanish settlement) depends on reliable water deliveries that scale industrial draw reduces.",
            "treasures": "Hispano cultural sites and acequia-irrigated agricultural landscapes face cumulative degradation."
        },
        "allCommunities": {
            "people": "All New Mexico residents share the water-stressed basin and the energy-grid load that AI-data-center expansion adds to. Property-tax revenue gains from IRB-financed construction are real but partial offsets.",
            "places": "The Middle Rio Grande Basin is a shared cultural and ecological landscape.",
            "practices": "Consent-based community-development practice is undermined by the shell-LLC land-acquisition pattern.",
            "treasures": "The IRC sec. 142 federal tax-exemption regime is itself a federal-policy treasure whose use to subsidize hyperscale AI-data-center construction at the cost of basin water and Indigenous consultation deserves scrutiny."
        },
        "environmentalJustice": {
            "people": "Communities lacking the legal and political resources to mount NHPA sec. 106 challenges or water-rights interventions bear the greatest cumulative-impact burden.",
            "places": "Valencia County and the broader Middle Rio Grande Basin.",
            "practices": "The shell-LLC pattern documented by Karen Hao narrows community-deliberation practice during the formative phase of project siting.",
            "treasures": "Federal tribal-consultation duties under NHPA sec. 106 are themselves environmental-justice instruments that the Los Lunas expansion has, on the available record, not engaged."
        }
    },
    "c": ["Indigenous", "Latiné", "All Communities", "environmentalJustice"],
    "U": "https://opencorporates.com/companies/us_nm/5193818",
    "_source": "manual",
}


# =================== ENTRY C: STARGATE PROJECT ===================
ENTRY_C = {
    "i": "stargate-project-trump-2025",
    "t": "Presidential Industrial-Policy Announcement",
    "n": "Stargate Project: White House Announcement of $500 Billion AI Infrastructure Joint Venture (OpenAI, SoftBank, Oracle, MGX), January 21, 2025",
    "T": '<span style="color: #991B1B;">Stargate Project Announcement:</span> Trump White House Joins OpenAI, SoftBank, Oracle, and MGX (UAE) to Announce $500 Billion AI Infrastructure Joint Venture; President Promises Executive Orders and Emergency Declarations to Fast-Track Permitting',
    "s": "Stargate Project announcement",
    "d": "2025-01-21",
    "a": "Trump II",
    "A": ["WH", "DOE", "FERC", "EPA", "DOI"],
    "S": "Active. Announced January 21, 2025 at the White House by President Trump alongside OpenAI CEO Sam Altman, SoftBank CEO Masayoshi Son, and Oracle Chairman Larry Ellison. $100 billion initial commitment, scaling to $500 billion over four years. Joint venture entity: Stargate LLC. Partners: OpenAI (operational responsibility), SoftBank (financial responsibility, chair held by Masayoshi Son), Oracle, and MGX (UAE sovereign-wealth investment fund affiliated with Mubadala Investment Company). Trump promised to use executive orders and emergency declarations to expedite federal permitting. Five additional Stargate data-center sites announced September 2025.",
    "L": "SEVERE",
    "D": (
        "<b>WHITE HOUSE ANNOUNCEMENT.</b> On January 21, 2025, President Donald Trump appeared at the White House alongside OpenAI CEO Sam Altman, SoftBank CEO Masayoshi Son, and Oracle Chairman Larry Ellison to announce the Stargate Project, a private-sector artificial-intelligence-infrastructure joint venture that Trump described as the largest AI-infrastructure project in history. Initial commitment: $100 billion. Headline four-year commitment: $500 billion. Trump publicly promised to use executive orders and emergency declarations to expedite federal permitting required to site Stargate data centers, energy infrastructure, and supporting facilities. Trump stated, \"I'm going to help a lot through emergency declarations. We have an emergency. We have to get this stuff built.\"<br><br>"
        "<b>JOINT-VENTURE STRUCTURE.</b> Stargate LLC is the legal vehicle for the project. Partners: OpenAI (operational responsibility), SoftBank (financial responsibility, chair held by Masayoshi Son), Oracle, and MGX. MGX is an Abu Dhabi-based AI-focused investment fund affiliated with Mubadala Investment Company, a sovereign-wealth instrument of the United Arab Emirates. The MGX participation makes Stargate a U.S.-Gulf-state joint venture, not a purely domestic vehicle. The Trump administration has subsequently facilitated additional U.S.-Gulf AI-infrastructure deals through presidential travel to the Gulf in May 2025.<br><br>"
        "<b>FEDERAL ACTION COMPONENTS.</b> The announcement is itself a presidential-administration industrial-policy event. Beyond the announcement, the federal-action components include: (1) Trump's announced intent to issue executive orders and emergency declarations to expedite siting and permitting; (2) the federal energy-permitting process for the dedicated power generation Stargate data centers will require, including potential FERC action on interconnection and rate matters; (3) federal environmental review (NEPA) requirements that emergency declarations may seek to waive or shorten; (4) federal land or right-of-way requirements where Stargate sites involve federal ownership; and (5) federal tribal-consultation duties under NHPA sec. 106 where Stargate sites are proximate to Indigenous cultural-resource interests.<br><br>"
        "<b>EXPANSION ANNOUNCEMENT.</b> In September 2025, OpenAI, Oracle, and SoftBank announced an expansion of Stargate to include five additional U.S. data-center sites. Specific siting details and federal-permitting actions for each site warrant separate tracker entries as they materialize.<br><br>"
        "<b>CULTURAL-RESOURCE HARM PATHWAYS.</b> Stargate at scale produces cultural-resource harm through five established pathways. (1) Water draw at hyperscale-data-center scale stresses regional water supply, particularly in arid-region siting (Southwest, Mountain West) where TCKC primary cultural communities (Indigenous, Latiné, Hispano) hold senior or culturally significant water-rights interests. (2) Energy-grid load drives natural-gas and nuclear-power expansion, with associated air-quality and siting harms documented at xAI Memphis (tracked at xai-colossus-memphis-cleanair-2026) and at Meta Los Lunas (tracked at meta-los-lunas-greater-kudu-2024). (3) Land acquisition through LLC and shell vehicles bypasses meaningful community consultation in formative project phases. (4) Federal-permitting fast-tracking through emergency declarations weakens NEPA review and tribal-consultation duties. (5) Foreign-sovereign-wealth participation (MGX/UAE) creates national-security and democratic-accountability concerns over the AI infrastructure of the United States.<br><br>"
        "<b>RELATIONSHIP TO BROADER FEDERAL ENERGY POLICY.</b> Stargate operates within the Trump II energy-policy regime articulated in EO 14154 (Unleashing American Energy, tracked at eo-14154) and Secretary's Order 3418 (tracked at so-3418). The same regime drives the Chaco mineral-withdrawal revocation (tracked at blm-chaco-withdrawal-revocation-2026) and the broader BLM public-lands rule rescission (tracked at v2025-doi-003). Stargate is the demand-side justification for the supply-side energy and lands actions tracked elsewhere in the tracker.<br><br>"
        "<b>RELATIONSHIP TO INTERNATIONAL AI POLITICS.</b> MGX participation, the May 2025 Trump-Altman Gulf trip and the resulting Abu Dhabi OpenAI deal, and the OpenAI-for-Countries program form an integrated U.S.-Gulf-AI-infrastructure axis whose international and domestic faces are interconnected. Karen Hao's reporting establishes the framing.<br><br>"
        "<b>CULTURAL RESOURCE THREAT ASSESSMENT.</b> The threat level is SEVERE. Stargate is the upstream-policy artifact that authorizes the downstream environmental, water, energy, and Indigenous-consultation harms documented at xAI Memphis, Meta Los Lunas, and other AI-infrastructure sites. The Trump-promised emergency-declaration mechanism for fast-tracking federal permitting weakens the federal-statutory framework (NEPA, NHPA, Clean Air Act, Clean Water Act, Endangered Species Act) under which TCKC primary cultural communities have historically secured legal protections for cultural resources."
        "<br><br>"
        "<b>SOURCES.</b><br>"
        "Primary corporate announcement: OpenAI, \"Announcing The Stargate Project,\" January 21, 2025. <a href=\"https://openai.com/index/announcing-the-stargate-project/\">https://openai.com/index/announcing-the-stargate-project/</a><br>"
        "Primary White House remarks (covered): CNN Business, \"Stargate: Trump announces a $500 billion AI infrastructure investment in the US,\" January 21, 2025. <a href=\"https://www.cnn.com/2025/01/21/tech/openai-oracle-softbank-trump-ai-investment/index.html\">https://www.cnn.com/2025/01/21/tech/openai-oracle-softbank-trump-ai-investment/index.html</a>; "
        "CBS News, \"Trump announces up to $500 billion in private sector AI infrastructure investment.\" <a href=\"https://www.cbsnews.com/news/trump-announces-private-sector-ai-infrastructure-investment/\">https://www.cbsnews.com/news/trump-announces-private-sector-ai-infrastructure-investment/</a>; "
        "CBS News, \"What is Stargate, Trump's ambitious AI infrastructure venture?\" <a href=\"https://www.cbsnews.com/news/trump-stargate-ai-openai-softbank-oracle-musk/\">https://www.cbsnews.com/news/trump-stargate-ai-openai-softbank-oracle-musk/</a>; "
        "CNBC, \"Trump announces AI infrastructure investment backed by Oracle, OpenAI and SoftBank.\" <a href=\"https://www.cnbc.com/2025/01/21/trump-ai-openai-oracle-softbank.html\">https://www.cnbc.com/2025/01/21/trump-ai-openai-oracle-softbank.html</a>; "
        "Time Magazine, \"What to Know About 'Stargate,' OpenAI's New Venture Announced by Trump.\" <a href=\"https://time.com/7209167/stargate-openai-donald-trump/\">https://time.com/7209167/stargate-openai-donald-trump/</a>; "
        "Built In, \"What Is the Stargate Project?\" <a href=\"https://builtin.com/articles/stargate-project\">https://builtin.com/articles/stargate-project</a><br>"
        "Expansion announcement: OpenAI and SoftBank, \"OpenAI, Oracle, and SoftBank expand Stargate with five new AI data center sites,\" September 24, 2025. <a href=\"https://openai.com/index/five-new-stargate-sites/\">https://openai.com/index/five-new-stargate-sites/</a>; "
        "SoftBank Group press release: <a href=\"https://group.softbank/en/news/press/20250924\">https://group.softbank/en/news/press/20250924</a><br>"
        "Joint-venture corporate reference: Wikipedia, \"Stargate LLC.\" <a href=\"https://en.wikipedia.org/wiki/Stargate_LLC\">https://en.wikipedia.org/wiki/Stargate_LLC</a><br>"
        "Karen Hao analysis: Democracy Now!, May 2025. <a href=\"https://www.youtube.com/watch?v=s4hZz9Vd0lY\">https://www.youtube.com/watch?v=s4hZz9Vd0lY</a> (Library reference: [INTERVIEW] Karen Hao on Sam Altman OpenAI and the Quasi-Religious Push for Artificial Intelligence - Democracy Now! (2025) [EN].md).<br>"
        "Related tracker entries: xai-colossus-memphis-cleanair-2026 (xAI Memphis); meta-los-lunas-greater-kudu-2024 (Meta Los Lunas); eo-14154 (EO 14154 Unleashing American Energy); so-3418 (Secretary's Order 3418); v2025-doi-003 (BLM Public Lands Rule rescission); blm-chaco-withdrawal-revocation-2026 (Chaco mineral withdrawal revocation, 2026-03-31)."
    ),
    "I": {
        "indigenous": {
            "people": "Indigenous communities adjacent to AI-data-center siting sites face land, water, and consultation harm. The Trump-promised emergency-declaration mechanism for fast-tracking federal permitting weakens NHPA sec. 106 tribal-consultation duties and NEPA tribal-impact analysis.",
            "places": "Indigenous cultural landscapes adjacent to AI-data-center siting locations face industrial encroachment.",
            "practices": "Tribal historic-preservation-officer (THPO) practice and federal-Indian-trust consultation practice are weakened by emergency-declaration permitting fast-tracks.",
            "treasures": "Cultural-resource sites within siting footprints, including unsurveyed archaeological resources, face exposure under fast-tracked permitting."
        },
        "africanDescendant": {
            "people": "African-descendant communities adjacent to AI-data-center siting sites face the same land, water, and consultation harm. The xAI Memphis case (tracked at xai-colossus-memphis-cleanair-2026) is the documented exemplar.",
            "places": "African-descendant cultural landscapes, including historic Black neighborhoods and Black-founded freedmen communities, face industrial encroachment under the same fast-tracking regime.",
            "practices": "Black community environmental-organizing practice (MCAP and allied organizations) is burdened by the need to litigate what regulatory state should have prevented.",
            "treasures": "Place-based African-descendant cultural sites, including Boxtown (Memphis) and parallel sites at Stargate node siting locations, face industrial degradation."
        },
        "latine": {
            "people": "Latiné communities adjacent to AI-data-center siting sites face water and land harm, particularly in Southwest and Mountain West sitings where Hispano land-grant communities hold senior water rights.",
            "places": "Hispano land-grant villages and Latiné agricultural communities face cumulative water stress where Stargate nodes are sited in arid regions.",
            "practices": "Acequia practice and Hispano agricultural practice depend on reliable water deliveries that hyperscale data-center draw reduces.",
            "treasures": "Hispano cultural sites and acequia-irrigated agricultural landscapes face cumulative degradation."
        },
        "asianAmerican": {
            "people": "Asian American communities, including Chinese American academic communities harmed by the China Initiative legacy and the broader U.S.-China research-talent flows that Hao documents (Library reference, *Empire of AI*, 2025), are part of the broader AI-infrastructure-policy political economy.",
            "places": "U.S. AI-research institutions and Chinese American academic networks within them face continued politicization.",
            "practices": "Cross-Pacific AI-research-talent practice has been disrupted by Trump-administration academic-targeting actions tracked elsewhere in the tracker.",
            "treasures": "U.S.-China AI-research collaboration, a long-running scientific tradition, is being damaged by the broader political economy of which Stargate is part."
        },
        "pacificIslander": {
            "people": "Pacific Islander communities, including those in Hawaii where any future Stargate Pacific node would site, face water, land, and energy harm under the same hyperscale-development pattern.",
            "places": "Pacific cultural landscapes face industrial-development encroachment under the same emergency-declaration regime.",
            "practices": "Pacific sovereignty and trust-territory consultation practices may be weakened by emergency-declaration fast-tracking.",
            "treasures": "Pacific cultural-resource sites face exposure under fast-tracked permitting if Stargate nodes site in the Pacific region."
        },
        "allCommunities": {
            "people": "All Americans share the energy-grid, water-resource, and air-quality consequences of hyperscale AI-data-center expansion. The democratic-accountability gap (Hao's horizontal-harm thesis) affects all communities.",
            "places": "U.S. landscapes affected by Stargate node siting face shared development load.",
            "practices": "Democratic-deliberation practice over technology infrastructure is weakened by fast-tracking and shell-LLC patterns.",
            "treasures": "Federal-statutory environmental and consultation regimes (NEPA, NHPA, Clean Air Act, Clean Water Act, Endangered Species Act) are themselves cultural-policy treasures whose erosion under emergency declarations harms all communities."
        }
    },
    "c": ["Indigenous", "African-descendant", "Latiné", "Asian", "Pacific Islander", "All Communities", "environmentalJustice"],
    "U": "https://openai.com/index/announcing-the-stargate-project/",
    "_source": "manual",
}


def main():
    if not DATA_PATH.exists():
        raise SystemExit(f"data.json not found at {DATA_PATH}")

    em_dash = "—"
    for label, e in [("A", ENTRY_A), ("B", ENTRY_B), ("C", ENTRY_C)]:
        if em_dash in json.dumps(e, ensure_ascii=False):
            raise SystemExit(f"ABORT: em-dash detected in entry {label} ({e['i']}).")

    shutil.copy2(DATA_PATH, BACKUP_PATH)
    print(f"Backup written: {BACKUP_PATH.name}")

    with DATA_PATH.open() as f:
        data = json.load(f)

    targets = [
        ("agency_actions", ENTRY_A),
        ("agency_actions", ENTRY_B),
        ("executive_actions", ENTRY_C),
    ]

    for cat, entry in targets:
        existing = data.get(cat, [])
        if any((e.get("id") or e.get("i")) == entry["i"] for e in existing):
            raise SystemExit(f"Entry {entry['i']} already exists in {cat}. Aborting.")

    for cat, entry in targets:
        data.setdefault(cat, []).append(entry)
        print(f"Inserted {entry['i']} into {cat}.")

    if "meta" in data and isinstance(data["meta"], dict):
        data["meta"]["lastUpdated"] = datetime.now().strftime("%Y-%m-%d")

    tmp = DATA_PATH.with_suffix(".json.tmp")
    with tmp.open("w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    tmp.replace(DATA_PATH)

    print("Done.")


if __name__ == "__main__":
    main()
