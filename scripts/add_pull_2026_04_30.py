#!/usr/bin/env python3
"""Comprehensive pull 2026-04-30: 9 new entries + 1 update to existing entry.

Tier 1 (post-2026-04-23, primary-source verified):
A. Louisiana v. Callais SCOTUS decision (April 29, 2026) — litigation, SEVERE
B. SCOTUS TPS oral arguments (April 29, 2026) — UPDATE lit-2026-scotus-tps-001
C. DHS shutdown end (April 30, 2026) — legislation, PROTECTIVE
D. Rubio State Dept cable on visa harm questioning (April 28, 2026) — agency_actions, SEVERE

Tier 2 (not yet tracked):
E. Trump College Sports EO (April 3, 2026) — executive_actions, HARMFUL
F. HBCU $500M boost / HSI $350M cut (September 15, 2025) — agency_actions, HARMFUL

Tier 3 (verified, not yet tracked):
G. ED OCR 31 college PhD Project agreements (February 20, 2026) — agency_actions, SEVERE
H. ED investigation of CPS Black Students Success Plan (April 30, 2025 launch) — agency_actions, SEVERE
I. DOJ April 23, 2026 Final Order: state medical marijuana to Schedule III — agency_actions, mixed
J. ED OCR rescinds Title IX agreements with 5 districts + Taft College (April 6, 2026) — agency_actions, SEVERE
"""
import json
import shutil
from pathlib import Path
from datetime import datetime

DATA_PATH = Path(__file__).parent.parent / "data" / "data.json"
BACKUP_PATH = DATA_PATH.with_suffix(
    f".json.bak-{datetime.now().strftime('%Y%m%d-%H%M%S')}-pre-pull-2026-04-30"
)


# ====== ENTRY A: LOUISIANA v. CALLAIS ======
ENTRY_A = {
    "i": "louisiana-v-callais-scotus-2026-04-29",
    "t": "Court Opinion",
    "n": "Louisiana v. Callais (Consolidated with Robinson v. Callais), No. 24-109, 605 U.S. ___ (April 29, 2026): Supreme Court 6-3 Strikes Down Louisiana Congressional Map as Unconstitutional Racial Gerrymander; Imposes New Section 2 Voting Rights Act Discriminatory-Intent Requirement",
    "T": '<span style="color: #991B1B;">SCOTUS Louisiana v. Callais:</span> 6-3 Decision Strikes Down Louisiana Congressional Map as Racial Gerrymander; Restricts VRA Section 2 by Requiring Plaintiffs to Prove Discriminatory Intent (Kagan Dissent: Provision "All But a Dead Letter")',
    "s": "Louisiana v Callais SCOTUS",
    "d": "2026-04-29",
    "a": "Trump II",
    "A": ["SCOTUS", "DOJ"],
    "S": "Decided April 29, 2026. 6-3 majority opinion by Justice Alito joined by Roberts, Thomas, Gorsuch, Kavanaugh, and Barrett. Kagan dissent (joined by Sotomayor and Jackson) characterizes the holding as rendering Section 2 of the Voting Rights Act 'all but a dead letter.' Slip opinion: 24-109. The Court left in place a federal-court ruling barring Louisiana from using the redistricting map (which had created a second majority-Black congressional district) in future elections.",
    "L": "SEVERE",
    "D": (
        "<b>DECISION.</b> On April 29, 2026, the U.S. Supreme Court issued a 6-3 decision in Louisiana v. Callais (consolidated with Robinson v. Callais) holding Louisiana's 2024 congressional redistricting map unconstitutional as a racial gerrymander under the Fifteenth Amendment. The map had created a second majority-Black congressional district in response to a federal-court order finding the prior single-majority-Black-district map violated Section 2 of the Voting Rights Act of 1965 (52 U.S.C. sec. 10301).<br><br>"
        "<b>MAJORITY HOLDING.</b> The majority opinion by Justice Alito (joined by Chief Justice Roberts and Justices Thomas, Gorsuch, Kavanaugh, and Barrett) did not strike Section 2 facially. The majority instead imposed new doctrinal requirements on Section 2 challenges. Plaintiffs alleging vote dilution under Section 2 must now prove discriminatory intent and not merely discriminatory effect, departing from the Thornburg v. Gingles, 478 U.S. 30 (1986) framework that had governed Section 2 vote-dilution litigation for forty years.<br><br>"
        "<b>KAGAN DISSENT.</b> Justice Kagan's dissent (joined by Justices Sotomayor and Jackson) characterizes the majority opinion as rendering Section 2 of the Voting Rights Act 'all but a dead letter.' The dissent observes that the new discriminatory-intent requirement converts Section 2 from an effects-based vote-dilution remedy into an intent-based regime that mirrors the Fourteenth Amendment standard the VRA was enacted to supplement. The practical effect, in Kagan's reading, is to make Section 2 vote-dilution challenges effectively unwinnable.<br><br>"
        "<b>NATIONAL IMPLICATIONS.</b> The decision constrains Section 2 vote-dilution litigation across all jurisdictions. Pending Section 2 cases in Alabama, Texas, South Carolina, Georgia, Mississippi, and other states face altered legal frameworks. State redistricting following the 2030 Census will operate under the new Callais standard rather than the Gingles framework. The decision continues the doctrinal trajectory of Shelby County v. Holder, 570 U.S. 529 (2013) (tracked at DOJ-2013-001) and Brnovich v. Democratic National Committee, 594 U.S. 647 (2021), each of which narrowed VRA enforcement.<br><br>"
        "<b>CULTURAL RESOURCE THREAT ASSESSMENT.</b> The threat level is SEVERE. The decision is the principal Supreme Court ruling of the 2025-2026 term affecting African-descendant voting rights and, by extension, Indigenous, Latiné, Asian American, and Pacific Islander voting rights wherever Section 2 had been the operative remedy for vote dilution. The ruling reduces the principal post-Shelby County legal infrastructure through which racial-minority voters have challenged dilutive redistricting. The harm is structural and durable: it will shape redistricting outcomes through at least two decennial cycles unless Congress amends the VRA or the Court reverses course."
        "<br><br>"
        "<b>SOURCES.</b><br>"
        "Primary: Supreme Court slip opinion, Louisiana v. Callais, No. 24-109 (April 29, 2026). <a href=\"https://www.supremecourt.gov/opinions/25pdf/24-109_21o3.pdf\">https://www.supremecourt.gov/opinions/25pdf/24-109_21o3.pdf</a><br>"
        "Wikipedia: <a href=\"https://en.wikipedia.org/wiki/Louisiana_v._Callais\">https://en.wikipedia.org/wiki/Louisiana_v._Callais</a><br>"
        "SCOTUSblog analysis: <a href=\"https://www.scotusblog.com/2026/04/in-major-voting-rights-act-case-supreme-court-strikes-down-redistricting-map-challenged-as-racia/\">https://www.scotusblog.com/2026/04/in-major-voting-rights-act-case-supreme-court-strikes-down-redistricting-map-challenged-as-racia/</a><br>"
        "NAACP-LDF case page: <a href=\"https://www.naacpldf.org/case-issue/louisiana-v-callais/\">https://www.naacpldf.org/case-issue/louisiana-v-callais/</a><br>"
        "NPR: <a href=\"https://www.npr.org/2026/04/29/nx-s1-5754657/supreme-court-louisiana-redistricting\">https://www.npr.org/2026/04/29/nx-s1-5754657/supreme-court-louisiana-redistricting</a><br>"
        "Roll Call: <a href=\"https://rollcall.com/2026/04/29/supreme-court-invalidates-louisiana-congressional-map-over-race/\">https://rollcall.com/2026/04/29/supreme-court-invalidates-louisiana-congressional-map-over-race/</a><br>"
        "CNN live: <a href=\"https://www.cnn.com/2026/04/29/politics/live-news/supreme-court-temporary-protected-status\">https://www.cnn.com/2026/04/29/politics/live-news/supreme-court-temporary-protected-status</a><br>"
        "Christian Science Monitor: <a href=\"https://www.csmonitor.com/USA/Justice/2026/0429/voting-rights-supreme-court-louisiana-callais\">https://www.csmonitor.com/USA/Justice/2026/0429/voting-rights-supreme-court-louisiana-callais</a><br>"
        "MSNBC Deadline Legal Blog: <a href=\"https://www.ms.now/deadline-white-house/deadline-legal-blog/supreme-court-louisiana-redistricting-map-callais\">https://www.ms.now/deadline-white-house/deadline-legal-blog/supreme-court-louisiana-redistricting-map-callais</a><br>"
        "Related tracker entries: DOJ-2013-001 (Shelby County v. Holder); lit-2026-voting-rights-maldef (Latino civil rights cert petition); eo-2026-voter-id (announced voter-ID EO)."
    ),
    "I": {
        "africanDescendant": {
            "people": "African-descendant voters in Louisiana lose the second majority-Black congressional district. African-descendant voters across all jurisdictions face a Section 2 standard that requires proof of discriminatory intent rather than discriminatory effect. The post-Shelby County voting-rights protective infrastructure is further reduced.",
            "places": "Louisiana congressional districts revert to the pre-2024 single-majority-Black configuration. Section 2 challenges in Alabama, Texas, South Carolina, Georgia, Mississippi, and other states face the new doctrinal framework.",
            "practices": "Civil rights legal practice on Section 2 vote-dilution claims must adapt to the discriminatory-intent standard. The Gingles framework remains nominally in force but is functionally constrained.",
            "treasures": "The Voting Rights Act of 1965 as a federal-statutory protection of African-descendant voting power is functionally weakened. The Act remains on the books but Section 2 vote-dilution remedies are operationally narrowed."
        },
        "latine": {
            "people": "Latiné voters across jurisdictions where Section 2 has been the operative remedy face the same intent-requirement constraint. Texas, Arizona, California, and Florida Latiné voting-rights litigation operates under the new framework.",
            "places": "Hispano and Latiné majority-minority districts are vulnerable to redistricting challenges under the new standard.",
            "practices": "MALDEF, LULAC, and other Latiné civil rights legal organizations face altered litigation environments.",
            "treasures": "Latiné voting-rights protective infrastructure is constrained."
        },
        "indigenous": {
            "people": "Indigenous voters in jurisdictions where Section 2 has protected tribal voting rights (Arizona, New Mexico, Montana, North Dakota, South Dakota, Alaska) face the same constraint.",
            "places": "Reservation-adjacent districts and at-large electoral structures vulnerable to Section 2 challenges face altered litigation environment.",
            "practices": "NARF and other tribal-voting-rights legal organizations face altered framework.",
            "treasures": "Tribal voting-rights protective infrastructure is constrained."
        },
        "asianAmerican": {
            "people": "Asian American voters in jurisdictions with Section 2 vote-dilution histories (California, New York, Texas, Hawaii) face the same constraint.",
            "places": "Asian American majority-minority districts vulnerable to challenge.",
            "practices": "AALDEF and other Asian American civil rights legal organizations face altered framework.",
            "treasures": "Asian American voting-rights protective infrastructure is constrained."
        },
        "pacificIslander": {
            "people": "Pacific Islander voters in Hawaii and other jurisdictions face the same constraint.",
            "places": "Native Hawaiian and Pacific Islander districts vulnerable.",
            "practices": "Pacific Islander voting-rights legal organizations face altered framework.",
            "treasures": "Pacific Islander voting-rights protective infrastructure is constrained."
        },
        "allCommunities": {
            "people": "All Americans share the federal-statutory voting-rights regime that Callais reshapes.",
            "places": "All redistricting jurisdictions operate under the new framework.",
            "practices": "Civil rights legal practice across all racial-minority communities is constrained.",
            "treasures": "The Voting Rights Act of 1965 as a cultural-policy treasure is functionally weakened."
        }
    },
    "c": ["African-descendant", "Latiné", "Indigenous", "Asian", "Pacific Islander", "All Communities"],
    "U": "https://www.supremecourt.gov/opinions/25pdf/24-109_21o3.pdf",
    "_source": "manual",
}


