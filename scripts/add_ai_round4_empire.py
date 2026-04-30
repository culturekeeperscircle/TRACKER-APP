#!/usr/bin/env python3
"""Four atomic additions, one backup.

A. EO of December 11, 2025: "Eliminating State Law Obstruction of National
   Artificial Intelligence Policy" (also referenced in coverage as
   "Ensuring a National Policy Framework for Artificial Intelligence").
   Category: executive_actions. Threat: SEVERE.

B. Trump Media and Technology Group / TAE Technologies $6 billion all-stock
   merger announced December 18, 2025. Conflict-of-interest advisory.
   Category: other_domestic. Threat: HARMFUL.

C. OpenAI / Sama Kenya data-annotation labor exploitation (Time
   investigation January 18, 2023; subsequent Kenyan parliament petition
   and African content-moderator unionization 2023). Category:
   international. Threat: HARMFUL.

D. Chile / Cerrillos Mosacat resistance to Google data center water
   draw (Google announced second Chilean data center in 2019; community
   organizing 2019-2023; Santiago environmental tribunal action; Google
   ultimately switched to less water-intensive technology). Category:
   international. Threat: PROTECTIVE.
"""
import json
import shutil
from pathlib import Path
from datetime import datetime

DATA_PATH = Path(__file__).parent.parent / "data" / "data.json"
BACKUP_PATH = DATA_PATH.with_suffix(
    f".json.bak-{datetime.now().strftime('%Y%m%d-%H%M%S')}-pre-round4-empire"
)


