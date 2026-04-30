#!/usr/bin/env python3
"""Add three discrete entries documenting the April 2026 attack on the
Presidential Records Act.

Entries:
1. OLC Slip Opinion (April 1, 2026) declaring the PRA facially
   unconstitutional. Author: Assistant Attorney General T. Elliot Gaiser,
   Office of Legal Counsel, U.S. Department of Justice. Category:
   agency_actions. Threat: SEVERE.

2. Warrington White House Counsel Memo (April 2, 2026) instructing EOP
   staff that PRA preservation rules are now discretionary. Author:
   White House Counsel David Alan Warrington. Category: executive_actions.
   Threat: SEVERE.

3. AHA + American Oversight v. Trump (filed April 7, 2026) in U.S.
   District Court for the District of Columbia, challenging the OLC
   opinion and the Warrington memo. Category: litigation.
   Threat: PROTECTIVE.

Cross-references each other and existing related entries:
- nara-archivist-firing / v2025-nara-001: Shogan firing (2025-02-07)
- nara-rubio-byron-appointment / v2025-nara-002: Rubio acting archivist + Byron Nixon Foundation appointment
- nara-presidential-library-firings / v2025-nara-003: Presidential library staff firings
- nara-rif-layoffs / v2025-nara-005: NARA RIF
- v2025-nara-004: American Oversight Signal-Gate lawsuit (2025-03-25)
"""
import json
import shutil
from pathlib import Path
from datetime import datetime

DATA_PATH = Path(__file__).parent.parent / "data" / "data.json"
BACKUP_PATH = DATA_PATH.with_suffix(
    f".json.bak-{datetime.now().strftime('%Y%m%d-%H%M%S')}-pre-pra-package"
)