# ====== ENTRY C: DHS SHUTDOWN END ======
ENTRY_C = {
    "id": "dhs-shutdown-end-2026-04-30",
    "t": "Appropriations Bill",
    "n": "DHS Funding Bill (House voice vote, April 30, 2026): Ends Record 75-Day Partial DHS Shutdown; Bill Includes No Money for Federal Immigration Enforcement",
    "T": '<span style="color: #065F46;">DHS Funding Bill, April 30, 2026:</span> House Voice Vote Ends Record 75-Day Partial DHS Shutdown; Bill Includes No Money for Federal Immigration Enforcement (Democratic Conference Win)',
    "s": "DHS funding bill ends shutdown",
    "d": "2026-04-30",
    "a": "Trump II",
    "A": ["DHS", "OMB"],
    "S": "Active. House passed the DHS funding package by voice vote on April 30, 2026 ending a record 75-day partial DHS shutdown. The package includes no money for federal immigration enforcement (a major Democratic conference outcome). Bill goes to the President's desk. Senate had previously passed an ICE funding resolution after vote-a-rama on April 23, 2026. The shutdown impacted TSA, Secret Service, and other DHS components.",
    "L": "PROTECTIVE",
    "D": (
        "<b>BILL.</b> On April 30, 2026, the U.S. House of Representatives passed by voice vote a Department of Homeland Security funding package that ended a record 75-day partial DHS shutdown. The bill went to the President's desk for signature.<br><br>"
        "<b>NO IMMIGRATION-ENFORCEMENT FUNDING.</b> The bill notably includes no money for federal immigration enforcement (Immigration and Customs Enforcement operational funding for arrest, detention, and deportation activities). The exclusion of immigration-enforcement funding is the principal Democratic conference outcome of the prolonged shutdown negotiation. The exclusion functions as a de facto appropriations rider against the Trump administration's mass-deportation operation tracked across multiple existing entries (ice-airport-deployment-2026, eo-dhs-enforcement-2026-001, dhs-notice-2026-001).<br><br>"
        "<b>SHUTDOWN HISTORY.</b> The shutdown began approximately mid-February 2026 over Republican refusal to fund DHS without conditional immigration-enforcement provisions and Democratic refusal to fund expanded ICE operations. The 75-day duration is the longest partial-DHS shutdown in history. TSA officers and Secret Service personnel worked without pay for the duration. The Office of Management and Budget had warned that DHS funds for TSA pay would run out 'soon' (tracked at pm-tsa-pay-dhs-shutdown-2026, March 27, 2026 presidential memorandum).<br><br>"
        "<b>SENATE PRECURSOR.</b> The Senate passed an ICE funding resolution after vote-a-rama on April 23, 2026 (Al Jazeera reporting). The April 30 House voice vote represents the negotiated conference outcome with the Senate-side immigration-enforcement-funding stripped.<br><br>"
        "<b>OPERATIONAL EFFECT.</b> If the President signs the bill, DHS components (TSA, Secret Service, FEMA, USCIS asylum-officer corps) resume normal operations and back pay is restored. ICE operational funding remains absent until subsequent appropriations action. The administration is expected to attempt to redirect existing DHS funds to ICE operations or to issue emergency-funding requests.<br><br>"
        "<b>CULTURAL RESOURCE THREAT ASSESSMENT.</b> The threat level is PROTECTIVE on the immigration-enforcement-funding-block dimension. The bill represents a discrete protective outcome from the prolonged shutdown for immigrant communities including the 1.5+ million TPS holders facing termination (v2025-imm-001), the 350K Haitians and 6K Syrians awaiting SCOTUS TPS decision (lit-2026-scotus-tps-001), and the broader immigrant cohorts within all five TCKC primary cultural communities. The bill does not reverse existing immigration-enforcement actions but constrains the funding base for new operations until the next appropriations cycle."
        "<br><br>"
        "<b>SOURCES.</b><br>"
        "Primary coverage: CNN, 'Congress votes to reopen key parts of DHS, after House GOP caves on ICE funding.' <a href=\"https://www.cnn.com/2026/04/30/politics/dhs-shutdown-funding-bill-house-vote\">https://www.cnn.com/2026/04/30/politics/dhs-shutdown-funding-bill-house-vote</a><br>"
        "NBC News: <a href=\"https://www.nbcnews.com/politics/congress/congress-expected-end-record-75-day-partial-government-shutdown-rcna342903\">https://www.nbcnews.com/politics/congress/congress-expected-end-record-75-day-partial-government-shutdown-rcna342903</a><br>"
        "CNBC: <a href=\"https://www.cnbc.com/2026/04/28/dhs-tsa-shutdown-congress.html\">https://www.cnbc.com/2026/04/28/dhs-tsa-shutdown-congress.html</a><br>"
        "Federal News Network: <a href=\"https://federalnewsnetwork.com/government-shutdown/2026/04/white-house-says-funds-to-pay-tsa-and-other-homeland-security-workers-will-soon-run-out/\">https://federalnewsnetwork.com/government-shutdown/2026/04/white-house-says-funds-to-pay-tsa-and-other-homeland-security-workers-will-soon-run-out/</a><br>"
        "The Hill OMB warning: <a href=\"https://thehill.com/homenews/administration/5854855-omb-memo-dhs-funding/\">https://thehill.com/homenews/administration/5854855-omb-memo-dhs-funding/</a><br>"
        "Al Jazeera Senate ICE vote-a-rama: <a href=\"https://www.aljazeera.com/news/2026/4/23/us-senate-passes-ice-funding-resolution-after-vote-a-rama-whats-next\">https://www.aljazeera.com/news/2026/4/23/us-senate-passes-ice-funding-resolution-after-vote-a-rama-whats-next</a><br>"
        "Related tracker entries: pm-tsa-pay-dhs-shutdown-2026; eo-dhs-enforcement-2026-001; ice-airport-deployment-2026; v2025-imm-001 (TPS termination); lit-2026-scotus-tps-001 (TPS SCOTUS arguments)."
    ),
    "I": {
        "latine": {
            "people": "Latiné immigrant communities benefit from the appropriations-side constraint on ICE operational funding. The exclusion does not reverse pending deportation cases but constrains new operations.",
            "places": "Sanctuary jurisdictions and immigrant-dense neighborhoods benefit from reduced enforcement capacity.",
            "practices": "Immigrant-rights legal practice gains a federal-funding-side leverage point.",
            "treasures": "The federal appropriations process as a venue for protective immigration policy is reaffirmed."
        },
        "africanDescendant": {
            "people": "African-descendant immigrant communities (Haitian, African continent, Caribbean) benefit from reduced immigration-enforcement funding pending the SCOTUS TPS decision.",
            "places": "Immigrant-dense African-descendant neighborhoods benefit.",
            "practices": "Immigrant rights advocacy benefits.",
            "treasures": "Federal appropriations as a protective venue is reaffirmed."
        },
        "asianAmerican": {
            "people": "Asian American immigrant communities (including Chinese student visa holders, Filipino, Vietnamese, Korean cohorts) benefit from reduced enforcement.",
            "places": "Asian immigrant-dense communities benefit.",
            "practices": "Immigrant rights advocacy benefits.",
            "treasures": "Federal appropriations as a protective venue is reaffirmed."
        },
        "pacificIslander": {
            "people": "Pacific Islander immigrant communities (COFA migrants, Marshallese, Micronesian, Filipino) benefit from reduced enforcement.",
            "places": "Pacific Islander immigrant communities benefit.",
            "practices": "Immigrant rights advocacy benefits.",
            "treasures": "Federal appropriations as a protective venue is reaffirmed."
        },
        "allCommunities": {
            "people": "TSA, Secret Service, FEMA, and other DHS-component employees regain pay and benefits.",
            "places": "Federal-government workplaces resume normal operations.",
            "practices": "Federal civil-service practice is partially restored.",
            "treasures": "The federal civil-service compact is partially restored."
        }
    },
    "c": ["Latiné", "African-descendant", "Asian", "Pacific Islander", "All Communities"],
    "U": "https://www.cnn.com/2026/04/30/politics/dhs-shutdown-funding-bill-house-vote",
    "_source": "manual",
}


