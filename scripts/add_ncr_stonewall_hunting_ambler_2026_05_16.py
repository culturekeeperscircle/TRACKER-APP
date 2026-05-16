#!/usr/bin/env python3
"""Add 9 federal-cultural-resource-threat entries identified 2026-05-14 and verified 2026-05-16.

Five concern Trump II National Capital Region cultural-landscape alterations:
A. East Wing demolition and White House Ballroom construction (executive_actions, SEVERE)
B. National Trust for Historic Preservation v. Trump ballroom lawsuit (litigation, PROTECTIVE)
C. Grassley immigration package $1B earmark for ballroom security (legislation, SEVERE)
D. East Potomac Golf Links conversion to championship course (executive_actions, SEVERE)
E. United States Triumphal Arch at Memorial Circle (executive_actions, SEVERE)

Two concern Stonewall National Monument Pride Flag:
F. NPS Acting Director Bowron's flag directive triggers Pride Flag removal (agency_actions, SEVERE)
G. Lambda Legal settlement reinstates Pride Flag with court-enforced permanence (litigation, PROTECTIVE)

One concerns NPS hunting rules:
H. Secretarial Order 3447 loosens hunting restrictions at ~55 NPS sites (agency_actions, SEVERE)

One concerns federal equity in Alaska critical-minerals extraction:
I. Federal $35.6M 10% stake in Trilogy Metals plus Ambler Access Project approval (executive_actions, SEVERE)

Sources verified 2026-05-16 via WebSearch. Backup written before insert.
"""
import json
import shutil
from pathlib import Path
from datetime import datetime

DATA_PATH = Path(__file__).parent.parent / "data" / "data.json"
BACKUP_PATH = DATA_PATH.with_suffix(
    f".json.bak-{datetime.now().strftime('%Y%m%d-%H%M%S')}-pre-ncr-stonewall-hunting-ambler"
)


# ============================================================================
# ENTRY A: EAST WING DEMOLITION AND WHITE HOUSE BALLROOM CONSTRUCTION
# ============================================================================
ENTRY_A = {
    "i": "ea-2025-white-house-ballroom-east-wing",
    "t": "Executive Action",
    "n": "Trump II White House East Wing Demolition (October 20-24, 2025) and 90,000-Square-Foot Ballroom Construction at President's Park (NCPC Approval 8-1 on April 2, 2026 Post-Demolition; Federal Cost Approaching $1 Billion with Security Add-Ons)",
    "T": "<span style=\"color: #991B1B;\">East Wing Demolished:</span> Trump II Administration Demolishes Historic East Wing of the White House to Build 90,000-Square-Foot Ballroom Addition, with NCPC Review Compressed and Conducted After Demolition Was Complete",
    "s": "East Wing demolition and ballroom construction at the White House.",
    "d": "2025-10-20",
    "a": "Trump II",
    "A": ["WH", "NPS", "DOI", "GSA", "NCPC", "CFA"],
    "S": "Active. Demolition of the historic East Wing began October 20, 2025 and was complete by October 24, 2025. Construction began September 2025. NCPC approved the final project design 8 to 1 on April 2, 2026, after demolition was complete. Project announced at $200 million in July 2025; revised to $300 million in October 2025; federal cost approaching $1 billion with security additions (see entry leg-2026-ballroom-security-appropriation). National Trust for Historic Preservation lawsuit pending (see lit-2025-nthp-v-trump-ballroom). A National Park Service report disclosed in May 2026 that demolition debris was dumped at a nearby public golf course and contains lead, chromium, and other toxic metals.",
    "L": "SEVERE",
    "D": (
        "<b>ACTION.</b> On July 31, 2025, the Trump II administration announced demolition of the East Wing of the White House and construction of a 90,000-square-foot ballroom in its place. Demolition began October 20, 2025 and was complete by October 24, 2025. Construction began September 2025. The East Wing, originally constructed in 1902 and significantly expanded under First Lady Eleanor Roosevelt's supervision in 1942, housed the Office of the First Lady, the White House Visitors' Office, the East Colonnade, the Family Theater, and the public tour entrance. It was a contributing structure to the White House and President's Park National Historic Landmark District (designated 1960) and a feature of the White House UNESCO World Heritage Site (inscribed 1987). The Presidential Emergency Operations Center beneath the East Wing was dismantled and is being replaced by a new below-grade facility at undisclosed cost.<br><br>"
        "<b>LEGAL MECHANISM.</b> Asserted presidential authority over the White House complex, exercised through the Executive Office of the President in coordination with the General Services Administration. The project initially proceeded without National Capital Planning Commission review under 40 U.S.C. sec. 8722 and without National Environmental Policy Act review under 42 U.S.C. sec. 4332. NCPC subsequently reviewed and approved the final project design 8 to 1 on April 2, 2026, after the East Wing was already demolished and construction was underway. The review was therefore post-hoc rather than the customary pre-construction review prescribed by the National Capital Planning Act.<br><br>"
        "<b>FINANCING TRAJECTORY.</b> The administration initially stated the project would be privately funded at approximately $200 million. The cost estimate rose to $300 million in October 2025. As of May 2026, the federal commitment, including security upgrades earmarked through Senator Grassley's immigration funding package (cross-reference leg-2026-ballroom-security-appropriation), approaches $1 billion. The progression from privately funded to a $1 billion federal commitment inverts the original public representation of the project's funding model.<br><br>"
        "<b>CULTURAL HERITAGE ANALYSIS.</b> The East Wing was the principal public-facing portion of the White House complex. The public tour entrance, the offices of every modern First Lady, and the Family Theater were all housed there. Its replacement with a private ballroom for invitation-only social events inverts that civic relationship. Public-access civic space has been converted to elite-access private space inside the most symbolically important federal building in the United States. The 1942 expansion was designed by Lorenzo Winslow under Eleanor Roosevelt's supervision. The Family Theater hosted screenings reflecting cultural priorities of every First Family across multiple administrations, including screenings of films by Black, Latine, Indigenous, and women filmmakers under the Obama and Biden administrations. The Jacqueline Kennedy Garden sits adjacent to the demolished structure. Demolition extinguishes the material record of more than a century of accumulated First Lady and presidential family decisions.<br><br>"
        "The compressed, post-hoc NCPC review establishes a precedent for executive demolition of National Historic Landmark fabric before the statutorily prescribed review process is complete. If the precedent stands, every federal historic property is at greater risk, including properties of cultural significance to communities tracked by this project (African Burial Ground National Monument, Manzanar National Historic Site, Stonewall National Monument, Cesar Chavez National Monument, and others).<br><br>"
        "<b>SECONDARY HARM.</b> A National Park Service report disclosed in May 2026 that demolition debris from the East Wing was dumped at a nearby public golf course and contains lead, chromium, and other toxic metals. The debris-disposal pattern compounds the cultural harm with public-health and environmental harm to nearby NPS-managed land. Cross-reference ea-2026-east-potomac-championship-golf.<br><br>"
        "<b>CONTEXT.</b> This action occurs alongside the Trump II administration's parallel projects at East Potomac Park (cross-reference ea-2026-east-potomac-championship-golf), Memorial Circle (cross-reference ea-2026-triumphal-arch-memorial-circle), and the Columbus statue at the White House South Lawn (cross-reference ea-2026-columbus-statue), and the broader monument and federal-aesthetic program under EO 14253 (Restoring Truth and Sanity to American History), EO 14189 (National Garden of American Heroes), and EO 14344 (Architecture: Beautiful Again). Together these actions constitute a coordinated executive program of physical alteration of the federally managed National Capital Region cultural landscape, advanced largely outside or ahead of the statutory review framework Congress prescribed.<br><br>"
        "<b>SOURCES.</b><br>"
        "White House announcement: <a href=\"https://www.whitehouse.gov/briefings-statements/2025/07/the-white-house-announces-white-house-ballroom-construction-to-begin/\">https://www.whitehouse.gov/briefings-statements/2025/07/the-white-house-announces-white-house-ballroom-construction-to-begin/</a><br>"
        "Axios NCPC hearing coverage: <a href=\"https://www.axios.com/2025/12/26/trump-white-house-ballroom-east-wing-review\">https://www.axios.com/2025/12/26/trump-white-house-ballroom-east-wing-review</a><br>"
        "Fortune on toxic-metal debris at public golf course: <a href=\"https://fortune.com/2026/05/07/white-house-east-wing-demolition-debris-toxic-metals-golf-course-trump/\">https://fortune.com/2026/05/07/white-house-east-wing-demolition-debris-toxic-metals-golf-course-trump/</a><br>"
        "TIME on military complex below ballroom: <a href=\"https://time.com/article/2026/04/17/white-house-military-complex-bunker-trump-ballroom/\">https://time.com/article/2026/04/17/white-house-military-complex-bunker-trump-ballroom/</a><br>"
        "Wikipedia background: <a href=\"https://en.wikipedia.org/wiki/White_House_State_Ballroom\">https://en.wikipedia.org/wiki/White_House_State_Ballroom</a>"
    ),
    "I": {
        "africanDescendant": {
            "people": "Black First Ladies-in-residence (Michelle Obama) used East Wing offices to advance initiatives of direct significance to African-descendant communities, including Let's Move, Reach Higher, and Joining Forces. The Family Theater hosted screenings of films by Black filmmakers and historical screenings of significance to African American cultural memory. The architectural record of these uses is destroyed.",
            "places": "President's Park sits within the broader cultural landscape of Black Washington and a city that is one of the United States' principal African-descendant cultural capitals. Demolition of NHL fabric without standard pre-construction review establishes a precedent endangering African American National Historic Landmarks (African Burial Ground, Frederick Douglass National Historic Site, Maggie L. Walker NHS, and others).",
            "practices": "Public-tour access to the White House has been a civic practice central to American political participation. Conversion of the public-tour entrance to private-ballroom space removes a longstanding public-access civic practice.",
            "treasures": "The material record of Black First Lady executive-branch labor (Michelle Obama's East Wing offices, the Family Theater's curatorial choices under Black First Families) is extinguished by demolition."
        },
        "latine": {
            "people": "Latine communities accessed the East Wing tour entrance and Family Theater programming under prior administrations that engaged Latine cultural institutions (including the Smithsonian National Museum of the American Latino partnership). Public-access civic space converts to private-ballroom use.",
            "places": "The demolition precedent endangers Latine National Historic Landmarks (Cesar Chavez National Monument, La Mesilla Plaza, and others) subject to NHPA Section 106 review.",
            "practices": "Public-tour civic practice that connected Latine families to the federal commemorative landscape is removed.",
            "treasures": "Latine cultural-policy infrastructure that ran through First Lady offices is materially erased."
        },
        "indigenous": {
            "people": "President's Park sits on the ancestral homelands of the Nacotchtank (Anacostan) and Piscataway peoples. Major federal alterations to the White House complex without standard pre-construction review proceed without consultation on land whose Indigenous historical claims have never been adequately addressed.",
            "places": "The compressed, post-hoc NHL review process establishes a precedent that endangers Indigenous sacred sites elsewhere on federal lands subject to NHPA Section 106. Indigenous National Historic Landmarks (Sand Creek Massacre, Bears Ears Cultural Resources, Chaco Culture, Effigy Mounds) face similar procedural risk.",
            "practices": "Federal consultation practice with tribal historic preservation offices loses procedural force when the executive branch demonstrates that it can demolish NHL fabric in advance of review.",
            "treasures": "Tribal Historic Preservation Office practice depends on the integrity of Section 106 review procedures. Those procedures are weakened by the East Wing precedent."
        },
        "asianAmerican": {
            "people": "Asian American visitors accessed the East Wing tour entrance and Family Theater programming under prior administrations. Public-access civic space converts to private-ballroom use.",
            "places": "The demolition precedent endangers Asian American National Historic Landmarks (Manzanar, Tule Lake, Minidoka, Wing Luke Museum) subject to NHPA Section 106 review.",
            "practices": "Public-tour civic practice that connected Asian American families to the federal commemorative landscape is removed.",
            "treasures": "Asian American cultural-policy infrastructure that ran through First Lady offices is materially erased."
        },
        "pacificIslander": {
            "people": "Pacific Islander visitors accessed the East Wing tour entrance and Family Theater programming under prior administrations. Public-access civic space converts to private-ballroom use.",
            "places": "The demolition precedent endangers Pacific Islander cultural sites (Honouliuli National Historic Site, the Pacific Islander cultural landscape at the Smithsonian Asian Pacific American Center) subject to NHPA Section 106 review.",
            "practices": "Public-tour civic practice that connected Pacific Islander families to the federal commemorative landscape is removed.",
            "treasures": "Pacific Islander cultural-policy infrastructure that ran through First Lady offices is materially erased."
        },
        "allCommunities": {
            "people": "Loss of public-facing civic space inside the White House. The East Wing housed the public tour entrance used by tens of thousands of Americans annually. Conversion to a private ballroom for invitation-only social events removes civic access. Demolition debris dumped at a nearby public golf course contains lead, chromium, and other toxic metals.",
            "places": "Demolition of a National Historic Landmark contributing structure and feature of a UNESCO World Heritage Site. NCPC review was conducted post-hoc on April 2, 2026, after demolition was already complete.",
            "practices": "Federal procedural practice governing review of construction on NHL fabric loses force when review can be compressed and conducted after demolition is complete.",
            "treasures": "The architectural fabric of the East Wing, the Office of the First Lady's institutional home, and the Family Theater are irrecoverable."
        }
    },
    "c": ["African-descendant", "Latiné", "Indigenous", "Asian", "Pacific Islander", "All Communities", "women", "lgbtq", "working-class"],
    "U": "https://www.whitehouse.gov/briefings-statements/2025/07/the-white-house-announces-white-house-ballroom-construction-to-begin/",
    "_source": "manual",
}