# =================== ENTRY 1: OLC OPINION ===================
OLC_ENTRY = {
    "i": "olc-pra-unconstitutional-2026",
    "t": "OLC Slip Opinion",
    "n": "DOJ-OLC Slip Opinion: Constitutionality of the Presidential Records Act (April 1, 2026)",
    "T": '<span style="color: #991B1B;">DOJ Office of Legal Counsel:</span> Slip Opinion Declaring the Presidential Records Act of 1978 Facially Unconstitutional',
    "s": "OLC opinion: PRA unconstitutional",
    "d": "2026-04-01",
    "a": "Trump II",
    "A": ["DOJ", "OLC"],
    "S": "Active. Slip opinion issued April 1, 2026 by Assistant Attorney General T. Elliot Gaiser, Office of Legal Counsel, U.S. Department of Justice. Operative within the Executive Branch as binding internal legal guidance. Under judicial challenge in AHA and American Oversight v. Trump (D.D.C.), filed April 7, 2026.",
    "L": "SEVERE",
    "D": (
        "<b>OLC SLIP OPINION.</b> On April 1, 2026, T. Elliot Gaiser, the Assistant Attorney General in the Office of Legal Counsel (OLC) of the U.S. Department of Justice, issued a slip opinion concluding that the Presidential Records Act of 1978 (44 U.S.C. §§ 2201 et seq.) is facially unconstitutional. The opinion runs four single-spaced pages of analysis. It is published as a slip opinion on the DOJ-OLC website and operates as binding internal legal guidance within the Executive Branch.<br><br>"
        "<b>HOLDING.</b> The OLC concludes that the Presidential Records Act is unconstitutional for two independent but interlocking reasons. First, the Act \"exceeds Congress's enumerated and implied powers.\" Second, it \"aggrandizes the Legislative Branch at the expense of the constitutional independence and autonomy of the Executive.\" The opinion further asserts, in operative terms, that President Donald Trump \"need not further comply\" with the Act's requirements.<br><br>"
        "<b>HISTORICAL ARGUMENT.</b> The OLC argues from history and tradition that, before the Presidential Recordings and Materials Preservation Act of 1974 and the Presidential Records Act of 1978, presidents owned and controlled their own papers. \"Over the first two centuries of the American experiment in self-government,\" the opinion states, \"Presidents owned and controlled presidential papers, and Congress obtained such papers through political negotiation and interbranch accommodation, rather than as a matter of right.\" The opinion treats the modern statutory regime as a departure from this longstanding practice and reads that departure as constitutionally suspect.<br><br>"
        "<b>ABSENCE OF JUDICIAL SUPPORT.</b> The OLC opinion cites no judicial precedent in support of its conclusion. The Supreme Court has previously rejected separation-of-powers challenges to presidential-records statutes, including in Nixon v. Administrator of General Services, 433 U.S. 425 (1977), which upheld the Presidential Recordings and Materials Preservation Act against an attack on similar grounds. The OLC opinion does not address Nixon v. Administrator of General Services on its merits.<br><br>"
        "<b>STATUTORY BACKGROUND.</b> Congress enacted the Presidential Records Act in 1978 in direct response to the Watergate-era concern that President Richard Nixon would destroy his presidential records. The Act establishes that presidential records are public property, requires the White House to preserve all official materials, and directs the National Archives and Records Administration (NARA) to take custody of those records when a president leaves office. Until April 1, 2026, the Act's constitutionality had gone largely unchallenged for nearly five decades.<br><br>"
        "<b>OPERATIONAL EFFECT.</b> The OLC opinion is binding internal Executive Branch legal guidance unless and until withdrawn by OLC or set aside by a federal court. Within hours of issuance, the White House Counsel began work on implementation. On April 2, 2026, White House Counsel David Alan Warrington circulated a memo to all EOP staff replacing the existing mandatory PRA preservation regime with discretionary guidance. (Tracked separately at olc-pra-warrington-memo-2026.)<br><br>"
        "<b>RELATIONSHIP TO PRIOR NARA DESTABILIZATION.</b> The OLC opinion arrives a little more than a year after the Trump administration's effort to remove and replace the leadership of the National Archives and Records Administration. Archivist of the United States Colleen J. Shogan, a Biden appointee confirmed by the Senate in 2023, was fired at Trump's direction on February 7, 2025 (tracked at nara-archivist-firing / v2025-nara-001). Marco Rubio was named Acting Archivist on February 14, 2025 with Nixon Foundation president Jim Byron installed as senior advisor (tracked at nara-rubio-byron-appointment / v2025-nara-002). NARA underwent staff firings at presidential libraries on February 18, 2025 (tracked at nara-presidential-library-firings / v2025-nara-003) and a 100+ employee Reduction-in-Force on April 15, 2025 (tracked at nara-rif-layoffs). The OLC opinion is the doctrinal capstone on a year-long campaign of institutional destabilization at the federal recordkeeping infrastructure.<br><br>"
        "<b>CULTURAL RESOURCE THREAT ASSESSMENT.</b> The threat level is SEVERE. Presidential records constitute the documentary substrate through which the federal government's treatment of culturally vulnerable communities is established, audited, and remembered. Records of federal Indian policy decisions, of civil rights enforcement, of immigration enforcement, of cultural-property repatriation negotiations, of treaty implementation, and of executive responses to community petitions are all created and held under the Presidential Records Act. A doctrine that allows a president to selectively preserve, destroy, or privately retain those records strikes at the foundation of historical accountability for the policies that shape the cultural continuity of African-descendant, Indigenous, Latiné, Asian, and Pacific Islander communities. The harm is direct, near-term, and partially irreversible. Records destroyed or privately retained cannot be recovered by court order against a former president without protracted litigation."
        "<br><br>"
        "<b>SOURCES.</b><br>"
        "Primary source: U.S. Department of Justice, Office of Legal Counsel, Slip Opinion, \"Constitutionality of the Presidential Records Act,\" April 1, 2026. <a href=\"https://www.justice.gov/olc/media/1434131/dl\">https://www.justice.gov/olc/media/1434131/dl</a><br>"
        "Independent legal analysis: Just Security, \"The Presidential Records Act is Constitutional.\" <a href=\"https://www.justsecurity.org/136242/presidential-records-act-constitutional/\">https://www.justsecurity.org/136242/presidential-records-act-constitutional/</a><br>"
        "News coverage: The Washington Post, \"Justice Dept. says the Presidential Records Act is unconstitutional,\" April 2, 2026. <a href=\"https://www.washingtonpost.com/national-security/2026/04/02/trump-doj-presidential-records-act/\">https://www.washingtonpost.com/national-security/2026/04/02/trump-doj-presidential-records-act/</a>; "
        "CNN, \"Trump's DOJ tells Trump he can hold onto government docs when he leaves office, contrary to Watergate-era law,\" April 3, 2026. <a href=\"https://www.cnn.com/2026/04/03/politics/trump-presidential-records-act-watergate\">https://www.cnn.com/2026/04/03/politics/trump-presidential-records-act-watergate</a>; "
        "Salon, \"DOJ Presidential Records Act argument threatens to send us back to time of presidents burning papers,\" April 17, 2026. <a href=\"https://www.salon.com/2026/04/17/doj-presidential-records-act-argument-threatens-to-send-us-back-to-time-of-presidents-burning-papers-partner/\">https://www.salon.com/2026/04/17/doj-presidential-records-act-argument-threatens-to-send-us-back-to-time-of-presidents-burning-papers-partner/</a>; "
        "The Conversation, \"A justice department opinion arguing the Presidential Records Act is unconstitutional could revert the nation to a time when presidents freely burned their papers.\" <a href=\"https://theconversation.com/a-justice-department-opinion-arguing-the-presidential-records-act-is-unconstitutional-could-revert-the-nation-to-a-time-when-presidents-freely-burned-their-papers-280078\">https://theconversation.com/a-justice-department-opinion-arguing-the-presidential-records-act-is-unconstitutional-could-revert-the-nation-to-a-time-when-presidents-freely-burned-their-papers-280078</a>; "
        "First Amendment Encyclopedia, \"Presidential Records Act and Department of Justice Challenge.\" <a href=\"https://firstamendment.mtsu.edu/article/presidential-records-act-and-department-of-justice-challenge/\">https://firstamendment.mtsu.edu/article/presidential-records-act-and-department-of-justice-challenge/</a><br>"
        "Related tracker entries: olc-pra-warrington-memo-2026 (Warrington WH Counsel implementation memo, 2026-04-02); aha-american-oversight-v-trump-2026 (AHA + American Oversight lawsuit, filed 2026-04-07); nara-archivist-firing / v2025-nara-001 (Shogan firing, 2025-02-07); nara-rubio-byron-appointment / v2025-nara-002 (Rubio + Byron appointments, 2025-02-14); nara-presidential-library-firings / v2025-nara-003 (presidential library staff firings, 2025-02-18); nara-rif-layoffs / v2025-nara-005 (NARA RIF, 2025-04-15); v2025-nara-004 (American Oversight Signal-Gate lawsuit, 2025-03-25)."
    ),
    "I": {
        "allCommunities": {
            "people": "Every American whose civil rights, citizenship, immigration status, treaty status, federal benefits, or cultural-property claims pass through Executive Branch decision-making is affected. Presidential records are the documentary record of those decisions. A doctrine that allows selective preservation or destruction of those records weakens public oversight of every cultural community's relationship with the federal government.",
            "places": "The National Archives and Records Administration (NARA) facilities in Washington and College Park, the system of presidential libraries across the country, and federal records centers nationwide depend on the PRA's mandatory transfer regime to receive presidential records at the close of each administration. The OLC opinion threatens that transfer regime.",
            "practices": "Archival practice, historical scholarship, descendant-community memory work, investigative journalism, and FOIA-based public-interest litigation all rely on the public character of presidential records under the PRA. The OLC opinion threatens each of these practices.",
            "treasures": "The presidential records of the Trump II administration constitute a unique cultural treasure whose preservation the OLC opinion places in doubt. Records of decisions affecting culturally vulnerable communities are most at risk of being unwritten, destroyed, or privately retained."
        },
        "indigenous": {
            "people": "Indigenous nations rely on presidential records to document the federal trust relationship, treaty implementation, federal Indian policy decisions, NAGPRA negotiations, and presidential responses to tribal petitions. The OLC opinion threatens the documentary basis on which Indigenous nations defend their rights against federal action.",
            "places": "Records concerning federal management of tribal lands, sacred sites, and cultural-heritage properties are presidential records under the PRA. Their selective preservation or destruction harms tribal place-based rights claims.",
            "practices": "Federal-Indian-policy practice and treaty-implementation practice depend on documentary records held in the federal recordkeeping system. Tribal historical scholarship and intergenerational memory work depend on access to those records.",
            "treasures": "Records concerning ancestral remains repatriation, sacred-object disposition, and cultural-heritage property under federal control are presidential records vulnerable to the OLC opinion's loosening of preservation requirements."
        },
        "africanDescendant": {
            "people": "African-descendant communities rely on presidential records to document civil rights enforcement, federal responses to racial-justice claims, cabinet-level decisions on voting rights, FBI and DOJ investigations of civil rights cold cases, and responses to community petitions. Patrick Eddington of the Cato Institute has argued that the OLC opinion could make voter-suppression efforts harder to detect; that argument applies with particular force to Black communities most affected by voter-suppression efforts.",
            "places": "Civil Rights Cold Case Records reviewed under the Civil Rights Cold Case Records Collection Act depend on the National Archives' authority to take custody of presidential records. The OLC opinion threatens that custodial chain.",
            "practices": "Black historical scholarship, civil rights legal practice, descendant-community memory work, and the practice of holding federal civil rights enforcement accountable through documentary records depend on the PRA. The OLC opinion threatens each of these practices.",
            "treasures": "Presidential records concerning civil rights enforcement, voting rights enforcement, and federal responses to racial violence are part of the documentary inheritance of African-descendant communities. The OLC opinion threatens that inheritance."
        },
        "latine": {
            "people": "Latiné communities rely on presidential records to document immigration policy decisions, deportation enforcement decisions, executive responses to border-policy litigation, and presidential decisions affecting Puerto Rico and other U.S. territories. The OLC opinion threatens the documentary basis for accountability over these decisions.",
            "places": "Records concerning federal management of border facilities, detention centers, and U.S. territorial relationships are presidential records under the PRA.",
            "practices": "Immigration-law scholarship, civil rights practice, and descendant-community memory work depend on access to presidential records.",
            "treasures": "Records of federal decisions concerning Latiné communities, including responses to civil rights petitions and disaster-response decisions affecting Puerto Rico, are part of the documentary inheritance vulnerable to the OLC opinion."
        },
        "asianAmerican": {
            "people": "Asian American communities rely on presidential records to document immigration enforcement decisions, federal responses to anti-Asian hate, and decisions affecting Chinese, Japanese, Korean, Vietnamese, South Asian, and Southeast Asian communities. Historical records concerning Japanese internment redress under the Civil Liberties Act of 1988 depend on the federal recordkeeping regime.",
            "places": "Records concerning federal management of Japanese internment site memorials and other Asian American historic sites are presidential and federal records under the PRA and adjacent regimes.",
            "practices": "Asian American historical scholarship, civil rights practice, and intergenerational memory work concerning federal treatment of Asian communities depend on access to presidential records.",
            "treasures": "The documentary record of federal decisions affecting Asian American communities, including immigration policy and civil rights enforcement, is vulnerable to the OLC opinion."
        },
        "pacificIslander": {
            "people": "Pacific Islander communities, including those under Compact of Free Association arrangements (Marshall Islands, Federated States of Micronesia, Palau) and U.S. territorial residents (Hawaii, Guam, American Samoa, Northern Marianas), rely on presidential records to document the federal trust relationship, COFA negotiations, and territorial governance decisions.",
            "places": "Records concerning federal management of U.S. territorial relationships, military-base land returns, and Pacific cultural-heritage sites are presidential records under the PRA.",
            "practices": "Pacific Islander historical scholarship, sovereignty practice, and intergenerational memory work concerning federal treatment of Pacific communities depend on access to presidential records.",
            "treasures": "Records concerning nuclear-testing-era federal decisions affecting Marshallese communities, military-base land disposition in Guam and Hawaii, and federal responses to climate-displacement claims are all part of the documentary inheritance vulnerable to the OLC opinion."
        }
    },
    "c": ["All Communities", "Indigenous", "African-descendant", "Latiné", "Asian", "Pacific Islander", "academicCommunity"],
    "U": "https://www.justice.gov/olc/media/1434131/dl",
    "_source": "manual",
}


