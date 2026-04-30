#!/usr/bin/env python3
"""Four atomic additions, one backup.

E. OpenAI for Countries program (Stargate-affiliated international AI
   infrastructure deployment). Category: international. Threat: HARMFUL.

F. EO 14300, "Ordering the Reform of the Nuclear Regulatory Commission"
   (signed May 23, 2025; Federal Register 2025-09798, May 29, 2025).
   Category: executive_actions. Threat: SEVERE.

G. Sam Altman Senate testimony on AI energy (natural gas, advanced
   nuclear including SMR fission and fusion). Industry-pressure
   advisory entry. Category: other_domestic. Threat: HARMFUL.

H. EO "Accelerating Medical Treatments for Serious Mental Illness"
   (April 2026), and FDA implementing actions. Category:
   executive_actions. Threat: HARMFUL.
"""
import json
import shutil
from pathlib import Path
from datetime import datetime

DATA_PATH = Path(__file__).parent.parent / "data" / "data.json"
BACKUP_PATH = DATA_PATH.with_suffix(
    f".json.bak-{datetime.now().strftime('%Y%m%d-%H%M%S')}-pre-round3-fda"
)


# =================== ENTRY E: OPENAI FOR COUNTRIES ===================
ENTRY_E = {
    "i": "openai-for-countries-2025",
    "t": "Corporate Program with Federal Coordination",
    "n": "OpenAI for Countries: Stargate-Affiliated International AI Infrastructure Deployment Program (Announced May 2025; First Phase 10 Country Partnerships)",
    "T": '<span style="color: #CA8A04;">OpenAI for Countries:</span> Stargate-Affiliated International AI Infrastructure Deployment Program. First Phase Targets 10 Country Partnerships; Frames Itself as "Democratic AI Rails" Against China',
    "s": "OpenAI for Countries program",
    "d": "2025-05-07",
    "a": "Trump II",
    "A": ["State", "Commerce", "OSTP"],
    "S": "Active. Announced by OpenAI on or about May 7, 2025 as the international expansion arm of the Stargate Project (tracked at stargate-project-trump-2025). First-phase target: 10 country or regional partnerships. Components: in-country data-center capacity, customized ChatGPT for citizens, sovereign-data partner agreements. Explicitly framed as building \"democratic AI rails\" against \"authoritarian\" Chinese AI. OpenAI's policy posture explicitly identifies partnership with the U.S. government as central to the program. Federal coordination through State Department, Commerce Department, and OSTP.",
    "L": "HARMFUL",
    "D": (
        "<b>PROGRAM AND FRAMING.</b> OpenAI announced the OpenAI for Countries program on or about May 7, 2025, presenting it as an international expansion arm of the Stargate Project (tracked at stargate-project-trump-2025). OpenAI characterizes the program as supporting countries that prefer to build on \"democratic AI rails\" and as a \"clear alternative to authoritarian versions of AI.\" The geopolitical framing positions the program against Chinese AI infrastructure expansion, particularly against China's Belt and Road and Global Development Initiative AI components.<br><br>"
        "<b>PROGRAM COMPONENTS.</b> The program offers partner countries: (1) in-country data-center capacity \"with secure data centers to help support the sovereignty of a country's data\"; (2) customized ChatGPT instances localized in language and culture to support healthcare, education, and public services; and (3) U.S.-led-stack export coordination through what OpenAI describes as a \"consortium model.\"<br><br>"
        "<b>FEDERAL-COORDINATION POSTURE.</b> OpenAI's stated policy posture explicitly identifies federal partnership as central. OpenAI has articulated three export-policy pillars: (1) partnering with the U.S. government to advance democratic standards; (2) incentivizing democratic AI and strengthening critical supply chains; and (3) using a consortium model to build a U.S.-led global AI stack. The federal coordination operates through State Department diplomatic channels, Commerce Department export-control framing, and OSTP AI policy coordination. The Trump-Altman May 2025 Gulf trip (Karen Hao Democracy Now! interview, May 2025; Library reference [INTERVIEW] Karen Hao on Sam Altman OpenAI ... Democracy Now! (2025) [EN].md) was the principal early presidential-administration facilitation of the program.<br><br>"
        "<b>FIRST-PHASE TARGET AND ABU DHABI ANCHOR.</b> OpenAI's first-phase target is 10 country or regional partnerships. The May 2025 Gulf trip yielded the Abu Dhabi anchor agreement, which Karen Hao characterized in her Democracy Now! testimony as the principal U.S.-Gulf AI-infrastructure deal of the period. MGX (Mubadala-affiliated UAE sovereign-wealth fund) is also the UAE Stargate partner, integrating the OpenAI-for-Countries deployment in Abu Dhabi with the Stargate domestic buildout.<br><br>"
        "<b>CRITIQUE FRAMING.</b> Karen Hao characterizes the program's \"democratic AI\" rhetoric as a self-authorizing claim disconnected from democratic deliberation. The Atlantic executive editor's framing, quoted by Hao, describes the major U.S. AI labs as \"techno-authoritarians.\" The democratic-deliberation gap operates on three dimensions: (1) recipient-country populations have limited mechanisms to consent to data-center siting, water and energy draw, and data-sovereignty terms; (2) source-country (U.S.) populations have limited mechanisms to scrutinize the bilateral deals struck through the program; (3) the program's claim to advance \"democratic AI\" is asserted by corporate fiat without democratic input.<br><br>"
        "<b>DIASPORA-COMMUNITY IMPLICATIONS.</b> The OpenAI for Countries program operates in regions with deep diaspora ties to all five TCKC primary cultural communities. African-descendant diaspora ties run through sub-Saharan Africa and the Caribbean. Latiné diaspora ties run through Latin America. Asian diaspora ties run through South, Southeast, and East Asia. Pacific Islander diaspora ties run through the Pacific. Indigenous diaspora ties run through Latin American Indigenous communities and other regions. The program's data-center siting, water and energy draw, and data-sovereignty terms shape the political economies of communities to which U.S.-based TCKC primary cultural communities are kin.<br><br>"
        "<b>CULTURAL RESOURCE THREAT ASSESSMENT.</b> The threat level is HARMFUL. The program is structurally ambiguous: it deploys U.S. corporate AI infrastructure abroad with U.S. federal coordination but does not itself constitute a discrete federal regulatory or financial action. The harm operates through three mechanisms. First, water and energy draw at scale in partner-country regions affects local communities and diaspora-kin populations. Second, data-sovereignty terms negotiated under U.S. corporate frameworks may foreclose Indigenous and minoritized-community data-governance protections that recipient countries might otherwise develop. Third, the geopolitical framing as \"democratic AI rails\" against \"authoritarian\" Chinese AI accelerates U.S.-China bipolar AI competition that constrains all third-party countries' policy autonomy."
        "<br><br>"
        "<b>SOURCES.</b><br>"
        "Primary corporate announcement: OpenAI, \"Introducing OpenAI for Countries.\" <a href=\"https://openai.com/global-affairs/openai-for-countries/\">https://openai.com/global-affairs/openai-for-countries/</a><br>"
        "Related corporate program: OpenAI, \"Introducing OpenAI for Government.\" <a href=\"https://openai.com/global-affairs/introducing-openai-for-government/\">https://openai.com/global-affairs/introducing-openai-for-government/</a><br>"
        "OpenAI policy posture: OpenAI, \"Ideas to Power Democratic AI,\" June 2025 (PDF). <a href=\"https://cdn.openai.com/global-affairs/9c98a71f-7d2f-4566-9da7-4a7628c60bea/oai-ideas-to-power-democratic-ai-june-2025.pdf\">https://cdn.openai.com/global-affairs/9c98a71f-7d2f-4566-9da7-4a7628c60bea/oai-ideas-to-power-democratic-ai-june-2025.pdf</a>; "
        "OpenAI Response to OSTP/NSF RFI on AI Action Plan (PDF). <a href=\"https://cdn.openai.com/global-affairs/ostp-rfi/ec680b75-d539-4653-b297-8bcf6e5f7686/openai-response-ostp-nsf-rfi-notice-request-for-information-on-the-development-of-an-artificial-intelligence-ai-action-plan.pdf\">https://cdn.openai.com/global-affairs/ostp-rfi/ec680b75-d539-4653-b297-8bcf6e5f7686/openai-response-ostp-nsf-rfi-notice-request-for-information-on-the-development-of-an-artificial-intelligence-ai-action-plan.pdf</a><br>"
        "Coverage: TechCrunch, \"OpenAI wants to team up with governments to grow AI infrastructure,\" May 7, 2025. <a href=\"https://techcrunch.com/2025/05/07/openai-wants-to-team-up-with-governments-to-grow-ai-infrastructure/\">https://techcrunch.com/2025/05/07/openai-wants-to-team-up-with-governments-to-grow-ai-infrastructure/</a>; "
        "Axios, \"OpenAI for Countries aims to build global AI infrastructure and beat China,\" May 7, 2025. <a href=\"https://www.axios.com/2025/05/07/openai-democratic-ai-expansion\">https://www.axios.com/2025/05/07/openai-democratic-ai-expansion</a>; "
        "Computerworld, \"OpenAI offers help promoting AI outside the US, but analysts question why countries would accept.\" <a href=\"https://www.computerworld.com/article/3980440/openai-offers-help-promoting-ai-outside-the-us-but-analysts-question-why-countries-would-accept.html\">https://www.computerworld.com/article/3980440/openai-offers-help-promoting-ai-outside-the-us-but-analysts-question-why-countries-would-accept.html</a>; "
        "Time, \"Inside OpenAI's Plan to Make AI More 'Democratic'.\" <a href=\"https://time.com/6684266/openai-democracy-artificial-intelligence/\">https://time.com/6684266/openai-democracy-artificial-intelligence/</a>; "
        "Nextgov/FCW, \"Industry calls for US leadership in AI as a democratic imperative,\" December 2025. <a href=\"https://www.nextgov.com/artificial-intelligence/2025/12/industry-calls-us-leadership-ai-democratic-imperative/410185/\">https://www.nextgov.com/artificial-intelligence/2025/12/industry-calls-us-leadership-ai-democratic-imperative/410185/</a><br>"
        "Library reference: [INTERVIEW] Karen Hao on Sam Altman OpenAI and the Quasi-Religious Push for Artificial Intelligence - Democracy Now! (2025) [EN].md.<br>"
        "Related tracker entries: stargate-project-trump-2025 (Stargate Project, 2025-01-21); eo-data-center-permitting-2025-07-23 (EO Accelerating Federal Permitting of Data Center Infrastructure, 2025-07-23); honor-the-earth-no-data-center-coalition-2026 (Honor the Earth coalition, 2026-04-22); altman-senate-testimony-ai-energy-2025 (Altman Senate testimony on AI energy)."
    ),
    "I": {
        "africanDescendant": {
            "people": "African-descendant diaspora communities in sub-Saharan Africa and the Caribbean face data-center water and energy draw at scale where partner-country deployments occur. U.S.-based African-descendant communities have direct kinship ties.",
            "places": "Partner-country data-center sites in Africa face industrial encroachment.",
            "practices": "African data-governance practice loses autonomy where OpenAI-for-Countries terms supplant locally-developed protections.",
            "treasures": "African Indigenous and community data-governance traditions face displacement by U.S. corporate frameworks."
        },
        "latine": {
            "people": "Latiné diaspora communities in Latin America face the same harm vector. U.S.-based Latiné communities have direct kinship ties.",
            "places": "Latin American partner-country sites face industrial encroachment.",
            "practices": "Latin American data-governance and digital-sovereignty practice is constrained.",
            "treasures": "Latin American digital-sovereignty traditions face displacement."
        },
        "asianAmerican": {
            "people": "Asian diaspora communities in South, Southeast, and East Asia face the same harm vector.",
            "places": "Asian partner-country sites face industrial encroachment.",
            "practices": "Asian data-governance practice is constrained.",
            "treasures": "Asian digital-sovereignty traditions face displacement."
        },
        "pacificIslander": {
            "people": "Pacific Islander populations face the same harm vector where Pacific deployments occur.",
            "places": "Pacific partner-country sites face industrial encroachment.",
            "practices": "Pacific data-governance practice is constrained.",
            "treasures": "Pacific digital-sovereignty traditions face displacement."
        },
        "indigenous": {
            "people": "Indigenous communities globally, including in Latin American partner countries, face the same harm vector.",
            "places": "Indigenous lands within partner-country deployment sites face industrial encroachment.",
            "practices": "Indigenous data-governance practice (CARE Principles for Indigenous Data Governance and parallel frameworks) is constrained.",
            "treasures": "Indigenous data-sovereignty traditions face displacement."
        },
        "allCommunities": {
            "people": "All recipient-country populations face the program's data-sovereignty and infrastructure terms. U.S. populations face the federal-policy-coordination consequences.",
            "places": "Partner-country deployment sites face shared development load.",
            "practices": "Democratic-deliberation practice over AI infrastructure is foreclosed by corporate-led international deployment.",
            "treasures": "Multilateral AI-governance frameworks (OECD AI Principles, UNESCO AI Recommendation) are weakened by bilateral OpenAI-led deployments."
        }
    },
    "c": ["African-descendant", "Latiné", "Asian", "Pacific Islander", "Indigenous", "All Communities"],
    "U": "https://openai.com/global-affairs/openai-for-countries/",
    "_source": "manual",
}