# ============================================================================
# ENTRY B: NTHP v. TRUMP BALLROOM LAWSUIT
# ============================================================================
ENTRY_B = {
    "i": "lit-2025-nthp-v-trump-ballroom",
    "t": "Court Filing",
    "n": "National Trust for Historic Preservation v. Trump (D.D.C. Filed December 2025): Preservation Coalition Suit Challenging East Wing Demolition and Ballroom Construction for Failure to File with NCPC, Conduct NEPA Review, or Secure Congressional Authorization (Preliminary Injunction Denied March 31, 2026)",
    "T": "<span style=\"color: #166534;\">Preservation Lawsuit:</span> National Trust for Historic Preservation Sues Trump II Administration in D.D.C. to Halt East Wing Demolition and Ballroom Construction; Preliminary Injunction Denied March 31, 2026 but Case Continues Post-NCPC Approval",
    "s": "NTHP v. Trump preservation litigation challenging East Wing demolition.",
    "d": "2025-12-09",
    "a": "Trump II",
    "A": ["DOJ", "WH", "NPS", "DOI", "GSA", "NCPC", "CFA"],
    "S": "Filed December 2025 in U.S. District Court for the District of Columbia. Plaintiff National Trust for Historic Preservation. Preliminary injunction denied by the court on March 31, 2026; the court left open the possibility for the plaintiff to enhance its legal arguments. NCPC subsequently voted 8 to 1 on April 2, 2026 to approve the final project design, after demolition was complete. Litigation continues to develop the legal record. PACER docket number to be confirmed.",
    "L": "PROTECTIVE",
    "D": (
        "<b>LITIGATION.</b> The National Trust for Historic Preservation filed a complaint in December 2025 in the United States District Court for the District of Columbia seeking declaratory and injunctive relief against the Trump II administration's demolition of the East Wing of the White House and construction of a large ballroom in its place.<br><br>"
        "<b>CLAIMS PRESENTED.</b> The complaint alleges that the project (1) was not filed with the National Capital Planning Commission as required by 40 U.S.C. sec. 8722, (2) began without an environmental assessment or environmental impact statement as required by NEPA (42 U.S.C. sec. 4332), and (3) was not authorized by Congress.<br><br>"
        "<b>PROCEDURAL POSTURE.</b> On March 31, 2026 the court denied the National Trust's motion for a preliminary injunction. The court left open the possibility for the plaintiff to enhance its legal arguments. On April 2, 2026 NCPC voted 8 to 1 to approve the final project design, an action the National Trust criticized as a post-hoc procedural fig leaf. Litigation continues to develop the legal record.<br><br>"
        "<b>SIGNIFICANCE.</b> This is a PROTECTIVE entry. The litigation is the principal legal vehicle through which the public, including communities of cultural significance whose access to the White House complex is at stake, can seek redress. A favorable ruling would establish that executive authority over the White House complex does not displace congressional procedural mandates governing federal historic properties, National Capital Region construction, and environmental review. An unfavorable ruling would entrench the precedent that the executive may demolish National Historic Landmark fabric in advance of the statutory review the Act prescribes. Cross-reference ea-2025-white-house-ballroom-east-wing (underlying demolition) and leg-2026-ballroom-security-appropriation (related congressional security appropriation).<br><br>"
        "<b>SOURCES.</b><br>"
        "PBS NewsHour on the suit's procedural and substantive claims: <a href=\"https://www.pbs.org/newshour/politics/preservationists-sue-trump-for-ballroom-project-reviews-and-congressional-approval\">https://www.pbs.org/newshour/politics/preservationists-sue-trump-for-ballroom-project-reviews-and-congressional-approval</a><br>"
        "ABC News: <a href=\"https://abcnews.com/Politics/national-trust-historic-preservation-sues-stop-white-house/story?id=128351219\">https://abcnews.com/Politics/national-trust-historic-preservation-sues-stop-white-house/story?id=128351219</a><br>"
        "Courthouse News on PI denial: <a href=\"https://www.courthousenews.com/judge-denies-effort-to-halt-white-house-ballroom-construction/\">https://www.courthousenews.com/judge-denies-effort-to-halt-white-house-ballroom-construction/</a><br>"
        "ABC News on judicial skepticism: <a href=\"https://abcnews.com/Politics/white-house-ballroom-judge-signals-skepticism-trump-administration/story?id=129471562\">https://abcnews.com/Politics/white-house-ballroom-judge-signals-skepticism-trump-administration/story?id=129471562</a><br>"
        "Fortune coverage: <a href=\"https://fortune.com/2025/12/14/trumps-east-wing-white-house-ballroom-challenged-lawsuit/\">https://fortune.com/2025/12/14/trumps-east-wing-white-house-ballroom-challenged-lawsuit/</a><br>"
        "Construction Owners coverage: <a href=\"https://www.constructionowners.com/news/national-trust-sues-over-white-house-east-wing-demolition\">https://www.constructionowners.com/news/national-trust-sues-over-white-house-east-wing-demolition</a>"
    ),
    "I": {
        "africanDescendant": {
            "people": "PROTECTIVE. Litigation seeks to halt demolition that destroyed the East Wing offices used by Black First Ladies and the Family Theater that hosted programming significant to African American cultural memory.",
            "places": "PROTECTIVE. A favorable ruling would strengthen Section 106 and NCPC review for African American National Historic Landmarks subject to future executive alteration.",
            "practices": "PROTECTIVE. The suit defends the procedural practice of pre-construction federal review on NHL fabric.",
            "treasures": "PROTECTIVE. The Voting Rights Act of 1965, the National Historic Preservation Act of 1966, and NEPA (1970) are all federal civil-rights and procedural treasures that the suit operationalizes."
        },
        "latine": {
            "people": "PROTECTIVE. Litigation defends procedural protections at federal historic properties of significance to Latine communities.",
            "places": "PROTECTIVE. A favorable ruling strengthens NHL review for Cesar Chavez NM, La Mesilla, and other Latine sites.",
            "practices": "PROTECTIVE. Civic-tour public access is defended by the suit's challenge to the conversion of the East Wing's tour entrance.",
            "treasures": "PROTECTIVE. The federal procedural framework protecting historic properties is defended."
        },
        "indigenous": {
            "people": "PROTECTIVE. Litigation strengthens NHPA Section 106 procedural protections on federal land. President's Park sits on Nacotchtank and Piscataway homelands; a favorable ruling reinforces consultation obligations.",
            "places": "PROTECTIVE. A favorable ruling protects sacred sites and ancestral lands at federally managed properties from future executive demolition without consultation.",
            "practices": "PROTECTIVE. THPO consultation practice is defended.",
            "treasures": "PROTECTIVE. The NHPA itself is operationalized."
        },
        "asianAmerican": {
            "people": "PROTECTIVE. Litigation defends procedural protections at federal historic properties of significance to Asian American communities.",
            "places": "PROTECTIVE. Manzanar, Tule Lake, Minidoka, and other Asian American NHLs benefit from a strong NCPC and Section 106 framework.",
            "practices": "PROTECTIVE. Federal-review practice is defended.",
            "treasures": "PROTECTIVE. The federal procedural framework protecting historic properties is defended."
        },
        "pacificIslander": {
            "people": "PROTECTIVE. Litigation defends procedural protections at federal historic properties of significance to Pacific Islander communities.",
            "places": "PROTECTIVE. Honouliuli National Historic Site and other Pacific Islander cultural sites benefit from a strong NCPC and Section 106 framework.",
            "practices": "PROTECTIVE. Federal-review practice is defended.",
            "treasures": "PROTECTIVE. The federal procedural framework protecting historic properties is defended."
        },
        "allCommunities": {
            "people": "PROTECTIVE. Litigation defends the public-tour civic access converted to private ballroom space and seeks to strengthen federal procedural review on NHL fabric.",
            "places": "PROTECTIVE. A favorable ruling protects every NHL property nationwide.",
            "practices": "PROTECTIVE. Pre-construction federal review on NHL fabric is the practice the suit defends.",
            "treasures": "PROTECTIVE. The National Historic Preservation Act and the National Environmental Policy Act are operationalized."
        }
    },
    "c": ["All Communities", "African-descendant", "Indigenous", "Latiné", "Asian", "Pacific Islander", "women", "lgbtq"],
    "U": "https://www.pbs.org/newshour/politics/preservationists-sue-trump-for-ballroom-project-reviews-and-congressional-approval",
    "_source": "manual",
}