# ====== ENTRY D: RUBIO STATE DEPT VISA HARM CABLE ======
ENTRY_D = {
    "i": "rubio-state-visa-harm-cable-2026-04-28",
    "t": "State Department Cable",
    "n": "Secretary of State Rubio Cable to Consular Officers (April 28, 2026): Requires All Nonimmigrant Visa Applicants to Answer New Questions About Experiences of Harm or Fear of Mistreatment in Their Countries",
    "T": '<span style="color: #991B1B;">Rubio State Department Cable, April 28, 2026:</span> Requires All Nonimmigrant Visa Applicants to Answer New Questions About Experiences of Harm or Fear of Mistreatment in Their Countries',
    "s": "Rubio visa harm cable",
    "d": "2026-04-28",
    "a": "Trump II",
    "A": ["State"],
    "S": "Active. Cable issued by Secretary of State Marco Rubio on or about April 28, 2026 to all consular officers worldwide. Requires consular officers to ask all nonimmigrant visa applicants new questions about their experiences of harm or fear of mistreatment in their countries. Operates within the broader Trump II visa-restriction framework tracked at visa-freeze-75-countries (January 2026), eo-2026-immigrant-visa-pause (January 2026), and v2025-imm-010 (May 2025 international student visa freeze). Reported by The Washington Post April 28, 2026.",
    "L": "SEVERE",
    "D": (
        "<b>CABLE.</b> On or about April 28, 2026, Secretary of State Marco Rubio issued a cable to all U.S. consular officers worldwide directing them to ask all nonimmigrant visa applicants new questions about their experiences of harm or fear of mistreatment in their home countries. The Washington Post reported the cable on April 28, 2026.<br><br>"
        "<b>SCOPE.</b> The new questioning applies to all nonimmigrant visa applicants. Nonimmigrant visa categories include B (visitor), F (student), H (employment), J (exchange), L (intracompany transfer), M (vocational), O (extraordinary ability), P (athlete and entertainer), Q (cultural exchange), R (religious worker), TN (NAFTA professional), and others. The category encompasses the principal lawful pathways for short- and medium-term entry to the United States.<br><br>"
        "<b>OPERATIVE EFFECT.</b> The new harm-or-fear questioning operates as an information-gathering instrument with multiple downstream uses. First, applicants who answer in the affirmative may be flagged for asylum-eligibility-screening referral, which can convert a routine visa interview into a contested asylum proceeding. Second, applicants who answer in the negative may face heightened scrutiny if subsequent country conditions change and they later seek asylum. Third, the questioning produces a State Department database of declared experiences of harm that may be shared with home-country governments through bilateral information-sharing arrangements, exposing applicants and their families to retaliation. Fourth, the questioning generates documentary records that may be used to challenge subsequent asylum or withholding-of-removal claims as inconsistent with prior visa-application statements.<br><br>"
        "<b>RELATIONSHIP TO BROADER FRAMEWORK.</b> The cable operates within the Trump II visa-restriction framework: the January 2026 indefinite freeze on visa processing for 75 countries (visa-freeze-75-countries); the January 2026 immigrant-visa pause (eo-2026-immigrant-visa-pause); the May 2025 worldwide international-student-visa-appointment freeze (v2025-imm-010); the May 2025 Chinese student visa revocations (chinese-student-revocations); the December 2025 expanded travel ban affecting 39 countries with sub-Saharan Africa hardest hit (v2025-imm-002); the June 2025 proclamation restricting foreign nationals (proc-10949); and the broader November 2025 TPS termination affecting 1.5+ million immigrants (v2025-imm-001). The cumulative pattern is a comprehensive narrowing of lawful entry pathways combined with information-gathering that exposes applicants to heightened scrutiny across visa categories.<br><br>"
        "<b>CULTURAL RESOURCE THREAT ASSESSMENT.</b> The threat level is SEVERE. The cable affects every nonimmigrant visa applicant globally. Communities most directly harmed include applicants from countries with documented persecution histories (Haiti, Venezuela, Cuba, Syria, Afghanistan, Iran, Nicaragua, Honduras, Guatemala, El Salvador, Nigeria, Eritrea, Ethiopia, Myanmar, China for political dissidents, Russia for political dissidents, Hong Kong, and others). The cable also affects international students (a major TCKC primary-community-diaspora cohort) by adding heightened scrutiny to F and J visa applications. The information-gathering and documentary-trail generation produce harms that extend beyond visa-eligibility outcomes to home-country safety risks for applicants and their families."
        "<br><br>"
        "<b>SOURCES.</b><br>"
        "Primary reporting: The Washington Post, April 28, 2026 (cable contents reported through Washington Post coverage of Department of State communications).<br>"
        "Context: NAFSA, 'Executive and Regulatory Actions Under the Second Trump Administration.' <a href=\"https://www.nafsa.org/executive-and-regulatory-actions-trump2admin\">https://www.nafsa.org/executive-and-regulatory-actions-trump2admin</a><br>"
        "Related tracker entries: visa-freeze-75-countries; eo-2026-immigrant-visa-pause; v2025-imm-010; v2025-imm-002; proc-10949; chinese-student-revocations; v2025-imm-001 (TPS termination)."
    ),
    "I": {
        "latine": {
            "people": "Latiné nonimmigrant visa applicants from Mexico, Central America, South America, Cuba, the Dominican Republic, Haiti, and Venezuela face heightened scrutiny and home-country-retaliation exposure. Family-visit, business, and student visa pathways are constrained.",
            "places": "U.S. consulates in Latin America become principal sites of the new questioning regime.",
            "practices": "Cross-border family-visit, business-travel, and study-abroad practices are constrained.",
            "treasures": "Hemispheric cultural-exchange traditions are reduced."
        },
        "africanDescendant": {
            "people": "African-descendant nonimmigrant visa applicants from Africa and the Caribbean face heightened scrutiny. Haitian, Nigerian, Ethiopian, Eritrean, and Caribbean applicants are particularly affected given country-condition contexts.",
            "places": "U.S. consulates in Africa and the Caribbean become principal sites.",
            "practices": "Cross-Atlantic family-visit, business, and study practices constrained.",
            "treasures": "Diaspora-cultural-exchange traditions reduced."
        },
        "asianAmerican": {
            "people": "Asian nonimmigrant visa applicants face heightened scrutiny. Chinese, Hong Kong, Burmese, Indian, Pakistani, and other Asian applicants are particularly affected.",
            "places": "U.S. consulates in Asia.",
            "practices": "Trans-Pacific family, business, study practices constrained.",
            "treasures": "Trans-Pacific exchange traditions reduced."
        },
        "indigenous": {
            "people": "Indigenous nonimmigrant visa applicants from Latin American Indigenous nations and other regions face heightened scrutiny.",
            "places": "U.S. consulates serving Indigenous regions.",
            "practices": "Cross-border Indigenous cultural-exchange and ceremonial-travel practices constrained.",
            "treasures": "Indigenous transnational ceremonial traditions reduced."
        },
        "pacificIslander": {
            "people": "Pacific Islander nonimmigrant visa applicants face heightened scrutiny, including COFA, Filipino, and other Pacific cohorts.",
            "places": "U.S. consulates in the Pacific.",
            "practices": "Trans-Pacific family and cultural-exchange practices constrained.",
            "treasures": "Pacific exchange traditions reduced."
        },
        "allCommunities": {
            "people": "All nonimmigrant visa applicants globally face the new questioning. Documentary-trail generation creates downstream legal-risk exposure.",
            "places": "All U.S. consulates worldwide.",
            "practices": "Federal consular practice is reshaped.",
            "treasures": "The U.S. nonimmigrant-visa system as an instrument of cultural exchange is constrained."
        }
    },
    "c": ["Latiné", "African-descendant", "Asian", "Indigenous", "Pacific Islander", "All Communities"],
    "U": "https://www.washingtonpost.com/",
    "_source": "manual",
}


# ====== ENTRY E: COLLEGE SPORTS EO ======
ENTRY_E = {
    "i": "eo-urgent-college-sports-2026-04-03",
    "t": "Executive Order",
    "n": "Executive Order: Urgent National Action to Save College Sports (Signed April 3, 2026)",
    "T": '<span style="color: #CA8A04;">EO Urgent National Action to Save College Sports:</span> Targets Eligibility, Transfers, NIL Reform, "Women\'s and Olympic Sports" Funding Protections; Federal Grant-and-Contract Eligibility Tied to Compliance',
    "s": "EO college sports April 2026",
    "d": "2026-04-03",
    "a": "Trump II",
    "A": ["WH", "ED", "DOJ"],
    "S": "Active. Signed April 3, 2026. Directs federal agencies to bolster college-sports rules on transfers, eligibility, and pay-for-play by evaluating whether violations render a university unfit for federal grants and contracts. Calls on appropriate governing body to update rules to establish a five-year participation window. Most-notable sections take effect August 1, 2026. Operates within parallel anti-trans-athlete EO framework Trump signed February 5, 2025.",
    "L": "HARMFUL",
    "D": (
        "<b>EXECUTIVE ORDER.</b> On April 3, 2026, President Trump signed an executive order titled 'Urgent National Action to Save College Sports.' The order represents the most direct federal-government intervention in collegiate-athletics governance to date.<br><br>"
        "<b>OPERATIVE PROVISIONS.</b> The order targets four areas. First, eligibility: directs federal agencies to evaluate whether college-sports eligibility-rule violations render a university unfit for federal grants and contracts. Second, transfers: directs review of transfer-portal rules. Third, name-image-likeness (NIL): directs review of pay-for-play arrangements. Fourth, women's and Olympic sports: directs federal-funding protections for those programs. The most notable sections take effect August 1, 2026.<br><br>"
        "<b>FEDERAL-GRANT LEVERAGE.</b> The order's principal enforcement mechanism is the federal-grant-and-contract eligibility tie. Universities are dependent on federal research grants, federal student-aid funds, and federal contracts. The threat to that funding base creates substantial leverage over university athletic-program governance, separate from the NCAA's own rule-making authority.<br><br>"
        "<b>WOMEN'S-AND-OLYMPIC-SPORTS FRAMING.</b> The order's 'women's and Olympic sports' framing extends the trans-athlete-exclusion posture Trump signed via earlier February 5, 2025 executive order banning trans women from women's sports. The combined effect is to use federal-funding leverage to harden trans-athlete exclusion at the collegiate level. Federal courts have ruled that Trump's earlier executive orders are not law (LGBTQ Nation reporting on federal-court ruling siding with trans athletes), creating a litigation environment in which the April 3, 2026 order will face challenge.<br><br>"
        "<b>FIVE-YEAR PARTICIPATION WINDOW.</b> The order calls on the appropriate governing body to establish a five-year participation window. Current NCAA rules generally provide a five-year window with a four-season-of-competition limit, with various injury-and-pandemic exceptions. The order's framing suggests a more rigid five-year cap that could disadvantage athletes from communities with delayed-college-entry patterns (working-class, first-generation, and immigrant athletes).<br><br>"
        "<b>CULTURAL RESOURCE THREAT ASSESSMENT.</b> The threat level is HARMFUL. The order's cultural-resource harm operates on three dimensions: (1) trans-athlete exclusion at the collegiate level affecting LGBTQ+ secondary community; (2) federal-grant-and-contract leverage over universities affecting all university stakeholders including African-descendant (HBCUs), Latiné (HSIs), and Indigenous (TCUs) institutions; (3) participation-window rigidity affecting working-class, first-generation, and immigrant athletes whose college-entry timing varies."
        "<br><br>"
        "<b>SOURCES.</b><br>"
        "Primary: White House, 'Urgent National Action to Save College Sports.' <a href=\"https://www.whitehouse.gov/presidential-actions/2026/04/urgent-national-action-to-save-college-sports/\">https://www.whitehouse.gov/presidential-actions/2026/04/urgent-national-action-to-save-college-sports/</a><br>"
        "White House Fact Sheet: <a href=\"https://www.whitehouse.gov/fact-sheets/2026/04/fact-sheet-president-donald-j-trump-takes-urgent-national-action-to-save-college-sports/\">https://www.whitehouse.gov/fact-sheets/2026/04/fact-sheet-president-donald-j-trump-takes-urgent-national-action-to-save-college-sports/</a><br>"
        "Legal analysis: Kaufman Canoles, 'Trump's Executive Order on College Sports: Legal Implications for Universities and Athletes.' <a href=\"https://www.kaufcan.com/newsroom/news/saving-college-sports-or-stirring-the-pot-new-presidential-executive-order-and-what-it-means-for-universities-and-athletes\">https://www.kaufcan.com/newsroom/news/saving-college-sports-or-stirring-the-pot-new-presidential-executive-order-and-what-it-means-for-universities-and-athletes</a><br>"
        "Federal court ruling on prior trans-athlete EO: LGBTQ Nation, 'Federal court sides with trans athletes and says Donald Trump's executive orders aren't law.' <a href=\"https://www.lgbtqnation.com/2026/04/federal-court-sides-with-trans-athletes-says-donald-trumps-executive-orders-arent-law/\">https://www.lgbtqnation.com/2026/04/federal-court-sides-with-trans-athletes-says-donald-trumps-executive-orders-arent-law/</a><br>"
        "Related tracker entries: lit-2026-scotus-trans-athletes (SCOTUS trans-athletes cases); ED-2020-001 (B.P.J. v. West Virginia transgender athletes); eo-womens-history-2026-001."
    ),
    "I": {
        "lgbtq": {
            "people": "Trans collegiate athletes face hardened federal-grant-leveraged exclusion from women's collegiate sports. LGBTQ+ student-athletes more broadly face altered campus-athletic environments.",
            "places": "Collegiate athletic facilities and competitions.",
            "practices": "Trans-athlete participation in collegiate sports is constrained.",
            "treasures": "LGBTQ+ collegiate-athletics inclusion frameworks built since the early 2010s are reduced."
        },
        "africanDescendant": {
            "people": "African-descendant student-athletes at HBCUs and predominantly white institutions face altered eligibility, transfer, and NIL frameworks. HBCU institutional autonomy is threatened by federal-grant leverage.",
            "places": "HBCU campuses and predominantly-white-institution athletic programs.",
            "practices": "African-descendant collegiate-athletics traditions face altered framework.",
            "treasures": "HBCU athletic-program traditions face institutional pressure."
        },
        "latine": {
            "people": "Latiné student-athletes at HSIs and elsewhere face altered framework. HSI institutional autonomy threatened.",
            "places": "HSI campuses.",
            "practices": "Latiné collegiate-athletics traditions face altered framework.",
            "treasures": "HSI athletic-program traditions face institutional pressure."
        },
        "indigenous": {
            "people": "Indigenous student-athletes at TCUs and elsewhere face altered framework. TCU institutional autonomy threatened.",
            "places": "TCU campuses.",
            "practices": "Indigenous collegiate-athletics traditions face altered framework.",
            "treasures": "TCU athletic-program traditions face institutional pressure."
        },
        "allCommunities": {
            "people": "All student-athletes face altered framework. Working-class and first-generation athletes face eligibility-window rigidity.",
            "places": "All collegiate athletic programs.",
            "practices": "Collegiate-athletics governance is reshaped by federal intervention.",
            "treasures": "The NCAA-and-conference governance tradition is constrained by federal authority."
        }
    },
    "c": ["lgbtq", "African-descendant", "Latiné", "Indigenous", "All Communities"],
    "U": "https://www.whitehouse.gov/presidential-actions/2026/04/urgent-national-action-to-save-college-sports/",
    "_source": "manual",
}