# =================== ENTRY F: EO 14300 NRC REFORM ===================
ENTRY_F = {
    "i": "eo-14300-nrc-reform-2025",
    "t": "Executive Order",
    "n": "Executive Order 14300: Ordering the Reform of the Nuclear Regulatory Commission (Signed May 23, 2025; Federal Register 2025-09798, May 29, 2025)",
    "T": '<span style="color: #991B1B;">EO 14300:</span> Ordering the Reform of the Nuclear Regulatory Commission. Imposes 18-Month Licensing Deadlines, NRC-DOGE Reorganization, Targets Quadrupling U.S. Nuclear Capacity to 400 GW by 2050',
    "s": "EO 14300 NRC reform",
    "d": "2025-05-23",
    "a": "Trump II",
    "A": ["NRC", "DOE", "DOGE"],
    "S": "Active. Signed May 23, 2025. Federal Register publication 2025-09798, May 29, 2025. Directs NRC to issue final rules and guidance within 18 months (by November 2026). Imposes binding 18-month deadline for final decisions on new-reactor license applications and 1-year deadline for license-extension decisions. Directs NRC reorganization in consultation with NRC's DOGE Team (per EO 14158). Targets quadrupling U.S. nuclear capacity to 400 GW by 2050. One of four nuclear-energy executive orders signed the same day, and the principal deregulatory instrument among them.",
    "L": "SEVERE",
    "D": (
        "<b>EXECUTIVE ORDER.</b> On May 23, 2025, President Trump signed Executive Order 14300, \"Ordering the Reform of the Nuclear Regulatory Commission.\" The order was published in the Federal Register on May 29, 2025 (FR 2025-09798). It is one of four nuclear-energy executive orders signed the same day; among them, EO 14300 is the principal deregulatory instrument restructuring the NRC's licensing posture and operational authority. The order operationalizes the AI-data-center demand-side pressure articulated by Sam Altman's May 8, 2025 Senate testimony (tracked at altman-senate-testimony-ai-energy-2025) and authorizes the regulatory rollbacks Karen Hao describes in her May 2025 Democracy Now! interview as nuclear deregulation lobbying.<br><br>"
        "<b>LICENSING-TIMELINE MANDATES.</b> The order imposes binding NRC-decision timelines: (1) no more than 18 months for final decision on an application to construct and operate a new reactor of any type, commencing with the first required step in the regulatory process; and (2) no more than 1 year for final decision on an application to continue operating an existing reactor of any type. The historical NRC licensing timeline for new construction-and-operating licenses has been substantially longer (often 4-6 years or more for first-of-a-kind designs), with iterative agency review designed to surface and address safety concerns. The compression to 18 months operates as a de facto presumption against extended-review safety processes.<br><br>"
        "<b>NRC REORGANIZATION VIA DOGE.</b> The order directs the NRC to reorganize \"in consultation with the NRC's DOGE Team\" as defined in EO 14158 (Establishing and Implementing the President's \"Department of Government Efficiency,\" January 20, 2025). The DOGE-mediated NRC restructuring is the principal mechanism through which historical NRC institutional capacity for safety review is reduced.<br><br>"
        "<b>WHOLESALE REGULATIONS REVIEW.</b> The order directs the NRC, in consultation with other executive departments, to undertake a review of NRC regulations and guidance documents and to issue final rules and guidance within 18 months. The NRC's published \"Wholesale Revision of Regulations Under Executive Order 14300\" page documents the agency's implementation. Final rules and guidance are due by November 2026.<br><br>"
        "<b>400-GW TARGET.</b> The order sets a target of quadrupling U.S. nuclear energy capacity to a total of 400 gigawatts (GW) by 2050. U.S. nuclear capacity in 2024 was approximately 95 GW. Quadrupling capacity by 2050 implies approximately 305 GW of new nuclear construction in 25 years, which is unprecedented at U.S. national scale and would require both small modular reactor (SMR) and large-scale-reactor deployment.<br><br>"
        "<b>AI-DATA-CENTER DEMAND DRIVER.</b> The order's implementation aligns with hyperscale-data-center electricity demand. The pipeline of conditional offtake agreements between data-center operators and SMR projects grew from 25 GW at end-2024 to 45 GW in 2025. AWS-Talen Energy June 2025 power purchase agreement (1.92 GW from Susquehanna nuclear plant; AWS plans to explore building new SMRs at Talen sites; AWS investing $20 billion in Pennsylvania) is one prominent operating-reactor example. DOE's July 24, 2025 site selections (Idaho National Laboratory, Oak Ridge Reservation, Paducah Gaseous Diffusion Plant, Savannah River Site) explicitly contemplate AI-data-center co-location at federal nuclear sites.<br><br>"
        "<b>NRC FINAL RULE OF MARCH 25, 2026.</b> On March 25, 2026, the NRC approved a final rule establishing a new risk-informed, performance-based, and technology-inclusive regulatory framework for licensing commercial nuclear plants, available for any reactor technology, size, and end use, including high-temperature gas-cooled reactors, liquid metal reactors, molten salt reactors, small modular reactors, microreactors, and innovative LWR designs. This is a principal implementation step under EO 14300.<br><br>"
        "<b>RELATIONSHIP TO ADVANCE ACT 2024.</b> The Accelerating Deployment of Versatile, Advanced Nuclear for Clean Energy Act of 2024 (ADVANCE Act, Pub. L. 118-67) had directed the NRC to improve efficiency in licensing review, establish an expedited process for new-reactor license applications, and advance regulatory strategies for microreactors. EO 14300 operates within and accelerates the ADVANCE Act framework. The ADVANCE Act explicitly required NRC to regulate \"in a manner that does not unnecessarily limit nuclear deployment,\" altering the NRC's historical safety-only mission to include facilitation of deployment.<br><br>"
        "<b>INDIGENOUS-LAND IMPLICATIONS.</b> Uranium fuel for the 305 GW of projected new nuclear capacity will accelerate uranium mining on Indigenous lands (tracked at usgs-critical-minerals-list-2025 and at honor-the-earth-no-data-center-coalition-2026). New reactor siting, including SMR co-location at federal sites and at AI-data-center campuses, involves federal NHPA sec. 106 consultation duties whose practical execution is constrained by EO 14300's 18-month decision timelines.<br><br>"
        "<b>CULTURAL RESOURCE THREAT ASSESSMENT.</b> The threat level is SEVERE. EO 14300 is the principal federal-deregulatory instrument enabling the AI-driven nuclear-power expansion. The 18-month licensing timeline, NRC-DOGE reorganization, and wholesale regulations review together restructure federal nuclear-safety regulation in ways that compress safety review and shift the NRC mission from safety-and-deployment balance to deployment-with-residual-safety. The cumulative effect is to enable accelerated uranium mining on Indigenous lands, accelerated reactor siting at federal sites, and reduced NHPA tribal-consultation effectiveness."
        "<br><br>"
        "<b>SOURCES.</b><br>"
        "Primary federal action: \"Ordering the Reform of the Nuclear Regulatory Commission,\" Federal Register 2025-09798, May 29, 2025. <a href=\"https://www.federalregister.gov/documents/2025/05/29/2025-09798/ordering-the-reform-of-the-nuclear-regulatory-commission\">https://www.federalregister.gov/documents/2025/05/29/2025-09798/ordering-the-reform-of-the-nuclear-regulatory-commission</a>; "
        "White House Fact Sheet: \"President Donald J. Trump Directs Reform of the Nuclear Regulatory Commission.\" <a href=\"https://www.whitehouse.gov/fact-sheets/2025/05/fact-sheet-president-donald-j-trump-directs-reform-of-the-nuclear-regulatory-commission/\">https://www.whitehouse.gov/fact-sheets/2025/05/fact-sheet-president-donald-j-trump-directs-reform-of-the-nuclear-regulatory-commission/</a><br>"
        "NRC implementation: NRC, \"Wholesale Revision of Regulations Under Executive Order 14300.\" <a href=\"https://www.nrc.gov/about-nrc/governing-laws/advance-act/wholesale-revision-regs\">https://www.nrc.gov/about-nrc/governing-laws/advance-act/wholesale-revision-regs</a>; "
        "NRC, \"About the ADVANCE Act.\" <a href=\"https://www.nrc.gov/about-nrc/governing-laws/advance-act/about-advance-act\">https://www.nrc.gov/about-nrc/governing-laws/advance-act/about-advance-act</a>; "
        "NRC, \"Effectiveness, Efficiency, and Timeliness Initiatives that Support Unleashing American Energy.\" <a href=\"https://www.nrc.gov/about-nrc/governing-laws/advance-act\">https://www.nrc.gov/about-nrc/governing-laws/advance-act</a><br>"
        "Government documents: Administration of Donald J. Trump, 2025, DCPD-202500633 (PDF). <a href=\"https://www.govinfo.gov/content/pkg/DCPD-202500633/pdf/DCPD-202500633.pdf\">https://www.govinfo.gov/content/pkg/DCPD-202500633/pdf/DCPD-202500633.pdf</a><br>"
        "Department of Energy summary: \"9 Key Takeaways from President Trump's Executive Orders on Nuclear Energy.\" <a href=\"https://www.energy.gov/ne/articles/9-key-takeaways-president-trumps-executive-orders-nuclear-energy\">https://www.energy.gov/ne/articles/9-key-takeaways-president-trumps-executive-orders-nuclear-energy</a><br>"
        "Critical analysis: Clean Air Task Force, \"Actions to Address Executive Order 14300: Reforming the Nuclear Regulatory Commission.\" <a href=\"https://www.catf.us/resource/actions-address-executive-order-14300-reforming-nuclear-regulatory-commission/\">https://www.catf.us/resource/actions-address-executive-order-14300-reforming-nuclear-regulatory-commission/</a><br>"
        "Legal analysis: Skadden Arps, \"Four Executive Orders Aim To Promote Nuclear Energy.\" <a href=\"https://www.skadden.com/insights/publications/2025/06/four-executive-orders-aim-to-promote-nuclear-energy\">https://www.skadden.com/insights/publications/2025/06/four-executive-orders-aim-to-promote-nuclear-energy</a>; "
        "K&L Gates, \"President Trump Issues Sweeping Executive Orders Targeting Nuclear Regulation,\" June 5, 2025. <a href=\"https://www.klgates.com/President-Trump-Issues-Sweeping-Executive-Orders-Targeting-Nuclear-Regulation-6-5-2025\">https://www.klgates.com/President-Trump-Issues-Sweeping-Executive-Orders-Targeting-Nuclear-Regulation-6-5-2025</a>; "
        "CSIS, \"White House Executive Orders Target Ambitious Nuclear Deployment in the United States and Abroad.\" <a href=\"https://www.csis.org/analysis/white-house-executive-orders-target-ambitious-nuclear-deployment-united-states-and-abroad\">https://www.csis.org/analysis/white-house-executive-orders-target-ambitious-nuclear-deployment-united-states-and-abroad</a>; "
        "Perkins Coie, \"NRC Finalizes a New Risk-Informed, Technology-Inclusive Regulatory Framework for Advanced Reactors\" (March 2026 final rule). <a href=\"https://perkinscoie.com/insights/blog/nrc-finalizes-new-risk-informed-technology-inclusive-regulatory-framework-advanced\">https://perkinscoie.com/insights/blog/nrc-finalizes-new-risk-informed-technology-inclusive-regulatory-framework-advanced</a>; "
        "Morgan Lewis, \"NRC Launches Fresh Licensing Framework for New Reactors,\" April 2026. <a href=\"https://www.morganlewis.com/pubs/2026/04/nrc-launches-fresh-licensing-framework-for-new-reactors\">https://www.morganlewis.com/pubs/2026/04/nrc-launches-fresh-licensing-framework-for-new-reactors</a><br>"
        "Industry context: Sustainable Tech Partner, \"Will Nuclear Energy Power AI Data Centers? Timeline of Developments, Proponents and Safety Discussions.\" <a href=\"https://sustainabletechpartner.com/news/will-nuclear-energy-power-ai-data-centers-timeline-of-developments-proponents-and-safety-discussions/\">https://sustainabletechpartner.com/news/will-nuclear-energy-power-ai-data-centers-timeline-of-developments-proponents-and-safety-discussions/</a>; "
        "EnkiAI, \"SMRs in 2025: Powering AI Data Centers and The Future.\" <a href=\"https://enkiai.com/data-center/smrs-in-2025-powering-ai-data-centers-the-future\">https://enkiai.com/data-center/smrs-in-2025-powering-ai-data-centers-the-future</a><br>"
        "Library reference: [INTERVIEW] Karen Hao on Sam Altman OpenAI and the Quasi-Religious Push for Artificial Intelligence - Democracy Now! (2025) [EN].md.<br>"
        "Related tracker entries: stargate-project-trump-2025 (Stargate Project, 2025-01-21); eo-data-center-permitting-2025-07-23 (EO Accelerating Federal Permitting of Data Center Infrastructure); usgs-critical-minerals-list-2025 (Final 2025 Critical Minerals List, with uranium re-listed); altman-senate-testimony-ai-energy-2025 (Altman Senate testimony on AI energy); honor-the-earth-no-data-center-coalition-2026 (Honor the Earth coalition); eo-14154 (EO 14154 Unleashing American Energy); so-3418 (Secretary's Order 3418)."
    ),
    "I": {
        "indigenous": {
            "people": "Indigenous nations face the principal cumulative-impact harm. The 18-month licensing timeline foreshortens the consultation window for new-reactor and SMR siting where reactors are co-located with AI data centers or sited adjacent to Indigenous lands. Uranium-mining acceleration on Navajo Nation, Pueblo lands, Ute lands, and other Indigenous territories follows directly from the projected 305 GW of new nuclear construction.",
            "places": "Sacred sites and cultural-heritage landscapes adjacent to existing federal nuclear sites (Idaho National Laboratory, Oak Ridge Reservation, Paducah, Savannah River) and to potential SMR co-location sites face industrial encroachment. Uranium-mining sites in the Four Corners, Black Hills, Grand Canyon, and Bears Ears regions face renewed development pressure.",
            "practices": "Tribal historic-preservation-officer (THPO) practice and NHPA sec. 106 consultation are practically constrained by 18-month NRC decision timelines. Indigenous environmental-monitoring practice is burdened.",
            "treasures": "Cultural-resource sites within new-reactor and uranium-mining footprints face exposure under fast-tracked permitting."
        },
        "africanDescendant": {
            "people": "African-descendant communities adjacent to existing federal nuclear sites (Savannah River, Oak Ridge) and to potential SMR siting locations face cumulative environmental-justice harm. The Savannah River Site is in proximity to historically Black communities in the South Carolina-Georgia region.",
            "places": "African-descendant cultural landscapes adjacent to nuclear-siting locations face industrial encroachment.",
            "practices": "Black-community environmental-organizing practice loses procedural leverage under foreshortened NRC review.",
            "treasures": "Place-based African-descendant cultural sites face industrial degradation."
        },
        "allCommunities": {
            "people": "All Americans share the federal nuclear-safety regime that EO 14300 restructures. Nuclear-plant workers face altered occupational-safety conditions under reorganized NRC oversight. Communities downwind of nuclear sites face accelerated permitting of new-construction projects.",
            "places": "U.S. landscapes affected by 305 GW of projected new nuclear construction face shared development load.",
            "practices": "Federal nuclear-safety regulation as a deliberative-democratic practice is restructured toward deployment-facilitation.",
            "treasures": "The federal NRC institutional capacity for safety review, accumulated since 1974, is reduced through DOGE-mediated reorganization."
        },
        "environmentalJustice": {
            "people": "Environmental-justice communities adjacent to nuclear sites face accelerated siting of new reactors under foreshortened review. Communities downwind of uranium-mining operations face cumulative health harms.",
            "places": "Environmental-justice neighborhoods proximate to nuclear and uranium-mining locations face cumulative-impact burden.",
            "practices": "Environmental-justice organizing practice loses NRC-review-period leverage points.",
            "treasures": "The federal Environmental Justice mandate is functionally weakened by the 18-month decision-timeline mandate."
        }
    },
    "c": ["Indigenous", "African-descendant", "All Communities", "environmentalJustice"],
    "U": "https://www.federalregister.gov/documents/2025/05/29/2025-09798/ordering-the-reform-of-the-nuclear-regulatory-commission",
    "_source": "manual",
}