# ============================================================================
# ENTRY C: GRASSLEY $1B BALLROOM SECURITY APPROPRIATION
# ============================================================================
ENTRY_C = {
    "i": "leg-2026-ballroom-security-appropriation",
    "t": "Legislation",
    "n": "Senate Republican Immigration Funding Package (Released May 5, 2026) Containing $1 Billion Earmark for Secret Service Security Adjustments and Upgrades Related to the East Wing Modernization Project (Bundled Inside Approximately $70 Billion ICE and CBP Enforcement Funding Reconciliation Vehicle)",
    "T": "<span style=\"color: #991B1B;\">$1B Taxpayer Earmark:</span> Senate Republican Immigration Funding Package Includes $1 Billion in Taxpayer Money for Security Adjustments and Upgrades Related to the East Wing Modernization Project, Contradicting Trump's Repeated Pledge That the Ballroom Would Be Privately Funded",
    "s": "Grassley immigration package $1B earmark for ballroom security.",
    "d": "2026-05-05",
    "a": "Trump II",
    "A": ["Congress", "WH", "Secret Service", "DHS", "ICE", "CBP", "OMB"],
    "S": "Under Senate consideration as of mid-May 2026. Senate Judiciary Committee Chairman Chuck Grassley (R-IA) released the funding bill on May 5, 2026. The $1 billion earmark is bundled inside a Senate Republican package allocating more than $70 billion to enforcement agencies over three years. Senate Republicans (Susan Collins, R-ME, among them) have publicly raised concerns. Bill number and full procedural status to be confirmed.",
    "L": "SEVERE",
    "D": (
        "<b>ACTION.</b> On May 5, 2026 Senate Judiciary Committee Chairman Chuck Grassley (R-IA) released a long-term immigration and border patrol funding bill that includes $1 billion earmarked for security adjustments and upgrades relating to the East Wing Modernization Project. The earmark is part of a larger Senate Republican package allocating more than $70 billion to enforcement agencies over three years, with the $1 billion specifically directed to the Secret Service for security at the new ballroom.<br><br>"
        "<b>LEGAL MECHANISM.</b> Article I, Section 9 appropriations power. The funding is bundled inside the Republican immigration and border-funding package rather than addressed in standalone or supplemental legislation specific to the East Wing project. The bundling structure makes the ballroom security earmark harder to vote against on its own merits because it is procedurally tied to immigration-enforcement spending. Bill number to be confirmed from Congress.gov.<br><br>"
        "<b>FISCAL AND CULTURAL ANALYSIS.</b> $1 billion in federal funds is approximately three times the entire annual budget of the National Endowment for the Humanities and roughly five times the annual budget of the National Endowment for the Arts. It exceeds the entire annual budget of the Institute of Museum and Library Services. The opportunity cost is severe. The same sum could fully fund the federal share of the deferred-maintenance backlog at multiple Indigenous and African American National Historic Sites, capitalize a permanent Cultural Sustainability endowment at NPS, complete Section 106 and NAGPRA compliance backlogs across the Department of the Interior, or substantially fund cultural data sovereignty infrastructure for federally recognized tribes.<br><br>"
        "<b>POLITICAL CONTEXT.</b> Trump publicly stated in September 2025, 'I'm paying for it; the country's not,' and in February 2026, 'no charge to the taxpayer whatsoever.' The pivot from privately funded to a $1 billion federal security earmark mirrors the funding pattern observed for other Trump II monumental projects (the National Garden of American Heroes was likewise initially announced as privately financed and later capitalized via redirected federal funding). Maine Republican Senator Susan Collins has publicly stated that the ballroom should be privately funded as originally pledged.<br><br>"
        "Cross-reference ea-2025-white-house-ballroom-east-wing (underlying demolition) and lit-2025-nthp-v-trump-ballroom (preservation litigation).<br><br>"
        "<b>SOURCES.</b><br>"
        "NPR: <a href=\"https://www.npr.org/2026/05/06/g-s1-120455/republicans-trump-ballroom-billion\">https://www.npr.org/2026/05/06/g-s1-120455/republicans-trump-ballroom-billion</a><br>"
        "The Hill: <a href=\"https://thehill.com/homenews/senate/5867162-gop-ballroom-billion-taxpayer-security/\">https://thehill.com/homenews/senate/5867162-gop-ballroom-billion-taxpayer-security/</a><br>"
        "CNN Politics: <a href=\"https://www.cnn.com/2026/05/05/politics/white-house-ballroom-taxpayers\">https://www.cnn.com/2026/05/05/politics/white-house-ballroom-taxpayers</a><br>"
        "CNN follow-up on Senate Republican calculus: <a href=\"https://www.cnn.com/2026/05/11/politics/trump-ballroom-security-funding-congress\">https://www.cnn.com/2026/05/11/politics/trump-ballroom-security-funding-congress</a><br>"
        "NBC News: <a href=\"https://www.nbcnews.com/politics/white-house/republicans-propose-1-billion-taxpayer-dollars-secure-trump-ballroom-rcna343637\">https://www.nbcnews.com/politics/white-house/republicans-propose-1-billion-taxpayer-dollars-secure-trump-ballroom-rcna343637</a><br>"
        "House Appropriations (Democrats) press release: <a href=\"https://democrats-appropriations.house.gov/news/press-releases/senate-republicans-unveil-70-billion-giveaway-ballroom-ice-and-cbp\">https://democrats-appropriations.house.gov/news/press-releases/senate-republicans-unveil-70-billion-giveaway-ballroom-ice-and-cbp</a><br>"
        "Snopes scope check: <a href=\"https://www.snopes.com/news/2026/05/08/taxpayers-white-house-ballroom/\">https://www.snopes.com/news/2026/05/08/taxpayers-white-house-ballroom/</a>"
    ),
    "I": {
        "africanDescendant": {
            "people": "$1 billion in federal funds redirected to ballroom security represents opportunity cost in the form of cultural-preservation, civil-rights, and community-development funding that could have flowed to African American communities. The Smithsonian National Museum of African American History and Culture annual federal appropriation could be doubled with this sum.",
            "places": "Deferred-maintenance backlog at African American National Historic Sites (Frederick Douglass, Maggie L. Walker, African Burial Ground, Pullman, and others) is unfunded while $1 billion goes to ballroom security.",
            "practices": "Black cultural-preservation practice depends on federal funding through NPS, NEH, NEA, and IMLS. The earmark reduces the political space for adequate appropriations to those programs.",
            "treasures": "The opportunity cost is measured against the federal cultural-policy infrastructure that protects African American cultural treasures."
        },
        "latine": {
            "people": "$1 billion is approximately the same magnitude as the federal investment that built the National Museum of the American Latino, currently being planned. Diverting that sum to ballroom security delays Latine cultural infrastructure.",
            "places": "Cesar Chavez National Monument and other Latine sites face deferred-maintenance backlogs that this sum could close.",
            "practices": "Latine cultural-preservation practice through NPS, NEH, NEA, and IMLS is constrained by federal-funding diversion.",
            "treasures": "Latine cultural-policy infrastructure is constrained by the opportunity cost."
        },
        "indigenous": {
            "people": "$1 billion is comparable to the entire annual BIA Tribal Priority Allocation budget. Diverting that sum to ballroom security represents a federal-priorities inversion that subordinates Indigenous cultural-resource needs to White House aesthetics.",
            "places": "NAGPRA compliance backlog, sacred-site protection, and Section 106 consultation infrastructure across DOI face funding deficits that this sum could close.",
            "practices": "Tribal cultural-preservation practice through Tribal Historic Preservation Offices is underfunded; the earmark reflects a federal-priorities inversion.",
            "treasures": "Indigenous cultural-data-sovereignty infrastructure, ancestral-remains repatriation, and sacred-site protection are all underfunded while $1 billion flows to ballroom security."
        },
        "asianAmerican": {
            "people": "Asian American cultural-policy investment (Smithsonian Asian Pacific American Center, Manzanar, Tule Lake, Minidoka) faces deferred-maintenance backlogs that this sum could close.",
            "places": "Japanese American incarceration sites and other Asian American NHLs face unmet capital needs.",
            "practices": "Asian American cultural-preservation practice through NPS, NEH, NEA, and IMLS is constrained.",
            "treasures": "Asian American cultural-policy infrastructure is constrained by the opportunity cost."
        },
        "pacificIslander": {
            "people": "Pacific Islander cultural-policy investment (Honouliuli National Historic Site, Smithsonian Asian Pacific American Center Pacific Islander programming) faces deferred-maintenance backlogs that this sum could close.",
            "places": "Pacific Islander cultural sites face unmet capital needs.",
            "practices": "Pacific Islander cultural-preservation practice through NPS, NEH, NEA, and IMLS is constrained.",
            "treasures": "Pacific Islander cultural-policy infrastructure is constrained by the opportunity cost."
        },
        "allCommunities": {
            "people": "$1 billion in taxpayer funds for ballroom security inverts the Trump administration's repeated public pledge that the project would be privately funded. The diversion of public funds to private-event-venue security at the White House represents a federal-priorities inversion at the scale of multiple federal cultural-agency annual budgets.",
            "places": "Federal cultural-resource infrastructure across NPS, NEH, NEA, IMLS, and the Smithsonian faces unmet capital and operating needs that this sum could substantially address.",
            "practices": "Federal cultural-policy budgeting practice is distorted by the bundled-earmark mechanism that ties ballroom security to immigration enforcement.",
            "treasures": "Federal cultural-policy infrastructure as a public treasure is reduced by the diversion."
        }
    },
    "c": ["All Communities", "African-descendant", "Indigenous", "Latiné", "Asian", "Pacific Islander", "working-class"],
    "U": "https://www.npr.org/2026/05/06/g-s1-120455/republicans-trump-ballroom-billion",
    "_source": "manual",
}


# ============================================================================
# ENTRY D: EAST POTOMAC GOLF LINKS CONVERSION TO CHAMPIONSHIP COURSE
# ============================================================================
ENTRY_D = {
    "i": "ea-2026-east-potomac-championship-golf",
    "t": "Executive Action",
    "n": "Trump II Conversion of East Potomac Golf Links (NPS-Managed, 1920 Public Course, National Register of Historic Places) into Championship Tournament-Grade Facility of More Than 7,600 Yards; National Links Trust Operating Agreement (May 8, 2026) Preserves Langston and Rock Creek Public Courses; Hains Point Status Reported as Untouched in May 14, 2026 Design Release",
    "T": "<span style=\"color: #991B1B;\">East Potomac Privatized for Championship Golf:</span> Trump II Administration Converts NPS-Managed Public Golf Course into Championship-Style Tournament Facility on McMillan-Plan Cultural Landscape, with National Links Trust Deal Preserving Langston and Rock Creek and Hains Point Status Reported as Untouched in May 2026 Design",
    "s": "East Potomac Golf Links converted to championship course on NPS land.",
    "d": "2026-05-08",
    "a": "Trump II",
    "A": ["DOI", "NPS", "GSA"],
    "S": "Active. Department of the Interior announced an operating-agreement deal with National Links Trust on May 8, 2026 keeping Langston Golf Course and Rock Creek Park Golf Course under NLT management as public courses. Interior Secretary Doug Burgum released East Potomac Golf Links design plans on May 14, 2026, showing a 7,600+ yard championship layout. Hains Point appears untouched in the May 14, 2026 design as released, contrary to some earlier reporting that indicated possible closure. Watchdog litigation pending; an emergency motion was filed in early May 2026 seeking to halt the project. Case caption to be confirmed.",
    "L": "SEVERE",
    "D": (
        "<b>ACTION.</b> The Trump II administration, through the Department of the Interior, is converting East Potomac Golf Links (a public NPS-managed golf course on the 327-acre East Potomac Park peninsula in Southwest Washington, opened 1920) into a championship-grade 18-hole tournament course of more than 7,600 yards from the championship tees and more than 5,700 yards from the front tees. The project is positioned to potentially host major professional tournaments, including the Ryder Cup. Interior Secretary Doug Burgum released design plans for the converted course on May 14, 2026.<br><br>"
        "<b>OPERATING-AGREEMENT DEAL.</b> On May 8, 2026, the Department of the Interior announced an operating-agreement deal with the National Links Trust under which Langston Golf Course and Rock Creek Park Golf Course will remain under NLT management and remain open to the public. This deal resolved one dimension of public concern about the broader project but does not address the underlying conversion of East Potomac Golf Links to a championship facility nor the procedural questions about the project's review.<br><br>"
        "<b>HAINS POINT STATUS.</b> As of the May 14, 2026 design release, reporting (WTOP, Washington Post) indicates that Hains Point (the southern tip of the peninsula, the location of historic public-recreation amenities including the former Awakening sculpture site, picnic areas, fishing access, and Cherry Blossom Festival viewpoints) appears untouched in the released design. Earlier proposals or reporting may have included Hains Point closure or absorption into the championship course; the May 2026 design as released does not confirm closure. This entry reports the May 2026 status and will be updated if the final scope is changed by subsequent NPS action or contractor changes.<br><br>"
        "<b>LEGAL MECHANISM.</b> Federal land-management action on NPS-administered land. Project subject to NEPA review (42 U.S.C. sec. 4332), Section 106 of the NHPA (54 U.S.C. sec. 306108) given East Potomac Park's National Register listing, and the National Capital Planning Act (40 U.S.C. sec. 8722). Status of each review to be confirmed. Watchdog organizations have filed litigation alleging procurement irregularities and absence of required environmental and historic review. An emergency motion was filed in early May 2026.<br><br>"
        "<b>CULTURAL HERITAGE AND ENVIRONMENTAL ANALYSIS.</b> East Potomac Park is part of the McMillan Plan landscape (1902) and contributes to the National Mall NHL District and the L'Enfant and McMillan Plan as historically significant federal city design. East Potomac Golf Course (1920) is one of the oldest continuously operating public golf courses in the United States. The historic significance of the site includes its role in municipal-recreation integration in the segregated Jim Crow capital.<br><br>"
        "The harms remain concrete and severable even with the National Links Trust deal preserving Langston and Rock Creek public access. Conversion of a public municipal course into a championship-grade tournament facility shifts the user base toward higher-income tournament players and away from the working-class DC residents who have used the public course for over a century. The conversion alters the cultural landscape of a contributing district to the National Mall NHL. Watchdog litigation alleges NEPA and Section 106 bypass and procurement irregularities. A National Park Service report disclosed in May 2026 that demolition debris from the East Wing was dumped at a nearby public golf course (cross-reference ea-2025-white-house-ballroom-east-wing). The pattern indicates that Trump II construction projects in the National Capital Region are using NPS-managed land as disposal sites.<br><br>"
        "<b>CONTEXT.</b> This action is part of a coordinated Trump II executive program of physical alteration of the National Capital Region cultural landscape outside or ahead of standard procedural review. Cross-reference ea-2025-white-house-ballroom-east-wing, ea-2026-triumphal-arch-memorial-circle, and ea-2026-columbus-statue.<br><br>"
        "<b>SOURCES.</b><br>"
        "Washington Post on the project's threat to a treasured DC park: <a href=\"https://www.washingtonpost.com/dc-md-va/2026/05/09/east-potomac-hains-point-trump-golf/\">https://www.washingtonpost.com/dc-md-va/2026/05/09/east-potomac-hains-point-trump-golf/</a><br>"
        "Washington Post on May 14, 2026 design release: <a href=\"https://www.washingtonpost.com/sports/2026/05/14/trump-administration-releases-new-design-east-potomac-golf-course/\">https://www.washingtonpost.com/sports/2026/05/14/trump-administration-releases-new-design-east-potomac-golf-course/</a><br>"
        "WTOP on the National Links Trust deal: <a href=\"https://wtop.com/dc/2026/05/dcs-public-golf-courses-will-remain-open-under-new-deal-with-trump-administration/\">https://wtop.com/dc/2026/05/dcs-public-golf-courses-will-remain-open-under-new-deal-with-trump-administration/</a><br>"
        "WTOP on Burgum design release: <a href=\"https://wtop.com/dc/2026/05/design-plans-for-east-potomac-golf-links-renovation-shared-by-trump-administration/\">https://wtop.com/dc/2026/05/design-plans-for-east-potomac-golf-links-renovation-shared-by-trump-administration/</a><br>"
        "Axios DC on the legal fight: <a href=\"https://www.axios.com/local/washington-dc/2026/05/04/trump-east-potomac-golf-course-plan-closure\">https://www.axios.com/local/washington-dc/2026/05/04/trump-east-potomac-golf-course-plan-closure</a><br>"
        "Washington Post on emergency motion: <a href=\"https://www.washingtonpost.com/sports/2026/05/03/east-potomac-golf-trump-emergency-lawsuit/\">https://www.washingtonpost.com/sports/2026/05/03/east-potomac-golf-trump-emergency-lawsuit/</a><br>"
        "Washington Post on judge ruling: <a href=\"https://www.washingtonpost.com/sports/2026/05/04/east-potomac-open-judge-ruling/\">https://www.washingtonpost.com/sports/2026/05/04/east-potomac-open-judge-ruling/</a>"
    ),
    "I": {
        "africanDescendant": {
            "people": "SE/SW DC residents (predominantly Black, including residents of Wards 6, 7, and 8 public and subsidized housing) have relied on East Potomac Park as accessible NPS open space. The historic East Potomac Golf Course was significant as a site of municipal-recreation integration in the segregated capital. Conversion to a championship tournament-grade course alters that public-recreation character even with the NLT deal preserving Langston and Rock Creek.",
            "places": "East Potomac Park is a contributing district to the National Mall NHL and part of the McMillan Plan landscape. Black DC's relationship to this NPS land is historic and ongoing. The Langston Golf Course (preserved under the NLT deal) is itself a Black-history site, established 1939 and named for Congressman John Mercer Langston, the first Black U.S. House member from Virginia and the first president of Virginia State University.",
            "practices": "Public-recreation practice by Black DC families on accessible NPS land is altered by the championship conversion. The Cherry Blossom Festival, an event of cross-community significance with significant Black DC family participation, is reshaped by the project.",
            "treasures": "The cultural-landscape integrity of East Potomac Park as Black-DC-accessible NPS open space is materially altered."
        },
        "latine": {
            "people": "Latine DC residents and visitors use East Potomac Park for recreation. Conversion to championship facility alters public access character.",
            "places": "East Potomac Park as accessible NPS open space serves Latine DC families.",
            "practices": "Public-recreation practice is altered by championship conversion.",
            "treasures": "Cultural-landscape integrity is altered."
        },
        "indigenous": {
            "people": "East Potomac Park sits on the ancestral homelands of the Nacotchtank (Anacostan) and Piscataway peoples along the Potomac River. Federal construction on land with Indigenous historical significance, especially riverine sites, raises Section 106 consultation questions.",
            "places": "The Potomac River corridor is ancestral Nacotchtank and Piscataway territory. Federal alteration of cultural landscape on this land without standard pre-construction consultation establishes a precedent.",
            "practices": "Federal Section 106 consultation practice with descendant tribal communities is at issue.",
            "treasures": "Indigenous historical claims to the Potomac corridor are inadequately addressed by the project's review process."
        },
        "asianAmerican": {
            "people": "Asian American DC residents and visitors use East Potomac Park for recreation. The Cherry Blossom Festival has significant Asian American participation and the cherry trees themselves were gifts from Japan in 1912.",
            "places": "The Cherry Blossom landscape at East Potomac Park is a site of Japanese American and broader Asian American cultural significance.",
            "practices": "Cherry Blossom viewing practice and Asian American public-recreation practice are affected.",
            "treasures": "The Cherry Blossom landscape is a cultural treasure of cross-community significance, with particular meaning for Japanese American communities."
        },
        "pacificIslander": {
            "people": "Pacific Islander DC residents and visitors use East Potomac Park for recreation. Conversion alters public access.",
            "places": "East Potomac Park as accessible NPS open space serves Pacific Islander DC families.",
            "practices": "Public-recreation practice is altered.",
            "treasures": "Cultural-landscape integrity is altered."
        },
        "allCommunities": {
            "people": "Privatization-style conversion of public NPS land. Even with the May 8, 2026 National Links Trust deal preserving Langston and Rock Creek as public courses, the East Potomac championship conversion alters the public-access character of NPS-managed land that has served working-class DC residents for over a century.",
            "places": "Conversion of NHL-District-contributing federal cultural landscape (McMillan Plan), with NEPA and Section 106 status disputed in pending litigation.",
            "practices": "Federal land-management practice on NPS land is altered by the conversion of a public municipal course to a championship tournament facility.",
            "treasures": "The McMillan Plan landscape as a cultural treasure of the federal city is altered."
        }
    },
    "c": ["All Communities", "African-descendant", "working-class", "Indigenous", "Asian", "Latiné", "Pacific Islander", "women", "lgbtq"],
    "U": "https://www.washingtonpost.com/dc-md-va/2026/05/09/east-potomac-hains-point-trump-golf/",
    "_source": "manual",
}