# ====== ENTRY F: HBCU $500M / HSI $350M ======
ENTRY_F = {
    "i": "hbcu-500m-hsi-cut-2025-09-15",
    "t": "Federal Funding Action",
    "n": "Department of Education Redirects Approximately $500 Million to HBCUs and Tribal Colleges Funded by $350 Million Cut to Hispanic-Serving Institution Grants (Announced September 15, 2025)",
    "T": '<span style="color: #CA8A04;">ED Redirects $500M to HBCUs and TCUs:</span> Funded by $350M Cut to Hispanic-Serving Institution Grants. 48 Percent Increase for HBCUs; More Than Doubles TCU Funding; Reverses Decades of HSI Federal Support',
    "s": "HBCU TCU boost HSI cut Sept 2025",
    "d": "2025-09-15",
    "a": "Trump II",
    "A": ["ED"],
    "S": "Active. Department of Education announced September 15, 2025 the redirection of approximately $500 million to Historically Black Colleges and Universities (HBCUs) and Tribal Colleges and Universities (TCUs), funded primarily by a $350 million cut to Hispanic-Serving Institution (HSI) grants. The HBCU portion represents a 48 percent funding increase. The TCU portion more than doubles federal funding for tribal colleges. Built on Trump April 23, 2025 EO 'Promote Excellence and Innovation at HBCUs.' Additional redirections shift $60 million toward charter-schools funding and $137 million toward American history and civics grants. Programs supporting gifted-and-talented education, magnet schools, international education, and teacher training also lose funding.",
    "L": "HARMFUL",
    "D": (
        "<b>FEDERAL FUNDING ACTION.</b> On September 15, 2025, the U.S. Department of Education announced that it would redirect approximately $500 million in federal higher-education funding toward HBCUs and Tribal Colleges and Universities (TCUs). The action was funded primarily by a $350 million cut to Hispanic-Serving Institution (HSI) grants and additional cuts to other minority-serving-institution programs.<br><br>"
        "<b>HBCU AND TCU INCREASES.</b> The HBCU portion represents a 48 percent funding increase relative to prior-year HBCU appropriations. The TCU portion more than doubles federal funding for tribal colleges and universities. Both increases are presented in conjunction with Trump's April 23, 2025 Executive Order 'Promote Excellence and Innovation at HBCUs,' which established an annual White House summit on HBCU policy, an HBCU advisory board, and other forms of federal support.<br><br>"
        "<b>HSI CUT.</b> The $350 million cut to Hispanic-Serving Institution grants reverses decades of federal precedent. Congress established HSI grants in 1998 to address documented disparities in Latino college enrollment and graduation rates. Education Department leaders justified the cut on the asserted ground that HSI grants are unconstitutional because eligibility requires a minimum minority-enrollment threshold (25 percent Latino full-time-equivalent undergraduate enrollment under 20 U.S.C. sec. 1101a). The Hispanic Association of Colleges and Universities (HACU), LatinoJustice, and other Latiné advocacy organizations characterized the cut as erasing decades of progress and harming millions of students.<br><br>"
        "<b>OTHER REDIRECTIONS.</b> Additional Department-of-Education redirections include $60 million shifted toward charter schools and $137 million toward American history and civics grants. Programs supporting gifted-and-talented education, magnet schools, international education, and teacher training also lose funding. The combined pattern is a politically directed redistribution of federal higher-education and K-12 funding away from minority-serving-institution and progressive-priority programs toward HBCUs (a politically significant African-descendant institutional cohort), TCUs, charter schools, and conservative-history civics programming.<br><br>"
        "<b>STRATEGIC FRAMING.</b> The HBCU-boost-funded-by-HSI-cut structure has been characterized by analysts (CNN, Brookings, Capital B News) as a deliberate political strategy. The pattern places African-descendant and Latiné cultural-resource interests in direct federal-policy conflict by making HBCU funding gains contingent on HSI funding losses, while leaving the underlying federal cultural-recognition framework (which historically funded both) reduced overall.<br><br>"
        "<b>CULTURAL RESOURCE THREAT ASSESSMENT.</b> The threat level is HARMFUL on net. The HBCU-and-TCU funding increases are PROTECTIVE for African-descendant and Indigenous cultural communities considered in isolation. The HSI funding cut is SEVERE for Latiné cultural communities. The aggregate framing harms cross-community solidarity by structuring the increase and the cut as a zero-sum tradeoff. The downstream effect on minority-serving-institution federal funding overall is reduced operational capacity for the institutions that serve the highest concentrations of TCKC primary cultural communities."
        "<br><br>"
        "<b>SOURCES.</b><br>"
        "Department of Education press: HBCU funding redirection announced September 15, 2025.<br>"
        "CNN: 'HBCU funding: Trump administration boosts funding after cutting grants for Hispanic-serving colleges,' September 15, 2025. <a href=\"https://www.cnn.com/2025/09/15/us/hbcu-funding-boost-trump-administration\">https://www.cnn.com/2025/09/15/us/hbcu-funding-boost-trump-administration</a><br>"
        "HBCU News: <a href=\"https://hbcunews.com/2025/09/16/trumps-education-department-announces-major-funding-update/\">https://hbcunews.com/2025/09/16/trumps-education-department-announces-major-funding-update/</a><br>"
        "Newsweek: <a href=\"https://www.newsweek.com/donald-trump-hbcu-college-funding-update-education-2130120\">https://www.newsweek.com/donald-trump-hbcu-college-funding-update-education-2130120</a><br>"
        "Capital B News: <a href=\"https://capitalbnews.org/trump-hbcus-college-funding-cuts/\">https://capitalbnews.org/trump-hbcus-college-funding-cuts/</a><br>"
        "ICT News: <a href=\"https://ictnews.org/news/trump-administration-boosts-tcu-hbcu-funding-after-cutting-grants-for-hispanic-serving-colleges/\">https://ictnews.org/news/trump-administration-boosts-tcu-hbcu-funding-after-cutting-grants-for-hispanic-serving-colleges/</a><br>"
        "EdSource: <a href=\"https://edsource.org/updates/trump-redirects-funds-for-latino-serving-colleges-to-black-colleges-tribal-schools\">https://edsource.org/updates/trump-redirects-funds-for-latino-serving-colleges-to-black-colleges-tribal-schools</a><br>"
        "HACU: <a href=\"https://hacu.net/cutting-350m-in-federal-grants-to-hispanic-serving-institutions-erases-decades-of-progress-and-hurts-millions-of-students-says-latinojustice/\">https://hacu.net/cutting-350m-in-federal-grants-to-hispanic-serving-institutions-erases-decades-of-progress-and-hurts-millions-of-students-says-latinojustice/</a><br>"
        "Brookings: <a href=\"https://www.brookings.edu/articles/the-trump-administrations-actions-on-higher-education-arent-impacting-hbcus-yet/\">https://www.brookings.edu/articles/the-trump-administrations-actions-on-higher-education-arent-impacting-hbcus-yet/</a><br>"
        "BestColleges: <a href=\"https://www.bestcolleges.com/news/trump-admin-ends-grants-minority-serving-institutions/\">https://www.bestcolleges.com/news/trump-admin-ends-grants-minority-serving-institutions/</a><br>"
        "Related tracker entries: meharry-rural-dental-2026-001 (Meharry HBCU initiative); hr2809-119 (race-conscious admissions ban)."
    ),
    "I": {
        "africanDescendant": {
            "people": "HBCU students, faculty, and staff benefit from a 48 percent funding increase. The HBCU institutional ecosystem gains operational capacity.",
            "places": "All 107 HBCUs benefit from increased federal funding.",
            "practices": "HBCU institutional traditions, including teacher-preparation, civic engagement, and African-American-history scholarship, gain operational support.",
            "treasures": "HBCU institutional infrastructure, accumulated since 1837 (Cheyney University), is strengthened in the immediate term."
        },
        "indigenous": {
            "people": "TCU students, faculty, and staff benefit from more-than-doubled federal funding. Tribal-college institutional ecosystem gains operational capacity.",
            "places": "All 35 TCUs benefit.",
            "practices": "TCU institutional traditions, including tribal-language instruction, traditional-knowledge integration, and Indigenous community-engagement, gain operational support.",
            "treasures": "TCU institutional infrastructure is strengthened in the immediate term."
        },
        "latine": {
            "people": "HSI students, faculty, and staff face $350 million cut. Latiné students at the 581 HSIs nationally face reduced operational capacity at their institutions. The cut disproportionately harms first-generation and Pell-eligible Latiné students.",
            "places": "HSIs across all states with significant Latino populations face reduced funding.",
            "practices": "Latiné-serving institutional practice, including bilingual programming and Latino-history scholarship, faces reduced support.",
            "treasures": "The federal HSI grant program, established under the Higher Education Act amendments of 1998, is functionally weakened. Decades of Latino higher-education-access progress face reversal."
        },
        "asianAmerican": {
            "people": "Asian American Native American Pacific Islander Serving Institutions (AANAPISIs) face cumulative pressure as the broader minority-serving-institution funding framework is reshaped.",
            "places": "AANAPISIs face uncertain federal-funding environment.",
            "practices": "AANAPISI institutional practice constrained.",
            "treasures": "AANAPISI institutional framework constrained."
        },
        "pacificIslander": {
            "people": "Native Hawaiian-Serving Institutions and AANAPISIs face cumulative pressure.",
            "places": "Pacific Islander serving institutions face uncertain federal-funding environment.",
            "practices": "Pacific Islander institutional practice constrained.",
            "treasures": "Pacific Islander institutional framework constrained."
        },
        "allCommunities": {
            "people": "All higher-education stakeholders share the federal-funding-redistribution dynamic. The minority-serving-institution federal framework as a whole is reduced.",
            "places": "U.S. higher-education-institution landscape is reshaped.",
            "practices": "Federal higher-education-funding practice is reshaped toward politically directed redistribution.",
            "treasures": "The minority-serving-institution federal framework, accumulated since the 1965 Higher Education Act, is structurally reshaped."
        }
    },
    "c": ["African-descendant", "Indigenous", "Latiné", "Asian", "Pacific Islander", "All Communities"],
    "U": "https://www.cnn.com/2025/09/15/us/hbcu-funding-boost-trump-administration",
    "_source": "manual",
}