# =================== ENTRY 2: WARRINGTON MEMO ===================
WARRINGTON_ENTRY = {
    "i": "olc-pra-warrington-memo-2026",
    "t": "Presidential Memorandum",
    "n": "White House Counsel Memo: Records Preservation Policy (April 2, 2026)",
    "T": '<span style="color: #991B1B;">White House Counsel Memo:</span> EOP Records-Preservation Rules Made Discretionary Following OLC Opinion',
    "s": "WH Counsel Warrington records-preservation memo",
    "d": "2026-04-02",
    "a": "Trump II",
    "A": ["EOP", "WH Counsel"],
    "S": "Active. Memo issued April 2, 2026 by White House Counsel David Alan Warrington to all Executive Office of the President staff. Released publicly through court filings in AHA and American Oversight v. Trump (D.D.C.). Operative as internal EOP guidance.",
    "L": "SEVERE",
    "D": (
        "<b>WH COUNSEL MEMO.</b> On April 2, 2026, the day after the OLC issued its slip opinion declaring the Presidential Records Act unconstitutional, White House Counsel David Alan Warrington circulated a memorandum to all Executive Office of the President (EOP) staff. The memo replaces the prior mandatory PRA-compliance regime with discretionary preservation guidance and was followed by a mandatory training. The memo was made public through court filings in AHA and American Oversight v. Trump (D.D.C.).<br><br>"
        "<b>FRAMING.</b> Warrington characterizes the Presidential Records Act as \"a significant departure from historical practice\" and grounds the new policy in the OLC opinion's conclusion that the Act is unconstitutional. The memo is framed as guidance rather than as a legal mandate. The administration nominally instructs staff to preserve records that may be needed in future litigation while removing the categorical preservation duty the PRA imposes.<br><br>"
        "<b>WEAKENED LANGUAGE: \"REQUIRED\" TO \"SHOULD\".</b> The 2017 White House records-preservation memo, in effect during President Trump's first term, used categorical language. It instructed staff that they were \"required to conduct all work-related communications on your official EOP email account, except in emergency circumstances.\" The April 2, 2026 memo uses discretionary language. EOP staff \"should\" conduct work-related communications on official accounts. EOP staff \"should\" avoid using personal devices for official government business \"whenever possible.\"<br><br>"
        "<b>WEAKENED PERSONAL-DEVICE CAPTURE RULE.</b> The 2017 memo required staff to forward to an official platform within 20 days, by screenshot or other means, any official-business material sent to or from personal accounts. It warned that \"any employee who intentionally fails to take these actions may be subject to administrative or even criminal penalties.\" The April 2, 2026 memo instead requires preservation only \"when they are the sole record of official decision-making, government action, or contain unique information not available elsewhere.\" Staffers are \"encouraged\" to memorialize the substance of personal-device exchanges in a memo or email rather than to capture the underlying exchange. Patrick Eddington of the Cato Institute observed that this approach \"is a great way to rewrite history.\"<br><br>"
        "<b>EOP COMPONENTS \"FREE TO RETAIN\" OR DISCARD PRIOR POLICIES.</b> The memo states that EOP components are \"free to retain\" their previous record-preservation policies. As University of Maryland archives-and-law professor Jason R. Baron has noted, the language also leaves them free not to. Baron concluded that \"while paying lip service to the need to preserve White House records, the memo actually gives EOP staff license to do the exact opposite.\" Baron further noted that nothing in the policy \"prevents the White House from directing the transfer or destruction of White House records, including tens of millions of e-mails, either before or after the end of the president's second term in office.\"<br><br>"
        "<b>WHAT THE MEMO DOES NOT ADDRESS.</b> The memo does not outline how President Trump or Vice President JD Vance personally should preserve records. The White House has not stated whether Trump intends to transfer his presidential records to NARA when he leaves office.<br><br>"
        "<b>SIGNAL DEPLOYMENT.</b> A White House official told The Washington Post on background that staff have been instructed to perform all work on their work device and that an approved Signal app can be downloaded onto White House phones, with assurances that Signal saves messages on those devices. Signal's default disappearing-messages and end-to-end-encryption features have been at the center of separate federal records litigation tracked at v2025-nara-004 (American Oversight Signal-Gate lawsuit, 2025-03-25).<br><br>"
        "<b>RELATIONSHIP TO OLC OPINION.</b> The Warrington memo is the operational implementation of the OLC opinion (tracked at olc-pra-unconstitutional-2026). The OLC opinion supplies the legal cover. The Warrington memo is the discretionary regime that replaces PRA compliance inside the EOP.<br><br>"
        "<b>CULTURAL RESOURCE THREAT ASSESSMENT.</b> The threat level is SEVERE. Discretionary preservation by an administration with established records-destruction patterns produces predictable selective loss. Records most likely to be destroyed or omitted are those documenting decisions adverse to culturally vulnerable communities: civil rights enforcement choices, immigration-enforcement directives, decisions affecting Indigenous trust obligations, and federal responses to community petitions. The shift from mandatory to discretionary preservation is the institutional mechanism by which selective loss becomes possible at scale."
        "<br><br>"
        "<b>SOURCES.</b><br>"
        "Primary source: White House Counsel David Alan Warrington, memorandum to EOP staff regarding records preservation policy, April 2, 2026 (released through court filings in AHA and American Oversight v. Trump, D.D.C.).<br>"
        "Secondary coverage: The Washington Post (via Detroit News), Maegan Vazquez, \"White House eases mandatory requirements for preserving presidential records,\" April 24, 2026. <a href=\"https://www.detroitnews.com/story/news/nation/2026/04/24/white-house-eases-mandatory-requirements-preserving-presidential-records/89769450007/\">https://www.detroitnews.com/story/news/nation/2026/04/24/white-house-eases-mandatory-requirements-preserving-presidential-records/89769450007/</a>; "
        "CNN, \"White House tells court it's preserving presidential records even though DOJ said law is unconstitutional,\" April 22, 2026. <a href=\"https://www.cnn.com/2026/04/22/politics/white-house-presidential-records-act\">https://www.cnn.com/2026/04/22/politics/white-house-presidential-records-act</a>; "
        "KBNW (Horizon Broadcasting Group), \"Senate Democrats press White House over loosened record-keeping policy,\" April 30, 2026. <a href=\"https://www.kbnwnews.com/2026/04/30/senate-democrats-press-white-house-over-loosened-record-keeping-policy/\">https://www.kbnwnews.com/2026/04/30/senate-democrats-press-white-house-over-loosened-record-keeping-policy/</a><br>"
        "Related tracker entries: olc-pra-unconstitutional-2026 (OLC opinion of 2026-04-01); aha-american-oversight-v-trump-2026 (AHA + American Oversight lawsuit, filed 2026-04-07); v2025-nara-004 (American Oversight Signal-Gate lawsuit, 2025-03-25); nara-archivist-firing / v2025-nara-001 (Shogan firing, 2025-02-07); nara-rubio-byron-appointment / v2025-nara-002 (Rubio + Byron appointments, 2025-02-14)."
    ),
    "I": {
        "allCommunities": {
            "people": "Every American who interacts with federal Executive Branch policymaking is affected. The discretionary preservation regime gives EOP staff license to omit, lose, or destroy records of the very decisions that constitute the federal-government's relationship with the public.",
            "places": "NARA facilities and presidential libraries that depend on a complete records transfer at the close of the administration face a discretionary, partial transfer.",
            "practices": "Investigative journalism, FOIA litigation, oversight investigations, congressional inquiry, and historical scholarship all depend on the predictable preservation of presidential records. The Warrington memo erodes the predictability that enables these practices.",
            "treasures": "The documentary record of the Trump II administration is the cultural treasure most directly threatened by the discretionary preservation regime."
        },
        "indigenous": {
            "people": "Indigenous communities rely on Executive Branch decision-records to defend treaty rights, federal trust obligations, and cultural-heritage claims. Records of those decisions are now subject to discretionary preservation.",
            "places": "Tribal lands, sacred sites, and cultural-heritage properties whose federal management is documented in EOP records face documentation gaps.",
            "practices": "Federal-Indian-law practice depends on the documentary record. Discretionary preservation undermines that practice.",
            "treasures": "Records of repatriation negotiations, sacred-object disposition, and cultural-heritage property under federal control are now under discretionary preservation."
        },
        "africanDescendant": {
            "people": "African-descendant communities rely on Executive Branch decision-records to defend voting rights, civil rights, and protection from racial violence. Patrick Eddington of the Cato Institute argued specifically that the discretionary regime could make voter-suppression efforts harder to detect.",
            "places": "Civil rights cold case records and federal civil rights enforcement records depend on robust preservation across the EOP.",
            "practices": "Civil rights legal practice, Black historical scholarship, and descendant-community memory work depend on the documentary record.",
            "treasures": "Records of federal responses to racial justice claims and civil rights enforcement decisions are now subject to discretionary preservation."
        },
        "latine": {
            "people": "Latiné communities rely on Executive Branch decision-records to document immigration enforcement, deportation decisions, and territorial governance affecting Puerto Rico and other U.S. territories.",
            "places": "Records of federal management of border facilities, detention centers, and territorial relationships are subject to discretionary preservation.",
            "practices": "Immigration-law scholarship and civil rights practice depend on the documentary record.",
            "treasures": "Records of decisions concerning Latiné communities, including disaster-response decisions affecting Puerto Rico, are now under discretionary preservation."
        },
        "asianAmerican": {
            "people": "Asian American communities rely on Executive Branch decision-records to document immigration enforcement and federal responses to anti-Asian hate.",
            "places": "Records of federal management of Asian American historic sites and memorials are subject to discretionary preservation.",
            "practices": "Asian American historical scholarship and civil rights practice depend on the documentary record.",
            "treasures": "Records of federal decisions affecting Asian communities are now under discretionary preservation."
        },
        "pacificIslander": {
            "people": "Pacific Islander communities, including those under COFA and U.S. territorial residents, rely on Executive Branch decision-records to document the federal trust relationship and territorial governance.",
            "places": "Records of federal management of territorial relationships, military-base land disposition, and Pacific cultural-heritage sites are subject to discretionary preservation.",
            "practices": "Pacific Islander sovereignty practice and historical scholarship depend on the documentary record.",
            "treasures": "Records of nuclear-testing-era federal decisions, military-base land disposition, and federal responses to climate-displacement claims are now under discretionary preservation."
        }
    },
    "c": ["All Communities", "Indigenous", "African-descendant", "Latiné", "Asian", "Pacific Islander", "academicCommunity"],
    "U": "https://www.detroitnews.com/story/news/nation/2026/04/24/white-house-eases-mandatory-requirements-preserving-presidential-records/89769450007/",
    "_source": "manual",
}