# ============================================================================
# ENTRY E: UNITED STATES TRIUMPHAL ARCH AT MEMORIAL CIRCLE
# ============================================================================
ENTRY_E = {
    "i": "ea-2026-triumphal-arch-memorial-circle",
    "t": "Executive Action",
    "n": "United States Triumphal Arch Construction at Memorial Circle (250 Feet Tall, 60-Foot Gilded Lady Liberty Statue, Inscriptions 'One Nation Under God' and 'Liberty and Justice for All', CFA Concept Approval April 16, 2026, Targeting Pre-July-4-2026 Semiquincentennial Completion, Veterans-Led Federal Litigation Pending)",
    "T": "<span style=\"color: #991B1B;\">250-Foot Triumphal Arch:</span> Trump II Administration Plans 250-Foot Triumphal Arch at Memorial Circle Topped by 60-Foot Gilded 'Lady Liberty,' Approved by Commission of Fine Arts April 16, 2026 Over Nearly Universal Public Opposition, with Veterans-Led Federal Litigation Pending",
    "s": "Triumphal Arch at Memorial Circle, viewshed alteration on National Mall.",
    "d": "2026-04-16",
    "a": "Trump II",
    "A": ["NPS", "DOI", "NCPC", "CFA", "GSA"],
    "S": "Active. CFA approved the design concept on April 16, 2026 in a contested vote. Site survey work has begun. A group of veterans and a historian filed federal litigation seeking to block construction, arguing the arch would disrupt the sightline between the Lincoln Memorial and Arlington House at Arlington National Cemetery. Nearly 1,000 public comments were submitted with reporting indicating 100 percent opposed the project. Target completion before July 4, 2026 (the U.S. semiquincentennial). Case caption and current construction status to be confirmed.",
    "L": "SEVERE",
    "D": (
        "<b>ACTION.</b> The Trump II administration announced plans for a 250-foot triumphal arch at Memorial Circle, the traffic and ceremonial circle on the Boundary Channel between the District of Columbia and Arlington, Virginia, at the western terminus of Arlington Memorial Bridge. The arch is to be topped by a 60-foot gilded statue the President has called Lady Liberty, flanked by two smaller golden eagles. The inscriptions are 'One Nation Under God' on the front face and 'Liberty and Justice for All' on the opposite face. The U.S. Commission of Fine Arts approved the design concept on April 16, 2026. The administration is targeting completion before July 4, 2026, the semiquincentennial of U.S. independence. Site survey work has begun.<br><br>"
        "<b>LEGAL MECHANISM.</b> Federal construction in the National Capital Region requires NCPC review under 40 U.S.C. sec. 8722 and Commission of Fine Arts review under 40 U.S.C. sec. 9102. CFA approved the concept on April 16, 2026. NCPC status to be confirmed. Construction within the viewshed of the National Mall NHL District and at the boundary of Arlington National Cemetery requires Section 106 NHPA consultation under 54 U.S.C. sec. 306108. A coalition of veterans and a historian have filed federal litigation alleging that the arch would disrupt the historically protected sightline between the Lincoln Memorial and Arlington House at Arlington National Cemetery.<br><br>"
        "<b>CULTURAL HERITAGE AND VIEWSHED ANALYSIS.</b> Memorial Bridge and Memorial Circle are the deliberately designed ceremonial axis of national reconciliation, completed in 1932 as the symbolic linkage of the Union Lincoln Memorial to Confederate-general-turned-cemetery Arlington House. The viewshed is bidirectional. From the Lincoln Memorial steps, the bridge frames Arlington House and the cemetery's wooded hillside. From Arlington House and the cemetery, the bridge frames the Lincoln Memorial, the Reflecting Pool, the Washington Monument, and the Capitol dome. This bidirectional ceremonial axis is one of the most recognized planned views in the United States and is integral to the National Mall as cultural landscape.<br><br>"
        "A 250-foot triumphal arch with a 60-foot gilded statue at Memorial Circle permanently interrupts both directions of view. From the Lincoln Memorial, the arch occupies the foreground that the McMillan Plan designed to be a wooded greensward rising to Arlington House. From Arlington House, the arch interrupts the framed view down the bridge axis to the Lincoln Memorial. The viewshed alteration is permanent and irreversible.<br><br>"
        "The choice of a triumphal arch as the architectural form is itself culturally significant. Triumphal arches in the European tradition (Arch of Constantine, Arc de Triomphe, Brandenburg Gate) commemorate military conquest. Inserting that form at the gateway to Arlington National Cemetery alters the meaning of the cemetery from a site of mourning, sacrifice, and reconciliation to a site of triumphal commemoration. The gilded statue called Lady Liberty and the inscriptions further reframe the site in nationalist-religious terms. The shift in meaning is consequential for Veterans, Gold Star families, and the millions of Americans for whom Arlington is a sacred space of mourning rather than triumph.<br><br>"
        "Public opposition is overwhelming. Nearly 1,000 public comments were submitted with reporting indicating 100 percent opposed the project. The CFA approval was contested. Veterans-led litigation is pending.<br><br>"
        "<b>CONTEXT.</b> This action is part of a coordinated Trump II executive program of physical alteration of the National Capital Region cultural landscape outside standard procedural review. Cross-reference ea-2025-white-house-ballroom-east-wing, ea-2026-east-potomac-championship-golf, ea-2026-columbus-statue, and the broader monument program under EO 14253, EO 14189, and EO 14344.<br><br>"
        "<b>SOURCES.</b><br>"
        "ARLnow on CFA approval: <a href=\"https://www.arlnow.com/2026/04/16/federal-commission-approves-concept-for-trumps-triumphal-arch-near-memorial-bridge/\">https://www.arlnow.com/2026/04/16/federal-commission-approves-concept-for-trumps-triumphal-arch-near-memorial-bridge/</a><br>"
        "ARLnow on 250-foot renderings: <a href=\"https://www.arlnow.com/2026/04/10/just-in-new-renderings-show-250-foot-triumphal-arch-proposed-for-traffic-circle-near-memorial-bridge/\">https://www.arlnow.com/2026/04/10/just-in-new-renderings-show-250-foot-triumphal-arch-proposed-for-traffic-circle-near-memorial-bridge/</a><br>"
        "NPR on Trump's released plans: <a href=\"https://www.npr.org/2026/04/11/nx-s1-5782027/trump-triumphal-arch-plans-architecture\">https://www.npr.org/2026/04/11/nx-s1-5782027/trump-triumphal-arch-plans-architecture</a><br>"
        "Al Jazeera on US panel approval: <a href=\"https://www.aljazeera.com/news/2026/4/16/us-panel-approves-trumps-design-for-massive-arch-in-washington-dc\">https://www.aljazeera.com/news/2026/4/16/us-panel-approves-trumps-design-for-massive-arch-in-washington-dc</a><br>"
        "TIME on global arch comparisons: <a href=\"https://time.com/article/2026/04/11/how-trump-s-proposed-triumphal-arch-stacks-up-against-others-around-the-world/\">https://time.com/article/2026/04/11/how-trump-s-proposed-triumphal-arch-stacks-up-against-others-around-the-world/</a><br>"
        "Prism on site surveys: <a href=\"https://www.prismnews.com/news/trumps-proposed-triumphal-arch-moves-forward-with-site\">https://www.prismnews.com/news/trumps-proposed-triumphal-arch-moves-forward-with-site</a><br>"
        "Washington Examiner on survey work: <a href=\"https://www.washingtonexaminer.com/news/white-house/4564041/survey-work-trump-triumphal-arch-dc/\">https://www.washingtonexaminer.com/news/white-house/4564041/survey-work-trump-triumphal-arch-dc/</a><br>"
        "Spectrum News on CFA vote: <a href=\"https://spectrumlocalnews.com/us/snplus/politics/2026/04/16/trump-triumphal-arch-washington-dc-commission-fine-arts-meeting-vote-approve-concept-\">https://spectrumlocalnews.com/us/snplus/politics/2026/04/16/trump-triumphal-arch-washington-dc-commission-fine-arts-meeting-vote-approve-concept-</a><br>"
        "WJLA on federal review: <a href=\"https://wjla.com/news/local/triumphal-arch-lincoln-memorial-arlington-national-cemetery-vote-trump-columbia-island-white-house-national-mall-washington-dc-historic-preservation-leavitt-monument-proposal-construction\">https://wjla.com/news/local/triumphal-arch-lincoln-memorial-arlington-national-cemetery-vote-trump-columbia-island-white-house-national-mall-washington-dc-historic-preservation-leavitt-monument-proposal-construction</a><br>"
        "Wikipedia: <a href=\"https://en.wikipedia.org/wiki/United_States_Triumphal_Arch\">https://en.wikipedia.org/wiki/United_States_Triumphal_Arch</a>"
    ),
    "I": {
        "africanDescendant": {
            "people": "Arlington National Cemetery contains the graves of Black Civil War USCT soldiers (in Section 27, the historic Freedman's Village site), Buffalo Soldiers, Tuskegee Airmen, and Black servicemembers from every American conflict. Reframing the cemetery's gateway as a site of military triumph rather than mourning alters the meaning of Black military sacrifice commemorated there.",
            "places": "Section 27 at Arlington (the Freedman's Village cemetery) and the broader Arlington landscape as a Black-history site are reframed by the arch's nationalist-triumphal architecture.",
            "practices": "Black families' practice of visiting Arlington for memorial purposes is altered by the cemetery's gateway being reframed in triumphal terms.",
            "treasures": "Arlington National Cemetery as a Black-history treasure (Section 27, the Freedman's Village memorial, Tuskegee Airmen graves) is reframed by the arch."
        },
        "latine": {
            "people": "Arlington contains the graves of Latine servicemembers across multiple conflicts. The cemetery's gateway being reframed as triumphal alters the meaning of Latine military sacrifice commemorated there.",
            "places": "Arlington as a site of Latine military memorial is reframed.",
            "practices": "Latine families' practice of visiting Arlington for memorial purposes is altered.",
            "treasures": "Arlington as a treasure of Latine military memorial is reframed."
        },
        "indigenous": {
            "people": "Memorial Circle and the Arlington side of the Potomac sit on Nacotchtank and Piscataway homelands. Federal construction of monumental military-triumphal architecture on Indigenous land without consultation compounds historical erasure with new permanent symbolic claims. Arlington also contains graves of Indigenous servicemembers (Code Talkers, Iraq and Afghanistan veterans).",
            "places": "Memorial Circle sits on Nacotchtank and Piscataway ancestral territory. The cultural landscape is altered without consultation.",
            "practices": "Indigenous families' practice of visiting Arlington for memorial purposes (including Code Talker memorials) is affected.",
            "treasures": "Indigenous claims to the Potomac corridor are further obscured by monumental construction."
        },
        "asianAmerican": {
            "people": "Arlington contains the graves of Asian American servicemembers including 442nd Regimental Combat Team Japanese American soldiers, Korean American, Filipino American, and Vietnamese American veterans. The cemetery's gateway being reframed alters the meaning of Asian American military sacrifice.",
            "places": "Arlington as a site of Asian American military memorial (notably the 442nd RCT) is reframed.",
            "practices": "Asian American families' practice of visiting Arlington for memorial purposes is altered.",
            "treasures": "The 442nd RCT memorial tradition at Arlington and broader Asian American military memorial are reframed."
        },
        "pacificIslander": {
            "people": "Arlington contains the graves of Pacific Islander servicemembers. Per-capita Pacific Islander military service rates are among the highest of any U.S. demographic group. The cemetery's gateway being reframed alters the meaning of Pacific Islander military sacrifice.",
            "places": "Arlington as a site of Pacific Islander military memorial is reframed.",
            "practices": "Pacific Islander families' practice of visiting Arlington for memorial purposes is altered.",
            "treasures": "Pacific Islander military memorial tradition at Arlington is reframed."
        },
        "allCommunities": {
            "people": "Permanent alteration of the National Mall's most-recognized planned bidirectional viewshed. The McMillan Plan ceremonial axis between the Lincoln Memorial and Arlington House is integral to the Mall as cultural landscape and is irreplaceable. Public opposition was nearly universal in the comment record. Arlington as a site of mourning, sacrifice, and reconciliation is the meaning Veterans, Gold Star families, and the public have understood for nearly a century. A triumphal arch reframes the cemetery's gateway in the European military-triumph tradition.",
            "places": "Construction within the National Mall NHL District and at the Arlington National Cemetery boundary, with significant adverse effect on character-defining viewsheds.",
            "practices": "Federal commemoration practice at the National Mall and Arlington is altered by the introduction of triumphal-arch architecture.",
            "treasures": "The McMillan Plan bidirectional viewshed and the Mall as cultural landscape are altered."
        }
    },
    "c": ["All Communities", "Veterans", "Indigenous", "African-descendant", "Asian", "Pacific Islander", "Latiné"],
    "U": "https://www.arlnow.com/2026/04/16/federal-commission-approves-concept-for-trumps-triumphal-arch-near-memorial-bridge/",
    "_source": "manual",
}