# =================== ENTRY A: STATE AI PREEMPTION EO ===================
ENTRY_A = {
    "i": "eo-state-ai-preemption-2025-12-11",
    "t": "Executive Order",
    "n": "Executive Order: Eliminating State Law Obstruction of National Artificial Intelligence Policy (Signed December 11, 2025)",
    "T": '<span style="color: #991B1B;">Executive Order:</span> Eliminating State Law Obstruction of National Artificial Intelligence Policy. Establishes DOJ AI Litigation Task Force, Directs FCC and FTC Agency-Created Preemption, Conditions BEAD Federal Broadband Funds on State AI-Law Conformity',
    "s": "EO state AI preemption Dec 11 2025",
    "d": "2025-12-11",
    "a": "Trump II",
    "A": ["WH", "DOJ", "FCC", "FTC", "Commerce"],
    "S": "Active. Signed December 11, 2025 by President Trump. Establishes a Department of Justice AI Litigation Task Force that challenges state AI laws in court. Directs the Federal Communications Commission to draft a federal reporting and disclosure standard preempting conflicting state laws. Directs the Federal Trade Commission to publish a policy statement using the FTC Act's prohibition on unfair and deceptive trade practices to preempt state laws requiring alterations to AI model outputs. Directs the Secretary of Commerce to issue a policy notice making BEAD broadband-funding eligibility conditional on state AI-law conformity. Directs the Special Advisor for AI and Crypto and the Assistant to the President for Science and Technology to prepare a legislative recommendation establishing a uniform federal AI policy framework that preempts state AI laws.",
    "L": "SEVERE",
    "D": (
        "<b>EXECUTIVE ORDER.</b> On December 11, 2025, President Trump signed an executive order titled \"Eliminating State Law Obstruction of National Artificial Intelligence Policy.\" The order operationalizes the Trump II administration's posture of federal preemption against state and local AI regulation. Karen Hao identifies the order in her Empire of AI book introduction (Library reference: [INTERVIEW] Karen Hao on Empire of AI Threatening Democracy and Creating a New Colonial World - Democracy Now! (2025) [EN].md) as a structural action that bars states and local governments from enacting their own AI regulations.<br><br>"
        "<b>FOUR PREEMPTION MECHANISMS.</b> The order establishes four distinct preemption mechanisms operating in parallel.<br>"
        "<i>1. DOJ Litigation.</i> The order establishes an AI Litigation Task Force within the Department of Justice. The Task Force is directed to challenge state AI laws in federal court and to assess any state laws that conflict with federal policy.<br>"
        "<i>2. Agency-Created Preemption.</i> The Federal Communications Commission is directed to draft a federal reporting and disclosure standard for AI deployment, the effect of which is to preempt conflicting state laws under the doctrine of conflict preemption. The Federal Trade Commission is directed to publish a policy statement holding that the FTC Act's prohibition on unfair and deceptive trade practices (15 U.S.C. sec. 45) preempts state laws requiring alterations to the truthful outputs of AI models.<br>"
        "<i>3. Conditional Federal Funding.</i> The Secretary of Commerce is directed to issue a policy notice establishing eligibility requirements for the Broadband Equity, Access, and Deployment (BEAD) Program under the Infrastructure Investment and Jobs Act. To the maximum extent permitted by law, states identified as having AI laws that conflict with federal policy may be rendered ineligible for BEAD funds.<br>"
        "<i>4. Legislative Recommendation.</i> The Special Advisor for AI and Crypto (David Sacks) and the Assistant to the President for Science and Technology are jointly directed to prepare a legislative recommendation establishing a uniform federal AI policy framework that preempts state AI laws.<br><br>"
        "<b>STATE AI LAWS AT RISK.</b> States whose laws are most likely targets include California (AB 2013 generative-AI training-data transparency; SB 942 California AI Transparency Act; AB 2273 Age-Appropriate Design Code Act AI provisions), Colorado (Colorado AI Act), Illinois (Biometric Information Privacy Act applied to AI), New York (AI Bias Audit Law for hiring; SAFE for Kids Act), Texas (TRAIGA Texas Responsible AI Governance Act), Utah (AI consumer-protection law), and a growing list of states with AI hiring-discrimination, deepfake, and electoral-AI statutes. The order targets these laws through both direct litigation and agency-rule-driven conflict preemption.<br><br>"
        "<b>LEGAL VULNERABILITY.</b> The executive order is widely characterized as legally vulnerable. The U.S. Supreme Court's preemption doctrine (Wyeth v. Levine, 555 U.S. 555 (2009); Arizona v. United States, 567 U.S. 387 (2012)) requires that federal preemption be either expressly stated by Congress or implied through field or conflict preemption analysis grounded in actual federal statutory authority. Tech-policy researchers and legal commentators have argued that the Trump administration cannot restrict state AI regulation without Congress passing a federal AI-preemption statute. Multiple constitutional challenges are anticipated, including from state attorneys general.<br><br>"
        "<b>RELATIONSHIP TO STATE-LEVEL CIVIL RIGHTS PROTECTIONS.</b> Many state AI laws function as civil-rights protections against AI-driven discrimination, hiring bias, deepfake-based harassment, electoral disinformation, and algorithmic harm. The Trump December 11 EO threatens these protections. Affected protections most directly relevant to the TCKC primary cultural communities include: Colorado AI Act consumer protection against algorithmic discrimination in housing, employment, and credit; Illinois BIPA protections against biometric capture (which has historical impact on African-descendant and Latiné communities through disparate facial-recognition error rates); and California and New York hiring-bias and election-disinformation protections.<br><br>"
        "<b>RELATIONSHIP TO BROADER PATTERN.</b> The order is one component of the Trump II administration's coordinated AI industrial-policy package: Stargate Project announcement (tracked at stargate-project-trump-2025); July 23, 2025 EO Accelerating Federal Permitting of Data Center Infrastructure (tracked at eo-data-center-permitting-2025-07-23); May 23, 2025 EO 14300 NRC Reform (tracked at eo-14300-nrc-reform-2025); November 6, 2025 Final 2025 Critical Minerals List with uranium re-listed (tracked at usgs-critical-minerals-list-2025); and the December 18, 2025 Trump Media and Technology Group / TAE Technologies $6 billion merger (tracked at tmtg-tae-fusion-merger-2025-12-18). The December 11 EO is the principal federal-deregulatory-preemption complement to the federal-incentives package.<br><br>"
        "<b>CULTURAL RESOURCE THREAT ASSESSMENT.</b> The threat level is SEVERE. State and local AI regulation has been the principal forum in which civil-rights protections against AI-driven discrimination, hiring bias, biometric harm, and electoral-AI manipulation have been enacted in the absence of comprehensive federal AI legislation. The order seeks to nullify those protections through litigation, agency rulemaking, and federal-funding conditions. The cumulative effect on TCKC primary cultural communities is to remove the operative civil-rights protective infrastructure for AI harms at the level (state) at which it currently exists."
        "<br><br>"
        "<b>SOURCES.</b><br>"
        "Primary federal action: White House, \"Eliminating State Law Obstruction of National Artificial Intelligence Policy,\" December 11, 2025. <a href=\"https://www.whitehouse.gov/presidential-actions/2025/12/eliminating-state-law-obstruction-of-national-artificial-intelligence-policy/\">https://www.whitehouse.gov/presidential-actions/2025/12/eliminating-state-law-obstruction-of-national-artificial-intelligence-policy/</a><br>"
        "Legal analysis: Sidley Austin, \"Unpacking the December 11, 2025 Executive Order: Ensuring a National Policy Framework for Artificial Intelligence.\" <a href=\"https://www.sidley.com/en/insights/newsupdates/2025/12/unpacking-the-december-11-2025-executive-order\">https://www.sidley.com/en/insights/newsupdates/2025/12/unpacking-the-december-11-2025-executive-order</a>; "
        "Sidley Data Matters Privacy Blog: <a href=\"https://datamatters.sidley.com/2025/12/23/unpacking-the-december-11-2025-executive-order-ensuring-a-national-policy-framework-for-artificial-intelligence/\">https://datamatters.sidley.com/2025/12/23/unpacking-the-december-11-2025-executive-order-ensuring-a-national-policy-framework-for-artificial-intelligence/</a>; "
        "Paul Hastings, \"President Trump Signs Executive Order Challenging State AI Laws.\" <a href=\"https://www.paulhastings.com/insights/client-alerts/president-trump-signs-executive-order-challenging-state-ai-laws\">https://www.paulhastings.com/insights/client-alerts/president-trump-signs-executive-order-challenging-state-ai-laws</a>; "
        "Latham and Watkins, \"AI Executive Order Targets State Laws and Seeks Uniform Federal Standards.\" <a href=\"https://www.lw.com/en/insights/ai-executive-order-targets-state-laws-and-seeks-uniform-federal-standards\">https://www.lw.com/en/insights/ai-executive-order-targets-state-laws-and-seeks-uniform-federal-standards</a>; "
        "DLA Piper, \"New Executive Order aims to preempt state AI regulation: Top points.\" <a href=\"https://www.dlapiper.com/en-us/insights/publications/2025/12/new-executive-order-aims-to-preempt-state-ai-regulation\">https://www.dlapiper.com/en-us/insights/publications/2025/12/new-executive-order-aims-to-preempt-state-ai-regulation</a>; "
        "Alston and Bird Consumer Finance, \"New Executive Order Aims to Curb State AI Regulation.\" <a href=\"https://www.alstonconsumerfinance.com/executive-order-state-ai-regulation/\">https://www.alstonconsumerfinance.com/executive-order-state-ai-regulation/</a>; "
        "Epstein Becker Green, \"Artificial Intelligence Regulation at a Crossroads: The Trump Administration's Preemption Push.\" <a href=\"https://www.workforcebulletin.com/artificial-intelligence-regulation-at-a-crossroads-the-trump-administrations-preemption-push\">https://www.workforcebulletin.com/artificial-intelligence-regulation-at-a-crossroads-the-trump-administrations-preemption-push</a><br>"
        "Civil-society analysis: Economic Policy Institute, \"Executive Order to challenge or deter state laws that would impact artificial intelligence (AI).\" <a href=\"https://www.epi.org/policywatch/executive-order-to-challenge-or-deter-state-laws-that-would-impact-artificial-intelligence-ai/\">https://www.epi.org/policywatch/executive-order-to-challenge-or-deter-state-laws-that-would-impact-artificial-intelligence-ai/</a><br>"
        "Coverage: NPR, \"Trump is trying to preempt state AI laws via an executive order. It may not be legal,\" December 11, 2025. <a href=\"https://www.npr.org/2025/12/11/nx-s1-5638562/trump-ai-david-sacks-executive-order\">https://www.npr.org/2025/12/11/nx-s1-5638562/trump-ai-david-sacks-executive-order</a><br>"
        "Library reference: [INTERVIEW] Karen Hao on Empire of AI Threatening Democracy and Creating a New Colonial World - Democracy Now! (2025) [EN].md.<br>"
        "Related tracker entries: stargate-project-trump-2025 (Stargate Project, 2025-01-21); eo-14300-nrc-reform-2025 (EO 14300 NRC Reform, 2025-05-23); eo-data-center-permitting-2025-07-23 (EO Accelerating Federal Permitting of Data Center Infrastructure); usgs-critical-minerals-list-2025 (Final 2025 Critical Minerals List); tmtg-tae-fusion-merger-2025-12-18 (TMTG-TAE merger, 2025-12-18); altman-senate-testimony-ai-energy-2025 (Altman Senate testimony); honor-the-earth-no-data-center-coalition-2026 (Honor the Earth coalition); openai-for-countries-2025 (OpenAI for Countries)."
    ),
    "I": {
        "africanDescendant": {
            "people": "Black communities lose state-level civil-rights protections against AI-driven hiring bias, biometric-misidentification harms (facial recognition has documented disparate error rates against darker-skinned faces), and AI-mediated electoral disinformation that has historically targeted Black voter mobilization. Illinois BIPA, New York hiring-bias law, and Colorado AI Act protections face preemption pressure.",
            "places": "African-descendant communities lose state-level forum for civil-rights advocacy on AI deployment in housing, employment, credit, and policing.",
            "practices": "Civil-rights legal practice loses the state-AI-law leverage points that have been the principal protective infrastructure in the absence of federal AI civil-rights legislation.",
            "treasures": "State AI civil-rights statutes, accumulated since 2018, are themselves cultural-policy treasures whose erosion under federal preemption harms African-descendant communities directly."
        },
        "indigenous": {
            "people": "Indigenous communities lose state-level AI-law protections that intersect with tribal-data-sovereignty efforts. Several states have enacted protections that align with the CARE Principles for Indigenous Data Governance.",
            "places": "Tribal-jurisdiction AI deployments operate within complex federal-state-tribal frameworks that the order may further complicate.",
            "practices": "Tribal-data-sovereignty practice loses state-level allies.",
            "treasures": "Tribal-data-sovereignty institutional frameworks face cumulative erosion."
        },
        "latine": {
            "people": "Latiné communities, including immigrant and undocumented populations subject to AI-mediated immigration enforcement and ICE biometric capture, lose state-level civil-rights protections against AI-driven discrimination.",
            "places": "Sanctuary jurisdictions lose AI-law protections that have been part of broader civil-rights infrastructure.",
            "practices": "Latiné civil-rights legal practice loses state-AI-law leverage points.",
            "treasures": "State-level civil-rights AI statutes, particularly those addressing immigration-enforcement AI, face preemption pressure."
        },
        "asianAmerican": {
            "people": "Asian American communities, including Chinese American academics and students subject to AI-mediated counterintelligence surveillance, lose state-level protections against AI-driven targeting.",
            "places": "Asian American communities in academic and research environments face cumulative state-AI-protection erosion.",
            "practices": "Asian American civil-rights practice loses state-level leverage points.",
            "treasures": "State-level civil-rights AI statutes that intersect with anti-Asian-discrimination protections face preemption pressure."
        },
        "lgbtq": {
            "people": "LGBTQ+ communities lose state-level AI-law protections against AI-driven outing, hiring discrimination, and content-moderation-based suppression of LGBTQ+ speech and resources.",
            "places": "State-level AI civil-rights jurisdictions lose enforcement authority.",
            "practices": "LGBTQ+ civil-rights legal practice loses state-AI-law leverage points.",
            "treasures": "State-level LGBTQ+-protective AI statutes face preemption pressure."
        },
        "allCommunities": {
            "people": "All Americans lose state-level civil-rights protections against AI-driven harms in the absence of comprehensive federal AI civil-rights legislation.",
            "places": "State and local AI regulatory jurisdictions lose enforcement authority.",
            "practices": "Federal-state regulatory-balance practice in AI is reshaped toward federal-preemption supremacy.",
            "treasures": "State AI civil-rights statutes, accumulated since 2018, face systematic erosion."
        }
    },
    "c": ["African-descendant", "Indigenous", "Latiné", "Asian", "lgbtq", "All Communities"],
    "U": "https://www.whitehouse.gov/presidential-actions/2025/12/eliminating-state-law-obstruction-of-national-artificial-intelligence-policy/",
    "_source": "manual",
}