# =================== ENTRY G: ALTMAN SENATE TESTIMONY ===================
ENTRY_G = {
    "i": "altman-senate-testimony-ai-energy-2025",
    "t": "Industry Pressure Advisory",
    "n": "Sam Altman Senate Testimony on AI Energy: Natural Gas (Short Term), Solar (Selective), Advanced Nuclear Fission and Fusion (Medium Term)",
    "T": '<span style="color: #CA8A04;">Industry Pressure Advisory:</span> Sam Altman Senate Testimony Endorsing Natural Gas, Solar, Advanced Nuclear Fission and Fusion as AI Energy Solutions; Anchors Industry Lobby for NRC and Energy Deregulation',
    "s": "Altman Senate testimony AI energy",
    "d": "2025-05-08",
    "a": "Trump II",
    "A": ["Senate", "DOE", "NRC"],
    "S": "Active. Sam Altman testified before the U.S. Senate (Commerce, Science, and Transportation Committee) on or about May 8, 2025 regarding AI energy needs, endorsing natural gas in the short term, selective solar, and advanced nuclear (fission, including SMRs, and fusion) in the medium term. The testimony anchors a broader AI-industry lobbying effort that, in conjunction with EO 14300 (NRC reform, May 23, 2025) and the July 23, 2025 data-center permitting EO, has restructured federal energy and nuclear-regulatory posture toward AI-data-center demand fulfillment.",
    "L": "HARMFUL",
    "D": (
        "<b>TESTIMONY.</b> On or about May 8, 2025, OpenAI CEO Sam Altman testified before the U.S. Senate Committee on Commerce, Science, and Transportation in a hearing on artificial intelligence policy. Asked about energy solutions for AI's accelerating electricity demand, Altman gave the operative summary that this entry tracks: \"In the short term, I think this probably looks like more natural gas. Although there are some applications where I think solar can really help. In the medium term, I hope it's advanced nuclear, fission and fusion. More energy is important well beyond AI.\"<br><br>"
        "<b>FRAMING.</b> Altman's testimony positioned natural-gas-and-nuclear as the operative answer to AI's electricity demand, with solar as a partial supplement. The framing aligned with the Trump II administration's parallel push for natural-gas expansion, coal-revival posture, and accelerated nuclear deployment. Karen Hao's May 2025 Democracy Now! interview characterizes the AI-industry's nuclear lobbying as part of a coordinated effort to claim the AI development approach \"doesn't have climate harms\" by invoking nuclear as the solve.<br><br>"
        "<b>FEDERAL ACTIONS DOWNSTREAM OF THE TESTIMONY.</b> Two federal actions in the weeks following the testimony operationalized its policy framing. On May 23, 2025 the President signed EO 14300, \"Ordering the Reform of the Nuclear Regulatory Commission\" (tracked at eo-14300-nrc-reform-2025), imposing 18-month licensing deadlines and DOGE-mediated NRC reorganization. On July 23, 2025 the President signed an executive order \"Accelerating Federal Permitting of Data Center Infrastructure\" (tracked at eo-data-center-permitting-2025-07-23), which authorizes federal financial support, FAST-41 fast-tracked permitting, and a NEPA major-Federal-action workaround for data-center construction. The two orders together implement the natural-gas-and-nuclear framing Altman articulated in his testimony.<br><br>"
        "<b>NUCLEAR-LOBBY POSTURE.</b> The AI-industry nuclear-deregulation lobbying that Karen Hao describes in her May 2025 Democracy Now! interview operates through several channels: industry trade associations (Information Technology Industry Council, Software Alliance), corporate-government relations (OpenAI, Microsoft, Google, Amazon, xAI lobbying offices), nuclear-industry coalitions (Nuclear Energy Institute, Nuclear Innovation Alliance), and direct corporate offtake-agreement engagement with operating reactors and SMR developers (e.g., AWS-Talen 1.92 GW Susquehanna PPA, June 2025). The cumulative effect is documented in the 25 GW (end-2024) to 45 GW (2025) growth in conditional offtake-agreement pipeline between data-center operators and SMR projects.<br><br>"
        "<b>SOLAR-AS-SUPPLEMENT FRAMING.</b> Karen Hao notes a structural problem with the solar-as-supplement framing for hyperscale data centers: data centers must run 24/7, and current grid-scale energy-storage solutions are insufficient to support 24/7 operation on solar alone. The framing therefore functions to acknowledge solar as a partial concession to environmental constituencies while preserving natural-gas-and-nuclear as the operative answer.<br><br>"
        "<b>NATURAL-GAS-AS-BRIDGE FRAMING.</b> Altman's \"short term\" natural-gas framing operates as a bridge to nuclear deployment that may take a decade or more to materialize at scale. The bridge framing, repeated by Krystal Two Bulls in her April 2026 Democracy Now! testimony (tracked at honor-the-earth-no-data-center-coalition-2026) as part of the AI-industry pattern, has operationalized expanded frac-gas drilling and coal-mining (tracked at coal-leasing-13m-acres) on Indigenous and rural lands.<br><br>"
        "<b>RELATIONSHIP TO THE BROADER AI-INDUSTRIAL-POLICY PACKAGE.</b> Altman's testimony anchors the federal-policy framing under which Stargate (tracked at stargate-project-trump-2025) and OpenAI for Countries (tracked at openai-for-countries-2025) operate. Industry-pressure advisory entries are tracked here because they shape the federal-policy environment in which discrete federal actions are subsequently issued.<br><br>"
        "<b>CULTURAL RESOURCE THREAT ASSESSMENT.</b> The threat level is HARMFUL. Altman's testimony is not itself a federal action and therefore does not produce direct cultural-resource harm. The testimony is the documented industry-articulated framing under which several severe federal actions (EO 14300, EO Accelerating Federal Permitting of Data Centers, USGS Critical Minerals List uranium re-listing, BLM Chaco mineral-withdrawal revocation, BLM coal-leasing expansion) were subsequently issued. Tracking the testimony establishes the documentary chain of industry-pressure-to-federal-action that the cultural-resource analysis depends on."
        "<br><br>"
        "<b>SOURCES.</b><br>"
        "Primary testimony excerpts: Democracy Now!, May 2025 interview with Karen Hao (Library reference). <a href=\"https://www.youtube.com/watch?v=s4hZz9Vd0lY\">https://www.youtube.com/watch?v=s4hZz9Vd0lY</a><br>"
        "Karen Hao's broader analysis: Hao, *Empire of AI* (Penguin Press, 2025) [Library candidate].<br>"
        "Industry context (offtake-agreement pipeline growth): International Energy Agency, \"Data centre electricity use surged in 2025, even with tightening bottlenecks driving a scramble for solutions.\" <a href=\"https://www.iea.org/news/data-centre-electricity-use-surged-in-2025-even-with-tightening-bottlenecks-driving-a-scramble-for-solutions\">https://www.iea.org/news/data-centre-electricity-use-surged-in-2025-even-with-tightening-bottlenecks-driving-a-scramble-for-solutions</a>; "
        "International Atomic Energy Agency, \"Data Centres, Artificial Intelligence and Cryptocurrencies Eye Advanced Nuclear to Meet Growing Power Needs.\" <a href=\"https://www.iaea.org/bulletin/data-centres-artificial-intelligence-and-cryptocurrencies-eye-advanced-nuclear-to-meet-growing-power-needs\">https://www.iaea.org/bulletin/data-centres-artificial-intelligence-and-cryptocurrencies-eye-advanced-nuclear-to-meet-growing-power-needs</a>; "
        "EnkiAI, \"SMRs in 2025: Powering AI Data Centers and The Future.\" <a href=\"https://enkiai.com/data-center/smrs-in-2025-powering-ai-data-centers-the-future\">https://enkiai.com/data-center/smrs-in-2025-powering-ai-data-centers-the-future</a>; "
        "Carbon Credits, \"2026: The Year Nuclear Power Reclaims Relevance With 15 Reactors, AI Demand, and China's Expansion.\" <a href=\"https://carboncredits.com/2026-the-year-nuclear-power-reclaims-relevance-with-15-reactors-ai-demand-and-chinas-expansion/\">https://carboncredits.com/2026-the-year-nuclear-power-reclaims-relevance-with-15-reactors-ai-demand-and-chinas-expansion/</a>; "
        "Introl, \"SMRs Power AI: $10B Nuclear Data Center Revolution.\" <a href=\"https://introl.com/blog/smr-nuclear-power-ai-data-centers-2025\">https://introl.com/blog/smr-nuclear-power-ai-data-centers-2025</a>; "
        "Shumaker, Loop & Kendrick, \"Nuclear Powered Artificial Intelligence (AI): Small Modular Reactors as an Emerging Power Source for AI Data Centers.\" <a href=\"https://www.shumaker.com/insight/nuclear-powered-artificial-intelligence-ai-small-modular-reactors-as-an-emerging-power-source-for-ai-data-centers/\">https://www.shumaker.com/insight/nuclear-powered-artificial-intelligence-ai-small-modular-reactors-as-an-emerging-power-source-for-ai-data-centers/</a>; "
        "Commonfund, \"AI Data Center and AI Power Demand: Will Nuclear Be the Answer?\" <a href=\"https://www.commonfund.org/cf-private-equity/data-center-and-ai-power-demand-will-nuclear-be-the-answer\">https://www.commonfund.org/cf-private-equity/data-center-and-ai-power-demand-will-nuclear-be-the-answer</a><br>"
        "Library references: [INTERVIEW] Karen Hao on Sam Altman OpenAI and the Quasi-Religious Push for Artificial Intelligence - Democracy Now! (2025) [EN].md; [INTERVIEW] Krystal Two Bulls (Honor the Earth) on Data Colonialism and the No Data Center Coalition - Democracy Now! (2026) [EN].md.<br>"
        "Related tracker entries: stargate-project-trump-2025 (Stargate Project); eo-14300-nrc-reform-2025 (EO 14300 NRC Reform); eo-data-center-permitting-2025-07-23 (EO Accelerating Federal Permitting of Data Center Infrastructure); usgs-critical-minerals-list-2025 (Critical Minerals List with uranium); honor-the-earth-no-data-center-coalition-2026 (Honor the Earth coalition); coal-leasing-13m-acres (BLM coal-leasing expansion); openai-for-countries-2025 (OpenAI for Countries); blm-chaco-withdrawal-revocation-2026 (Chaco mineral-withdrawal revocation)."
    ),
    "I": {
        "indigenous": {
            "people": "Indigenous communities bear the cumulative downstream cost of the natural-gas-and-nuclear framing Altman articulated. Frac-gas-on-Indigenous-lands, uranium-mining-on-Indigenous-lands, and SMR-co-location-near-Indigenous-cultural-sites all flow from this framing.",
            "places": "Indigenous cultural landscapes face cumulative encroachment under the nuclear-and-gas buildout the testimony anchored.",
            "practices": "Tribal-government deliberation practice and federal-Indian-trust consultation practice face cumulative pressure under foreshortened federal-action timelines.",
            "treasures": "Indigenous cultural-resource sites face cumulative exposure."
        },
        "africanDescendant": {
            "people": "African-descendant communities adjacent to natural-gas processing, nuclear sites, and AI-data-center sites face cumulative harm.",
            "places": "African-descendant cultural landscapes face cumulative encroachment.",
            "practices": "Black-community environmental-organizing practice faces cumulative procedural disadvantage.",
            "treasures": "African-descendant cultural sites face cumulative degradation."
        },
        "allCommunities": {
            "people": "All Americans share the federal energy-and-environmental-policy framing that Altman articulated and that the May-July 2025 federal actions implemented.",
            "places": "U.S. landscapes face cumulative AI-energy-buildout load.",
            "practices": "Federal energy-and-environmental policymaking practice is shaped by industry-pressure framing.",
            "treasures": "Federal-statutory environmental and consultation regimes face cumulative pressure."
        },
        "environmentalJustice": {
            "people": "Environmental-justice communities bear cumulative harm at every node of the natural-gas-and-nuclear buildout that the testimony anchored.",
            "places": "Environmental-justice neighborhoods face cumulative-impact harm.",
            "practices": "Environmental-justice organizing practice faces cumulative procedural disadvantage.",
            "treasures": "Federal Environmental Justice mandate faces cumulative pressure."
        }
    },
    "c": ["Indigenous", "African-descendant", "All Communities", "environmentalJustice"],
    "U": "https://www.youtube.com/watch?v=s4hZz9Vd0lY",
    "_source": "manual",
}