# ============================================================================
# ENTRY F: STONEWALL PRIDE FLAG REMOVAL (BOWRON DIRECTIVE)
# ============================================================================
ENTRY_F = {
    "i": "agency-2026-stonewall-pride-flag-removed",
    "t": "Agency Action",
    "n": "NPS Acting Director Jessica Bowron's January 2026 Flag Directive Prohibiting Non-Agency Flags Triggers Early-February 2026 Removal of the Pride Flag from Stonewall National Monument at Christopher Park in Greenwich Village, New York",
    "T": "<span style=\"color: #991B1B;\">Pride Flag Removed from Stonewall:</span> NPS Acting Director Jessica Bowron Signs January 2026 Directive Prohibiting Non-Agency Flags, Triggering February 2026 Removal of the Pride Flag from Stonewall National Monument at Christopher Park, the First U.S. National Monument Dedicated to LGBTQ History",
    "s": "Pride Flag removed from Stonewall National Monument under NPS directive.",
    "d": "2026-02-10",
    "a": "Trump II",
    "A": ["NPS", "DOI"],
    "S": "Active until reversed by April 13, 2026 Stonewall settlement (cross-reference lit-2026-stonewall-pride-flag-settlement). Lambda Legal lawsuit filed February 17, 2026. Congressional letter from Rep. Dan Goldman (D-NY) and colleagues sent February 11, 2026 to Interior Secretary Burgum and NPS Acting Director Bowron objecting to the removal.",
    "L": "SEVERE",
    "D": (
        "<b>ACTION.</b> The National Park Service, under Trump II administration leadership, removed the Pride Flag (Rainbow Flag) from Stonewall National Monument at Christopher Park (38-64 Christopher Street, Manhattan, New York) in early February 2026. The removal followed a January 2026 NPS directive, signed by Acting Director Jessica Bowron, prohibiting non-agency flags and pennants other than the U.S. flag and the Interior Department flag at NPS sites. The flag removal was preceded by a February 2025 NPS edit removing references to transgender and queer people from the agency's Stonewall webpage.<br><br>"
        "<b>LEGAL MECHANISM.</b> Internal NPS administrative directive on flag display at federal units. Stonewall National Monument was designated by President Obama on June 24, 2016 by Presidential Proclamation 9465 (81 Fed. Reg. 42223), the first U.S. national monument dedicated to LGBTQ rights and history. Christopher Park, the small triangular park across from the Stonewall Inn, is the federal-land component of the monument.<br><br>"
        "<b>CULTURAL HERITAGE ANALYSIS.</b> The Pride Flag at Stonewall is not decorative. It is constitutive of the monument's commemorative meaning. Stonewall National Monument exists specifically because the 1969 Stonewall Uprising, led by Black and Latine trans women including Marsha P. Johnson, Stormé DeLarverie, and Sylvia Rivera and the broader LGBTQ community of Greenwich Village, is the foundational event of the modern American LGBTQ civil rights movement. The Pride Flag, designed by Gilbert Baker in 1978, is the principal symbol of that movement. Removing the Pride Flag from Stonewall is the symbolic equivalent of removing the Pan-African colors from the National Museum of African American History and Culture or removing the AIM flag from a site commemorating Wounded Knee. The flag and the monument are inseparable as commemorative meaning.<br><br>"
        "The non-agency flags framing is consequential. By treating the Pride Flag as a generic non-agency asset rather than a constitutive element of a specific monument's commemorative function, the directive reframes a community-defining symbol as bureaucratically equivalent to any other flag. The administrative form is itself a denial of the monument's designating purpose. Critics including Lambda Legal noted that the directive contained an exemption for flags that provide historical context, an exemption that plainly covers the Pride Flag at Stonewall.<br><br>"
        "The cultural harm is multiplicative. Stonewall National Monument is the principal federal recognition of LGBTQ history and rights. Its visible symbolism is the principal way visitors, especially LGBTQ youth, recognize their inclusion in the federally commemorated American story. Removal communicates federal disrecognition.<br><br>"
        "<b>CONTEXT.</b> This action coincides with the Trump II administration's broader rollback of federal LGBTQ recognition (EO 14168, Defending Women from Gender Ideology Extremism; removal of trans and queer content from federal websites; restoration of military service restrictions; defunding of LGBTQ health and education programs). The Stonewall flag removal is the most visible federal-monument-level expression of that broader program.<br><br>"
        "Cross-reference lit-2026-stonewall-pride-flag-settlement (Lambda Legal lawsuit and the April 13, 2026 settlement reinstating the Pride Flag with permanent-installation language). Cross-reference eo-14168 (Defending Women from Gender Ideology Extremism).<br><br>"
        "<b>SOURCES.</b><br>"
        "CNN on flag removal: <a href=\"https://www.cnn.com/2026/02/10/politics/pride-flag-removed-stonewall-monument-trump-administration\">https://www.cnn.com/2026/02/10/politics/pride-flag-removed-stonewall-monument-trump-administration</a><br>"
        "Axios on the underlying flag policy: <a href=\"https://www.axios.com/2026/02/10/stonewall-pride-flag-removed-national-park-service\">https://www.axios.com/2026/02/10/stonewall-pride-flag-removed-national-park-service</a><br>"
        "ABC News: <a href=\"https://abcnews.com/US/trump-admin-removes-pride-flag-stonewall-national-monument/story?id=130023944\">https://abcnews.com/US/trump-admin-removes-pride-flag-stonewall-national-monument/story?id=130023944</a><br>"
        "The Hill on resulting lawsuit: <a href=\"https://thehill.com/regulation/court-battles/5745979-stonewall-monument-pride-flag/\">https://thehill.com/regulation/court-battles/5745979-stonewall-monument-pride-flag/</a><br>"
        "Sierra Club press release: <a href=\"https://www.sierraclub.org/press-releases/2026/02/national-park-service-removes-pride-flag-stonewall-national-monument\">https://www.sierraclub.org/press-releases/2026/02/national-park-service-removes-pride-flag-stonewall-national-monument</a><br>"
        "Goldman congressional letter (Feb 11, 2026): <a href=\"https://goldman.house.gov/sites/evo-subsites/goldman.house.gov/files/evo-media-document/2.11.26-letter-to-nps-on-stonewall-pride-flag-removal.1.pdf\">https://goldman.house.gov/sites/evo-subsites/goldman.house.gov/files/evo-media-document/2.11.26-letter-to-nps-on-stonewall-pride-flag-removal.1.pdf</a><br>"
        "Ark Valley Voice on lawsuit: <a href=\"https://arkvalleyvoice.com/pride-flag-removed-from-stonewall-national-monument-lawsuit-ensues-to-return-it/\">https://arkvalleyvoice.com/pride-flag-removed-from-stonewall-national-monument-lawsuit-ensues-to-return-it/</a><br>"
        "TIME on NY officials' response: <a href=\"https://time.com/7377621/stonewall-national-monument-new-york-officials-pride-flag-removed-trump-administration/\">https://time.com/7377621/stonewall-national-monument-new-york-officials-pride-flag-removed-trump-administration/</a>"
    ),
    "I": {
        "africanDescendant": {
            "people": "Marsha P. Johnson and Stormé DeLarverie (both Black) led the 1969 Stonewall Uprising. The Pride Flag at Stonewall commemorates Black trans leadership in the founding event of the modern LGBTQ rights movement. Removal erases that Black trans leadership from federal commemoration. Black LGBTQ youth lose visible federal recognition at the monument that uniquely commemorates them.",
            "places": "Stonewall National Monument as a site of Black trans-leadership commemoration is materially altered by the flag's removal.",
            "practices": "Federal commemorative practice that recognized Black trans leadership in the LGBTQ rights movement is suspended.",
            "treasures": "The Pride Flag at Stonewall as a treasure commemorating Black trans leadership in the modern LGBTQ rights movement is removed."
        },
        "latine": {
            "people": "Sylvia Rivera (Puerto Rican) and other Latine LGBTQ leaders were central to the Stonewall Uprising. Federal removal of the Pride Flag at Stonewall erases Latine trans leadership from federal commemoration. Latine LGBTQ youth lose visible federal recognition.",
            "places": "Stonewall NM as a site of Latine trans-leadership commemoration is altered.",
            "practices": "Federal commemorative practice that recognized Latine trans leadership is suspended.",
            "treasures": "The Pride Flag at Stonewall as a treasure commemorating Latine trans leadership is removed."
        },
        "indigenous": {
            "people": "Indigenous Two-Spirit and LGBTQ community members are commemorated at Stonewall as part of the broader movement that the flag represents. Christopher Park sits on Lenape (Lenapehoking) ancestral homeland. Federal disrecognition compounds historical erasure.",
            "places": "Christopher Park on Lenape land becomes a site of compounded erasure.",
            "practices": "Indigenous Two-Spirit federal recognition (already inadequate) is further diminished.",
            "treasures": "Federal LGBTQ commemorative infrastructure that Indigenous Two-Spirit advocates have helped build is diminished."
        },
        "asianAmerican": {
            "people": "Asian American LGBTQ community members lose visible federal recognition at the principal federal LGBTQ monument.",
            "places": "Stonewall as a site of cross-community LGBTQ commemoration is altered.",
            "practices": "Federal LGBTQ commemorative practice loses force.",
            "treasures": "The Pride Flag at Stonewall as a treasure of cross-community LGBTQ commemoration is removed."
        },
        "pacificIslander": {
            "people": "Pacific Islander LGBTQ community members (including the Native Hawaiian Mahu tradition) lose visible federal recognition.",
            "places": "Stonewall as a site of cross-community LGBTQ commemoration is altered.",
            "practices": "Federal LGBTQ commemorative practice loses force.",
            "treasures": "The Pride Flag at Stonewall as a treasure of cross-community LGBTQ commemoration is removed."
        },
        "allCommunities": {
            "people": "Direct federal disrecognition of LGBTQ commemoration at the principal federal monument to LGBTQ history. The Pride Flag at Stonewall is constitutive of the monument's commemorative meaning. Removal is communicative federal action denying the monument's designating purpose. Removal of a community-defining symbol from a federal monument designated specifically for that community establishes a precedent for selective federal disrecognition of any commemorated community.",
            "places": "Stonewall National Monument is the only U.S. national monument designated specifically for LGBTQ history. Removal of the Pride Flag from the federal land component (Christopher Park) attacks the visible federal recognition of the site.",
            "practices": "Federal monument-display practice is converted into a tool of selective disrecognition. The non-agency flags framing makes community-defining symbols bureaucratically interchangeable.",
            "treasures": "The Pride Flag at Stonewall, designed by Gilbert Baker in 1978, is a treasure of the modern LGBTQ rights movement. Its removal from the principal federal site of LGBTQ commemoration is the most visible federal-monument-level expression of the Trump II administration's broader LGBTQ rollback."
        }
    },
    "c": ["lgbtq", "All Communities", "African-descendant", "Latiné", "Indigenous", "Asian", "Pacific Islander"],
    "U": "https://www.cnn.com/2026/02/10/politics/pride-flag-removed-stonewall-monument-trump-administration",
    "_source": "manual",
}