# =================== ENTRY B: TMTG-TAE FUSION MERGER ===================
ENTRY_B = {
    "i": "tmtg-tae-fusion-merger-2025-12-18",
    "t": "Conflict-of-Interest Advisory",
    "n": "Trump Media and Technology Group / TAE Technologies $6 Billion All-Stock Merger Announced December 18, 2025: Trump-Family Business Acquires Stake in Nuclear-Fusion-for-AI Plant Under Federal AI Industrial-Policy Package",
    "T": '<span style="color: #CA8A04;">Conflict-of-Interest Advisory:</span> Trump Media (TMTG) and TAE Technologies $6 Billion All-Stock Merger. Trump-Family Business Acquires Stake in Nuclear-Fusion-for-AI Plant; Devin Nunes Co-CEO; First Utility-Scale Fusion Plant Targeted for 2026 Construction',
    "s": "TMTG-TAE fusion merger Dec 18 2025",
    "d": "2025-12-18",
    "a": "Trump II",
    "A": ["WH", "Office of Government Ethics", "DOE", "NRC"],
    "S": "Active. Definitive merger agreement signed December 18, 2025. All-stock transaction valued at over $6 billion. Trump Media and Technology Group Corp. (TMTG) merging with TAE Technologies, Inc. Each company's shareholders to own approximately 50 percent of the combined company on a fully diluted equity basis. TMTG providing up to $200 million cash at signing plus $100 million at S-4 filing. Devin Nunes (former Republican congressman, current TMTG CEO) becomes co-CEO with TAE CEO Michl Binderbauer. Combined company plans to site and commence construction of \"world's first utility-scale fusion power plant\" in 2026 to power AI. Closing expected mid-2026 subject to shareholder and regulatory approval. Ethics watchdogs (CNN reporting) flagged conflict-of-interest concerns.",
    "L": "HARMFUL",
    "D": (
        "<b>MERGER AGREEMENT.</b> On December 18, 2025, Trump Media and Technology Group Corp. (TMTG, NASDAQ ticker DJT) and TAE Technologies, Inc. announced the signing of a definitive merger agreement combining the two companies in an all-stock transaction valued at over $6 billion. Upon closing (expected mid-2026, subject to shareholder and regulatory approval), shareholders of each company will own approximately 50 percent of the combined company on a fully diluted equity basis. TMTG agreed to provide up to $200 million cash to TAE at signing and an additional $100 million at S-4 filing. DJT stock rose 33 percent on the announcement.<br><br>"
        "<b>LEADERSHIP.</b> Devin Nunes, the Republican congressman who resigned from the U.S. House of Representatives in 2021 to become CEO of Trump Media, will be co-CEO of the combined company alongside TAE Technologies CEO Michl Binderbauer.<br><br>"
        "<b>TAE TECHNOLOGIES.</b> TAE Technologies has designed, built, and operated five fusion reactors. The company has raised over $1.3 billion from investors including Google, Chevron Technology Ventures, Goldman Sachs, Sumitomo, and New Enterprise Associates. The company holds more than 1,600 patents in fusion-energy technology. The combined entity plans to site and commence construction of the \"world's first utility-scale fusion power plant\" in 2026, with the explicit purpose of powering artificial-intelligence data centers under what the announcement frames as \"America's AI dominance and energy security.\"<br><br>"
        "<b>CONFLICT-OF-INTEREST CONCERN.</b> The merger places the Trump family's principal business equity (TMTG, in which the Trump family holds a controlling stake) into a 50-percent ownership position in a nuclear-fusion firm whose explicit purpose is powering AI under federal AI industrial-policy actions the Trump administration is implementing. The president has signed multiple federal AI-and-nuclear actions during 2025: Stargate Project announcement (tracked at stargate-project-trump-2025); EO 14300 reforming the NRC and targeting 400 GW of new nuclear capacity by 2050 (tracked at eo-14300-nrc-reform-2025); EO Accelerating Federal Permitting of Data Center Infrastructure (tracked at eo-data-center-permitting-2025-07-23); USGS Final 2025 Critical Minerals List adding uranium (tracked at usgs-critical-minerals-list-2025); and the December 11, 2025 EO preempting state AI regulation (tracked at eo-state-ai-preemption-2025-12-11). Each of these federal actions creates value for nuclear-fusion-for-AI businesses. The president's family business is now positioned to capture that value directly.<br><br>"
        "<b>ETHICS-WATCHDOG RESPONSE.</b> CNN reported on December 22, 2025 that ethics watchdogs are alarmed by the merger. The conflict-of-interest concern is structural: the president signs federal actions that subsidize, fast-track, deregulate, or otherwise create market value for AI-and-nuclear infrastructure; the president's family business owns 50 percent of a fusion firm built to capture that value; the federal Office of Government Ethics has weakened recusal-and-divestiture enforcement under the Trump II administration's restructured-ethics posture.<br><br>"
        "<b>FUSION-POWER FEASIBILITY.</b> No utility-scale fusion power plant has yet been operated anywhere in the world. TAE Technologies has operated experimental reactors at sub-utility-scale. The 2026 construction timeline announced for the \"world's first utility-scale fusion power plant\" is aggressive relative to the operational readiness of fusion technology globally. Even successful demonstrator-fusion projects elsewhere (ITER, NIF achievement of net energy gain in 2022, several private-fusion demonstrators) are not currently positioned to deliver utility-scale electricity to a data center on the announced timeline. The fusion-power-for-AI framing therefore operates more as policy and stock-market narrative than as near-term grid reality.<br><br>"
        "<b>RELATIONSHIP TO THE TRUMP MEDIA-AND-CRYPTO PORTFOLIO.</b> TMTG has previously diversified into crypto and other ventures during 2024-2025. The TAE merger adds energy and AI infrastructure to the portfolio. The pattern is consistent with the Trump family business converting presidential political capital into market positions across federally regulated industries.<br><br>"
        "<b>CULTURAL RESOURCE THREAT ASSESSMENT.</b> The threat level is HARMFUL. The merger does not directly produce cultural-resource harm as a discrete event. The HARMFUL classification reflects three structural concerns. First, the merger creates a direct presidential conflict of interest in federal AI-and-nuclear policy whose downstream effects (uranium mining on Indigenous lands, data-center water draw on Indigenous and rural lands, NRC deregulation, state AI-law preemption) are tracked elsewhere in the tracker as SEVERE. Second, presidential-family equity in federally regulated industries undermines the federal-ethics framework whose preservation is itself a cultural-policy treasure. Third, the fusion-power narrative provides political cover for AI-energy-buildout decisions whose actual fuel sources (natural gas, coal, conventional fission) produce documented cultural-resource harm to TCKC primary cultural communities."
        "<br><br>"
        "<b>SOURCES.</b><br>"
        "Primary corporate announcement: TAE Technologies, \"Trump Media and Technology Group to Merge with TAE Technologies.\" <a href=\"https://tae.com/trump-media-and-technology-group-to-merge-with-tae-technologies/\">https://tae.com/trump-media-and-technology-group-to-merge-with-tae-technologies/</a><br>"
        "Coverage: PBS NewsHour, \"Trump Media to merge with nuclear fusion company that wants to power AI.\" <a href=\"https://www.pbs.org/newshour/politics/trump-media-to-merge-with-nuclear-fusion-company-that-wants-to-power-ai\">https://www.pbs.org/newshour/politics/trump-media-to-merge-with-nuclear-fusion-company-that-wants-to-power-ai</a>; "
        "CNBC, \"Trump Media announces $6 billion merger with fusion company TAE Technologies; DJT stock soars 33%,\" December 18, 2025. <a href=\"https://www.cnbc.com/2025/12/18/trump-media-djt-tae-fusion-merger.html\">https://www.cnbc.com/2025/12/18/trump-media-djt-tae-fusion-merger.html</a>; "
        "ABC News, \"Trump Media announces $6 billion merger with nuclear fusion company.\" <a href=\"https://abcnews.com/Business/trump-media-announces-6-billion-merger-nuclear-fusion/story?id=128516029\">https://abcnews.com/Business/trump-media-announces-6-billion-merger-nuclear-fusion/story?id=128516029</a>; "
        "Fortune, \"Trump goes nuclear: The president's tech and media umbrella will merge with a fusion reactor developer in a deal valued north of $6 billion.\" <a href=\"https://fortune.com/2025/12/18/trump-media-technology-group-tae-technologies-nuclear-reactor-power-deal-merger/\">https://fortune.com/2025/12/18/trump-media-technology-group-tae-technologies-nuclear-reactor-power-deal-merger/</a>; "
        "Fortune (TAE CEO interview): <a href=\"https://fortune.com/2025/12/18/trump-media-nuclear-fusion-tae-technologies-michl-binderbauer/\">https://fortune.com/2025/12/18/trump-media-nuclear-fusion-tae-technologies-michl-binderbauer/</a>; "
        "American Nuclear Society / Nuclear Newswire, \"Trump Media to merge with fusion startup TAE Technologies in $6B deal,\" December 19, 2025. <a href=\"https://www.ans.org/news/2025-12-19/article-7632/trump-media-to-merge-with-fusion-startup-tae-technologies-in-6b-deal/\">https://www.ans.org/news/2025-12-19/article-7632/trump-media-to-merge-with-fusion-startup-tae-technologies-in-6b-deal/</a>; "
        "Spokesman-Review, \"Why is Trump's media company getting involved with nuclear power?\" December 19, 2025. <a href=\"https://www.spokesman.com/stories/2025/dec/19/why-is-trumps-media-company-getting-involved-with-/\">https://www.spokesman.com/stories/2025/dec/19/why-is-trumps-media-company-getting-involved-with-/</a><br>"
        "Ethics-watchdog coverage: CNN Business, \"Ethics watchdogs are alarmed by $6 billion marriage of Trump's social media platform and nuclear fusion company,\" December 22, 2025. <a href=\"https://edition.cnn.com/2025/12/22/business/trump-stock-fusion\">https://edition.cnn.com/2025/12/22/business/trump-stock-fusion</a><br>"
        "Library reference: [INTERVIEW] Karen Hao on Empire of AI Threatening Democracy and Creating a New Colonial World - Democracy Now! (2025) [EN].md.<br>"
        "Related tracker entries: stargate-project-trump-2025 (Stargate Project, 2025-01-21); eo-14300-nrc-reform-2025 (EO 14300 NRC Reform, 2025-05-23); eo-data-center-permitting-2025-07-23 (EO Accelerating Federal Permitting of Data Center Infrastructure); usgs-critical-minerals-list-2025 (Final 2025 Critical Minerals List); eo-state-ai-preemption-2025-12-11 (EO Eliminating State Law Obstruction of National AI Policy); altman-senate-testimony-ai-energy-2025 (Altman Senate testimony on AI energy); honor-the-earth-no-data-center-coalition-2026 (Honor the Earth coalition)."
    ),
    "I": {
        "indigenous": {
            "people": "Indigenous communities bear the cumulative downstream harm of presidential-family-equity in nuclear-fusion-for-AI. Uranium mining on Indigenous lands (tracked at usgs-critical-minerals-list-2025) produces cultural-resource harm whose policy authorization runs through the same federal-actions package the merger captures value from.",
            "places": "Indigenous lands face cumulative encroachment under federal-actions-driven nuclear and AI buildout.",
            "practices": "Federal-Indian-trust consultation practice operates within a federal-ethics environment that the merger weakens.",
            "treasures": "Federal-ethics framework is itself a cultural-policy treasure whose erosion harms Indigenous communities."
        },
        "africanDescendant": {
            "people": "African-descendant communities bear the cumulative downstream harm of AI-data-center buildout (xAI Memphis tracked at xai-colossus-memphis-cleanair-2026 is the documented exemplar). The merger captures value from federal actions that authorize that buildout.",
            "places": "African-descendant communities adjacent to AI-energy-infrastructure siting locations face cumulative harm.",
            "practices": "Federal civil-rights and environmental-justice consultation practice operates within a federal-ethics environment the merger weakens.",
            "treasures": "Federal-ethics framework is a cultural-policy treasure."
        },
        "allCommunities": {
            "people": "All Americans share the federal-ethics environment that presidential-family-equity in regulated industries weakens. The merger sets a precedent for converting presidential political capital into market positions in federally regulated industries.",
            "places": "U.S. federal-regulatory landscape is shaped by presidential-family-equity considerations.",
            "practices": "Federal-ethics practice (recusal, divestiture, blind trust frameworks) is undermined.",
            "treasures": "The federal-ethics framework, accumulated under Ethics in Government Act of 1978 (5 U.S.C. App.) and subsequent reforms, is a cultural-policy treasure whose erosion is structural."
        }
    },
    "c": ["Indigenous", "African-descendant", "All Communities"],
    "U": "https://tae.com/trump-media-and-technology-group-to-merge-with-tae-technologies/",
    "_source": "manual",
}


