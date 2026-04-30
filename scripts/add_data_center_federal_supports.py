#!/usr/bin/env python3
"""Three atomic additions, one backup.

Entry D. EO July 23, 2025: "Accelerating Federal Permitting of Data Center
  Infrastructure." Category: executive_actions. Threat: SEVERE.

Entry E. Final 2025 List of Critical Minerals (USGS / DOI), released
  November 6, 2025, adding uranium and nine other minerals. Category:
  agency_actions. Threat: SEVERE.

Entry F. Honor the Earth's No Data Center Coalition / Krystal Two Bulls
  Indigenous-frontline testimony documenting 103-160 proposed hyperscale
  data centers on Native lands and the Tulsa, Oklahoma City, Seminole
  Nation, and Muscogee protective actions. Category: other_domestic.
  Threat: PROTECTIVE.
"""
import json
import shutil
from pathlib import Path
from datetime import datetime

DATA_PATH = Path(__file__).parent.parent / "data" / "data.json"
BACKUP_PATH = DATA_PATH.with_suffix(
    f".json.bak-{datetime.now().strftime('%Y%m%d-%H%M%S')}-pre-dc-federal-supports"
)


# =================== ENTRY D: JULY 2025 DATA-CENTER EO ===================
ENTRY_D = {
    "i": "eo-data-center-permitting-2025-07-23",
    "t": "Executive Order",
    "n": "Executive Order: Accelerating Federal Permitting of Data Center Infrastructure (July 23, 2025)",
    "T": '<span style="color: #991B1B;">Executive Order:</span> Accelerating Federal Permitting of Data Center Infrastructure. Fast-Tracks Federal Permitting, NEPA Workarounds, FAST-41 Treatment, and Federal Financial Support for AI Data Centers Above 100 MW',
    "s": "EO data-center permitting July 2025",
    "d": "2025-07-23",
    "a": "Trump II",
    "A": ["WH", "DOC", "OSTP", "DOE", "DOI", "DOD", "EPA", "FERC"],
    "S": "Active. Issued July 23, 2025. Directs federal agencies to streamline permitting reviews, provide federal financial support, and utilize federal land for the expedited development of \"Qualifying Projects\" (data centers requiring more than 100 MW of new load, supporting energy infrastructure, semiconductor facilities, and networking equipment). FAST-41 treatment authorized. NEPA \"major Federal action\" presumption removed where federal contribution is below 50 percent of project cost. DOE announced four site selections (Idaho National Laboratory, Oak Ridge Reservation, Paducah Gaseous Diffusion Plant, Savannah River Site) one day later, on July 24, 2025.",
    "L": "SEVERE",
    "D": (
        "<b>EXECUTIVE ORDER.</b> On July 23, 2025, President Trump signed an executive order titled \"Accelerating Federal Permitting of Data Center Infrastructure.\" The order directs federal agencies to streamline environmental review and permitting, to provide federal financial support, and to make federal land available for the expedited development of artificial-intelligence data center infrastructure. The order operationalizes the Stargate Project announcement of January 21, 2025 (tracked at stargate-project-trump-2025) by establishing a permanent federal-permitting and federal-financing infrastructure to support hyperscale data-center buildout.<br><br>"
        "<b>QUALIFYING PROJECTS.</b> The order defines \"Qualifying Projects\" as data centers requiring greater than 100 megawatts of new load, supporting energy-infrastructure projects related to data-center energy needs, semiconductor facilities, networking equipment, and other data-center or related infrastructure projects selected by the Secretary of Defense or the Secretary of the Interior. Federal Tribal lands are explicitly included in the federal-land utilization scope.<br><br>"
        "<b>FINANCIAL SUPPORT INITIATIVE.</b> The Secretary of Commerce, in consultation with the Director of the Office of Science and Technology Policy (OSTP) and other federal departments, is directed to launch an initiative to provide financial support for Qualifying Projects, including loans, loan guarantees, grants, tax incentives, and off-take agreements (federal commitments to purchase a guaranteed share of project output, typically used to secure private financing).<br><br>"
        "<b>FAST-41 TREATMENT.</b> Qualifying Projects are eligible for streamlined federal-permitting review under the Fixing America's Surface Transportation Act (FAST Act) Title 41 (42 U.S.C. sec. 4370m et seq.), administered by the Federal Permitting Improvement Steering Council (FPISC). FAST-41 sets binding agency-coordination timelines and is the primary vehicle through which federal-permitting timelines for major infrastructure projects can be compressed.<br><br>"
        "<b>NEPA WORKAROUND.</b> The order specifies that federal financial assistance such as loans, loan guarantees, grants, tax incentives, or similar support shall not be treated as a \"major Federal action\" under the National Environmental Policy Act (NEPA, 42 U.S.C. sec. 4321 et seq.) if the agency does not have significant control or responsibility over how the funds are used. The order presumes that the agency does not have substantial control or responsibility where the federal contribution is less than 50 percent of total project cost. This presumption forecloses Environmental Impact Statement (EIS) preparation for federally subsidized data-center construction below the 50-percent threshold and removes the principal federal-statutory mechanism through which Indigenous and environmental-justice communities have historically secured legal protections from major infrastructure decisions.<br><br>"
        "<b>DOE SITE SELECTIONS (PARALLEL ACTION).</b> One day after the executive order, on July 24, 2025, the Department of Energy announced four federal sites for public-private data-center and energy-generation development partnerships: Idaho National Laboratory (Idaho), Oak Ridge Reservation (Tennessee), Paducah Gaseous Diffusion Plant (Kentucky), and Savannah River Site (South Carolina / Georgia). All four are existing federal-energy or federal-nuclear properties with established environmental and safety remediation legacies. Site-specific solicitations were anticipated by end-2025 with selections in 2025. Site-specific federal actions at any of these four locations warrant separate tracker entries as they materialize.<br><br>"
        "<b>HYPERSCALE-INDUSTRY DEMAND DRIVERS.</b> Hyperscale data-center demand is driven by the AI training and inference compute requirements of OpenAI, Microsoft, Google, Meta, Amazon, xAI, and Oracle. Karen Hao's reporting (Library reference, *Empire of AI*, 2025) and her May 2025 Democracy Now! interview document the corporate political-economic pressure underlying the executive-order action. Krystal Two Bulls's April 2026 Democracy Now! testimony (Library reference, [INTERVIEW] Krystal Two Bulls (Honor the Earth) on Data Colonialism and the No Data Center Coalition - Democracy Now! (2026)) documents the Indigenous-frontline impact of the buildout.<br><br>"
        "<b>RELATIONSHIP TO INDIGENOUS-LAND DATA-CENTER SITING.</b> Honor the Earth tracks 103 to 160 proposed hyperscale data centers on or near Native lands. The July 23, 2025 executive order's federal-permitting fast-tracking, federal-financing supports, and NEPA major-federal-action workaround together remove principal legal-statutory friction points that Indigenous nations have historically used to secure protective consultation and EIS-derived modifications of major-infrastructure projects. The order is the principal upstream federal-policy driver of the data-center-on-Indigenous-land harm pattern documented at honor-the-earth-no-data-center-coalition-2026.<br><br>"
        "<b>RELATIONSHIP TO ENERGY POLICY.</b> The order operates within the Trump II energy-policy regime articulated in EO 14154 (Unleashing American Energy, tracked at eo-14154) and Secretary's Order 3418 (tracked at so-3418). Hyperscale data-center demand drives the parallel federal actions on uranium critical-minerals listing (tracked at usgs-critical-minerals-list-2025), nuclear-power revival, coal-leasing expansion (tracked at coal-leasing-13m-acres), and Chaco-region oil-and-gas leasing (tracked at blm-chaco-withdrawal-revocation-2026).<br><br>"
        "<b>CULTURAL RESOURCE THREAT ASSESSMENT.</b> The threat level is SEVERE. The order is the principal federal-permitting and federal-financing instrument that authorizes hyperscale data-center buildout at the scale Stargate announced. The NEPA major-Federal-action workaround alone is sufficient to qualify the order as SEVERE under the cultural-continuity rubric, because it removes the principal federal-statutory framework through which Indigenous and environmental-justice communities have secured legal protections for cultural resources since 1969. Combined with FAST-41 streamlining and the federal-financial-support initiative, the order produces a permitting and financing regime that materially reshapes the federal-cultural-resource-protection landscape across all five TCKC primary cultural communities."
        "<br><br>"
        "<b>SOURCES.</b><br>"
        "Primary White House materials: \"Accelerating Federal Permitting of Data Center Infrastructure,\" presidential action of July 23, 2025. <a href=\"https://www.whitehouse.gov/presidential-actions/2025/07/accelerating-federal-permitting-of-data-center-infrastructure/\">https://www.whitehouse.gov/presidential-actions/2025/07/accelerating-federal-permitting-of-data-center-infrastructure/</a>; "
        "White House Fact Sheet: \"President Donald J. Trump Accelerates Federal Permitting of Data Center Infrastructure.\" <a href=\"https://www.whitehouse.gov/fact-sheets/2025/07/fact-sheet-president-donald-j-trump-accelerates-federal-permitting-of-data-center-infrastructure/\">https://www.whitehouse.gov/fact-sheets/2025/07/fact-sheet-president-donald-j-trump-accelerates-federal-permitting-of-data-center-infrastructure/</a><br>"
        "Primary CRS analysis: Congressional Research Service, R48762, \"Data Center Energy Infrastructure: Federal Permit Requirements.\" <a href=\"https://www.congress.gov/crs-product/R48762\">https://www.congress.gov/crs-product/R48762</a><br>"
        "Legal analysis: White and Case LLP, \"Trump administration issues executive order to streamline data center development.\" <a href=\"https://www.whitecase.com/insight-alert/trump-administration-issues-executive-order-streamline-data-center-development\">https://www.whitecase.com/insight-alert/trump-administration-issues-executive-order-streamline-data-center-development</a>; "
        "Cox Castle, \"New Executive Order Promotes Development of Data Centers Supporting AI.\" <a href=\"https://www.coxcastle.com/publication-new-executive-order-promotes-development-of-data-centers-supporting-ai\">https://www.coxcastle.com/publication-new-executive-order-promotes-development-of-data-centers-supporting-ai</a>; "
        "Hunton, \"President Trump Announces AI Action Plan and Accelerated Permitting and Financing for Data Centers.\" <a href=\"https://www.hunton.com/the-nickel-report/president-trump-announces-ai-action-plan-and-accelerated-permitting-and-financing-for-datacenters\">https://www.hunton.com/the-nickel-report/president-trump-announces-ai-action-plan-and-accelerated-permitting-and-financing-for-datacenters</a>; "
        "Mayer Brown, \"Federal Action to Fuel Data Center Boom,\" August 2025. <a href=\"https://www.mayerbrown.com/en/insights/publications/2025/08/federal-action-to-fuel-data-center-boom\">https://www.mayerbrown.com/en/insights/publications/2025/08/federal-action-to-fuel-data-center-boom</a><br>"
        "Bipartisan Policy Center, \"Strategic Federal Actions Aim to Strengthen AI and Energy Infrastructure.\" <a href=\"https://bipartisanpolicy.org/explainer/strategic-federal-actions-aim-to-strengthen-ai-and-energy-infrastructure/\">https://bipartisanpolicy.org/explainer/strategic-federal-actions-aim-to-strengthen-ai-and-energy-infrastructure/</a><br>"
        "Industry coverage: Data Center Dynamics, \"Trump signs EO for data center Federal permitting and tax incentives.\" <a href=\"https://www.datacenterdynamics.com/en/news/trump-signs-eo-for-data-center-federal-permitting-and-tax-incentives/\">https://www.datacenterdynamics.com/en/news/trump-signs-eo-for-data-center-federal-permitting-and-tax-incentives/</a>; "
        "SLR Consulting, \"New US federal action will drive data center development.\" <a href=\"https://www.slrconsulting.com/us/insights/federal-action-data-center-development/\">https://www.slrconsulting.com/us/insights/federal-action-data-center-development/</a><br>"
        "Library reference: [INTERVIEW] Krystal Two Bulls (Honor the Earth) on Data Colonialism and the No Data Center Coalition - Democracy Now! (2026) [EN].md; [INTERVIEW] Karen Hao on Sam Altman OpenAI and the Quasi-Religious Push for Artificial Intelligence - Democracy Now! (2025) [EN].md.<br>"
        "Related tracker entries: stargate-project-trump-2025 (Stargate Project, 2025-01-21); usgs-critical-minerals-list-2025 (Final 2025 Critical Minerals List, 2025-11-06); honor-the-earth-no-data-center-coalition-2026 (Honor the Earth coalition, 2026-04-22); xai-colossus-memphis-cleanair-2026 (xAI Memphis); meta-los-lunas-greater-kudu-2024 (Meta Los Lunas); eo-14154 (EO 14154 Unleashing American Energy); so-3418 (Secretary's Order 3418); blm-chaco-withdrawal-revocation-2026 (Chaco mineral withdrawal revocation); coal-leasing-13m-acres (13.1M acres opened to coal mining)."
    ),
    "I": {
        "indigenous": {
            "people": "Indigenous nations face the principal cumulative-impact harm. Federal-permitting fast-tracking, FAST-41 treatment, and the NEPA major-federal-action workaround together remove the legal mechanisms through which tribes have historically secured consultation, EIS modifications, and protective settlements on major infrastructure projects.",
            "places": "Tribal lands and federal lands proximate to tribal cultural-resource interests are explicitly within the executive order's federal-land-utilization scope. Indigenous cultural landscapes face industrial encroachment under fast-tracked permitting.",
            "practices": "Tribal historic-preservation-officer (THPO) practice, federal-Indian-trust consultation practice, and tribal-government deliberation practice are weakened by FAST-41 timelines and NEPA workarounds.",
            "treasures": "Cultural-resource sites within Qualifying Project siting footprints face exposure under fast-tracked permitting. NHPA sec. 106 consultation duties remain technically intact but are practically constrained by FAST-41 binding timelines."
        },
        "africanDescendant": {
            "people": "African-descendant communities face the same fast-tracked-permitting harm vector as documented at xAI Memphis (tracked at xai-colossus-memphis-cleanair-2026). The NEPA workaround removes the principal federal-statutory mechanism through which Black communities have secured environmental-justice protections.",
            "places": "Historically Black neighborhoods, freedmen-founded communities, and Mississippi Delta communities face industrial encroachment.",
            "practices": "Black community environmental-organizing practice (MCAP and allied organizations) is burdened by reduced federal-statutory leverage.",
            "treasures": "Place-based African-descendant cultural sites face industrial degradation."
        },
        "latine": {
            "people": "Latiné communities face cumulative harm where Qualifying Projects site in arid-region locations with senior Hispano water rights or Indigenous-Latiné cultural landscapes.",
            "places": "Hispano land-grant villages and Latiné agricultural communities face cumulative water and land stress.",
            "practices": "Acequia practice and Hispano agricultural practice depend on water deliveries that hyperscale draw reduces.",
            "treasures": "Hispano cultural sites face cumulative degradation."
        },
        "allCommunities": {
            "people": "All Americans share the federal-permitting and environmental-review architecture that the order weakens. The NEPA workaround narrows public-participation rights across the entire federal-permitting regime, not only for data centers.",
            "places": "U.S. landscapes affected by Qualifying Project siting face shared development load.",
            "practices": "Federal-permitting and environmental-review practice as instruments of democratic accountability are weakened.",
            "treasures": "The federal-statutory environmental and consultation regimes (NEPA, NHPA, Clean Air Act, Clean Water Act, Endangered Species Act) are themselves cultural-policy treasures whose erosion under the order harms all communities."
        },
        "environmentalJustice": {
            "people": "Environmental-justice communities lose the principal federal-statutory leverage through which they have historically secured modifications of major infrastructure projects.",
            "places": "Environmental-justice neighborhoods face accelerated industrial siting under reduced procedural protection.",
            "practices": "Environmental-justice organizing practice loses the NEPA-EIS leverage point.",
            "treasures": "The federal Environmental Justice mandate, articulated under EO 12898 (1994) and subsequent orders, is functionally weakened by the major-Federal-action workaround."
        }
    },
    "c": ["Indigenous", "African-descendant", "Latiné", "All Communities", "environmentalJustice"],
    "U": "https://www.whitehouse.gov/presidential-actions/2025/07/accelerating-federal-permitting-of-data-center-infrastructure/",
    "_source": "manual",
}