# ============================================================================
# ENTRY G: LAMBDA LEGAL STONEWALL SETTLEMENT
# ============================================================================
ENTRY_G = {
    "i": "lit-2026-stonewall-pride-flag-settlement",
    "t": "Court Filing",
    "n": "Lambda Legal and Washington Litigation Group v. NPS and DOI (S.D.N.Y. Filed February 17, 2026): Stonewall National Monument Pride Flag Restoration Settlement Announced April 13, 2026 Requiring NPS to Rehang the Pride Flag Within Seven Days and Maintain It Permanently Alongside the U.S. Flag and the NPS Flag with Court-Retained Enforcement Jurisdiction",
    "T": "<span style=\"color: #166534;\">Pride Flag Restored at Stonewall:</span> Lambda Legal and Washington Litigation Group Secure Court-Enforceable Settlement Requiring NPS to Rehang the Pride Flag at Stonewall National Monument Within Seven Days and Maintain It Permanently with Court-Retained Enforcement Jurisdiction",
    "s": "Lambda Legal settlement permanently restores Pride Flag at Stonewall NM.",
    "d": "2026-04-13",
    "a": "Trump II",
    "A": ["NPS", "DOI", "DOJ"],
    "S": "Settlement reached April 13, 2026. Pride Flag to be rehung within seven days of settlement, flying permanently alongside the U.S. flag and the NPS flag. Court retains jurisdiction to enforce the stipulation. Lambda Legal filed the underlying suit on February 17, 2026 on behalf of multiple LGBTQ nonprofit organizations. Plaintiff list and case caption to be confirmed.",
    "L": "PROTECTIVE",
    "D": (
        "<b>LITIGATION AND SETTLEMENT.</b> Following the February 2026 removal of the Pride Flag from Stonewall National Monument (cross-reference agency-2026-stonewall-pride-flag-removed), Lambda Legal and Washington Litigation Group filed suit on February 17, 2026 on behalf of multiple LGBTQ nonprofit organizations against the National Park Service, the Department of the Interior, and Interior Secretary Doug Burgum. The complaint argued that the Trump II flag directive illegally targeted the LGBTQ community, because the directive contained an exemption for flags that provide historical context, an exemption that plainly covers the Pride Flag at Stonewall.<br><br>"
        "<b>SETTLEMENT TERMS.</b> On April 13, 2026, Lambda Legal announced a court-enforceable settlement with the federal government providing that: (1) The Pride Flag will be rehung at Stonewall National Monument's official flagpole within seven days of the settlement. (2) The Pride Flag will fly permanently at Stonewall alongside the U.S. flag and the National Park Service flag. (3) The Pride Flag will not be removed except for practical reasons such as maintenance. (4) The court retains jurisdiction to enforce the stipulation. (5) The settlement confirms that the Pride Flag complies with both the law and NPS policy, including the historical-context exemption.<br><br>"
        "<b>SIGNIFICANCE.</b> This is a PROTECTIVE entry of structural importance. Court-retained jurisdiction to enforce a stipulated permanent-installation provision at a designated national monument is a relatively rare protective mechanism that survives administration change. The stipulation binds the executive branch from future administrative removal of the Pride Flag from Stonewall NM, regardless of which administration holds office. If the stipulation holds, it establishes a model for other community-defining symbols at other federal monument sites that have been or could be threatened with administrative removal.<br><br>"
        "<b>SCOPE AND LIMITS.</b> The protection runs to the Pride Flag at Stonewall NM specifically. It does not, by its own terms, protect other LGBTQ federal recognition (designation of additional sites, programmatic LGBTQ funding, federal-employment nondiscrimination, the restored Stonewall webpage content, etc.). The stipulation is a defensive perimeter around the most visible federal LGBTQ symbol. The broader Trump II rollback under EO 14168 continues.<br><br>"
        "Cross-reference agency-2026-stonewall-pride-flag-removed (underlying removal). Cross-reference eo-14168 (Defending Women from Gender Ideology Extremism framework).<br><br>"
        "<b>SOURCES.</b><br>"
        "Lambda Legal victory announcement: <a href=\"https://lambdalegal.org/newsroom/us_20260413_victory-trump-administration-agrees-to-restore-pride-flag-at-stonewall/\">https://lambdalegal.org/newsroom/us_20260413_victory-trump-administration-agrees-to-restore-pride-flag-at-stonewall/</a><br>"
        "CNN on settlement: <a href=\"https://www.cnn.com/2026/04/13/politics/pride-flag-stonewall-monument\">https://www.cnn.com/2026/04/13/politics/pride-flag-stonewall-monument</a><br>"
        "Courthouse News: <a href=\"https://www.courthousenews.com/trump-administration-settles-suit-returns-pride-flag-to-nyc-stonewall-monument/\">https://www.courthousenews.com/trump-administration-settles-suit-returns-pride-flag-to-nyc-stonewall-monument/</a><br>"
        "Metro Weekly: <a href=\"https://www.metroweekly.com/2026/04/stonewall-pride-flag-lawsuit-settlement\">https://www.metroweekly.com/2026/04/stonewall-pride-flag-lawsuit-settlement</a><br>"
        "CBS New York: <a href=\"https://www.cbsnews.com/newyork/news/stonewall-national-monument-pride-flag-restored/\">https://www.cbsnews.com/newyork/news/stonewall-national-monument-pride-flag-restored/</a><br>"
        "Washington Blade: <a href=\"https://www.washingtonblade.com/2026/04/13/court-orders-pride-flag-to-return-to-stonewall/\">https://www.washingtonblade.com/2026/04/13/court-orders-pride-flag-to-return-to-stonewall/</a><br>"
        "Advocate: <a href=\"https://www.advocate.com/politics/national/stonewall-monument-pride-flag-restored\">https://www.advocate.com/politics/national/stonewall-monument-pride-flag-restored</a>"
    ),
    "I": {
        "africanDescendant": {
            "people": "PROTECTIVE. Federal commemoration of Black trans leadership in the Stonewall Uprising (Marsha P. Johnson, Stormé DeLarverie) is restored at the federal monument site. Black LGBTQ youth regain visible federal recognition.",
            "places": "PROTECTIVE. Stonewall National Monument as a site of Black trans-leadership commemoration is restored to its designating commemorative configuration.",
            "practices": "PROTECTIVE. Federal commemorative practice recognizing Black trans leadership is restored.",
            "treasures": "PROTECTIVE. The Pride Flag at Stonewall, as a treasure commemorating Black trans leadership, is restored and court-protected against future administrative removal."
        },
        "latine": {
            "people": "PROTECTIVE. Federal commemoration of Latine trans leadership in the Stonewall Uprising (Sylvia Rivera) is restored at the federal monument site. Latine LGBTQ youth regain visible federal recognition.",
            "places": "PROTECTIVE. Stonewall NM as a site of Latine trans-leadership commemoration is restored.",
            "practices": "PROTECTIVE. Federal commemorative practice recognizing Latine trans leadership is restored.",
            "treasures": "PROTECTIVE. The Pride Flag at Stonewall, as a treasure commemorating Latine trans leadership, is restored and court-protected."
        },
        "indigenous": {
            "people": "PROTECTIVE. Indigenous Two-Spirit community recognition through the Pride Flag at Stonewall is restored.",
            "places": "PROTECTIVE. Christopher Park on Lenape land regains its commemorative configuration.",
            "practices": "PROTECTIVE. Federal LGBTQ commemorative practice is restored.",
            "treasures": "PROTECTIVE. The Pride Flag at Stonewall is restored as a federal commemorative treasure."
        },
        "asianAmerican": {
            "people": "PROTECTIVE. Asian American LGBTQ community recognition through the Pride Flag at Stonewall is restored.",
            "places": "PROTECTIVE. Stonewall NM regains its cross-community commemorative configuration.",
            "practices": "PROTECTIVE. Federal LGBTQ commemorative practice is restored.",
            "treasures": "PROTECTIVE. The Pride Flag at Stonewall is restored as a cross-community commemorative treasure."
        },
        "pacificIslander": {
            "people": "PROTECTIVE. Pacific Islander LGBTQ community recognition (including the Mahu tradition) through the Pride Flag at Stonewall is restored.",
            "places": "PROTECTIVE. Stonewall NM regains its cross-community commemorative configuration.",
            "practices": "PROTECTIVE. Federal LGBTQ commemorative practice is restored.",
            "treasures": "PROTECTIVE. The Pride Flag at Stonewall is restored as a cross-community commemorative treasure."
        },
        "allCommunities": {
            "people": "PROTECTIVE. Restoration of the Pride Flag at the principal federal LGBTQ monument, with court-retained jurisdiction enforcing permanent installation binding future administrations against removal. Establishes a model for stipulated permanent-installation language protecting community-defining symbols at federal monument sites against administrative removal.",
            "places": "PROTECTIVE. Stonewall National Monument restored to its designating commemorative configuration, with the Pride Flag protected against future administrative removal by stipulated court-enforced settlement.",
            "practices": "PROTECTIVE. Federal monument-display practice is reaffirmed as bound by community-specific commemorative purposes.",
            "treasures": "PROTECTIVE. Lambda Legal and Washington Litigation Group have established a settlement structure that other communities can model for protecting community-defining symbols at other federal monument sites."
        }
    },
    "c": ["lgbtq", "All Communities", "African-descendant", "Latiné", "Indigenous", "Asian", "Pacific Islander"],
    "U": "https://lambdalegal.org/newsroom/us_20260413_victory-trump-administration-agrees-to-restore-pride-flag-at-stonewall/",
    "_source": "manual",
}