# =================== ENTRY C: KENYA OPENAI/SAMA LABOR ===================
ENTRY_C = {
    "i": "openai-sama-kenya-data-annotation-2023",
    "t": "International Labor Exploitation Documentation",
    "n": "OpenAI / Sama Kenya Data-Annotation Labor: Time Investigation January 18, 2023; Workers Paid $1.32 to $2 per Hour to Read Graphic Content for ChatGPT Filter Training; Subsequent Kenyan Parliament Petition and African Content-Moderator Unionization",
    "T": '<span style="color: #CA8A04;">International Labor Exploitation:</span> OpenAI / Sama Kenya Data-Annotation Workers Paid $1.32 to $2 per Hour to Read Graphic Sexual and Violent Content (Including Child Sexual Abuse Material) to Train ChatGPT Filter; Workers Develop PTSD, Subsequently Petition Kenyan Parliament and Unionize',
    "s": "OpenAI Sama Kenya labor",
    "d": "2023-01-18",
    "a": "Trump II",
    "A": ["State", "Commerce"],
    "S": "Active. Time magazine published its investigation January 18, 2023 documenting OpenAI's outsourcing through San Francisco-based partner Sama of ChatGPT-filter training data labeling to Kenyan workers paid $1.32 to $2 per hour. Workers required to read graphic violent and sexual content including child sexual abuse material. Workers developed PTSD, paranoia, depression, anxiety, insomnia, and sexual dysfunction without psychosocial support. Subsequent actions: Kenyan workers petitioned the Kenyan Parliament for investigation of OpenAI and Sama; 150 African content moderators voted to unionize across firms (Time reporting, May 2023). Karen Hao's Empire of AI book and her Democracy Now! interview document the case as a primary example of the AI-empire labor extraction.",
    "L": "HARMFUL",
    "D": (
        "<b>EXPOSE.</b> On January 18, 2023, Time magazine published an investigation by Billy Perrigo titled \"OpenAI Used Kenyan Workers on Less Than $2 Per Hour to Make ChatGPT Less Toxic.\" The investigation documented OpenAI's contracting through San Francisco-based data-labeling firm Sama of Kenyan workers to read and categorize graphic violent and sexual content for the purpose of training ChatGPT's content-filter model. The investigation became one of the foundational primary-source documents of AI-supply-chain labor exploitation and is referenced extensively in Karen Hao's Empire of AI book and her May 2025 Democracy Now! interview (Library reference: [INTERVIEW] Karen Hao on Empire of AI Threatening Democracy and Creating a New Colonial World - Democracy Now! (2025) [EN].md).<br><br>"
        "<b>WORK CONDITIONS.</b> Kenyan workers were paid wages between $1.32 and $2.00 per hour, varying by seniority and performance. The work required reading and categorizing graphic content including descriptions of child sexual abuse, bestiality, murder, suicide, torture, self-harm, and incest. Workers also categorized AI-generated content, where OpenAI prompted its own AI models to imagine the worst content on the internet so that the resulting outputs could be used to train the content filter. The workers received no psychosocial support during or after the contract. Documented mental-health consequences include post-traumatic stress disorder, paranoia, depression, anxiety, insomnia, and sexual dysfunction. One worker reported recurring visions after reading a graphic description of bestiality involving a child.<br><br>"
        "<b>CONTRACTUAL STRUCTURE.</b> OpenAI did not directly employ the Kenyan workers. The contractual chain ran from OpenAI to Sama (a San Francisco-headquartered data-labeling firm operating in East Africa) to the Kenyan workers as Sama contractors. The structure has been criticized as a labor-arbitrage and liability-shielding mechanism whereby Silicon Valley AI companies capture the upstream training-data benefit while distributing the downstream labor and trauma costs to global-south contractor workforces.<br><br>"
        "<b>WORKER RESPONSE.</b> In 2023, Kenyan content moderators petitioned the Kenyan Parliament to investigate OpenAI and Sama for exploitative labor practices. Multiple Kenyan civil-society organizations and labor lawyers supported the petition. In May 2023, Time reported that 150 African content moderators across multiple AI and social-media firms voted to unionize, forming what was characterized as the first African content-moderator union. The unionization effort was led by workers who had labeled content for OpenAI's ChatGPT, Facebook, and other major platforms.<br><br>"
        "<b>OPENAI RESPONSE.</b> OpenAI publicly responded to the Kenya \"toxic work\" petition through ITWeb Africa coverage, characterizing the work as essential safety infrastructure for ChatGPT. The response did not address the wage levels, the absence of psychosocial support, or the contractor-mediation structure that distanced OpenAI from direct labor responsibility.<br><br>"
        "<b>FEDERAL NEXUS.</b> The federal-action angle is indirect. U.S. corporate AI training operates outside U.S. labor protections when contracted through foreign-jurisdiction firms. The Federal Trade Commission's December 11, 2025 EO directive (tracked at eo-state-ai-preemption-2025-12-11) and the broader U.S. AI industrial-policy package (tracked at stargate-project-trump-2025 and openai-for-countries-2025) create the demand environment under which AI-supply-chain labor practices like the Kenya case proliferate. The U.S. State Department and Department of Commerce hold operative authorities over labor-rights provisions in trade agreements and bilateral cooperation with Kenya, neither of which has been invoked to address the documented harm.<br><br>"
        "<b>RELATIONSHIP TO TCKC PRIMARY COMMUNITIES.</b> The Kenya case affects African-descendant communities directly through diaspora kinship between Kenyan workers and U.S.-based African American communities. The case is a primary-source documentation of the AI-supply-chain labor pattern that operates analogously across other global-south sites (Philippines, Madagascar, Venezuela, Colombia). Karen Hao's Empire of AI thesis frames the pattern as colonial extraction.<br><br>"
        "<b>CULTURAL RESOURCE THREAT ASSESSMENT.</b> The threat level is HARMFUL. The harms documented in the Time investigation are concrete, individual, and severe: PTSD, paranoia, depression, anxiety, insomnia, sexual dysfunction in the affected workforce, with no psychosocial-support framework to address them. The structural harm extends to the broader pattern of AI-supply-chain labor exploitation in the global south. The PROTECTIVE counter-actions (Kenyan parliamentary petition, African content-moderator unionization) are part of the same case and demonstrate the resistance Karen Hao identifies as the route to reclaiming agency."
        "<br><br>"
        "<b>SOURCES.</b><br>"
        "Primary investigation: Time magazine (Billy Perrigo), \"OpenAI Used Kenyan Workers Making $2 an Hour to Filter Traumatic Content from ChatGPT,\" January 18, 2023 (Vice mirror with full coverage). <a href=\"https://www.vice.com/en/article/openai-used-kenyan-workers-making-dollar2-an-hour-to-filter-traumatic-content-from-chatgpt/\">https://www.vice.com/en/article/openai-used-kenyan-workers-making-dollar2-an-hour-to-filter-traumatic-content-from-chatgpt/</a><br>"
        "Subsequent unionization: Time, \"150 African Workers for AI Companies Vote to Unionize,\" May 2023. <a href=\"https://time.com/6275995/chatgpt-facebook-african-workers-union/\">https://time.com/6275995/chatgpt-facebook-african-workers-union/</a><br>"
        "Kenyan parliamentary petition: Citizen Digital, \"Kenyan moderators behind ChatGPT want parliament to probe OpenAI, Sama over exploitation.\" <a href=\"https://www.citizen.digital/tech/kenyan-moderators-behind-chatgpt-want-parliament-to-probe-openai-sama-over-exploitation-n323387\">https://www.citizen.digital/tech/kenyan-moderators-behind-chatgpt-want-parliament-to-probe-openai-sama-over-exploitation-n323387</a>; "
        "DailyAI, \"Kenyan AI content moderators petition the government over traumatic working conditions,\" August 2023. <a href=\"https://dailyai.com/2023/08/kenyan-ai-content-moderators-petition-the-government-over-traumatic-working-conditions/\">https://dailyai.com/2023/08/kenyan-ai-content-moderators-petition-the-government-over-traumatic-working-conditions/</a><br>"
        "OpenAI response: ITWeb Africa, \"Exclusive: OpenAI responds to Kenya's 'toxic work' petition.\" <a href=\"https://itweb.africa/article/exclusive-openai-responds-to-kenyas-toxic-work-petition/lwrKxq3YNky7mg1o\">https://itweb.africa/article/exclusive-openai-responds-to-kenyas-toxic-work-petition/lwrKxq3YNky7mg1o</a><br>"
        "Worker testimony: CMSWire, \"AI Content Moderators Battling Exploitation, Trauma.\" <a href=\"https://www.cmswire.com/digital-experience/he-helped-train-chatgpt-it-traumatized-him/\">https://www.cmswire.com/digital-experience/he-helped-train-chatgpt-it-traumatized-him/</a>; "
        "Medianama, \"Kenyan Workers Expose Disturbing Work Conditions in AI Data Labelling for OpenAI,\" July 2023. <a href=\"https://www.medianama.com/2023/07/223-kenyan-workers-call-for-investigation-into-exploitation-by-openai-3/\">https://www.medianama.com/2023/07/223-kenyan-workers-call-for-investigation-into-exploitation-by-openai-3/</a><br>"
        "Documentation: AI Incident Database, \"Incident 450: Kenyan Data Annotators Allegedly Exposed to Graphic Content for OpenAI's AI.\" <a href=\"https://incidentdatabase.ai/cite/450/\">https://incidentdatabase.ai/cite/450/</a>; "
        "OECD AI, \"Kenyan Content Moderators Traumatized While Training OpenAI's ChatGPT,\" May 19, 2023. <a href=\"https://oecd.ai/en/incidents/2023-05-19-0496\">https://oecd.ai/en/incidents/2023-05-19-0496</a><br>"
        "Academic analysis: SAIS Perspectives (Johns Hopkins), \"Ethical AI Principles Omit Kenyan Content Moderators,\" April 2024. <a href=\"https://www.saisperspectives.com/dcs-blog/2024/4/1/ethical-ai-principles-omit-kenyan-content-moderators\">https://www.saisperspectives.com/dcs-blog/2024/4/1/ethical-ai-principles-omit-kenyan-content-moderators</a><br>"
        "Library reference: [INTERVIEW] Karen Hao on Empire of AI Threatening Democracy and Creating a New Colonial World - Democracy Now! (2025) [EN].md.<br>"
        "Related tracker entries: stargate-project-trump-2025 (Stargate Project, 2025-01-21); openai-for-countries-2025 (OpenAI for Countries, 2025-05-07); altman-senate-testimony-ai-energy-2025 (Altman Senate testimony); xai-colossus-memphis-cleanair-2026 (xAI Memphis labor and pollution harms in U.S.)."
    ),
    "I": {
        "africanDescendant": {
            "people": "Kenyan content-moderation workers, primarily working-age adults from urban Nairobi neighborhoods, faced direct labor exploitation and documented mental-health harm. The diaspora connection to U.S.-based African American communities runs through both kinship and the broader African-descendant transnational labor solidarity tradition. The Kenyan parliamentary petition and the African content-moderator unionization are PROTECTIVE actions African-descendant labor organizing.",
            "places": "Nairobi-area Sama offices and worker communities. Kenyan parliament. The Kenyan AI-content-moderation labor market.",
            "practices": "Kenyan labor-organizing practice and African content-moderator unionization practice. Cross-Atlantic labor solidarity with Black labor traditions in the United States.",
            "treasures": "African content-moderator unionization institutional knowledge, accumulated through this case and parallel cases at Facebook (Sama also contracted Facebook content moderation) and other AI and social-media firms."
        },
        "allCommunities": {
            "people": "All ChatGPT users benefit from the content filter that the Kenyan workers' labor produced. The benefit asymmetry (cheap labor in the global south, expensive product in the global north) is the core empire-of-AI logic Karen Hao identifies.",
            "places": "AI-supply-chain labor sites in the global south face systemic exposure to graphic content without psychosocial-support frameworks.",
            "practices": "AI-corporate-responsibility practice has been forced to engage with content-moderator labor conditions through this case and subsequent ones.",
            "treasures": "The institutional documentation of the case (Time investigation, OECD AI incident database, AI Incident Database) is itself a cultural-policy treasure for AI-labor accountability."
        }
    },
    "c": ["African-descendant", "All Communities"],
    "U": "https://www.vice.com/en/article/openai-used-kenyan-workers-making-dollar2-an-hour-to-filter-traumatic-content-from-chatgpt/",
    "_source": "manual",
}