# =================== ENTRY E: 2025 CRITICAL MINERALS LIST ===================
ENTRY_E = {
    "i": "usgs-critical-minerals-list-2025",
    "t": "Final Rule",
    "n": "USGS / Department of the Interior: Final 2025 List of Critical Minerals (60 minerals; 10 added including uranium, copper, silver, lead, silicon, metallurgical coal, phosphate, potash, boron, and rhenium)",
    "T": '<span style="color: #991B1B;">USGS / DOI Final 2025 Critical Minerals List:</span> Adds Uranium, Copper, Silver, Lead, Silicon, Metallurgical Coal, Phosphate, Potash, Boron, and Rhenium to Federal Critical-Minerals Designation; Drives Mining on Indigenous Lands',
    "s": "USGS Critical Minerals List 2025",
    "d": "2025-11-06",
    "a": "Trump II",
    "A": ["DOI", "USGS", "DOE"],
    "S": "Active. Final 2025 List of Critical Minerals released November 6, 2025 by the Department of the Interior through the United States Geological Survey. The final list contains 60 minerals. Ten minerals were added compared to the 2022 list: boron, copper, lead, metallurgical coal, phosphate, potash, rhenium, silicon, silver, and uranium. Federal Register publication: 90 FR (2025-19813), November 7, 2025. The listing was directed by EO 14154 (Unleashing American Energy, January 20, 2025) and supports federal incentives for domestic mining, including on Indigenous lands.",
    "L": "SEVERE",
    "D": (
        "<b>FINAL LIST.</b> On November 6, 2025, the Department of the Interior, through the United States Geological Survey, released the Final 2025 List of Critical Minerals. The list contains 60 minerals deemed essential to U.S. economic and national security. Federal Register publication is 90 FR (2025-19813), November 7, 2025. The list adds 10 minerals compared to the 2022 list: boron, copper, lead, metallurgical coal, phosphate, potash, rhenium, silicon, silver, and uranium. Critical-mineral status triggers federal incentives, fast-tracked permitting, Defense Production Act invocations, federal procurement preferences, and federal financial support across multiple statutory regimes for domestic mining and processing.<br><br>"
        "<b>URANIUM RE-ADDED.</b> Uranium was on the 2018 Critical Minerals List but had been removed from the 2022 list. EO 14154 (Unleashing American Energy, January 20, 2025) directed the Secretary of the Interior to instruct USGS to consider updating the list, including for the potential of including uranium. During the interagency review period, the Department of Energy expressed support for adding uranium to the final 2025 list. DOE cited uranium's importance for electricity generation and national security. The re-listing of uranium operationalizes the Trump II administration's nuclear-power revival, which is itself driven by hyperscale-data-center electricity demand under the Stargate Project (tracked at stargate-project-trump-2025) and the July 23, 2025 data-center-permitting executive order (tracked at eo-data-center-permitting-2025-07-23).<br><br>"
        "<b>METALLURGICAL COAL ADDED.</b> Metallurgical coal (coking coal, used in steelmaking) was added to the list. The Department of Energy cited the importance of metallurgical coal to domestic steel production and projected steel-production growth. The listing supports the Trump II administration's coal-revival posture and integrates with the BLM coal-leasing expansion of September 2025 (tracked at coal-leasing-13m-acres).<br><br>"
        "<b>INDIGENOUS-LAND MINING IMPLICATIONS.</b> Critical-minerals designation accelerates federal supports for domestic extraction. Many of the listed minerals are concentrated under Indigenous lands or under federal lands proximate to Indigenous cultural-resource interests. Uranium reserves cluster in the Four Corners region (Navajo Nation, Pueblo nations, Ute communities), in the Black Hills (Oceti Sakowin), and in the Grand Canyon and Bears Ears regions. Copper reserves cluster in the Southwest (San Carlos Apache, Tohono O'odham, and other affected tribes). Silver reserves overlap with Western tribal lands. Krystal Two Bulls's April 22, 2026 Democracy Now! testimony (tracked at honor-the-earth-no-data-center-coalition-2026) names uranium specifically as a critical-minerals-list addition that drives mining on Indigenous lands to fuel the data-center-driven nuclear revival.<br><br>"
        "<b>FEDERAL STATUTORY CASCADE.</b> Critical-mineral status triggers cascading federal supports under multiple statutes: Defense Production Act (DPA, 50 U.S.C. sec. 4501 et seq.) Title III invocations for federal financial support of mining and processing; the Bipartisan Infrastructure Law's critical-mineral grant programs (Pub. L. 117-58); FAST-41 streamlined permitting for critical-mineral projects; federal procurement preferences; and DOE Loan Programs Office support. The cumulative effect is to convert the listing into a federal subsidy and fast-tracking package for domestic mining.<br><br>"
        "<b>RELATIONSHIP TO BROADER PATTERN.</b> The 2025 Critical Minerals List is one component of a coordinated Trump II Interior strategy connecting hyperscale-data-center demand to mining and energy expansion on Indigenous lands. Stargate (tracked at stargate-project-trump-2025) is the demand-side announcement. The July 23, 2025 EO (tracked at eo-data-center-permitting-2025-07-23) is the permitting and financing instrument. The Critical Minerals List is the materials-supply policy. EO 14154 (tracked at eo-14154) and Secretary's Order 3418 (tracked at so-3418) are the upstream energy-policy authorities. The Chaco mineral-withdrawal revocation (tracked at blm-chaco-withdrawal-revocation-2026) and the BLM coal-leasing expansion (tracked at coal-leasing-13m-acres) are downstream lands-and-leasing actions.<br><br>"
        "<b>CULTURAL RESOURCE THREAT ASSESSMENT.</b> The threat level is SEVERE. Critical-minerals designation operates as a federal-policy multiplier on mining proposals affecting Indigenous lands. The uranium addition specifically drives expanded mining in regions with documented historical-uranium-mining harm to Indigenous communities (Navajo Nation Cold War-era uranium contamination; Black Hills uranium controversies; Grand Canyon uranium proposals). The metallurgical-coal addition compounds the BLM coal-leasing expansion. The cumulative pattern is the accelerated extraction of materials from Indigenous and rural lands to fuel the AI-data-center buildout on those same lands."
        "<br><br>"
        "<b>SOURCES.</b><br>"
        "Primary federal action: USGS, \"Interior Department releases final 2025 List of Critical Minerals,\" November 6, 2025. <a href=\"https://www.usgs.gov/news/science-snippet/interior-department-releases-final-2025-list-critical-minerals\">https://www.usgs.gov/news/science-snippet/interior-department-releases-final-2025-list-critical-minerals</a>; "
        "DOI press release: <a href=\"https://www.doi.gov/pressreleases/interior-department-releases-final-2025-list-critical-minerals\">https://www.doi.gov/pressreleases/interior-department-releases-final-2025-list-critical-minerals</a>; "
        "Federal Register: \"Final 2025 List of Critical Minerals,\" 90 FR (2025-19813), November 7, 2025. <a href=\"https://www.federalregister.gov/documents/2025/11/07/2025-19813/final-2025-list-of-critical-minerals\">https://www.federalregister.gov/documents/2025/11/07/2025-19813/final-2025-list-of-critical-minerals</a>; "
        "USGS About the 2025 List: <a href=\"https://www.usgs.gov/programs/mineral-resources-program/science/about-2025-list-critical-minerals\">https://www.usgs.gov/programs/mineral-resources-program/science/about-2025-list-critical-minerals</a><br>"
        "Draft list (August 2025): Federal Register, \"2025 Draft List of Critical Minerals,\" August 26, 2025. <a href=\"https://www.federalregister.gov/documents/2025/08/26/2025-16311/2025-draft-list-of-critical-minerals\">https://www.federalregister.gov/documents/2025/08/26/2025-16311/2025-draft-list-of-critical-minerals</a>; "
        "DOI draft list press release: <a href=\"https://www.doi.gov/pressreleases/department-interior-releases-draft-2025-list-critical-minerals\">https://www.doi.gov/pressreleases/department-interior-releases-draft-2025-list-critical-minerals</a>; "
        "USGS draft list news: <a href=\"https://www.usgs.gov/news/science-snippet/department-interior-releases-draft-2025-list-critical-minerals\">https://www.usgs.gov/news/science-snippet/department-interior-releases-draft-2025-list-critical-minerals</a><br>"
        "Congressional analysis: Congressional Research Service, R47982, \"Critical Mineral Resources: National Policy and Critical Minerals List.\" <a href=\"https://www.congress.gov/crs-product/R47982\">https://www.congress.gov/crs-product/R47982</a><br>"
        "Industry analysis: Brownstein Hyatt Farber Schreck, \"Critical Update! USGS Expands Mineral List.\" <a href=\"https://www.bhfs.com/insight/critical-update-usgs-expands-mineral-list/\">https://www.bhfs.com/insight/critical-update-usgs-expands-mineral-list/</a>; "
        "Society for Mining, Metallurgy and Exploration, \"Ten minerals added to the 2025 Critical Minerals list.\" <a href=\"https://me.smenet.org/ten-minerals-added-to-the-2025-critical-minerals-list/\">https://me.smenet.org/ten-minerals-added-to-the-2025-critical-minerals-list/</a><br>"
        "Library reference: [INTERVIEW] Krystal Two Bulls (Honor the Earth) on Data Colonialism and the No Data Center Coalition - Democracy Now! (2026) [EN].md.<br>"
        "Related tracker entries: stargate-project-trump-2025 (Stargate Project, 2025-01-21); eo-data-center-permitting-2025-07-23 (EO Accelerating Federal Permitting of Data Center Infrastructure); honor-the-earth-no-data-center-coalition-2026 (Honor the Earth coalition); eo-14154 (EO 14154 Unleashing American Energy); so-3418 (Secretary's Order 3418); blm-chaco-withdrawal-revocation-2026 (Chaco mineral withdrawal revocation); coal-leasing-13m-acres (13.1M acres opened to coal mining)."
    ),
    "I": {
        "indigenous": {
            "people": "Indigenous nations face the principal cumulative harm. Uranium reserves cluster in regions with established Indigenous-uranium-harm histories (Navajo Nation Cold War-era uranium-mining contamination; Black Hills, Oceti Sakowin uranium controversies; Grand Canyon, Havasupai uranium proposals; Bears Ears region). Copper reserves cluster in the Southwest (San Carlos Apache Oak Flat litigation; Tohono O'odham). Silver reserves overlap with Western tribal lands.",
            "places": "Indigenous cultural landscapes face accelerated mineral-extraction encroachment. Uranium-mining sites adjacent to Navajo Nation, Pueblo lands, and Ute lands face renewed development pressure. Sacred sites in the Black Hills, Bears Ears, Grand Canyon, and Oak Flat face renewed mineral-extraction proposals.",
            "practices": "Tribal historic-preservation-officer (THPO) practice, NHPA sec. 106 consultation, and tribal-environmental-monitoring practice are burdened by accelerated permitting under critical-minerals-driven Defense Production Act and FAST-41 invocations.",
            "treasures": "Sacred lands, cultural-heritage sites, and ancestral remains within mining-project footprints face exposure. Historical uranium-contamination remediation obligations on the Navajo Nation are unresolved as new uranium mining is incentivized."
        },
        "africanDescendant": {
            "people": "African-descendant communities adjacent to critical-mineral mining and processing sites face cumulative environmental-justice harm. Phosphate mining in the southeastern U.S., for example, has historical environmental-justice impacts on Black communities.",
            "places": "African-descendant communities downstream and downwind of critical-mineral processing facilities face cumulative-impact harm.",
            "practices": "Black-community environmental-organizing practice loses procedural leverage under accelerated permitting.",
            "treasures": "African-descendant cultural sites adjacent to mining operations face cumulative degradation."
        },
        "latine": {
            "people": "Latiné communities, including Hispano communities in the Southwest and Latin American immigrant communities employed in mining and processing operations, face cumulative environmental and labor harm.",
            "places": "Hispano land-grant villages adjacent to copper-mining operations face cumulative water and air harm.",
            "practices": "Acequia practice and Hispano agricultural practice face cumulative water-quality risk from upstream mining.",
            "treasures": "Hispano cultural sites and acequia-irrigated agricultural landscapes face cumulative degradation."
        },
        "allCommunities": {
            "people": "All Americans share the federal critical-minerals industrial-policy regime that the listing operationalizes. Workers in critical-minerals mining and processing face occupational-health risk.",
            "places": "U.S. landscapes affected by mining-project siting face shared development load.",
            "practices": "Federal-permitting and environmental-review practice are weakened by Defense-Production-Act fast-tracking.",
            "treasures": "Federal-statutory environmental and consultation regimes are functionally weakened."
        }
    },
    "c": ["Indigenous", "African-descendant", "Latiné", "All Communities", "environmentalJustice"],
    "U": "https://www.federalregister.gov/documents/2025/11/07/2025-19813/final-2025-list-of-critical-minerals",
    "_source": "manual",
}