# ============================================================================
# ENTRY H: SECRETARIAL ORDER 3447 NPS HUNTING REPEAL
# ============================================================================
ENTRY_H = {
    "i": "so-3447-nps-hunting-restrictions-repeal",
    "t": "Agency Action",
    "n": "Interior Secretarial Order 3447 (Signed January 2026 by Doug Burgum) Directing the National Park Service to Loosen Hunting and Trapping Restrictions at Approximately 55 NPS Sites (15 With Immediate Loosening and Approximately 40 Under Near-Term Review), with the 63 Congressionally Designated National Parks Largely Protected by Separate Federal Laws",
    "T": "<span style=\"color: #991B1B;\">SO 3447:</span> Interior Secretary Burgum Orders NPS to Loosen Hunting and Trapping Restrictions Across Approximately 55 NPS Sites, with 15 Sites Immediately Affected and Approximately 40 Under Near-Term Review",
    "s": "Secretarial Order 3447 loosens NPS hunting restrictions at ~55 sites.",
    "d": "2026-01-15",
    "a": "Trump II",
    "A": ["DOI", "NPS", "FWS", "BLM"],
    "S": "Active. Secretarial Order signed January 2026 by Interior Secretary Doug Burgum. Implementation underway. Reporting (Outside magazine, Washington Post, PBS, US News, Sierra Club) indicates approximately 55 NPS sites are affected: 15 with immediate loosening of hunting restrictions, approximately 40 under near-term review. The 63 congressionally designated National Parks (capital N) are largely not in the affected set because most are protected from hunting by separate federal statutes (Yellowstone under the 1872 organic act, Yosemite and others under their establishing acts). Sierra Club and other conservation organizations have announced opposition; litigation is anticipated. Exact SO 3447 issuance date and full list of affected sites to be confirmed from the Federal Register and the Outside investigation.",
    "L": "SEVERE",
    "D": (
        "<b>ACTION.</b> Interior Secretary Doug Burgum signed Secretarial Order 3447 in January 2026 directing the National Park Service to review existing hunting restrictions at NPS units and to provide recommendations for expanding opportunities. Reporting indicates that 15 NPS sites had hunting restrictions immediately loosened under the order, with approximately 40 additional sites under near-term review for similar loosening. The total affected universe is approximately 55 NPS units. The 63 congressionally designated National Parks (capital N) are largely not in the affected set, because most are protected from hunting by separate federal statutes (Yellowstone under the 1872 organic act, Yosemite and others under their establishing acts).<br><br>"
        "<b>LEGAL MECHANISM.</b> Secretarial Order, a form of internal Interior Department directive. NPS hunting regulations are codified at 36 C.F.R. sec. 2.2 (governing wildlife) and unit-specific regulations under 36 C.F.R. Part 7. Changes to those regulations ordinarily require notice-and-comment rulemaking under the Administrative Procedure Act. The use of a Secretarial Order to direct rapid changes raises APA process questions, in addition to NEPA review questions (42 U.S.C. sec. 4332) for actions significantly affecting the human environment and NHPA Section 106 questions for actions affecting traditional cultural properties.<br><br>"
        "<b>CULTURAL HERITAGE AND COMMUNITY ANALYSIS.</b> The cultural-resource and community impacts of expanded hunting at NPS units cut across multiple dimensions.<br><br>"
        "<i>Visitor safety.</i> Welcome centers, visitor centers, and interpretive sites are concentrated visitor zones with children, elderly visitors, ADA-needs visitors, and group-tour participants. Buffer zones around visitor infrastructure are standard safety practice. Loosening those buffers creates visitor-safety risk and may chill visitation by historically excluded groups (Black, Latine, AAPI, LGBTQ families whose NPS visitation rates have been increasing in recent years from a historically low baseline).<br><br>"
        "<i>Tribal treaty rights.</i> Several federally recognized tribes hold treaty hunting rights on ceded territories that include or border NPS lands. The Crow, Eastern Shoshone, and Bannock have treaty interests in the Greater Yellowstone area. The Blackfeet have treaty interests in the Glacier National Park area. Pacific Northwest tribes (Yakama, Nez Perce, Confederated Tribes of the Colville Reservation, and others under the Stevens treaties) have treaty interests at Olympic, Mount Rainier, and North Cascades. The Anishinaabe (Bad River, Red Cliff, Lac Courte Oreilles, and other Ojibwe bands) have treaty interests at Apostle Islands National Lakeshore. Loosening of NPS hunting restrictions interacts in complex ways with these treaty rights.<br><br>"
        "<i>Indigenous food sovereignty.</i> For Indigenous communities with established subsistence-hunting relationships to NPS lands (Alaska Native communities under ANILCA, and tribes with treaty hunting on ceded territories), expanded sport hunting by non-Indigenous hunters affects population health of culturally significant species, including caribou, elk, deer, bison, and waterfowl.<br><br>"
        "<i>Culturally significant wildlife.</i> Several NPS units contain wildlife of specific cultural significance to particular communities (bison at multiple western NPS units for Lakota, Cheyenne, Arapaho, and other Plains tribes; salmon at Pacific Northwest units for Coast Salish, Chinookan, and other tribes; alligators and Florida panthers at Big Cypress for Seminole and Miccosukee). Increased hunting pressure on culturally significant species affects those communities' cultural-resource relationships.<br><br>"
        "<i>Historically excluded visitors.</i> NPS visitation by Black, Latine, AAPI, LGBTQ, and disabled visitors has been increasing from a historically low baseline. Visible firearms and active hunting near welcome centers may chill that visitation pattern, reversing a slow trend toward more inclusive NPS visitorship.<br><br>"
        "<b>AFFECTED NPS UNITS.</b> Per the Outside magazine investigation, 55 NPS sites are affected. The full list will be added to this entry when verified from the Outside investigation and the Federal Register. Likely categories include National Preserves where hunting is already authorized (Big Cypress, Mojave, Big Thicket, Bering Land Bridge, Denali Preserve portion, Lake Clark Preserve portion, Wrangell-St. Elias Preserve portion, Gates of the Arctic Preserve portion, Yukon-Charley Rivers Preserve, Noatak Preserve), National Recreation Areas (Glen Canyon, Lake Mead, Whiskeytown, Curecanti, Bighorn Canyon), National Seashores (Cape Hatteras, Cape Lookout, Padre Island, Gulf Islands, Assateague Island, Fire Island), and other NPS unit types where hunting is conditionally permitted under unit-specific authorizing legislation.<br><br>"
        "<b>CONGRESSIONALLY DESIGNATED NATIONAL PARKS NOT IN AFFECTED SET.</b> The 63 capital-N National Parks are largely protected from hunting by separate federal statutes. Yellowstone (WY/MT/ID) and Yosemite (CA) are the most commonly cited as protected by separate federal laws. Several Alaska National Parks (Denali, Gates of the Arctic, Lake Clark, Wrangell-St. Elias, Kobuk Valley, Glacier Bay, Katmai, Kenai Fjords) have unit-specific subsistence-hunting authorizations under ANILCA. Grand Teton has unit-specific elk-reduction authorization since 1950.<br><br>"
        "<b>CONTEXT.</b> SO 3447 is part of a broader Trump II program of accelerated resource extraction and use on federal public lands, including the Ambler Mine equity stake (cross-reference ea-2025-trilogy-metals-ambler-equity), expanded oil and gas leasing, and reductions in NEPA review under EO 14154 (Unleashing American Energy).<br><br>"
        "<b>SOURCES.</b><br>"
        "Outside magazine investigation (55 sites): <a href=\"https://www.outsideonline.com/outdoor-adventure/environment/trump-national-park-hunting-restrictions-rollback/\">https://www.outsideonline.com/outdoor-adventure/environment/trump-national-park-hunting-restrictions-rollback/</a><br>"
        "Washington Post: <a href=\"https://www.washingtonpost.com/politics/2026/05/08/trump-burgum-hunting-trapping-rollback-restrictions/cc91dc9c-4b08-11f1-a119-857cd2bf4fd4_story.html\">https://www.washingtonpost.com/politics/2026/05/08/trump-burgum-hunting-trapping-rollback-restrictions/cc91dc9c-4b08-11f1-a119-857cd2bf4fd4_story.html</a><br>"
        "PBS News: <a href=\"https://www.pbs.org/newshour/politics/trump-is-lifting-restrictions-on-hunting-in-national-parks-and-other-areas\">https://www.pbs.org/newshour/politics/trump-is-lifting-restrictions-on-hunting-in-national-parks-and-other-areas</a><br>"
        "US News: <a href=\"https://www.usnews.com/news/us/articles/2026-05-08/trump-is-quietly-lifting-restrictions-on-hunting-in-national-parks-refuges-and-wilderness-areas\">https://www.usnews.com/news/us/articles/2026-05-08/trump-is-quietly-lifting-restrictions-on-hunting-in-national-parks-refuges-and-wilderness-areas</a><br>"
        "Snopes scope clarification: <a href=\"https://www.snopes.com/news/2026/05/14/trump-hunting-in-national-parks/\">https://www.snopes.com/news/2026/05/14/trump-hunting-in-national-parks/</a><br>"
        "Sierra Club press release: <a href=\"https://www.sierraclub.org/press-releases/2026/05/trump-administration-moves-strip-conservation-america-s-public-lands\">https://www.sierraclub.org/press-releases/2026/05/trump-administration-moves-strip-conservation-america-s-public-lands</a><br>"
        "Society of Environmental Journalists summary: <a href=\"https://www.sej.org/headlines/trump-admin-orders-rapid-end-some-hunting-rules-federal-lands\">https://www.sej.org/headlines/trump-admin-orders-rapid-end-some-hunting-rules-federal-lands</a>"
    ),
    "I": {
        "africanDescendant": {
            "people": "Black NPS visitation has been increasing from a historically low baseline. Visible firearms and active hunting near welcome centers may chill that visitation pattern, reversing a slow trend toward more inclusive NPS visitorship. Specific affected NPS units include Cape Hatteras National Seashore (significant Black-history coastal landscape including Gullah Geechee Cultural Heritage Corridor extension and the historic Pea Island Lifesavers, the all-Black USLSS crew based at Pea Island Station).",
            "places": "Gullah Geechee Cultural Heritage Corridor extends along NPS units in the Outer Banks and Atlantic coast. Cape Hatteras, Cape Lookout, Cumberland Island, and Gulf Islands National Seashores all sit within or adjacent to the Corridor's cultural landscape. Loosened hunting restrictions affect those landscapes.",
            "practices": "Black NPS visitation practice, growing slowly from a historically low baseline, is chilled by visible firearms and active hunting at visitor-center proximity.",
            "treasures": "Wildlife at NPS units significant to African American history (Pea Island, the Gullah Geechee landscape, the Outer Banks) face increased hunting pressure."
        },
        "latine": {
            "people": "Latine NPS visitation has been increasing from a historically low baseline. Visible firearms and active hunting near welcome centers may chill that visitation pattern. Specific affected NPS units include Padre Island National Seashore (significant Tejano coastal landscape).",
            "places": "Tejano coastal landscape at Padre Island and other Gulf Coast NPS units affected by loosened hunting.",
            "practices": "Latine NPS visitation practice is chilled.",
            "treasures": "Wildlife at NPS units significant to Latine history face increased hunting pressure."
        },
        "indigenous": {
            "people": "Loosening of NPS hunting restrictions interacts in complex ways with tribal treaty rights, ANILCA subsistence arrangements, and culturally significant wildlife populations. Expanded sport hunting by non-Indigenous hunters affects population health of caribou, bison, elk, deer, salmon, and other species of specific cultural significance to multiple tribes. APA, NEPA, and Section 106 process questions raise consultation concerns. Specific affected units include Big Cypress National Preserve (Seminole and Miccosukee), Apostle Islands National Lakeshore (Anishinaabe treaty rights), Bering Land Bridge National Preserve (Iñupiaq subsistence), and many others.",
            "places": "Treaty-ceded territories overlapping NPS lands across the country (Crow at Greater Yellowstone, Blackfeet at Glacier, Stevens-treaty tribes in Pacific Northwest, Anishinaabe at Apostle Islands) are affected by hunting-restriction changes that may interact with treaty-rights regimes.",
            "practices": "Tribal subsistence-hunting practice under ANILCA in Alaska and treaty hunting practice on ceded territories elsewhere are affected by changes to non-Indigenous hunting regulations on the same lands.",
            "treasures": "Bison (Lakota, Cheyenne, Arapaho, and other Plains tribes), salmon (Coast Salish, Chinookan, and other Pacific Northwest tribes), caribou (Iñupiaq, Koyukon, Gwich'in), and other culturally significant wildlife face increased hunting pressure."
        },
        "asianAmerican": {
            "people": "Asian American NPS visitation has been increasing from a historically low baseline. Visible firearms and active hunting near welcome centers may chill that visitation pattern. Specific affected units include some NPS units near Asian American historical sites.",
            "places": "Asian American visitorship to NPS units is affected by safety changes.",
            "practices": "Asian American NPS visitation practice is chilled.",
            "treasures": "Wildlife at NPS units significant to Asian American history face increased hunting pressure."
        },
        "pacificIslander": {
            "people": "Native Hawaiian cultural relationships to land and species are particularly significant at Hawaiʻi Volcanoes National Park and Haleakalā National Park, both protected from hunting by separate federal laws. Pacific Islander NPS visitorship is affected by changes at other NPS units.",
            "places": "Pacific Islander cultural landscapes at NPS units are affected.",
            "practices": "Pacific Islander NPS visitation practice and Native Hawaiian cultural-resource relationships are affected.",
            "treasures": "Wildlife at NPS units significant to Pacific Islander cultural traditions face increased hunting pressure."
        },
        "allCommunities": {
            "people": "Visitor-safety risk at welcome centers and visitor infrastructure. Loosening of buffer zones around concentrated visitor zones creates safety risk and may chill visitation by historically excluded groups. Public-access recreation on NPS lands disproportionately serves working-class visitors who lack private alternatives.",
            "places": "Approximately 55 NPS sites are affected by Secretarial Order 3447. The 63 congressionally designated National Parks are largely protected by separate federal laws, but the affected universe includes major National Preserves, National Recreation Areas, and National Seashores.",
            "practices": "Federal land-management practice on NPS lands shifts from a recreation-and-preservation framework toward an extraction-and-use framework. The Secretarial Order mechanism is being used to bypass standard APA notice-and-comment rulemaking.",
            "treasures": "Wildlife at affected NPS units face increased hunting pressure. The administrative-rulemaking process that protects federal lands is weakened by the use of Secretarial Orders to direct rapid regulatory changes."
        }
    },
    "c": ["Indigenous", "All Communities", "African-descendant", "Latiné", "Asian", "Pacific Islander", "working-class", "Veterans", "women", "lgbtq"],
    "U": "https://www.outsideonline.com/outdoor-adventure/environment/trump-national-park-hunting-restrictions-rollback/",
    "_source": "manual",
}