# =================== ENTRY D: CHILE CERRILLOS GOOGLE ===================
ENTRY_D = {
    "i": "chile-google-cerrillos-mosacat-resistance",
    "t": "International Indigenous-and-Water-Rights Resistance",
    "n": "Chile / Cerrillos / Mosacat: Community Resistance to Google's Second Latin American Data Center (Announced 2019; 7 Billion Liters Water Authorization 2020; 4-5 Years of Sustained Activism; Santiago Environmental Tribunal Action; Google Switches to Less Water-Intensive Technology)",
    "T": '<span style="color: #065F46;">International PROTECTIVE Resistance:</span> Chile / Cerrillos / Mosacat Community Blocks Google Second Data Center for 4-5 Years; Santiago Environmental Tribunal Engages; Google Forced to Switch to Less Water-Intensive Technology',
    "s": "Chile Cerrillos Google Mosacat resistance",
    "d": "2019-01-01",
    "a": "Trump II",
    "A": ["State", "USTR"],
    "S": "Active. Google announced its second Chilean data center proposal for the Cerrillos commune of greater Santiago in 2019. In 2020, Chilean environmental authority authorized the data center to extract 228 liters of water per second (over 7 billion liters annually). Mosacat (Movimiento Socio Ambiental Comunitario por el Agua y el Territorio, the Socio-Environmental Community Movement for Land and Water) led sustained activism from 2019 through 2023. Activism escalated to Google Chile, Google Mountain View, and the Chilean government. Santiago environmental tribunal engaged. Chilean government established a community-corporation-government roundtable. Google ultimately switched to less water-intensive cooling technology. Activism continues; community describes the fight as not over.",
    "L": "PROTECTIVE",
    "D": (
        "<b>RESISTANCE OVERVIEW.</b> The community of Cerrillos, in the greater Santiago metropolitan region of Chile, has sustained four to five years of organized resistance against Google's proposed second Chilean data center. The resistance has been led by Mosacat (Movimiento Socio Ambiental Comunitario por el Agua y el Territorio, the Socio-Environmental Community Movement for Land and Water), a community organization formed to defend local water resources. The resistance is documented in Karen Hao's Empire of AI book and in her May 2025 Democracy Now! interview (Library reference: [INTERVIEW] Karen Hao on Empire of AI Threatening Democracy and Creating a New Colonial World - Democracy Now! (2025) [EN].md) as one of the principal global-south frontline cases of AI-data-center water-rights resistance.<br><br>"
        "<b>HISTORICAL BACKGROUND.</b> Chile underwent extensive water-resource privatization under the Augusto Pinochet dictatorship (1973-1990) following the 1981 Water Code (Decreto con Fuerza de Ley No. 1.122). The Cerrillos community is one of a small number of communities in the greater Santiago region that retained access to a public freshwater resource. The resource services both the Cerrillos community and emergency supply for the broader Santiago region.<br><br>"
        "<b>GOOGLE PROJECT.</b> Google opened its first Latin American data center in Quilicura (a different commune of Santiago) in 2015. In 2019, Google announced a second Chilean data center proposed for the Cerrillos commune. Mosacat activists reviewed Google's documentation and discovered that the new center was authorized to use approximately twice the water volume of the Quilicura facility. In 2020, Chile's environmental authority authorized the Cerrillos facility to extract 228 liters of water per second, equivalent to over 7 billion liters per year.<br><br>"
        "<b>COMMUNITY ORGANIZING.</b> Mosacat activists pursued boots-on-the-ground organizing: door-to-door neighbor outreach, community flyer distribution, public-meeting convening, and sustained media engagement. The activists discovered that Google was registered for tax purposes at the location of its administrative offices (not the Cerrillos data-center site), so the community would not see direct tax benefit from the data center. Mosacat's framing was that Google was extracting freshwater from a community that retained one of the last public water resources in greater Santiago without giving the community any benefit in return.<br><br>"
        "<b>ESCALATION.</b> Activism escalated through three institutional levels. First, Google Chile sent representatives. Second, when the Chile-level engagement was inadequate, the activists escalated to Google Mountain View headquarters. Karen Hao reports that the Mountain View representatives sent to Chile in response only spoke English. Third, the activism reached the Chilean government, which established a roundtable convening community residents, Google representatives, and government officials.<br><br>"
        "<b>SANTIAGO ENVIRONMENTAL TRIBUNAL.</b> Santiago's environmental tribunal engaged the project, reviewing the water-use authorization in light of Mosacat's documentation of the Quilicura wetland's vulnerability to additional industrial water draw under ongoing drought conditions.<br><br>"
        "<b>GOOGLE'S TECHNOLOGY SWITCH.</b> After years of sustained activism, Google decided to use a less water-intensive cooling technology for the Cerrillos facility. The activists characterize this as a partial victory rather than a final resolution. Tania Rodríguez of Mosacat described the situation as extractivism and characterized the seat at the table as gained through pressure rather than offered as good faith.<br><br>"
        "<b>RELATIONSHIP TO TCKC PRIMARY COMMUNITIES.</b> The Cerrillos resistance affects Latiné communities directly through diaspora kinship between Chilean residents and U.S.-based Latiné communities. Indigenous Mapuche communities in southern Chile face parallel water-rights and territorial-rights pressures that intersect with broader extractive-industry patterns documented across Latin America. The case is a primary-source documentation of successful global-south frontline resistance to AI-data-center water extraction.<br><br>"
        "<b>RELATIONSHIP TO U.S. PARALLELS.</b> The Cerrillos resistance is the international parallel to Honor the Earth's No Data Center Coalition organizing on Indigenous lands in the United States (tracked at honor-the-earth-no-data-center-coalition-2026). Both cases demonstrate that organized community resistance can interrupt corporate AI-infrastructure-buildout projects, and both provide replicable tactical playbooks for adjacent communities.<br><br>"
        "<b>CULTURAL RESOURCE THREAT ASSESSMENT.</b> The threat level is PROTECTIVE. The Cerrillos community's organizing represents one of the most documented successful frontline resistances to U.S. tech-empire AI-data-center extraction. Its concrete outcomes (project blocked four to five years; less water-intensive technology adopted by Google; Santiago environmental tribunal engagement; community-corporation-government roundtable established) demonstrate that the AI-empire is not invulnerable. The case provides empirical support for Karen Hao's reclamation-of-agency thesis."
        "<br><br>"
        "<b>SOURCES.</b><br>"
        "Primary coverage: Rest of World, \"Data centers bring environmental concerns, like excess water use, to Chile,\" 2024. <a href=\"https://restofworld.org/2024/data-centers-environmental-issues/\">https://restofworld.org/2024/data-centers-environmental-issues/</a>; "
        "AlgorithmWatch, \"With Google as My Neighbor, Will There Still Be Water?\" <a href=\"https://algorithmwatch.org/en/protests-against-data-centers/\">https://algorithmwatch.org/en/protests-against-data-centers/</a>; "
        "Rest of World, \"From Chile to the Philippines, meet the people pushing back on AI,\" 2026. <a href=\"https://restofworld.org/2026/ai-pushback-chile-mexico-kenya-philippines/\">https://restofworld.org/2026/ai-pushback-chile-mexico-kenya-philippines/</a>; "
        "Business and Human Rights Resource Centre, \"Chile: Tech giants build dozens of data centers while activists raise environmental concerns.\" <a href=\"https://www.business-humanrights.org/en/latest-news/chile-tech-giants-build-dozens-of-data-centers-in-chile-while-activist-raise-environmental-concerns/\">https://www.business-humanrights.org/en/latest-news/chile-tech-giants-build-dozens-of-data-centers-in-chile-while-activist-raise-environmental-concerns/</a><br>"
        "Academic analysis: \"Divergent Futures in a Damaged Territory: The Rise of Data Centers and Water Conflicts in Santiago de Chile,\" Journal of Urban Technology, 2025. <a href=\"https://www.tandfonline.com/doi/full/10.1080/10630732.2025.2546784\">https://www.tandfonline.com/doi/full/10.1080/10630732.2025.2546784</a><br>"
        "Regional analysis: Mongabay, \"The Cloud vs. drought: Water hog data centers threaten Latin America, critics say,\" November 2023. <a href=\"https://news.mongabay.com/2023/11/the-cloud-vs-drought-water-hog-data-centers-threaten-latin-america-critics-say/\">https://news.mongabay.com/2023/11/the-cloud-vs-drought-water-hog-data-centers-threaten-latin-america-critics-say/</a>; "
        "Nearshore Americas, \"Water Scarcity Jeopardizes Data Center Projects in Chile and Uruguay.\" <a href=\"https://nearshoreamericas.com/water-scarcity-jeopardizes-data-center-projects-in-chile-and-uruguay/\">https://nearshoreamericas.com/water-scarcity-jeopardizes-data-center-projects-in-chile-and-uruguay/</a>; "
        "Nearshore Americas, \"Water-Guzzling Data Centers Spark Outrage Across Latin America.\" <a href=\"https://nearshoreamericas.com/water-guzzling-data-centers-spark-outrage-across-latin-america/\">https://nearshoreamericas.com/water-guzzling-data-centers-spark-outrage-across-latin-america/</a>; "
        "LatinAmerican Post, \"The Fight Over Water, Power, and the Future of AI In Chile's Data Desert.\" <a href=\"https://latinamericanpost.com/business-and-finance/the-fight-over-water-power-and-the-future-of-ai-in-chiles-data-desert/\">https://latinamericanpost.com/business-and-finance/the-fight-over-water-power-and-the-future-of-ai-in-chiles-data-desert/</a>; "
        "San Juan Daily Star, \"How Chile embodies AI's no-win politics.\" <a href=\"https://www.sanjuandailystar.com/post/how-chile-embodies-ai-s-no-win-politics\">https://www.sanjuandailystar.com/post/how-chile-embodies-ai-s-no-win-politics</a><br>"
        "Library reference: [INTERVIEW] Karen Hao on Empire of AI Threatening Democracy and Creating a New Colonial World - Democracy Now! (2025) [EN].md.<br>"
        "Related tracker entries: honor-the-earth-no-data-center-coalition-2026 (Honor the Earth, U.S. parallel); openai-for-countries-2025 (OpenAI for Countries, international AI infrastructure deployment); openai-sama-kenya-data-annotation-2023 (OpenAI Kenya labor)."
    ),
    "I": {
        "latine": {
            "people": "Chilean residents of Cerrillos, with diaspora kinship to U.S.-based Latiné communities, demonstrate replicable community organizing against U.S. tech-empire water extraction. The case is a model for Latiné and Latin American community organizing across the hemisphere.",
            "places": "Cerrillos commune of greater Santiago, the Quilicura wetlands, and the broader Santiago metropolitan freshwater system are the protected places.",
            "practices": "Mosacat's tactical playbook (door-to-door outreach, public meetings, escalation to corporate headquarters and government, environmental-tribunal engagement, multi-stakeholder roundtables) extends a replicable Latin American community-organizing tradition.",
            "treasures": "Public-water-resource access in greater Santiago is preserved through community organizing. The Quilicura wetlands ecosystem is protected from accelerated degradation."
        },
        "indigenous": {
            "people": "Mapuche and other Indigenous communities in Chile face parallel water-rights and territorial-rights pressures that the Cerrillos case implicitly engages.",
            "places": "Indigenous-affiliated water resources in Chile and parallel cases across Latin America benefit from the precedent.",
            "practices": "Indigenous water-rights and environmental-justice practice across Latin America gains a successful precedent.",
            "treasures": "Public-water-resource frameworks in post-Pinochet Chile face cumulative privatization pressure; the Cerrillos resistance defends a remaining public resource."
        },
        "allCommunities": {
            "people": "All communities globally facing AI-data-center siting benefit from the Cerrillos precedent.",
            "places": "Global community-organizing infrastructure against AI-data-center water draw gains a documented success case.",
            "practices": "International community-corporation-government roundtable practice as a tool for AI-infrastructure deliberation gains a precedent.",
            "treasures": "Global civil-society documentation of successful AI-empire resistance is a cultural-policy treasure."
        },
        "environmentalJustice": {
            "people": "Frontline environmental-justice communities globally benefit from the Cerrillos precedent and tactical playbook.",
            "places": "Environmental-justice neighborhoods proximate to AI-data-center proposals benefit from documented successful organizing.",
            "practices": "Environmental-justice organizing practice gains an international success case.",
            "treasures": "International environmental-justice movement institutional knowledge is preserved and extended through the Cerrillos resistance."
        }
    },
    "c": ["Latiné", "Indigenous", "All Communities", "environmentalJustice"],
    "U": "https://restofworld.org/2024/data-centers-environmental-issues/",
    "_source": "manual",
}


def main():
    if not DATA_PATH.exists():
        raise SystemExit(f"data.json not found at {DATA_PATH}")

    em_dash = "—"
    for label, e in [("A", ENTRY_A), ("B", ENTRY_B)]:
        if em_dash in json.dumps(e, ensure_ascii=False):
            raise SystemExit(f"ABORT: em-dash detected in entry {label} ({e['i']}).")

    shutil.copy2(DATA_PATH, BACKUP_PATH)
    print(f"Backup written: {BACKUP_PATH.name}")

    with DATA_PATH.open() as f:
        data = json.load(f)

    # Per Prince's directive 2026-04-30: only A (state AI preemption EO) and
    # B (TMTG-TAE merger). Entries C (Kenya OpenAI/Sama labor) and D (Chile
    # Cerrillos Mosacat) drafted but not added per Prince's nomination response.
    targets = [
        ("executive_actions", ENTRY_A),
        ("other_domestic", ENTRY_B),
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