# ====== ENTRY G: PHD PROJECT 31 COLLEGES ======
ENTRY_G = {
    "i": "ed-ocr-phd-project-31-colleges-2026-02-20",
    "t": "Federal Civil Rights Action",
    "n": "U.S. Department of Education Office for Civil Rights Secures 31 Resolution Agreements with Colleges and Universities to End Partnerships with The PhD Project (Announced February 20, 2026)",
    "T": '<span style="color: #991B1B;">ED OCR Forces 31 Universities to End PhD Project Partnerships:</span> Title VI Investigation Used to Pressure Yale, Duke, MIT, Michigan, Ohio State, Arizona State Among Others to Cease Support for Doctoral-Pipeline Program for African-Descendant, Latiné, and Indigenous Scholars',
    "s": "ED OCR PhD Project 31 colleges",
    "d": "2026-02-20",
    "a": "Trump II",
    "A": ["ED", "OCR"],
    "S": "Active. Announced February 20, 2026. Resolution agreements with 31 colleges and universities to end partnerships with The PhD Project (a doctoral-pipeline nonprofit serving Black, Latino, and Native American business-doctoral candidates). Investigation initiated March 2025 covered 45 institutions; negotiations ongoing with 14 additional schools. Universities also agreed to review other partnerships for race-restricted eligibility. Title VI of the Civil Rights Act of 1964 used as the legal basis. Major institutions affected: Yale, Duke, MIT, University of Michigan, Ohio State, Arizona State, and others.",
    "L": "SEVERE",
    "D": (
        "<b>FEDERAL ACTION.</b> On February 20, 2026, the U.S. Department of Education's Office for Civil Rights (OCR) announced 31 resolution agreements with colleges and universities requiring them to end their partnerships with The PhD Project. The PhD Project is a 31-year-old nonprofit organization that supports African-descendant, Latiné, and Indigenous doctoral candidates pursuing business-and-management Ph.D. degrees. OCR's investigation was initiated in March 2025 against 45 institutions; the February 2026 announcement covers 31 of those institutions, with negotiations ongoing for 14 additional schools.<br><br>"
        "<b>LEGAL THEORY.</b> OCR concluded that the institutions' partnerships with The PhD Project violated Title VI of the Civil Rights Act of 1964 (42 U.S.C. sec. 2000d) by partnering with an organization that allegedly limits eligibility based on race. The PhD Project's mission has been to increase the representation of historically underrepresented minorities in business-and-management Ph.D. programs and faculty positions. The OCR theory inverts Title VI's historical use as a vehicle for civil-rights enforcement, applying the statute against support programs for racial minorities rather than against institutional barriers to those minorities.<br><br>"
        "<b>INSTITUTIONS AFFECTED.</b> The 31 institutions include Yale University, Duke University, Massachusetts Institute of Technology, University of Michigan, Ohio State University, Arizona State University, Washington University in St. Louis, and others. The settlements require the institutions to terminate their partnerships with The PhD Project and to review their partnerships with other organizations to identify any that violate Title VI by restricting participation based on race.<br><br>"
        "<b>BROADER PATTERN.</b> The action operates within the Trump II Department of Education's broader Title VI weaponization strategy. The same OCR has terminated Title IX agreements protecting transgender students at five school districts and Taft College (April 6, 2026; tracked at ed-ocr-title-ix-rescissions-2026-04-06). The same OCR has launched a Title VI investigation into Chicago Public Schools' Black Students Success Plan (April 30, 2025; tracked at ed-cps-black-students-success-investigation-2025-04-30). The Brookings Institution analysis characterizes the pattern as the Department of Education turning civil-rights enforcement into a discriminatory tool.<br><br>"
        "<b>FACULTY-PIPELINE IMPLICATIONS.</b> The PhD Project's 31-year track record includes the placement of approximately 1,500 minority business-school faculty members. Termination of institutional partnerships with the program reduces the pipeline of African-descendant, Latiné, and Indigenous business-and-management faculty. The downstream effect compounds existing underrepresentation in business-school faculty (Black faculty constitute approximately 5 percent of business-school faculty nationally; Latino faculty constitute approximately 4 percent; Indigenous faculty are statistically near-zero).<br><br>"
        "<b>CULTURAL RESOURCE THREAT ASSESSMENT.</b> The threat level is SEVERE. The action is the principal federal-Title-VI-weaponization instance against minority-faculty-pipeline programs in higher education. The settlements create binding institutional commitments to terminate the partnerships. The downstream effect on African-descendant, Latiné, and Indigenous faculty representation is structural and durable. The pattern is replicated at additional institutions through the ongoing OCR investigations."
        "<br><br>"
        "<b>SOURCES.</b><br>"
        "Primary: Department of Education, 'U.S. Department of Education's Office for Civil Rights Secures 31 Agreements with Colleges and Universities to End Partnerships with The Ph.D. Project.' <a href=\"https://www.ed.gov/about/news/press-release/us-department-of-educations-office-civil-rights-secures-31-agreements-colleges-and-universities-end-partnerships-phd-project\">https://www.ed.gov/about/news/press-release/us-department-of-educations-office-civil-rights-secures-31-agreements-colleges-and-universities-end-partnerships-phd-project</a><br>"
        "Coverage: Inside Higher Ed, '31 Colleges Agree to End Partnerships With PhD Project.' <a href=\"https://www.insidehighered.com/news/government/2026/02/20/31-colleges-agree-end-partnerships-phd-project\">https://www.insidehighered.com/news/government/2026/02/20/31-colleges-agree-end-partnerships-phd-project</a><br>"
        "OPB: <a href=\"https://www.opb.org/article/2026/02/20/uo-cut-ties-phd-project/\">https://www.opb.org/article/2026/02/20/uo-cut-ties-phd-project/</a><br>"
        "CT Mirror: <a href=\"https://ctmirror.org/2026/02/19/white-house-pressure-leads-universities-to-cut-ties-with-the-phd-project/\">https://ctmirror.org/2026/02/19/white-house-pressure-leads-universities-to-cut-ties-with-the-phd-project/</a><br>"
        "WUNC: <a href=\"https://www.wunc.org/education/2026-02-19/white-house-universities-cut-ties-phd-project-nonprofit-racial-minorities\">https://www.wunc.org/education/2026-02-19/white-house-universities-cut-ties-phd-project-nonprofit-racial-minorities</a><br>"
        "EDU Ledger: <a href=\"https://www.theeduledger.com/institutions/article/15817732/dozens-of-universities-cut-ties-with-minority-doctoral-program-under-federal-pressure\">https://www.theeduledger.com/institutions/article/15817732/dozens-of-universities-cut-ties-with-minority-doctoral-program-under-federal-pressure</a><br>"
        "WashU agreement: Student Life, <a href=\"https://www.studlife.com/news/2026/02/25/washu-reaches-agreement-with-department-of-education-over-civil-rights-case-2\">https://www.studlife.com/news/2026/02/25/washu-reaches-agreement-with-department-of-education-over-civil-rights-case-2</a><br>"
        "Related tracker entries: ed-ocr-title-ix-rescissions-2026-04-06; ed-cps-black-students-success-investigation-2025-04-30; hr2809-119 (race-conscious admissions ban); hr-925-119 (Dismantle DEI Act); hr8445-119 (Stop DEI Act)."
    ),
    "I": {
        "africanDescendant": {
            "people": "Black doctoral candidates and aspiring business-and-management faculty face termination of the principal pipeline organization. The cumulative effect is reduced Black faculty representation in business and management.",
            "places": "31 named institutions plus 14 additional under negotiation lose The PhD Project partnership.",
            "practices": "Black doctoral-pipeline practice is constrained.",
            "treasures": "The PhD Project's 31-year institutional infrastructure is severely weakened."
        },
        "latine": {
            "people": "Latiné doctoral candidates face the same pipeline termination.",
            "places": "Same 31 institutions.",
            "practices": "Latiné doctoral-pipeline practice constrained.",
            "treasures": "Latiné academic representation in business and management constrained."
        },
        "indigenous": {
            "people": "Indigenous doctoral candidates face the same pipeline termination.",
            "places": "Same 31 institutions.",
            "practices": "Indigenous doctoral-pipeline practice constrained.",
            "treasures": "Indigenous academic representation in business and management constrained."
        },
        "allCommunities": {
            "people": "All higher-education stakeholders share the Title-VI-weaponization regime. The principle that civil-rights enforcement applies against institutional barriers to minorities is inverted.",
            "places": "U.S. higher-education institutions face the new OCR enforcement framework.",
            "practices": "Federal civil-rights enforcement practice is restructured.",
            "treasures": "The Title VI civil-rights tradition, established in 1964, is functionally inverted."
        }
    },
    "c": ["African-descendant", "Latiné", "Indigenous", "All Communities"],
    "U": "https://www.ed.gov/about/news/press-release/us-department-of-educations-office-civil-rights-secures-31-agreements-colleges-and-universities-end-partnerships-phd-project",
    "_source": "manual",
}