# =================== ENTRY 3: AHA + AMERICAN OVERSIGHT LAWSUIT ===================
LAWSUIT_ENTRY = {
    "i": "aha-american-oversight-v-trump-2026",
    "t": "Court Filing",
    "n": "American Historical Association and American Oversight v. Trump (D.D.C., filed April 7, 2026)",
    "T": '<span style="color: #065F46;">AHA and American Oversight v. Trump:</span> Federal Lawsuit Challenging OLC Opinion and Warrington Memo',
    "s": "AHA + American Oversight PRA lawsuit",
    "d": "2026-04-07",
    "a": "Trump II",
    "A": ["DOJ", "OLC", "EOP"],
    "S": "Active. Filed April 7, 2026 in U.S. District Court for the District of Columbia by the American Historical Association and American Oversight. Plaintiffs subsequently filed a preliminary injunction motion. Citizens for Responsibility and Ethics in Washington (CREW) has signaled it intends to pursue separate litigation.",
    "L": "PROTECTIVE",
    "D": (
        "<b>LAWSUIT.</b> On April 7, 2026, the American Historical Association (AHA), the largest membership association of historians in the world, and American Oversight, a nonprofit government-records-access watchdog, filed suit in the U.S. District Court for the District of Columbia challenging the OLC opinion of April 1, 2026 (tracked at olc-pra-unconstitutional-2026) and the Warrington White House Counsel memo of April 2, 2026 (tracked at olc-pra-warrington-memo-2026).<br><br>"
        "<b>RELIEF SOUGHT.</b> The complaint asks the court to (1) declare the Presidential Records Act of 1978 constitutional; (2) block the Trump administration from relying on the OLC opinion as a basis for non-compliance with the PRA; and (3) compel compliance with the Act's preservation, transfer, and public-access requirements. Plaintiffs subsequently filed a preliminary injunction motion seeking interim relief while the case proceeds.<br><br>"
        "<b>LEGAL THEORY.</b> The complaint argues that the OLC opinion \"relies on virtually no judicial authority and defies binding Supreme Court precedent outright.\" Plaintiffs cite Nixon v. Administrator of General Services, 433 U.S. 425 (1977), in which the Supreme Court rejected separation-of-powers challenges to a presidential-records statute on grounds materially indistinguishable from those the OLC now advances. The complaint characterizes the OLC opinion as \"a radical attempt to nullify a law that has governed presidential records for nearly half a century.\"<br><br>"
        "<b>PLAINTIFFS' STATEMENTS.</b> AHA leadership stated that \"presidential records are essential for transparency and accountability in our democracy; they are also essential sources for researching and understanding the American past.\" American Oversight executive director Chioma Chukwu stated that \"the Trump administration is inviting the selective preservation of presidential records, which is inconsistent with the law.\"<br><br>"
        "<b>PARALLEL LITIGATION SIGNALED.</b> CREW (Citizens for Responsibility and Ethics in Washington) has indicated it will pursue separate litigation. CREW senior litigation counsel Jon Maier stated that the new records policy is \"inconsistent\" with the PRA and that the administration \"doesn't get to pick and choose which parts of the law it wants to follow.\"<br><br>"
        "<b>RELATIONSHIP TO PRIOR PRA-ENFORCEMENT LITIGATION.</b> American Oversight previously sued in March 2025 over the Trump II administration's use of Signal for federal communications and the resulting failure to preserve those communications under the PRA (tracked at v2025-nara-004). The April 2026 lawsuit is the second major American Oversight PRA-enforcement suit of the Trump II administration and addresses the doctrinal question (constitutionality of the Act itself) that the Signal-Gate suit could not reach.<br><br>"
        "<b>CULTURAL RESOURCE THREAT ASSESSMENT.</b> The threat level is PROTECTIVE. The lawsuit, if successful, would restore the categorical preservation regime under which presidential records concerning federal decisions affecting culturally vulnerable communities are preserved and made publicly available. The case is the principal judicial vehicle through which the OLC opinion can be set aside. A preliminary injunction would arrest selective records destruction while the constitutional question is litigated."
        "<br><br>"
        "<b>SOURCES.</b><br>"
        "Primary sources (plaintiff statements): "
        "American Historical Association, \"AHA Files Lawsuit to Defend the Presidential Records Act.\" <a href=\"https://www.historians.org/news/aha-files-lawsuit-to-defend-the-presidential-records-act/\">https://www.historians.org/news/aha-files-lawsuit-to-defend-the-presidential-records-act/</a>; "
        "American Historical Association, \"AHA, American Oversight File Preliminary Injunction in Presidential Records Act Lawsuit.\" <a href=\"https://www.historians.org/news/aha-american-oversight-file-preliminary-injunction-in-presidential-records-act-lawsuit/\">https://www.historians.org/news/aha-american-oversight-file-preliminary-injunction-in-presidential-records-act-lawsuit/</a>; "
        "American Oversight, \"American Oversight and Historians Sue to Block Trump's Effort to Evade Presidential Records Law.\" <a href=\"https://americanoversight.org/american-oversight-and-historians-sue-to-block-trumps-effort-to-evade-presidential-records-law/\">https://americanoversight.org/american-oversight-and-historians-sue-to-block-trumps-effort-to-evade-presidential-records-law/</a><br>"
        "Secondary coverage: CBS News, \"Lawsuit challenges Justice Department memo that declared presidential records law unconstitutional.\" <a href=\"https://www.cbsnews.com/news/justice-department-memo-presidential-records-act-lawsuit/\">https://www.cbsnews.com/news/justice-department-memo-presidential-records-act-lawsuit/</a>; "
        "New York Almanack, \"Watchdog, Historians Sue to Block Trump Effort to Evade Presidential Records Law.\" <a href=\"https://www.newyorkalmanack.com/2026/04/trump-presidential-records-suit/\">https://www.newyorkalmanack.com/2026/04/trump-presidential-records-suit/</a>; "
        "News Channel 3-12 (KEYT), \"Historians and oversight group challenge Justice Department's rewriting of federal preservation law,\" April 7, 2026. <a href=\"https://keyt.com/news/crime/2026/04/07/historians-and-oversight-group-challenge-justice-departments-rewriting-of-federal-preservation-law/\">https://keyt.com/news/crime/2026/04/07/historians-and-oversight-group-challenge-justice-departments-rewriting-of-federal-preservation-law/</a><br>"
        "Related tracker entries: olc-pra-unconstitutional-2026 (OLC opinion of 2026-04-01); olc-pra-warrington-memo-2026 (Warrington WH Counsel memo of 2026-04-02); v2025-nara-004 (American Oversight Signal-Gate lawsuit, 2025-03-25); nara-archivist-firing / v2025-nara-001 (Shogan firing, 2025-02-07); lit-2026-neh-acls-lawsuit (parallel scholarly-association federal-records litigation)."
    ),
    "I": {
        "allCommunities": {
            "people": "All Americans benefit from a successful judicial defense of the PRA. The lawsuit's success would preserve public access to the documentary record of federal decision-making across every domain of American life.",
            "places": "NARA facilities and presidential libraries depend on the categorical PRA transfer regime. The lawsuit defends the legal basis for that transfer.",
            "practices": "Historical scholarship, investigative journalism, FOIA practice, oversight investigation, and descendant-community memory work all benefit from a successful defense of the PRA.",
            "treasures": "The presidential records of every administration are the cultural treasure the lawsuit seeks to protect."
        },
        "indigenous": {
            "people": "Indigenous communities benefit from preserved access to records of federal Indian policy decisions, treaty implementation, and cultural-heritage negotiations.",
            "places": "Records concerning federal management of tribal lands and sacred sites are preserved if the lawsuit succeeds.",
            "practices": "Federal-Indian-law practice and tribal historical scholarship depend on the documentary record the lawsuit defends.",
            "treasures": "Records of NAGPRA negotiations and other cultural-heritage federal decisions are preserved if the lawsuit succeeds."
        },
        "africanDescendant": {
            "people": "African-descendant communities benefit from preserved access to records of civil rights enforcement, voting rights enforcement, and federal responses to racial-justice claims.",
            "places": "Civil rights cold case records and federal civil rights enforcement records depend on the categorical preservation regime the lawsuit defends.",
            "practices": "Civil rights legal practice and Black historical scholarship benefit from a successful defense of the PRA.",
            "treasures": "Records of federal responses to racial-justice claims are preserved if the lawsuit succeeds."
        },
        "latine": {
            "people": "Latiné communities benefit from preserved access to records of immigration enforcement, deportation decisions, and territorial governance affecting Puerto Rico and other U.S. territories.",
            "places": "Records of federal management of border facilities and territorial relationships are preserved if the lawsuit succeeds.",
            "practices": "Immigration-law scholarship and civil rights practice depend on the documentary record the lawsuit defends.",
            "treasures": "Records of federal decisions concerning Latiné communities are preserved if the lawsuit succeeds."
        },
        "asianAmerican": {
            "people": "Asian American communities benefit from preserved access to records of immigration enforcement and federal responses to anti-Asian hate.",
            "places": "Records of federal management of Asian American historic sites are preserved if the lawsuit succeeds.",
            "practices": "Asian American historical scholarship benefits from a successful defense of the PRA.",
            "treasures": "Records of federal decisions affecting Asian communities are preserved if the lawsuit succeeds."
        },
        "pacificIslander": {
            "people": "Pacific Islander communities benefit from preserved access to records of the federal trust relationship and territorial governance.",
            "places": "Records of federal management of territorial relationships and Pacific cultural-heritage sites are preserved if the lawsuit succeeds.",
            "practices": "Pacific Islander sovereignty practice depends on the documentary record the lawsuit defends.",
            "treasures": "Records of nuclear-testing-era federal decisions and federal responses to climate-displacement claims are preserved if the lawsuit succeeds."
        }
    },
    "c": ["All Communities", "Indigenous", "African-descendant", "Latiné", "Asian", "Pacific Islander", "academicCommunity"],
    "U": "https://americanoversight.org/american-oversight-and-historians-sue-to-block-trumps-effort-to-evade-presidential-records-law/",
    "_source": "manual",
}


def main():
    if not DATA_PATH.exists():
        raise SystemExit(f"data.json not found at {DATA_PATH}")

    shutil.copy2(DATA_PATH, BACKUP_PATH)
    print(f"Backup written: {BACKUP_PATH.name}")

    with DATA_PATH.open() as f:
        data = json.load(f)

    targets = [
        ("agency_actions", OLC_ENTRY),
        ("executive_actions", WARRINGTON_ENTRY),
        ("litigation", LAWSUIT_ENTRY),
    ]

    em_dash = "—"
    for cat, entry in targets:
        if em_dash in json.dumps(entry, ensure_ascii=False):
            raise SystemExit(f"ABORT: em-dash detected in entry {entry['i']}.")
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