# =================== ENTRY H: FDA / EO MENTAL ILLNESS ===================
ENTRY_H = {
    "i": "eo-mental-illness-fda-acceleration-2026",
    "t": "Executive Order with FDA Implementation",
    "n": "Executive Order: Accelerating Medical Treatments for Serious Mental Illness (April 2026), and FDA Implementation Including National Priority Vouchers for Psychedelic Drugs",
    "T": '<span style="color: #CA8A04;">EO Accelerating Medical Treatments for Serious Mental Illness:</span> Directs FDA Commissioner National Priority Vouchers for Psychedelic Drugs (Including Ibogaine), HHS-VA Coordination on Psychedelic Trials, and Attorney General Reviews for DEA Rescheduling',
    "s": "EO Mental Illness FDA Acceleration",
    "d": "2026-04-22",
    "a": "Trump II",
    "A": ["WH", "HHS", "FDA", "VA", "DOJ", "DEA"],
    "S": "Active. Executive Order \"Accelerating Medical Treatments for Serious Mental Illness\" signed April 2026. FDA implementing announcement followed via FDA press release (https://www.fda.gov/news-events/press-announcements/fda-accelerates-action-treatments-serious-mental-illness-following-executive-order; the press release URL was 404 at time of tracker entry but the announcement is documented through HHS, GlobeNewswire, and other federal-information mirrors). HHS Secretary Robert F. Kennedy Jr. is the named principal HHS official. The order directs FDA Commissioner's National Priority Vouchers for psychedelic drugs with Breakthrough Therapy designation, HHS-VA coordination on psychedelic clinical trials and real-world evidence, and Attorney General reviews for post-FDA-approval DEA rescheduling.",
    "L": "HARMFUL",
    "D": (
        "<b>EXECUTIVE ORDER.</b> In April 2026, President Trump signed an executive order titled \"Accelerating Medical Treatments for Serious Mental Illness.\" The order directs federal action to accelerate research, FDA approval, and regulated access to mental-health treatments framed as targeting \"devastating, complex, and treatment-resistant\" conditions. The principal accelerated drug class is psychedelic compounds, including ibogaine, named in HHS-Secretary Robert F. Kennedy Jr.'s implementing statement.<br><br>"
        "<b>FDA IMPLEMENTATION.</b> The FDA followed the executive order with an implementing announcement, \"FDA Accelerates Action on Treatments for Serious Mental Illness Following Executive Order.\" The press release URL on the FDA website (https://www.fda.gov/news-events/press-announcements/fda-accelerates-action-treatments-serious-mental-illness-following-executive-order) returned a 404 error at the time of this tracker entry. The implementing announcement is preserved through HHS, GlobeNewswire, and the Health.gov mirror. The implementing actions include: (1) Commissioner's National Priority Vouchers for appropriate psychedelic drugs that have received Breakthrough Therapy designations; (2) HHS-FDA collaboration with the Department of Veterans Affairs to increase clinical-trial participation, data sharing, and real-world evidence generation regarding psychedelic drugs; and (3) Attorney General reviews of relevant products upon successful completion of Phase 3 clinical trials, with DEA rescheduling targeted as soon as possible upon FDA approval.<br><br>"
        "<b>VETERANS-FOCUSED FRAMING.</b> The order's public framing centers veterans as the principal beneficiary population. HHS Secretary Kennedy stated that the order accelerates \"research, approval, and responsible access to promising mental health treatments, including psychedelic therapies like ibogaine, to confront our nation's mental health crisis head-on, especially for our veterans.\" The veterans framing creates a politically protective rhetorical envelope around what is also a substantial Indigenous-cultural and historically minoritized-community concern.<br><br>"
        "<b>INDIGENOUS-CEREMONIAL-MEDICINE TENSIONS.</b> Several psychedelic compounds federally regulated under Schedule I have established Indigenous-ceremonial uses protected under various federal frameworks. Peyote (mescaline) ceremonial use is protected for federally recognized Native American Church members under the American Indian Religious Freedom Act Amendments of 1994 (42 U.S.C. sec. 1996a) and BIA peyote regulations. Ayahuasca ceremonial use was protected for the Uniao do Vegetal in Gonzales v. UDV, 546 U.S. 418 (2006). Ibogaine has documented Indigenous ceremonial use in the Bwiti tradition of Gabon. The federalization of these compounds through FDA approval and DEA rescheduling pathways creates a tension between expanded clinical access (potentially beneficial for treatment-resistant patients) and federalization of compounds with Indigenous-ceremonial provenance. Indigenous-led and reparative pathways for psychedelic-medicine policy have been articulated by organizations including the Chacruna Institute and the North Star Project. The FDA-and-DEA-led pathway under this executive order does not, on the available record, integrate Indigenous-ceremonial-medicine reparative principles.<br><br>"
        "<b>HISTORICAL COERCIVE-PSYCHIATRY CONCERN.</b> \"Serious mental illness\" framing in U.S. federal policy has historical association with coercive-psychiatry deployment, particularly toward racialized communities and unhoused populations. The Trump II administration's parallel posture on homelessness, encampments, and civil-commitment policy creates an environment in which acceleration of treatment access could intersect with coerced-treatment deployment. The cultural-resource analysis here flags structural concern; documentation of specific coercive-deployment patterns under this order requires monitoring as implementation proceeds.<br><br>"
        "<b>STRUCTURAL FEATURES THE ENTRY TRACKS.</b> (1) Commissioner's National Priority Voucher use for psychedelic drugs (an accelerated FDA review pathway with policy implications beyond psychedelics). (2) HHS-VA-FDA data-sharing arrangement that may shape veterans-population real-world-evidence generation. (3) Attorney General-led DEA rescheduling pathway that operationalizes federal Schedule reform via executive coordination. (4) HHS Secretary Kennedy's leadership of an implementation framework that intersects with separate HHS-policy controversies tracked elsewhere.<br><br>"
        "<b>RELATIONSHIP TO BROADER FEDERAL HEALTH-POLICY PATTERN.</b> The order operates within a Trump II HHS-policy environment that has included the dismantling of public-health agencies (USAID, NIH research-grant cuts, CDC restructuring) and the alteration of federal health-data infrastructure (tracked elsewhere in the tracker as relevant). Acceleration of FDA review pathways for psychedelic mental-health treatments operates in parallel with reduced federal investment in non-pharmacological mental-health infrastructure (community mental-health centers, public-hospital psychiatric capacity, harm-reduction services).<br><br>"
        "<b>CULTURAL RESOURCE THREAT ASSESSMENT.</b> The threat level is HARMFUL. The order is structurally ambiguous: accelerated FDA approval of psychedelic mental-health treatments could expand access for treatment-resistant patients, including veterans with treatment-resistant PTSD, which is a beneficial direction. The HARMFUL classification reflects three structural concerns: (1) federalization of compounds with documented Indigenous-ceremonial provenance without integration of Indigenous-led reparative pathways; (2) the historical association of \"serious mental illness\" framing with coercive-psychiatry deployment toward racialized and unhoused communities; and (3) the parallel-policy environment of reduced federal investment in non-pharmacological mental-health infrastructure. The classification will warrant re-evaluation as implementation specifics emerge."
        "<br><br>"
        "<b>SOURCES.</b><br>"
        "Primary executive order: White House, \"Accelerating Medical Treatments for Serious Mental Illness,\" April 2026. <a href=\"https://www.whitehouse.gov/presidential-actions/2026/04/accelerating-medical-treatments-for-serious-mental-illness/\">https://www.whitehouse.gov/presidential-actions/2026/04/accelerating-medical-treatments-for-serious-mental-illness/</a><br>"
        "White House Fact Sheet: \"President Donald J. Trump is Accelerating Medical Treatments for Serious Mental Illness.\" <a href=\"https://www.whitehouse.gov/fact-sheets/2026/04/fact-sheet-president-donald-j-trump-is-accelerating-medical-treatments-for-serious-mental-illness/\">https://www.whitehouse.gov/fact-sheets/2026/04/fact-sheet-president-donald-j-trump-is-accelerating-medical-treatments-for-serious-mental-illness/</a>; "
        "White House release: \"President Trump's Landmark Order Advances Breakthrough Mental Health Treatments. Delivering New Hope to Veterans.\" <a href=\"https://www.whitehouse.gov/releases/2026/04/president-trumps-landmark-order-advances-breakthrough-mental-health-treatments-delivering-new-hope-to-veterans/\">https://www.whitehouse.gov/releases/2026/04/president-trumps-landmark-order-advances-breakthrough-mental-health-treatments-delivering-new-hope-to-veterans/</a><br>"
        "FDA implementing announcement (URL returned 404 at time of tracker entry): <a href=\"https://www.fda.gov/news-events/press-announcements/fda-accelerates-action-treatments-serious-mental-illness-following-executive-order\">https://www.fda.gov/news-events/press-announcements/fda-accelerates-action-treatments-serious-mental-illness-following-executive-order</a><br>"
        "HHS mirror of FDA announcement: <a href=\"https://www.hhs.gov/press-room/fda-accelerates-action-treatments-serious-mental-illness-following-executive-order.html\">https://www.hhs.gov/press-room/fda-accelerates-action-treatments-serious-mental-illness-following-executive-order.html</a>; "
        "Health.gov mirror: <a href=\"https://health.gov/news/fda-accelerates-action-treatments-serious-mental-illness-following-executive-order-0\">https://health.gov/news/fda-accelerates-action-treatments-serious-mental-illness-following-executive-order-0</a>; "
        "GlobeNewswire: <a href=\"https://www.globenewswire.com/news-release/2026/04/24/3281062/0/en/FDA-Accelerates-Action-on-Treatments-for-Serious-Mental-Illness-Following-Executive-Order.html\">https://www.globenewswire.com/news-release/2026/04/24/3281062/0/en/FDA-Accelerates-Action-on-Treatments-for-Serious-Mental-Illness-Following-Executive-Order.html</a>; "
        "Drugs.com: <a href=\"https://www.drugs.com/news/fda-accelerates-action-treatments-serious-mental-illness-following-executive-order-129800.html\">https://www.drugs.com/news/fda-accelerates-action-treatments-serious-mental-illness-following-executive-order-129800.html</a>; "
        "Drug Topics: \"Executive Order Aims to Expand Therapies for Serious Mental Illness.\" <a href=\"https://www.drugtopics.com/view/executive-order-aims-to-expand-therapies-for-serious-mental-illness\">https://www.drugtopics.com/view/executive-order-aims-to-expand-therapies-for-serious-mental-illness</a><br>"
        "Related tracker entries: To be cross-referenced as parallel HHS and homelessness-policy entries are added (specific cross-reference IDs to be filled in upon Prince's review of the tracker for adjacent entries)."
    ),
    "I": {
        "indigenous": {
            "people": "Indigenous communities with established ceremonial uses of psychedelic compounds (Native American Church peyote, Bwiti ibogaine, Amazonian and other ayahuasca lineages) face federalization of compounds with Indigenous-ceremonial provenance under FDA-DEA review pathways that do not integrate Indigenous-led reparative principles.",
            "places": "Ceremonial-medicine practice sites face uncertain federal-policy environment as federal scheduling of psychedelic compounds shifts.",
            "practices": "Indigenous ceremonial-medicine practice operates within federal frameworks (AIRFA Amendments, Gonzales v. UDV) whose stability depends on continued federal recognition of religious-use exemptions. Federalization of psychedelic compounds through FDA-DEA pathways may reshape this environment.",
            "treasures": "Traditional ecological and pharmacological knowledge held by Indigenous communities concerning psychedelic compounds is part of the cultural heritage at issue. The order does not, on the available record, recognize this knowledge as a basis for benefit-sharing or reparative engagement."
        },
        "africanDescendant": {
            "people": "African-descendant communities, particularly Black communities historically subjected to coercive psychiatric treatment under racialized \"serious mental illness\" framings, face structural concern from the order's framing. Bwiti ceremonial use of ibogaine in West Africa is part of African-descendant heritage.",
            "places": "Black-community mental-health spaces and harm-reduction sites face altered federal-policy environment.",
            "practices": "Black-community mental-health and harm-reduction practice depends on funding environments parallel to the order's focus on FDA-approved pharmacological pathways.",
            "treasures": "Black-community mental-health institutional traditions, including peer-support and culturally-responsive-care models, face uncertain federal funding environment."
        },
        "latine": {
            "people": "Latiné communities with ceremonial-medicine traditions (Amazonian ayahuasca, Mexican-Mesoamerican psilocybin lineages) face federalization concerns parallel to Indigenous communities.",
            "places": "Latin American ceremonial-medicine sites face uncertain federal-policy environment.",
            "practices": "Latiné ceremonial-medicine practice operates within parallel federal frameworks.",
            "treasures": "Latiné ceremonial-medicine traditional knowledge faces federalization concerns."
        },
        "lgbtq": {
            "people": "LGBTQ+ veterans, who face elevated rates of treatment-resistant PTSD and depression related to military-sexual-trauma and discrimination histories, are part of the population the order frames as principal beneficiaries.",
            "places": "VA mental-health facilities face altered psychedelic-treatment policy environment.",
            "practices": "VA mental-health practice expands to incorporate psychedelic therapies under the order's HHS-VA coordination directive.",
            "treasures": "Veteran mental-health care institutional capacity expands in psychedelic-therapy directions while potentially contracting elsewhere."
        },
        "allCommunities": {
            "people": "All veterans face altered VA mental-health treatment environment. Treatment-resistant PTSD, depression, and anxiety patients face expanded psychedelic-treatment access pathways.",
            "places": "VA medical centers, FDA-approved clinical-trial sites, and post-approval clinic infrastructure face expanded psychedelic-treatment deployment.",
            "practices": "Federal mental-health treatment practice shifts toward FDA-approved psychedelic therapies under accelerated review.",
            "treasures": "Federal mental-health-treatment institutional knowledge expands in psychedelic-therapy directions."
        }
    },
    "c": ["Indigenous", "African-descendant", "Latiné", "lgbtq", "All Communities"],
    "U": "https://www.whitehouse.gov/presidential-actions/2026/04/accelerating-medical-treatments-for-serious-mental-illness/",
    "_source": "manual",
}


def main():
    if not DATA_PATH.exists():
        raise SystemExit(f"data.json not found at {DATA_PATH}")

    em_dash = "—"
    for label, e in [("E", ENTRY_E), ("F", ENTRY_F), ("G", ENTRY_G), ("H", ENTRY_H)]:
        if em_dash in json.dumps(e, ensure_ascii=False):
            raise SystemExit(f"ABORT: em-dash detected in entry {label} ({e['i']}).")

    shutil.copy2(DATA_PATH, BACKUP_PATH)
    print(f"Backup written: {BACKUP_PATH.name}")

    with DATA_PATH.open() as f:
        data = json.load(f)

    targets = [
        ("international", ENTRY_E),
        ("executive_actions", ENTRY_F),
        ("other_domestic", ENTRY_G),
        ("executive_actions", ENTRY_H),
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