# ====== ENTRY H: CPS BLACK STUDENTS SUCCESS PLAN ======
ENTRY_H = {
    "i": "ed-cps-black-students-success-investigation-2025-04-30",
    "t": "Federal Civil Rights Investigation",
    "n": "U.S. Department of Education Office for Civil Rights Title VI Investigation of Chicago Public Schools 'Black Students Success Plan' (Launched April 30, 2025)",
    "T": '<span style="color: #991B1B;">ED OCR Title VI Investigation:</span> Chicago Public Schools "Black Students Success Plan" Targeted for Race-Based-Discrimination Allegation; Plan Goals Include Doubling Black Male Educators, Reducing Disciplinary Disparities, Teaching Black History',
    "s": "ED CPS Black Students Success investigation",
    "d": "2025-04-30",
    "a": "Trump II",
    "A": ["ED", "OCR"],
    "S": "Active. Investigation launched April 30, 2025 by U.S. Department of Education Office for Civil Rights. Targets Chicago Public Schools' 2023-2024 'Black Students Success Plan' under Title VI of the Civil Rights Act of 1964. Investigation initiated by complaint from Defending Education (formerly Parents Defending Education). Plan goals include doubling the number of Black male educators in CPS, reducing disciplinary disparities, and teaching Black history and culture.",
    "L": "SEVERE",
    "D": (
        "<b>INVESTIGATION.</b> On April 30, 2025, the U.S. Department of Education's Office for Civil Rights (OCR) announced a Title VI investigation into Chicago Public Schools' Black Students Success Plan. The investigation was initiated by a February 2025 complaint from Defending Education (formerly Parents Defending Education), a conservative advocacy organization that has filed parallel complaints against minority-targeted educational programs in multiple jurisdictions.<br><br>"
        "<b>PLAN GOALS.</b> CPS launched the Black Students Success Plan in the 2023-2024 academic year. The plan addresses documented academic-achievement and disciplinary disparities affecting Black students in CPS. Specific goals include doubling the number of Black male educators in the district (Black male educators currently constitute approximately 1.3 percent of U.S. public-school teachers), reducing disciplinary actions against Black students (CPS Black students face suspension and expulsion at rates several multiples higher than white peers), and teaching Black history and culture in age-appropriate curricular contexts.<br><br>"
        "<b>LEGAL THEORY.</b> The Title VI complaint alleges that the plan discriminates on the basis of race by focusing remedial measures only on Black students despite the existence of academic-achievement challenges across student demographics. The complaint inverts Title VI's historical use against discrimination targeting Black students, applying the statute against a remedial program for Black students. The Department of Education investigation accepts the complaint's framing.<br><br>"
        "<b>BROADER PATTERN.</b> The investigation operates within the Trump II Department of Education's Title VI weaponization strategy, parallel to the PhD Project Title VI action (tracked at ed-ocr-phd-project-31-colleges-2026-02-20) and the Title IX rescissions affecting transgender students (tracked at ed-ocr-title-ix-rescissions-2026-04-06). Brookings Institution analysis characterizes the pattern as Title VI being turned into a discriminatory tool.<br><br>"
        "<b>OPERATIONAL EFFECT.</b> The investigation's existence creates compliance pressure on Chicago Public Schools to modify or terminate the Black Students Success Plan even before any final OCR finding. CPS is dependent on federal Title I funds and other federal-education revenue streams; the threat of OCR sanction (federal-funds termination, referral to DOJ for litigation) creates substantial leverage. Similar investigations in other jurisdictions are likely chilling effects on parallel race-targeted educational programs.<br><br>"
        "<b>CULTURAL RESOURCE THREAT ASSESSMENT.</b> The threat level is SEVERE. The investigation challenges the legitimacy of race-targeted remedial education programs that have been a principal civil-rights instrument in U.S. K-12 education since the post-Brown era. The downstream effect, if the OCR theory prevails, is to constrain school-district capacity to address documented racial disparities in academic achievement, discipline, and educator representation. Black students in CPS and parallel jurisdictions face reduced district-level remedial-program capacity."
        "<br><br>"
        "<b>SOURCES.</b><br>"
        "Primary: Department of Education, 'U.S. Department of Education's Office for Civil Rights Launches Title VI Investigation into Chicago Public Schools.' <a href=\"https://www.ed.gov/about/news/press-release/us-department-of-educations-office-civil-rights-launches-title-vi-investigation-chicago-public-schools\">https://www.ed.gov/about/news/press-release/us-department-of-educations-office-civil-rights-launches-title-vi-investigation-chicago-public-schools</a><br>"
        "ABC7 Chicago: <a href=\"https://abc7chicago.com/post/us-department-education-investigating-chicago-public-schools-black-students-success-plan-defending-complaint/16281583/\">https://abc7chicago.com/post/us-department-education-investigating-chicago-public-schools-black-students-success-plan-defending-complaint/16281583/</a><br>"
        "NBC News: <a href=\"https://www.nbcnews.com/news/us-news/education-department-opens-investigation-chicago-public-schools-rcna203761\">https://www.nbcnews.com/news/us-news/education-department-opens-investigation-chicago-public-schools-rcna203761</a><br>"
        "CBS Chicago: <a href=\"https://www.cbsnews.com/chicago/news/department-education-chicago-public-schools-black-student-success-plan/\">https://www.cbsnews.com/chicago/news/department-education-chicago-public-schools-black-student-success-plan/</a><br>"
        "WTTW Chicago: <a href=\"https://news.wttw.com/2025/04/30/education-department-investigating-cps-black-student-success-plan-over-discrimination\">https://news.wttw.com/2025/04/30/education-department-investigating-cps-black-student-success-plan-over-discrimination</a><br>"
        "The 74 Million: <a href=\"https://www.the74million.org/article/chicago-public-schools-black-student-success-plan-under-investigation-over-dei/\">https://www.the74million.org/article/chicago-public-schools-black-student-success-plan-under-investigation-over-dei/</a><br>"
        "Critical analysis: Kids First Chicago, 'Investigation into CPS Black Student Success Plan Misses the Mark on Defending Civil Rights.' <a href=\"https://kidsfirstchicago.org/blog/investigation-into-cps-black-student-success-plan-misses-the-mark-on-defending-civil-rights\">https://kidsfirstchicago.org/blog/investigation-into-cps-black-student-success-plan-misses-the-mark-on-defending-civil-rights</a><br>"
        "Brookings: <a href=\"https://www.brookings.edu/articles/how-the-us-department-of-education-has-turned-civil-rights-enforcement-into-a-discriminatory-tool/\">https://www.brookings.edu/articles/how-the-us-department-of-education-has-turned-civil-rights-enforcement-into-a-discriminatory-tool/</a><br>"
        "Related tracker entries: ed-ocr-phd-project-31-colleges-2026-02-20; ed-ocr-title-ix-rescissions-2026-04-06."
    ),
    "I": {
        "africanDescendant": {
            "people": "CPS Black students and Black educators face the operational and legal challenge of the investigation. Black male educators specifically face the threat to the doubling-recruitment goal.",
            "places": "Chicago Public Schools system. Parallel jurisdictions with race-targeted remedial programs face chilling effect.",
            "practices": "Race-targeted remedial educational practice in K-12 settings is constrained.",
            "treasures": "Federal Title VI as a protective instrument for Black students is functionally inverted into an attack on Black-supportive programs."
        },
        "allCommunities": {
            "people": "All school districts with race-targeted remedial programs face chilling effect.",
            "places": "U.S. K-12 educational landscape.",
            "practices": "Federal civil-rights enforcement in education is reshaped.",
            "treasures": "The post-Brown civil-rights tradition is functionally inverted."
        }
    },
    "c": ["African-descendant", "All Communities"],
    "U": "https://www.ed.gov/about/news/press-release/us-department-of-educations-office-civil-rights-launches-title-vi-investigation-chicago-public-schools",
    "_source": "manual",
}