# ============================================================================
# ENTRY I: TRILOGY METALS FEDERAL EQUITY + AMBLER ACCESS PROJECT
# ============================================================================
ENTRY_I = {
    "i": "ea-2025-trilogy-metals-ambler-equity",
    "t": "Executive Action",
    "n": "Trump II Reversal of Biden-Era Ambler Access Project Right-of-Way Denial (October 2025), Approval of 211-Mile Industrial Mining Road Through Brooks Range Foothills Across Iñupiat and Koyukon Athabascan Homelands, with Simultaneous Federal $35.6 Million 10 Percent Equity Stake in Trilogy Metals Plus Warrants for Additional 7.5 Percent (Federal Government as Both Regulator and Equity Owner)",
    "T": "<span style=\"color: #991B1B;\">Ambler Greenlight Plus Federal Equity:</span> Trump II Administration Reverses Biden Right-of-Way Denial for 211-Mile Ambler Access Project Mining Road Across Indigenous Alaska, and Takes $35.6 Million 10 Percent Equity Stake in Trilogy Metals Plus Warrants for Additional 7.5 Percent (Federal Government as Both Regulator and Equity Owner)",
    "s": "Federal equity in Trilogy Metals + approval of Ambler Access Project road.",
    "d": "2025-10-07",
    "a": "Trump II",
    "A": ["DOI", "BLM", "ACOE", "Treasury", "DOE", "WH"],
    "S": "Active. Ambler Access Project approval announced October 2025. Trilogy Metals equity stake closed October 2025: $35.6 million for 10 percent equity plus warrants for an additional 7.5 percent. Federal equity position in the road itself under active consideration as of March 2026. Reverses Biden administration's June 2024 ROW denial that was substantially based on ANILCA Section 810 subsistence analysis. Litigation expected from Tanana Chiefs Conference (representing 42 Interior Alaska tribes), Northwest Arctic Borough, Native Village of Allakaket, Native Village of Alatna, Trustees for Alaska, and conservation coalition. Current litigation status to be confirmed.",
    "L": "SEVERE",
    "D": (
        "<b>ACTION.</b> In October 2025 the Trump II administration took two coordinated actions affecting the Ambler mining district and the Ambler Access Project in Alaska. First, the administration reversed the Biden-era right-of-way denial for the Ambler Access Project, a 211-mile industrial road that would cut through the southern foothills of the Brooks Range to provide ground access to the Ambler mining district. Second, the administration announced a federal investment of $35.6 million in Trilogy Metals (the principal mining company benefiting from the road) for a 10 percent equity stake, with warrants for an additional 7.5 percent stake. As of March 2026, the administration is also considering taking a direct equity position in the road project itself, which would make the federal government both a regulator of the project and an equity owner in its commercial benefit. Interior Secretary Doug Burgum stated that approval would unlock copper, cobalt, and other critical minerals that the United States needs to win the AI arms race against China.<br><br>"
        "<b>LEGAL MECHANISM.</b> Right-of-way reversal under the Federal Land Policy and Management Act (FLPMA) and the Alaska National Interest Lands Conservation Act (ANILCA). Federal equity investment in Trilogy Metals appears to use Defense Production Act Title III authority or similar critical-minerals authorities. The specific federal investment authority used to be confirmed. The structural posture of the federal government as both regulator and equity owner in the same project is novel and raises significant conflict-of-interest, fiduciary-duty, and procurement-integrity questions that the existing federal land-management framework was not designed to address.<br><br>"
        "<b>CULTURAL HERITAGE AND INDIGENOUS RIGHTS ANALYSIS.</b> The Ambler Access Project would cross approximately 30 miles of Gates of the Arctic National Preserve and would cut through the ancestral and contemporary homelands of multiple Iñupiat and Koyukon Athabascan communities, including the Native Villages of Allakaket, Alatna, Anaktuvuk Pass, Hughes, Huslia, Kobuk, Shungnak, Ambler, and Kiana, among others. The Tanana Chiefs Conference (representing 42 Interior Alaska tribes) and the Northwest Arctic Borough have been the principal Indigenous opponents of the project, joined by Trustees for Alaska and a coalition of conservation organizations.<br><br>"
        "The harms are multidimensional and severe.<br><br>"
        "<i>Western Arctic Caribou Herd.</i> The road would cross the migration route of the Western Arctic Caribou Herd, one of the largest caribou herds in North America. The herd has declined from approximately 490,000 animals in 2003 to approximately 152,000 in 2023, a roughly 70 percent decline. The herd is the principal subsistence resource for Iñupiat and Koyukon communities across the region. Industrial road traffic, dust deposition, and habitat fragmentation are known to alter caribou migration.<br><br>"
        "<i>Teshekpuk Caribou Herd.</i> The neighboring Teshekpuk Caribou Herd faces similar pressures from oil-and-gas development on the North Slope. Cumulative pressure on Alaska's caribou populations is severe.<br><br>"
        "<i>Salmon and freshwater fisheries.</i> The road would cross more than 2,800 streams and rivers, including tributaries of the Kobuk and Koyukuk Rivers, both of which support salmon runs of subsistence and cultural significance.<br><br>"
        "<i>Subsistence law.</i> Under ANILCA Section 810, federal actions affecting subsistence resources in Alaska require evaluation of subsistence impacts and consultation with affected communities. The Biden-era ROW denial was substantially based on Section 810 analysis. The Trump II reversal effectively overrides that subsistence-impact analysis.<br><br>"
        "<i>Free, prior, and informed consent.</i> Multiple affected Iñupiat and Koyukon Athabascan tribes have publicly opposed the project. The U.N. Declaration on the Rights of Indigenous Peoples (UNDRIP), which the United States endorsed in 2010, recognizes Indigenous peoples' right to free, prior, and informed consent for projects affecting their lands. The Ambler reversal proceeds over the opposition of multiple affected tribes.<br><br>"
        "<i>Federal conflict of interest.</i> The simultaneous role of the federal government as ROW regulator, federal-lands trustee, and equity owner in the project's commercial beneficiary creates a structural conflict of interest. Federal officials reviewing future permitting, environmental compliance, or enforcement decisions affecting Trilogy Metals are simultaneously deciding matters affecting the value of the government's equity position. The federal trust responsibility to Alaska Native tribes is in direct structural tension with the federal equity interest in the mining company.<br><br>"
        "<b>CONTEXT.</b> This action is part of a broader Trump II program described in Reuters reporting as the administration's pivot to buying stakes in critical sectors (also including federal equity in Intel under DPA Title III, and other critical-minerals and AI-infrastructure plays). The framing as winning the AI arms race against China connects the Ambler project to a broader executive program of accelerated resource extraction justified by national-security and AI-infrastructure rationales. The action also reverses a key Biden-era environmental and Indigenous-rights decision (the June 2024 ROW denial), establishing a precedent that ROW denials grounded in Section 810 subsistence analysis and consultation can be reversed by subsequent administrations without substantively addressing the underlying subsistence and cultural concerns. Cross-reference so-3447-nps-hunting-restrictions-repeal for the parallel rollback of NPS hunting restrictions affecting cumulative wildlife-population pressures across federal lands.<br><br>"
        "<b>SOURCES.</b><br>"
        "Fortune on the October 2025 stake announcement: <a href=\"https://fortune.com/2025/10/07/trump-alaska-megamine-ambler-road-mine-trilogy-metals-stake/\">https://fortune.com/2025/10/07/trump-alaska-megamine-ambler-road-mine-trilogy-metals-stake/</a><br>"
        "Alaska Beacon on March 2026 road-equity consideration: <a href=\"https://alaskabeacon.com/2026/03/13/trump-administration-mulling-investment-in-controversial-alaska-mining-road/\">https://alaskabeacon.com/2026/03/13/trump-administration-mulling-investment-in-controversial-alaska-mining-road/</a><br>"
        "Alaska Public Media on regulator-investor structural problem: <a href=\"https://alaskapublic.org/programs/alaska-economic-report/2025-12-11/to-ambler-mining-company-u-s-government-is-both-investor-and-regulator\">https://alaskapublic.org/programs/alaska-economic-report/2025-12-11/to-ambler-mining-company-u-s-government-is-both-investor-and-regulator</a><br>"
        "Yahoo Finance on the stock impact and 10 percent stake: <a href=\"https://finance.yahoo.com/news/trilogy-metals-stock-explodes-on-news-of-10-stake-by-trump-admin-and-eo-ordering-permits-for-alaska-road-141434093.html\">https://finance.yahoo.com/news/trilogy-metals-stock-explodes-on-news-of-10-stake-by-trump-admin-and-eo-ordering-permits-for-alaska-road-141434093.html</a><br>"
        "Alaska Public Media on Democratic congressional criticism: <a href=\"https://alaskapublic.org/news/politics/washington-d-c/2026-03-26/u-s-house-democrat-derides-trump-admins-investment-in-alaska-mine-project\">https://alaskapublic.org/news/politics/washington-d-c/2026-03-26/u-s-house-democrat-derides-trump-admins-investment-in-alaska-mine-project</a><br>"
        "Fox Business on Biden reversal: <a href=\"https://www.foxbusiness.com/politics/trump-reverses-biden-block-alaska-project-us-takes-10-stake-unlock-critical-minerals\">https://www.foxbusiness.com/politics/trump-reverses-biden-block-alaska-project-us-takes-10-stake-unlock-critical-minerals</a><br>"
        "Ainvest on EO ordering permits: <a href=\"https://www.ainvest.com/news/trump-approves-road-project-alaska-stake-trilogy-metals-2510-71/\">https://www.ainvest.com/news/trump-approves-road-project-alaska-stake-trilogy-metals-2510-71/</a>"
    ),
    "I": {
        "indigenous": {
            "people": "Project advances over opposition of multiple affected Iñupiat and Koyukon Athabascan tribes (Tanana Chiefs Conference representing 42 Interior Alaska tribes; Northwest Arctic Borough; Native Villages of Allakaket, Alatna, Anaktuvuk Pass, and others). ANILCA Section 810 subsistence analysis is effectively overridden. Federal trust responsibility to Alaska Native tribes is in direct structural tension with the federal equity interest in Trilogy Metals. UNDRIP free, prior, and informed consent standard is violated.",
            "places": "211-mile industrial road would cross approximately 30 miles of Gates of the Arctic National Preserve and cut through the ancestral and contemporary homelands of multiple Iñupiat and Koyukon Athabascan communities. The road would cross more than 2,800 streams and rivers in the Kobuk and Koyukuk watersheds.",
            "practices": "Subsistence-knowledge transmission depends on continued availability of caribou, salmon, and other subsistence resources. Habitat fragmentation and population decline disrupt that transmission. Caribou hunting, salmon fishing, and other subsistence practices on which Iñupiat and Koyukon Athabascan food security and cultural practice depend are directly threatened.",
            "treasures": "Western Arctic Caribou Herd has declined approximately 70 percent since 2003 (from approximately 490,000 to approximately 152,000). The herd is a cultural treasure of Iñupiat and Koyukon Athabascan communities. Salmon runs in the Kobuk and Koyukuk watersheds are similarly treasured."
        },
        "africanDescendant": {
            "people": "African American Alaska Native communities and the broader African American population of Alaska are affected by the precedent of federal equity in extractive industries on Indigenous lands.",
            "places": "The federal-equity precedent affects future federal-land decisions in regions where African American and African-descendant communities have cultural-resource interests.",
            "practices": "Federal trust responsibility practice is undermined by the regulator-investor conflict, with downstream effects on federal trust responsibility to all groups that depend on it.",
            "treasures": "The federal trust responsibility itself, as a legal-cultural treasure, is structurally weakened."
        },
        "latine": {
            "people": "Latine communities are affected by the precedent of federal equity in extractive industries that compromises federal land-management impartiality.",
            "places": "The precedent affects future federal land decisions in regions where Latine communities have cultural-resource interests.",
            "practices": "Federal land-management practice loses impartiality.",
            "treasures": "The federal regulatory framework as a public treasure is weakened."
        },
        "asianAmerican": {
            "people": "Asian American communities are affected by the precedent of federal equity in extractive industries.",
            "places": "The precedent affects future federal land decisions.",
            "practices": "Federal land-management practice loses impartiality.",
            "treasures": "The federal regulatory framework as a public treasure is weakened."
        },
        "pacificIslander": {
            "people": "Pacific Islander and Native Hawaiian communities are affected by the precedent of federal equity in extractive industries, particularly relevant given Indo-Pacific critical-minerals geopolitics. The precedent affects future federal-land decisions in Hawaii, the COFA states (Marshall Islands, Federated States of Micronesia, Palau), and other Pacific Islander cultural-resource landscapes.",
            "places": "The precedent affects future federal land decisions in Pacific Islander cultural-resource landscapes.",
            "practices": "Federal land-management practice loses impartiality.",
            "treasures": "The federal regulatory framework as a public treasure is weakened."
        },
        "allCommunities": {
            "people": "Federal equity ownership in a privately held mining company that the same federal government regulates and whose access to federal land the same federal government controls is a structurally novel conflict of interest. The precedent affects every federal-lands resource decision going forward. Alaska Native and rural Alaska residents are disproportionately working-class and disproportionately dependent on subsistence resources. The cumulative impact of Ambler on subsistence wildlife affects them most directly.",
            "places": "Gates of the Arctic National Preserve, the Brooks Range foothills, and the Kobuk and Koyukuk River watersheds face industrial-road and downstream mining impacts.",
            "practices": "Federal land-management practice is restructured by the regulator-investor combination.",
            "treasures": "The federal trust responsibility, ANILCA Section 810, and the federal regulatory framework protecting federal public lands are all weakened by the precedent."
        }
    },
    "c": ["Indigenous", "All Communities", "African-descendant", "Latiné", "Asian", "Pacific Islander", "working-class"],
    "U": "https://fortune.com/2025/10/07/trump-alaska-megamine-ambler-road-mine-trilogy-metals-stake/",
    "_source": "manual",
}


# ============================================================================
# INSERT
# ============================================================================
def main():
    if not DATA_PATH.exists():
        raise SystemExit(f"data.json not found at {DATA_PATH}")

    em_dash = "—"
    new_entries = [
        ("executive_actions", ENTRY_A),
        ("litigation", ENTRY_B),
        ("legislation", ENTRY_C),
        ("executive_actions", ENTRY_D),
        ("executive_actions", ENTRY_E),
        ("agency_actions", ENTRY_F),
        ("litigation", ENTRY_G),
        ("agency_actions", ENTRY_H),
        ("executive_actions", ENTRY_I),
    ]

    # Pre-flight: em-dash check (Prince's writing-style rules + script's existing convention)
    for cat, e in new_entries:
        eid = e.get("id") or e.get("i")
        if em_dash in json.dumps(e, ensure_ascii=False):
            raise SystemExit(f"ABORT: em-dash detected in {eid}.")

    shutil.copy2(DATA_PATH, BACKUP_PATH)
    print(f"Backup written: {BACKUP_PATH.name}")

    with DATA_PATH.open() as f:
        data = json.load(f)

    # Pre-flight: dedupe check
    for cat, entry in new_entries:
        eid = entry.get("id") or entry.get("i")
        existing = data.get(cat, [])
        if any((e.get("id") or e.get("i")) == eid for e in existing):
            raise SystemExit(f"Entry {eid} already exists in {cat}. Aborting.")

    # Insert
    for cat, entry in new_entries:
        data.setdefault(cat, []).append(entry)
        eid = entry.get("id") or entry.get("i")
        print(f"Inserted {eid} into {cat}.")

    # Update meta.lastUpdated if present
    if "meta" in data and isinstance(data["meta"], dict):
        data["meta"]["lastUpdated"] = datetime.now().strftime("%Y-%m-%d")

    # Atomic write
    tmp = DATA_PATH.with_suffix(".json.tmp")
    with tmp.open("w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    tmp.replace(DATA_PATH)

    # Summary
    print()
    print("Done. Counts after insert:")
    for cat in ("executive_actions", "litigation", "legislation", "agency_actions"):
        print(f"  {cat}: {len(data.get(cat, []))}")


if __name__ == "__main__":
    main()