# =================== ENTRY F: HONOR THE EARTH NO DATA CENTER COALITION ===================
ENTRY_F = {
    "i": "honor-the-earth-no-data-center-coalition-2026",
    "t": "Indigenous Civil-Society Advisory Report",
    "n": "Honor the Earth's No Data Center Coalition: 103-160 Hyperscale Data Centers Proposed on Native Lands; Krystal Two Bulls Democracy Now! Earth Day 2026 Testimony",
    "T": '<span style="color: #065F46;">Honor the Earth, No Data Center Coalition:</span> Krystal Two Bulls Documents 103 to 160 Hyperscale Data Centers Proposed on Native Lands and the Tulsa, Oklahoma City, Seminole Nation, and Muscogee Protective Actions',
    "s": "Honor the Earth No Data Center Coalition",
    "d": "2026-04-22",
    "a": "Trump II",
    "A": ["BIA", "DOI", "DOE", "EPA"],
    "S": "Active. Honor the Earth (Indigenous-led environmental-justice nonprofit, founded 1993) launched the No Data Center Coalition in 2025. Executive Director Krystal Two Bulls (Oglala Lakota and Northern Cheyenne) testified on Democracy Now! Earth Day broadcast, April 22, 2026. The coalition tracks 103 to 160 proposed hyperscale data centers on Native lands or within 30 miles of Native lands through a crowdsource map. Documented protective wins: Tulsa City Council 9-month moratorium, Oklahoma City moratorium through 2027, Seminole Nation unanimous moratorium, Muscogee Nation blocked resolution.",
    "L": "PROTECTIVE",
    "D": (
        "<b>ORGANIZATION AND TESTIMONY.</b> Honor the Earth is an Indigenous-led environmental-justice nonprofit founded in 1993. In 2025 it launched the No Data Center Coalition. Executive Director Krystal Two Bulls (Oglala Lakota and Northern Cheyenne, longtime Standing Rock #NoDAPL organizer) gave the principal public testimony on the coalition's work in a Democracy Now! Earth Day 2026 broadcast on April 22, 2026, joining from the Northern Cheyenne Reservation in southeastern Montana. Two Bulls's testimony establishes the principal Indigenous-frontline framing of the AI-data-center buildout as \"data colonialism\" and as a continuation of settler-colonial land grabs.<br><br>"
        "<b>SCALE OF THE PATTERN.</b> The coalition's crowdsource map tracks 103 to 160 proposed hyperscale data centers on Native lands or within 30 miles of Native lands. Operators identified by Two Bulls: Microsoft, Google, Apple, Meta, Amazon. Approach pattern: subsidiary entities (e.g., Greater Kudu LLC for Meta, tracked at meta-los-lunas-greater-kudu-2024); Native-owned energy-company partners; non-disclosure agreements (NDAs) presented to tribal leadership before constituent deliberation; \"solar panels\" framing pivoting to hyperscale data center.<br><br>"
        "<b>QUANTIFIED HARMS DOCUMENTED.</b> Two Bulls's testimony documents specific quantified harms from existing hyperscale data centers. (1) Water draw of 300,000 to 2,700,000 gallons per facility per year, with reports up to 5,000,000 gallons per year; corporate \"closed-loop\" and \"water-positive\" claims have been dispelled by reporting on existing facilities. (2) Noise of approximately 97 decibels at hyperscale facilities (compared with 140 dB LRAD eardrum-rupture threshold), producing long-term hearing loss risk. (3) Heat-island effect of up to 16 degrees Fahrenheit on adjacent land, compounding ecosystem stress and water-temperature increases sufficient to drive ecological collapse. (4) Documented cancers and respiratory illnesses tied to existing facilities. (5) Bloomberg analysis: electricity costs rise nearly 267 percent near data centers. (6) Montana residential rate inflation: bills \"almost doubled\"; documented case of $900 monthly bill for a single resident in a trailer home in a non-extreme winter. (7) Job-promise versus job-reality: ~1,500 construction-phase jobs (often awarded to specialized non-local contractors) collapsing to as few as 3 full-time operations jobs (documented case at Rapid City, South Dakota).<br><br>"
        "<b>FEDERAL DRIVERS.</b> Two Bulls explicitly names two federal-action drivers in her testimony. First, the recent re-addition of uranium to the federal Critical Minerals List (tracked at usgs-critical-minerals-list-2025), which accelerates uranium mining on Indigenous lands to fuel the data-center-driven nuclear revival. Second, the federal nuclear-power revival itself, paired with coal-industry revitalization and frac-gas expansion as bridge fuels until nuclear comes online. The federal data-center permitting executive order of July 23, 2025 (tracked at eo-data-center-permitting-2025-07-23) and the Stargate Project (tracked at stargate-project-trump-2025) are the upstream federal-policy authorizations.<br><br>"
        "<b>STRUCTURAL FACTORS Two Bulls IDENTIFIES.</b> Two Bulls names five structural factors that make Indigenous lands particularly conducive to hyperscale data-center siting: (1) large land bases on land-based tribal nations; (2) water access; (3) tax incentives; (4) lack of legal infrastructure to hold corporations accountable; (5) jurisdictional complexity on Indigenous lands; and (6) extreme-poverty conditions making job-promise narratives appealing.<br><br>"
        "<b>PROTECTIVE WINS.</b> The coalition has supported and contributed to multiple protective actions. (1) Tulsa City Council 9-month moratorium on data-center development. (2) Oklahoma City moratorium banning data-center development through 2027. (3) Seminole Nation unanimous moratorium. (4) Muscogee Nation blocked a resolution that would have advanced a hyperscale data center. Two Bulls characterizes Oklahoma as the strategic test case because it is \"the crossroads of every extractive industry in the United States.\"<br><br>"
        "<b>MOVEMENT-BUILDING GENEALOGY.</b> Two Bulls draws an explicit line from Standing Rock / Dakota Access Pipeline to data colonialism. The #NoDAPL coalition's multinational-Indigenous-solidarity composition (Latin American, U.S., Canadian Indigenous nations and non-Native allies) is reproduced in the No Data Center Coalition's organizing approach. The Honor the Earth tactical playbook (town halls, tribal-council meetings, door-knocking, petitions, agriculture and rancher coalitions, local-government engagement) is documented in her testimony.<br><br>"
        "<b>RELATIONSHIP TO TRACKER PATTERN.</b> Two Bulls's testimony documents the Indigenous-frontline manifestation of the federal AI-data-center industrial policy package: Stargate Project demand-side announcement (tracked at stargate-project-trump-2025), the July 23, 2025 federal data-center permitting EO (tracked at eo-data-center-permitting-2025-07-23), the Critical Minerals List uranium re-listing (tracked at usgs-critical-minerals-list-2025), and the energy-policy upstream authorities (eo-14154, so-3418). The coalition's protective work is the most consequential Indigenous-led counter-organizing in the AI infrastructure space.<br><br>"
        "<b>CULTURAL RESOURCE THREAT ASSESSMENT.</b> The threat level is PROTECTIVE. The Honor the Earth No Data Center Coalition is the principal Indigenous-led civil-society response to the federal data-center industrial-policy package. Its protective wins (Tulsa, Oklahoma City, Seminole Nation, Muscogee) demonstrate that local and tribal-government action can interrupt the federal-corporate buildout pattern at the siting level. The coalition's crowdsource map and documentation infrastructure are themselves cultural-policy treasures whose preservation supports Indigenous environmental-justice organizing nationally."
        "<br><br>"
        "<b>SOURCES.</b><br>"
        "Primary testimony: Democracy Now!, \"'Data Colonialism': Native Communities Fight AI Data Centers on Indigenous Land,\" April 22, 2026. <a href=\"https://www.democracynow.org/2026/4/22/krystal_twobulls_indigenous_lands_data_centers\">https://www.democracynow.org/2026/4/22/krystal_twobulls_indigenous_lands_data_centers</a><br>"
        "Honor the Earth campaign overview: <a href=\"https://www.honorearth.org/stopdatacolonialism\">https://www.honorearth.org/stopdatacolonialism</a><br>"
        "Coverage and analysis: Truthout, \"Indigenous Activists Decry 'Data Colonialism' of AI Boom in Their Communities.\" <a href=\"https://truthout.org/video/indigenous-activists-decry-data-colonialism-of-ai-boom-in-their-communities/\">https://truthout.org/video/indigenous-activists-decry-data-colonialism-of-ai-boom-in-their-communities/</a>; "
        "ICT News, \"In Indian Country, data centers come with a familiar threat of colonialism. These organizers are fighting back.\" <a href=\"https://ictnews.org/news/in-indian-country-data-centers-come-with-a-familiar-threat-of-colonialism-these-organizers-are-fighting-back/\">https://ictnews.org/news/in-indian-country-data-centers-come-with-a-familiar-threat-of-colonialism-these-organizers-are-fighting-back/</a>; "
        "Futurism, \"Tech Companies Are Using Insidious Tactics to Build Data Centers on Indigenous Lands, Activists Say.\" <a href=\"https://futurism.com/artificial-intelligence/data-centers-tribal-communities\">https://futurism.com/artificial-intelligence/data-centers-tribal-communities</a>; "
        "NationofChange, \"'Data Colonialism': Native communities fight AI data centers on indigenous land.\" <a href=\"https://www.nationofchange.org/2026/04/23/data-colonialism-native-communities-fight-ai-data-centers-on-indigenous-land/\">https://www.nationofchange.org/2026/04/23/data-colonialism-native-communities-fight-ai-data-centers-on-indigenous-land/</a>; "
        "Let's Data Science, \"Indigenous Groups Resist Data Centers on Tribal Lands.\" <a href=\"https://letsdatascience.com/news/indigenous-groups-resist-data-centers-on-tribal-lands-fdd4a331\">https://letsdatascience.com/news/indigenous-groups-resist-data-centers-on-tribal-lands-fdd4a331</a>; "
        "Newsbytes, \"Seminole Nation bans data centers while tech seeks Indigenous lands.\" <a href=\"https://www.newsbytesapp.com/news/science/seminole-nation-bans-data-centers-while-tech-seeks-indigenous-lands/tldr\">https://www.newsbytesapp.com/news/science/seminole-nation-bans-data-centers-while-tech-seeks-indigenous-lands/tldr</a><br>"
        "Library reference: [INTERVIEW] Krystal Two Bulls (Honor the Earth) on Data Colonialism and the No Data Center Coalition - Democracy Now! (2026) [EN].md.<br>"
        "Related tracker entries: stargate-project-trump-2025 (Stargate Project, 2025-01-21); eo-data-center-permitting-2025-07-23 (EO Accelerating Federal Permitting of Data Center Infrastructure, 2025-07-23); usgs-critical-minerals-list-2025 (Final 2025 Critical Minerals List, 2025-11-06); xai-colossus-memphis-cleanair-2026 (xAI Memphis, 2026-04-01); meta-los-lunas-greater-kudu-2024 (Meta Los Lunas, 2024-12); blm-chaco-withdrawal-revocation-2026 (Chaco mineral withdrawal revocation, 2026-03-31); v2026-indigenous-cultural-threat-analysis (Indigenous aggregate analysis); DOI-2020-001 (Standing Rock Sioux Tribe v. U.S. Army Corps of Engineers, DAPL)."
    ),
    "I": {
        "indigenous": {
            "people": "All Indigenous nations facing proposed hyperscale data-center siting on or near tribal lands benefit from the coalition's documentation and organizing infrastructure. Indigenous tribal-government leadership benefits from independent technical analysis on water draw, noise, heat-island effects, electricity-rate inflation, and job-promise reality, free from corporate-NDA constraints.",
            "places": "103 to 160 proposed sites are documented through the coalition's crowdsource map. The protective wins at Seminole Nation, Muscogee Nation, Tulsa, and Oklahoma City represent place-based victories.",
            "practices": "The coalition's tactical playbook (town halls, door-knocking, tribal-council engagement, agriculture-and-rancher coalition-building) extends Indigenous environmental-justice organizing practice from the Standing Rock #NoDAPL era into the AI-infrastructure era.",
            "treasures": "The crowdsource-map documentation infrastructure is itself an Indigenous-led cultural-policy treasure that supports tribal-government decision-making and intertribal coordination."
        },
        "allCommunities": {
            "people": "All communities benefit from the coalition's documentation of hyperscale-data-center harm patterns. Rural communities adjacent to Indigenous lands benefit from coalition organizing.",
            "places": "Local-government and tribal-government protective actions in Tulsa, Oklahoma City, Seminole Nation, and Muscogee Nation establish replicable models.",
            "practices": "Civil-society-led federal-action documentation practice is strengthened by the coalition's transparency work against corporate NDAs.",
            "treasures": "The independent civil-society-led tracking infrastructure is itself a democratic-accountability treasure."
        },
        "environmentalJustice": {
            "people": "Environmental-justice communities benefit from the coalition's documentation of cumulative harm patterns and from its replication of the Standing Rock #NoDAPL solidarity model.",
            "places": "Environmental-justice neighborhoods proximate to data-center proposals receive coalition organizing support.",
            "practices": "Environmental-justice organizing practice is strengthened by the coalition's tactical playbook.",
            "treasures": "Environmental-justice movement institutional knowledge is preserved and extended through the coalition's work."
        }
    },
    "c": ["Indigenous", "All Communities", "environmentalJustice"],
    "U": "https://www.democracynow.org/2026/4/22/krystal_twobulls_indigenous_lands_data_centers",
    "_source": "manual",
}


def main():
    if not DATA_PATH.exists():
        raise SystemExit(f"data.json not found at {DATA_PATH}")

    em_dash = "—"
    for label, e in [("D", ENTRY_D), ("E", ENTRY_E), ("F", ENTRY_F)]:
        if em_dash in json.dumps(e, ensure_ascii=False):
            raise SystemExit(f"ABORT: em-dash detected in entry {label} ({e['i']}).")

    shutil.copy2(DATA_PATH, BACKUP_PATH)
    print(f"Backup written: {BACKUP_PATH.name}")

    with DATA_PATH.open() as f:
        data = json.load(f)

    targets = [
        ("executive_actions", ENTRY_D),
        ("agency_actions", ENTRY_E),
        ("other_domestic", ENTRY_F),
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