# ====== ENTRY I: DOJ MARIJUANA RESCHEDULING ======
ENTRY_I = {
    "i": "doj-marijuana-schedule-iii-2026-04-23",
    "t": "Department of Justice Final Order",
    "n": "DOJ Final Order: Cannabis Subject to State Medical Marijuana License Rescheduled to Schedule III of Controlled Substances Act (Acting AG Todd Blanche, April 23, 2026)",
    "T": '<span style="color: #CA8A04;">DOJ Final Order:</span> Cannabis Subject to State Medical Marijuana License Rescheduled to Schedule III. Acting AG Todd Blanche Signs April 23, 2026 Pursuant to Trump December 18, 2025 EO. DEA Hearing on Broader Rescheduling Set for June 29, 2026',
    "s": "DOJ marijuana Schedule III April 2026",
    "d": "2026-04-23",
    "a": "Trump II",
    "A": ["DOJ", "DEA", "Treasury", "IRS"],
    "S": "Active. DOJ Final Order signed April 23, 2026 by Acting Attorney General Todd Blanche. Reschedules two categories of marijuana from Schedule I to Schedule III: (1) FDA-approved drug products containing marijuana; (2) marijuana subject to a state-issued license to manufacture, distribute, or dispense for medical purposes only. Order issued pursuant to Trump December 18, 2025 Executive Order directing federal agencies to expedite marijuana rescheduling. DEA expedited hearing on broader rescheduling (all marijuana from Schedule I to Schedule III) scheduled for June 29, 2026 at the DEA Hearing Facility, Arlington, Virginia. Treasury and IRS announced parallel guidance on tax consequences. DEA Medical Marijuana Dispensary Registration Portal opened April 29, 2026.",
    "L": "HARMFUL",
    "D": (
        "<b>FINAL ORDER.</b> On April 23, 2026, the Department of Justice issued a Final Order under Acting Attorney General Todd Blanche immediately placing two categories of marijuana in Schedule III of the Controlled Substances Act (21 U.S.C. sec. 812): (1) drug products containing marijuana that have been approved by the U.S. Food and Drug Administration; (2) marijuana subject to a state-issued license to manufacture, distribute, or dispense for medical purposes only. The Order was issued pursuant to President Trump's December 18, 2025 Executive Order directing federal agencies to expedite marijuana rescheduling.<br><br>"
        "<b>BROADER RESCHEDULING HEARING.</b> The DEA published a Notice of Hearing on the proposed rulemaking to transfer all marijuana (including non-state-licensed and non-FDA-approved categories) from Schedule I to Schedule III. The hearing is scheduled to commence June 29, 2026 at 9:00 a.m. ET at the DEA Hearing Facility in Arlington, Virginia.<br><br>"
        "<b>TAX AND BANKING IMPLICATIONS.</b> The Treasury Department and IRS announced April 23, 2026 that they will issue guidance addressing federal tax consequences of the rescheduling, acknowledging that the Schedule III placement is expected to have significant positive tax consequences for state-licensed medical-marijuana businesses. Schedule III status removes the IRC sec. 280E business-deduction prohibition that has applied to state-legal cannabis operations. Banking-and-financial-services access for state-licensed medical-marijuana businesses also stands to expand.<br><br>"
        "<b>DEA REGISTRATION PORTAL.</b> The DEA Medical Marijuana Dispensary Registration Portal opened April 29, 2026 at 9:00 a.m. ET. State-licensed medical-marijuana operators may submit applications for federal registration through the portal.<br><br>"
        "<b>RELATIONSHIP TO INDIGENOUS-CEREMONIAL-MEDICINE FRAMEWORK.</b> The rescheduling does not alter the federal regulatory framework governing Indigenous-ceremonial use of peyote (mescaline, Schedule I, with American Indian Religious Freedom Act Amendments of 1994 (42 U.S.C. sec. 1996a) Native American Church exemption) or other psychedelic ceremonial medicines (ayahuasca under Gonzales v. UDV, 546 U.S. 418 (2006)). The marijuana rescheduling intersects with Indigenous-ceremonial-medicine policy through the parallel federal psychedelic-medicine pathway opened by the April 22, 2026 EO Accelerating Medical Treatments for Serious Mental Illness (tracked at eo-mental-illness-fda-acceleration-2026), which directs Commissioner's National Priority Vouchers for psychedelic drugs and DEA rescheduling reviews. The combined federal posture is selective rescheduling of FDA-approved psychedelic and cannabis compounds without integration of Indigenous-ceremonial-medicine reparative principles.<br><br>"
        "<b>RACIAL-JUSTICE IMPLICATIONS.</b> Marijuana criminalization has produced documented disparate-impact harm against African-descendant and Latiné communities. African-descendant Americans are arrested for marijuana offenses at approximately 3.6 times the rate of white Americans despite roughly equal use rates. The federal rescheduling reduces some forward-looking enforcement exposure but does not retroactively expunge state and federal marijuana convictions. Pending federal sentencing for ongoing cases may be affected. Past convictions remain on records absent further executive clemency or congressional action.<br><br>"
        "<b>CULTURAL RESOURCE THREAT ASSESSMENT.</b> The threat level is HARMFUL on net, with structural ambiguity. The rescheduling produces partial PROTECTIVE outcomes for state-legal cannabis operators (tax-deduction access, banking access) and reduces forward-looking federal-enforcement exposure. The HARMFUL classification reflects three structural concerns: (1) the rescheduling is selective (only FDA-approved and state-licensed medical) and leaves recreational-cannabis users exposed to federal Schedule III enforcement; (2) the rescheduling does not address past marijuana convictions whose disparate-impact harm to African-descendant and Latiné communities is the primary cultural-resource issue; (3) the parallel psychedelic-rescheduling pathway operates without Indigenous-ceremonial-medicine reparative integration. The classification will warrant re-evaluation as DEA hearing outcomes and broader rescheduling decisions emerge."
        "<br><br>"
        "<b>SOURCES.</b><br>"
        "Primary: DOJ Final Order, April 23, 2026 (Acting AG Todd Blanche).<br>"
        "Foley Hoag analysis: <a href=\"https://foleyhoag.com/news-and-insights/publications/alerts-and-updates/2026/april/cannabis-rescheduling-doj-treasury-and-dea-updates-since-the-april-23-order/\">https://foleyhoag.com/news-and-insights/publications/alerts-and-updates/2026/april/cannabis-rescheduling-doj-treasury-and-dea-updates-since-the-april-23-order/</a><br>"
        "Foley Hoag immediate analysis: <a href=\"https://foleyhoag.com/news-and-insights/publications/alerts-and-updates/2026/april/doj-immediately-reschedules-state-licensed-medical-cannabis-to-schedule-iii-and-restarts-the-clock/\">https://foleyhoag.com/news-and-insights/publications/alerts-and-updates/2026/april/doj-immediately-reschedules-state-licensed-medical-cannabis-to-schedule-iii-and-restarts-the-clock/</a><br>"
        "Filter Magazine: <a href=\"https://filtermag.org/doj-reclassifies-medical-marijuana-schedule-iii/\">https://filtermag.org/doj-reclassifies-medical-marijuana-schedule-iii/</a><br>"
        "Dentons: <a href=\"https://www.dentons.com/en/insights/alerts/2026/april/23/doj-reschedules\">https://www.dentons.com/en/insights/alerts/2026/april/23/doj-reschedules</a><br>"
        "Gibson Dunn: <a href=\"https://www.gibsondunn.com/dea-downschedules-state-medical-marijuana-to-schedule-iii-expedited-hearing-set-to-consider-broader-rescheduling/\">https://www.gibsondunn.com/dea-downschedules-state-medical-marijuana-to-schedule-iii-expedited-hearing-set-to-consider-broader-rescheduling/</a><br>"
        "Health Data Consortium: <a href=\"https://healthdataconsortium.org/marijuana-schedule-iii-2026-doj-order/\">https://healthdataconsortium.org/marijuana-schedule-iii-2026-doj-order/</a><br>"
        "Duane Morris: <a href=\"https://www.duanemorris.com/alerts/relief_finally_dea_issues_order_expediting_cannabis_rescheduling_schedule_iii_0426.html\">https://www.duanemorris.com/alerts/relief_finally_dea_issues_order_expediting_cannabis_rescheduling_schedule_iii_0426.html</a><br>"
        "Foley and Lardner: <a href=\"https://www.foley.com/insights/publications/2026/04/dea-issues-long-awaited-final-order-rescheduling-certain-marijuana-products-to-schedule-iii-what-it-means-what-it-doesnt-and-what-comes-next/\">https://www.foley.com/insights/publications/2026/04/dea-issues-long-awaited-final-order-rescheduling-certain-marijuana-products-to-schedule-iii-what-it-means-what-it-doesnt-and-what-comes-next/</a><br>"
        "Moritz Law: <a href=\"https://moritzlaw.osu.edu/faculty-and-research/drug-enforcement-and-policy-center/research-and-grants/policy-and-data-analyses/federal-marijuana-rescheduling\">https://moritzlaw.osu.edu/faculty-and-research/drug-enforcement-and-policy-center/research-and-grants/policy-and-data-analyses/federal-marijuana-rescheduling</a><br>"
        "Related tracker entries: eo-mental-illness-fda-acceleration-2026 (parallel psychedelic-medicine pathway)."
    ),
    "I": {
        "africanDescendant": {
            "people": "African-descendant Americans, who face approximately 3.6x marijuana-arrest disparity, see partial forward-looking enforcement-exposure reduction. Past convictions are not expunged. The disparate-impact harm of decades of criminalization persists.",
            "places": "African-descendant communities affected by historical drug-war policing.",
            "practices": "Black-community advocacy on marijuana policy reform gains a structural opening.",
            "treasures": "The federal drug-policy regime as a vehicle of racial-justice reform is partially activated."
        },
        "latine": {
            "people": "Latiné Americans face parallel disparate-impact reductions on a forward-looking basis. Past convictions persist.",
            "places": "Latiné communities affected by drug-war policing.",
            "practices": "Latiné community advocacy on drug-policy reform gains opening.",
            "treasures": "Latiné community drug-policy frameworks expand."
        },
        "indigenous": {
            "people": "Indigenous communities operating state-licensed medical-marijuana programs on reservation lands gain federal banking and tax access. Indigenous-ceremonial-medicine integration is not addressed.",
            "places": "Tribal-land cannabis operations.",
            "practices": "Tribal-cannabis-program practice gains federal financial-services access.",
            "treasures": "Tribal cannabis-policy frameworks expand."
        },
        "allCommunities": {
            "people": "All medical-marijuana patients in state-legal jurisdictions face partial federal regulatory clarification. State-legal cannabis operators face improved tax and banking environment.",
            "places": "State-legal cannabis-jurisdiction landscape.",
            "practices": "Federal cannabis-regulatory practice is reshaped.",
            "treasures": "The federal Controlled Substances Act framework is partially restructured."
        }
    },
    "c": ["African-descendant", "Latiné", "Indigenous", "All Communities"],
    "U": "https://foleyhoag.com/news-and-insights/publications/alerts-and-updates/2026/april/doj-immediately-reschedules-state-licensed-medical-cannabis-to-schedule-iii-and-restarts-the-clock/",
    "_source": "manual",
}


# ====== ENTRY J: ED OCR TITLE IX RESCISSIONS ======
ENTRY_J = {
    "i": "ed-ocr-title-ix-rescissions-2026-04-06",
    "t": "Federal Civil Rights Action",
    "n": "U.S. Department of Education Office for Civil Rights Rescinds Title IX Resolution Agreements with Five School Districts and Taft College Protecting Transgender Students (April 6, 2026)",
    "T": '<span style="color: #991B1B;">ED OCR Rescinds Title IX Agreements:</span> Five School Districts (Cape Henlopen DE, Delaware Valley PA, Fife WA, La Mesa-Spring Valley CA, Sacramento City CA) and Taft College CA Lose Federal Protections for Transgender Students',
    "s": "ED OCR Title IX rescissions Apr 2026",
    "d": "2026-04-06",
    "a": "Trump II",
    "A": ["ED", "OCR"],
    "S": "Active. Announced April 6, 2026. Office for Civil Rights partial-termination of six resolution agreements originally negotiated under Obama and Biden administrations. Affected institutions: Cape Henlopen School District (Delaware), Delaware Valley School District (Pennsylvania), Fife School District (Washington), La Mesa-Spring Valley School District (California), Sacramento City Unified School District (California), and Taft College (California). The terminations remove federal requirements for staff training on respecting students' preferred names and pronouns and for allowing students to use bathrooms aligning with their gender identity. OCR justification: prior agreements were based on the Biden administration's interpretation that federal antidiscrimination law applies to discrimination on the basis of gender identity rather than sex.",
    "L": "SEVERE",
    "D": (
        "<b>FEDERAL ACTION.</b> On April 6, 2026, the U.S. Department of Education's Office for Civil Rights (OCR) announced the partial termination of six Title IX resolution agreements protecting transgender students. The agreements had been negotiated under the Obama and Biden administrations following OCR investigations of discrimination complaints.<br><br>"
        "<b>AFFECTED INSTITUTIONS.</b> The terminations affect five school districts: Cape Henlopen School District (Delaware), Delaware Valley School District (Pennsylvania), Fife School District (Washington), La Mesa-Spring Valley School District (California), and Sacramento City Unified School District (California). Additionally, OCR announced it would no longer enforce a resolution agreement with Taft College (a community college in California).<br><br>"
        "<b>PROTECTIONS REMOVED.</b> The rescinded agreements had required affected institutions to implement specific transgender-student protections including: (1) staff training on respecting students' preferred names and pronouns; (2) allowing students to use bathrooms and facilities that align with their gender identity; (3) enforcing prohibitions on harassment based on gender identity. The rescissions remove the federal-government enforcement authority for these protections at the affected institutions.<br><br>"
        "<b>OCR LEGAL JUSTIFICATION.</b> OCR characterized the rescinded agreements as based on the Biden administration's 'distorted' interpretation that federal antidiscrimination law applies to discrimination on the basis of 'gender identity,' not sex. The OCR position parallels the Trump administration's broader rollback of transgender-student protections under Title IX, including federal-court litigation tracked at lit-2026-scotus-trans-athletes (SCOTUS trans-athletes cases) and the April 3, 2026 College Sports EO (tracked at eo-urgent-college-sports-2026-04-03).<br><br>"
        "<b>CHILLING EFFECT.</b> Chalkbeat analysis on April 14, 2026 characterized the rescissions as likely to spark a chain reaction of chilled civil-rights complaints in schools nationally. The rescissions signal to school districts that resolution agreements protecting transgender students may be terminated by future OCR action, reducing district incentive to enter into such agreements during ongoing OCR investigations. The downstream effect compounds the broader Trump II Department of Education Title IX rollback.<br><br>"
        "<b>BROADER PATTERN.</b> The rescissions operate within the Trump II Department of Education's coordinated Title VI and Title IX weaponization strategy, parallel to the PhD Project Title VI action (tracked at ed-ocr-phd-project-31-colleges-2026-02-20) and the CPS Black Students Success Plan investigation (tracked at ed-cps-black-students-success-investigation-2025-04-30). The combined effect is the inversion of federal civil-rights enforcement: protections for racial minorities and transgender students are recharacterized as discriminatory, and the federal-statutory framework is leveraged against the protective programs rather than against the underlying discrimination.<br><br>"
        "<b>CULTURAL RESOURCE THREAT ASSESSMENT.</b> The threat level is SEVERE for LGBTQ+ students at the affected institutions and chilled districts nationwide. Transgender students at the five named school districts and Taft College face removal of federal-enforcement-backed protections. The harm is operational and individualized: students lose name-and-pronoun-respect training mandates and bathroom-access protections at their institutions. Indirect harm extends to all districts that may decline to enter resolution agreements pending the OCR-rescission environment."
        "<br><br>"
        "<b>SOURCES.</b><br>"
        "Primary coverage: National Law Review, 'ED Civil Rights Office Rescinds Title IX Resolution Agreements With 5 Schools.' <a href=\"https://natlawreview.com/article/ed-civil-rights-office-rescinds-title-ix-resolution-agreements-5-schools\">https://natlawreview.com/article/ed-civil-rights-office-rescinds-title-ix-resolution-agreements-5-schools</a><br>"
        "Ogletree: <a href=\"https://ogletree.com/insights-resources/blog-posts/ed-civil-rights-office-rescinds-title-ix-resolution-agreements-with-5-schools/\">https://ogletree.com/insights-resources/blog-posts/ed-civil-rights-office-rescinds-title-ix-resolution-agreements-with-5-schools/</a><br>"
        "EdWeek: <a href=\"https://www.edweek.org/policy-politics/trump-admin-terminates-several-agreements-to-protect-transgender-students/2026/04\">https://www.edweek.org/policy-politics/trump-admin-terminates-several-agreements-to-protect-transgender-students/2026/04</a><br>"
        "K-12 Dive: <a href=\"https://www.k12dive.com/news/trump-education-department-rescinds-title-ix-pacts-protecting-lgbtq-students/816776/\">https://www.k12dive.com/news/trump-education-department-rescinds-title-ix-pacts-protecting-lgbtq-students/816776/</a><br>"
        "Inside Higher Ed: <a href=\"https://www.insidehighered.com/news/quick-takes/2026/04/07/education-dept-scraps-some-civil-rights-agreements\">https://www.insidehighered.com/news/quick-takes/2026/04/07/education-dept-scraps-some-civil-rights-agreements</a><br>"
        "Chalkbeat (chain-reaction analysis): <a href=\"https://www.chalkbeat.org/2026/04/14/trump-ending-title-ix-agreements-could-chill-civil-rights-complaints/\">https://www.chalkbeat.org/2026/04/14/trump-ending-title-ix-agreements-could-chill-civil-rights-complaints/</a><br>"
        "California-specific coverage: National Today, 'U.S. Ends Title IX Agreement With California School District Over Trans Student Protections.' <a href=\"https://nationaltoday.com/us/ca/spring-valley-ca/news/2026/04/07/u-s-ends-title-ix-agreement-with-california-school-district-over-trans-student-protections/\">https://nationaltoday.com/us/ca/spring-valley-ca/news/2026/04/07/u-s-ends-title-ix-agreement-with-california-school-district-over-trans-student-protections/</a><br>"
        "Related tracker entries: ed-ocr-phd-project-31-colleges-2026-02-20; ed-cps-black-students-success-investigation-2025-04-30; eo-urgent-college-sports-2026-04-03; lit-2026-scotus-trans-athletes."
    ),
    "I": {
        "lgbtq": {
            "people": "Transgender students at the five named school districts and Taft College face removal of federal-enforcement-backed name-and-pronoun and bathroom-access protections. Transgender students at districts considering Title IX resolution agreements face chilling effect.",
            "places": "Cape Henlopen DE, Delaware Valley PA, Fife WA, La Mesa-Spring Valley CA, Sacramento City CA, Taft College CA. Plus chilled districts nationwide.",
            "practices": "Transgender-student-protective school practice loses federal enforcement backing. LGBTQ+ student-organizing practice faces reduced institutional support.",
            "treasures": "Title IX as a federal-statutory protection for transgender students is functionally constrained."
        },
        "allCommunities": {
            "people": "All LGBTQ+ students and allies at affected institutions face altered school environments.",
            "places": "U.S. K-12 educational landscape and California community college sector.",
            "practices": "Federal Title IX enforcement practice is reshaped against transgender-student protection.",
            "treasures": "Title IX as a cultural-policy treasure is functionally constrained."
        }
    },
    "c": ["lgbtq", "All Communities"],
    "U": "https://natlawreview.com/article/ed-civil-rights-office-rescinds-title-ix-resolution-agreements-5-schools",
    "_source": "manual",
}


# ====== UPDATE TO ENTRY B: SCOTUS TPS ORAL ARGUMENTS ======
TPS_UPDATE_BLOCK = (
    "<br><br>"
    "<b>APRIL 29, 2026 ORAL ARGUMENTS UPDATE.</b> "
    "On April 29, 2026, the Supreme Court heard oral arguments in the consolidated TPS cases. Conservative justices appeared to lean toward backing the Trump administration's termination of Temporary Protected Status for approximately 350,000 Haitians and 6,000 Syrians. The conservative wing focused not on whether Trump violated federal law or the Equal Protection Clause by ending TPS for Haitian and Syrian nationals, but almost entirely on whether a federal court may review such termination decisions. Justice Sotomayor raised concerns about potential discrimination, citing Trump's prior controversial statements about Haiti. Justice Jackson noted that 'the position of the United States is that we have an actual racial epithet that we aren't allowed to look at all the context.' The decision is expected by June 2026. If the Court rules for the administration, TPS terminations for Haitians and Syrians proceed, with deportation processes activated against affected populations. Cross-references: louisiana-v-callais-scotus-2026-04-29 (parallel April 29 SCOTUS day with major civil-rights implications); v2025-imm-001 (TPS terminations for 1.5+ million); lit-2026-haiti-tps-extension; doj-v-syrian-tps-holders-2026.<br>"
    "Coverage of April 29 oral arguments: NPR, 'Supreme Court appears to lean toward ending TPS for some migrants.' <a href=\"https://www.npr.org/2026/04/29/nx-s1-5804707/supreme-court-tps\">https://www.npr.org/2026/04/29/nx-s1-5804707/supreme-court-tps</a>; "
    "Washington Post: <a href=\"https://www.washingtonpost.com/immigration/2026/04/29/supreme-court-tps-haitians-syrians-immigration/\">https://www.washingtonpost.com/immigration/2026/04/29/supreme-court-tps-haitians-syrians-immigration/</a>; "
    "Roll Call: <a href=\"https://rollcall.com/2026/04/28/supreme-court-to-hear-oral-arguments-over-deportation-protections/\">https://rollcall.com/2026/04/28/supreme-court-to-hear-oral-arguments-over-deportation-protections/</a>; "
    "Newsmax: <a href=\"https://www.newsmax.com/us/supreme-court-immigration-deportation/2026/04/29/id/1254669/\">https://www.newsmax.com/us/supreme-court-immigration-deportation/2026/04/29/id/1254669/</a>; "
    "CNN live: <a href=\"https://www.cnn.com/2026/04/29/politics/live-news/supreme-court-temporary-protected-status\">https://www.cnn.com/2026/04/29/politics/live-news/supreme-court-temporary-protected-status</a>"
)


def main():
    if not DATA_PATH.exists():
        raise SystemExit(f"data.json not found at {DATA_PATH}")

    em_dash = "—"
    new_entries = [
        ("litigation", ENTRY_A),
        ("legislation", ENTRY_C),
        ("agency_actions", ENTRY_D),
        ("executive_actions", ENTRY_E),
        ("agency_actions", ENTRY_F),
        ("agency_actions", ENTRY_G),
        ("agency_actions", ENTRY_H),
        ("agency_actions", ENTRY_I),
        ("agency_actions", ENTRY_J),
    ]

    for cat, e in new_entries:
        eid = e.get("id") or e.get("i")
        if em_dash in json.dumps(e, ensure_ascii=False):
            raise SystemExit(f"ABORT: em-dash detected in {eid}.")
    if em_dash in TPS_UPDATE_BLOCK:
        raise SystemExit("ABORT: em-dash detected in TPS update block.")

    shutil.copy2(DATA_PATH, BACKUP_PATH)
    print(f"Backup written: {BACKUP_PATH.name}")

    with DATA_PATH.open() as f:
        data = json.load(f)

    # Insert new entries
    for cat, entry in new_entries:
        eid = entry.get("id") or entry.get("i")
        existing = data.get(cat, [])
        if any((e.get("id") or e.get("i")) == eid for e in existing):
            raise SystemExit(f"Entry {eid} already exists in {cat}. Aborting.")
    for cat, entry in new_entries:
        data.setdefault(cat, []).append(entry)
        eid = entry.get("id") or entry.get("i")
        print(f"Inserted {eid} into {cat}.")

    # Update existing TPS entry
    target = None
    for e in data.get("litigation", []):
        if (e.get("id") or e.get("i")) == "lit-2026-scotus-tps-001":
            target = e
            break
    if target is None:
        print("WARNING: lit-2026-scotus-tps-001 not found; skipping TPS update.")
    else:
        if "APRIL 29, 2026 ORAL ARGUMENTS UPDATE" in target.get("D", ""):
            print("TPS entry already updated. Skipping.")
        else:
            target["D"] = target["D"] + TPS_UPDATE_BLOCK
            print("Updated lit-2026-scotus-tps-001 with April 29, 2026 oral arguments block.")

    if "meta" in data and isinstance(data["meta"], dict):
        data["meta"]["lastUpdated"] = datetime.now().strftime("%Y-%m-%d")

    tmp = DATA_PATH.with_suffix(".json.tmp")
    with tmp.open("w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    tmp.replace(DATA_PATH)

    print("Done.")


if __name__ == "__main__":
    main()
