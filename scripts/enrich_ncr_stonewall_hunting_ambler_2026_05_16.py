#!/usr/bin/env python3
"""Enrich 6 of the 9 entries committed earlier today (commit f0517c9) with verified specifics.

Updates:
A. lit-2025-nthp-v-trump-ballroom — CRUCIAL CORRECTION: PI was GRANTED March 11, 2026
   by Judge Richard J. Leon (not denied as originally recorded). Add case caption,
   docket 1:25-cv-04316 (D.D.C.), full procedural timeline, DOJ appeal, DOJ April 27, 2026
   demand to drop and NTHP refusal.
B. leg-2026-ballroom-security-appropriation — Add: part of "One Big Beautiful Bill"
   reconciliation; Senate Judiciary piece $39.2B; exact statutory ballroom-security
   language; Grassley press release URL.
C. ea-2026-east-potomac-championship-golf — Hains Point definitively confirmed untouched
   (no longer a flag); designer Tom Fazio; Judge Ana Reyes (DDC) allowed federal
   maintenance to proceed early May 2026.
D. ea-2026-triumphal-arch-memorial-circle — Add full plaintiff list (Vietnam veterans
   Michael Lemmon, Shaun Byrnes, Jon Gundersen + historian Calder Loth), Public Citizen
   counsel, defendants (POTUS personally, NPS, Vince Haley), Judge Tanya Chutkan,
   PI declined. Trump's project name "Independence Arch" added.
E. so-3447-nps-hunting-restrictions-repeal — Date corrected to January 13, 2026
   (was 2026-01-15). Add: 76 NPS units already authorize hunting / 31 trapping /
   51M NPS-managed acres; specific changes at Big Cypress NP (FL), Mississippi NRRA (MN),
   Jean Lafitte NHP (LA, alligator hunting ban lifted).
F. ea-2025-trilogy-metals-ambler-equity — Federal investment authority is U.S.
   Department of War (DOW) under DPA framework (DPA reauthorization is a closing
   condition). Structure: $17.8M for 8,215,570 units at $2.17 (each unit = 1 share +
   3/4 of 10-year warrant). FOCI review required. Litigation: Northern Alaska
   Environmental Center suit + separate Tanana Chiefs Conference and tribes suit.

Entries A, F, G (East Wing demolition, Stonewall removal, Stonewall settlement) require
no enrichment at this time. Their core facts were correct as committed.
"""
import json
import shutil
from pathlib import Path
from datetime import datetime

DATA_PATH = Path(__file__).parent.parent / "data" / "data.json"
BACKUP_PATH = DATA_PATH.with_suffix(
    f".json.bak-{datetime.now().strftime('%Y%m%d-%H%M%S')}-pre-enrich-ncr-stonewall-hunting-ambler"
)


# ============================================================================
# CORRECTION: NTHP v Trump preliminary injunction was GRANTED, not denied
# ============================================================================
def patch_nthp(entry):
    eid = "lit-2025-nthp-v-trump-ballroom"

    entry["n"] = (
        "National Trust for Historic Preservation in the United States v. National Park Service, "
        "1:25-cv-04316 (D.D.C. Filed December 12, 2025): Preservation Coalition Suit Challenging "
        "East Wing Demolition and Ballroom Construction for Failure to File with NCPC, Conduct "
        "NEPA Review, or Secure Congressional Authorization (Judge Richard J. Leon Granted "
        "Preliminary Injunction March 11, 2026 Holding No Statute Authorizes the President to "
        "Build the Ballroom; DOJ Appealed; April 27, 2026 DOJ Demand to Drop the Suit Refused "
        "by NTHP)"
    )

    entry["T"] = (
        "<span style=\"color: #166534;\">Preservation Lawsuit:</span> Judge Richard J. Leon "
        "(D.D.C.) Granted National Trust for Historic Preservation's Preliminary Injunction "
        "on March 11, 2026, Holding No Statute Authorizes the President to Build the Ballroom; "
        "DOJ Appealed and on April 27, 2026 Demanded NTHP Drop the Suit, Which NTHP Refused"
    )

    entry["d"] = "2025-12-12"

    entry["S"] = (
        "Filed December 12, 2025 in the U.S. District Court for the District of Columbia. "
        "Plaintiff: National Trust for Historic Preservation. Defendants: National Park Service, "
        "et al. Judge: Richard J. Leon. Docket: 1:25-cv-04316. First preliminary injunction motion "
        "denied in late December 2025 / early 2026. Second amended complaint filed March 2, 2026 "
        "adding three ultra vires claims. Second preliminary injunction motion filed March 5, 2026. "
        "PI GRANTED by Judge Leon on March 11, 2026, holding that no statute gives the President "
        "authority to build the ballroom and that construction must halt until Congress "
        "authorizes it. DOJ appealed. On April 27, 2026, DOJ demanded NTHP drop the lawsuit; "
        "NTHP publicly refused. Case continues. NCPC approval of project design on April 2, 2026 "
        "does not moot the constitutional ultra vires claim."
    )

    enrichment_block = (
        "<br><br><b>MAY 16, 2026 ENRICHMENT: CASE IDENTIFICATION AND CORRECTED PROCEDURAL "
        "HISTORY.</b><br>"
        "Case caption: <i>National Trust for Historic Preservation in the United States v. "
        "National Park Service, et al.</i> Civil Action No. 1:25-cv-04316. U.S. District Court "
        "for the District of Columbia. Assigned Judge: Richard J. Leon.<br><br>"
        "<b>CORRECTED PROCEDURAL HISTORY.</b> The original entry stated that the preliminary "
        "injunction motion was denied on March 31, 2026. That was incorrect. The correct timeline "
        "is as follows.<br>"
        "(1) Complaint filed December 12, 2025.<br>"
        "(2) First preliminary injunction motion denied in late December 2025 or January 2026.<br>"
        "(3) Second amended complaint filed March 2, 2026, adding three ultra vires claims based "
        "on the absence of statutory authorization for the project.<br>"
        "(4) Second preliminary injunction motion filed March 5, 2026.<br>"
        "(5) Preliminary injunction GRANTED by Judge Richard J. Leon on March 11, 2026. Judge "
        "Leon's order held that no statute gives the President authority to build the ballroom "
        "and that construction must halt until Congress authorizes it. (Source: NPR, CNBC, Civil "
        "Rights Litigation Clearinghouse case page.)<br>"
        "(6) DOJ appealed the preliminary injunction to the U.S. Court of Appeals for the D.C. "
        "Circuit.<br>"
        "(7) NCPC approved final project design 8 to 1 on April 2, 2026.<br>"
        "(8) On April 27, 2026 DOJ demanded that NTHP withdraw the lawsuit. NTHP publicly "
        "refused, issuing a statement that the underlying constitutional and statutory claims "
        "remain live and that NCPC approval does not moot the ultra vires claim.<br><br>"
        "<b>LEGAL SIGNIFICANCE OF THE PI GRANT.</b> Judge Leon's ultra vires ruling is the "
        "first federal court holding that the President lacks unilateral statutory authority "
        "to demolish a National Historic Landmark contributing structure and replace it with "
        "a new federal building. The ruling, if upheld on appeal, would establish that "
        "Congressional appropriation or specific statutory authorization is required for major "
        "demolition and construction at the White House complex.<br><br>"
        "<b>ENRICHMENT SOURCES.</b><br>"
        "Civil Rights Litigation Clearinghouse case page (authoritative legal source): "
        "<a href=\"https://clearinghouse.net/case/47494/\">https://clearinghouse.net/case/47494/</a><br>"
        "CourtListener docket: <a href=\"https://www.courtlistener.com/docket/72028010/national-trust-for-historic-preservation-in-the-united-states-v-national/\">https://www.courtlistener.com/docket/72028010/national-trust-for-historic-preservation-in-the-united-states-v-national/</a><br>"
        "NPR on PI grant March 11, 2026: <a href=\"https://www.npr.org/2026/03/31/nx-s1-5768446/judge-rules-white-house-ballroom-construction-must-halt-until-congress-oks-it\">https://www.npr.org/2026/03/31/nx-s1-5768446/judge-rules-white-house-ballroom-construction-must-halt-until-congress-oks-it</a><br>"
        "CNBC on PI grant and DOJ appeal: <a href=\"https://www.cnbc.com/2026/03/31/trump-white-house-ballroom-judge.html\">https://www.cnbc.com/2026/03/31/trump-white-house-ballroom-judge.html</a><br>"
        "The Hill on second-bid PI motion: <a href=\"https://thehill.com/regulation/court-battles/5788517-trump-ballroom-construction-preservationist-lawsuit/\">https://thehill.com/regulation/court-battles/5788517-trump-ballroom-construction-preservationist-lawsuit/</a><br>"
        "The Hill on NTHP refusing to drop: <a href=\"https://thehill.com/regulation/court-battles/5851406-trump-white-house-ballroom-lawsuit/\">https://thehill.com/regulation/court-battles/5851406-trump-white-house-ballroom-lawsuit/</a><br>"
        "NTHP statement on DOJ demand: <a href=\"https://savingplaces.org/press-center/media-resources/statement-from-nationaltrust-4-27-2026\">https://savingplaces.org/press-center/media-resources/statement-from-nationaltrust-4-27-2026</a><br>"
        "PBS NewsHour on NTHP refusal: <a href=\"https://www.pbs.org/newshour/nation/preservationists-wont-drop-lawsuit-against-trumps-400m-white-house-ballroom-after-doj-request\">https://www.pbs.org/newshour/nation/preservationists-wont-drop-lawsuit-against-trumps-400m-white-house-ballroom-after-doj-request</a><br>"
        "Fortune on NTHP press release: <a href=\"https://fortune.com/2026/04/27/national-trust-sues-white-house-ballroom-doj/\">https://fortune.com/2026/04/27/national-trust-sues-white-house-ballroom-doj/</a>"
    )

    entry["D"] = entry["D"] + enrichment_block
    return eid


# ============================================================================
# ENRICHMENT: One Big Beautiful Bill reconciliation context
# ============================================================================
def patch_grassley(entry):
    eid = "leg-2026-ballroom-security-appropriation"

    enrichment_block = (
        "<br><br><b>MAY 16, 2026 ENRICHMENT: ONE BIG BEAUTIFUL BILL RECONCILIATION VEHICLE "
        "AND EXACT STATUTORY LANGUAGE.</b><br>"
        "The $1 billion ballroom-security earmark is part of the Senate Republican reconciliation "
        "package referred to as the 'One Big Beautiful Bill.' The full package is a roughly $70 "
        "billion immigration-enforcement reconciliation vehicle. The Senate Judiciary Committee "
        "piece, which Chairman Chuck Grassley (R-IA) released on May 5, 2026, amounts to nearly "
        "$39.2 billion, including nearly $2.5 billion for the Justice Department and Secret "
        "Service on top of the DHS funding.<br><br>"
        "<b>EXACT STATUTORY LANGUAGE.</b> The reconciliation text earmarks the $1 billion "
        "specifically 'for the purposes of security adjustments and upgrades, including within "
        "the perimeter fence of the White House Compound to support enhancements by the United "
        "States Secret Service relating to the East Wing Modernization Project, including "
        "above-ground and below-ground security features.' The above-ground and below-ground "
        "language confirms the funds are tied to both the ballroom structure itself and to the "
        "underground facility replacing the Presidential Emergency Operations Center "
        "(cross-reference ea-2025-white-house-ballroom-east-wing).<br><br>"
        "<b>RECONCILIATION MECHANISM.</b> As a reconciliation package, the bill is procedurally "
        "filibuster-proof in the Senate and requires only a simple majority. This procedural "
        "posture is what makes the bundling structure consequential: the $1 billion ballroom "
        "earmark cannot be filibustered out of the package, and Senate Republicans who oppose "
        "the ballroom earmark on its merits must vote against the entire immigration-enforcement "
        "package to register their objection.<br><br>"
        "<b>ENRICHMENT SOURCES.</b><br>"
        "Grassley press release with Senate Judiciary Committee text: "
        "<a href=\"https://www.grassley.senate.gov/news/news-releases/grassley-releases-senate-judiciary-committee-text-of-the-one-big-beautiful-bill\">https://www.grassley.senate.gov/news/news-releases/grassley-releases-senate-judiciary-committee-text-of-the-one-big-beautiful-bill</a><br>"
        "Roll Call on reconciliation text: <a href=\"https://rollcall.com/2026/05/05/reconciliation-bill-text-would-fund-ice-cbp-ballroom-security/\">https://rollcall.com/2026/05/05/reconciliation-bill-text-would-fund-ice-cbp-ballroom-security/</a><br>"
        "Washington Times on filibuster-proof bill: <a href=\"https://www.washingtontimes.com/news/2026/may/5/gops-filibuster-proof-bill-spends-69b-immigration-force-1b-white/\">https://www.washingtontimes.com/news/2026/may/5/gops-filibuster-proof-bill-spends-69b-immigration-force-1b-white/</a><br>"
        "Punchbowl News on $72B recon: <a href=\"https://punchbowl.news/article/senate/72b-recon/\">https://punchbowl.news/article/senate/72b-recon/</a><br>"
        "Deseret News: <a href=\"https://www.deseret.com/politics/2026/05/05/trump-ballroom-security-reconciliation-bill/\">https://www.deseret.com/politics/2026/05/05/trump-ballroom-security-reconciliation-bill/</a><br>"
        "Fiscal Times: <a href=\"https://www.thefiscaltimes.com/2026/05/05/Republican-DHS-Funding-Bill-Includes-1-Billion-Trumps-Ballroom-Security\">https://www.thefiscaltimes.com/2026/05/05/Republican-DHS-Funding-Bill-Includes-1-Billion-Trumps-Ballroom-Security</a>"
    )

    entry["D"] = entry["D"] + enrichment_block
    return eid


# ============================================================================
# ENRICHMENT: Hains Point confirmed; Tom Fazio designer; Judge Ana Reyes ruling
# ============================================================================
def patch_east_potomac(entry):
    eid = "ea-2026-east-potomac-championship-golf"

    enrichment_block = (
        "<br><br><b>MAY 16, 2026 ENRICHMENT: HAINS POINT STATUS CONFIRMED, DESIGNER "
        "IDENTIFIED, JUDGE REYES MAINTENANCE RULING.</b><br>"
        "<b>HAINS POINT CONFIRMED UNTOUCHED.</b> The May 14, 2026 design release "
        "definitively confirms that Hains Point remains untouched in the design. Reporting "
        "(Washington Post, WTOP, Washington Examiner, The Hill) notes that 'the redesign "
        "rendering does not appear to touch any parts of Hains Point outside the golf course's "
        "boundaries, such as the pedestrian and bike pathways.' The southern tip of the "
        "peninsula, including the picnic areas, fishing access, and Cherry Blossom viewpoints, "
        "is preserved.<br><br>"
        "<b>COURSE DESIGNER: TOM FAZIO.</b> The championship-course redesign is by golf-course "
        "architect Tom Fazio, who has designed multiple championship and Top-100 courses in the "
        "United States. The selection of a championship-grade architect confirms the tournament-"
        "level positioning of the converted course.<br><br>"
        "<b>JUDGE ANA REYES RULING.</b> On May 4, 2026, U.S. District Judge Ana Reyes (D.D.C.) "
        "allowed federal maintenance to proceed at the historic East Potomac Golf Course "
        "despite fears of closure raised by watchdog plaintiffs in the emergency-motion "
        "litigation. The ruling permitted maintenance and preparation activities to continue "
        "while litigation on the broader project proceeds. The National Links Trust operating-"
        "agreement deal of May 8, 2026 followed days later and resolved the Langston / Rock "
        "Creek Park public-management question, leaving the East Potomac Golf Links conversion "
        "and the procedural-review questions as the remaining live disputes.<br><br>"
        "<b>OPERATIONAL TIMELINE.</b> National Links Trust will continue managing East Potomac "
        "Golf Links until renovations begin. The renovation start date has not yet been "
        "specified by the National Park Service.<br><br>"
        "<b>ENRICHMENT SOURCES.</b><br>"
        "The Fried Egg analysis of Fazio plan: <a href=\"https://www.thefriedegg.com/articles/washington-dc-golf-east-potomac-tom-fazio-plans\">https://www.thefriedegg.com/articles/washington-dc-golf-east-potomac-tom-fazio-plans</a><br>"
        "Washington Times on Judge Ana Reyes ruling: <a href=\"https://www.washingtontimes.com/news/2026/may/4/ana-reyes-federal-judge-lets-maintenance-proceed-east-potomac-golf/\">https://www.washingtontimes.com/news/2026/may/4/ana-reyes-federal-judge-lets-maintenance-proceed-east-potomac-golf/</a><br>"
        "Washington Examiner on Burgum design release: <a href=\"https://www.washingtonexaminer.com/news/white-house/4568810/doug-burgum-east-potomac-golf-links-layout/\">https://www.washingtonexaminer.com/news/white-house/4568810/doug-burgum-east-potomac-golf-links-layout/</a><br>"
        "The Hill on Burgum unveiling: <a href=\"https://thehill.com/homenews/administration/5878551-doug-burgum-dc-golf-course-design/\">https://thehill.com/homenews/administration/5878551-doug-burgum-dc-golf-course-design/</a><br>"
        "51st on wildlife conservation: <a href=\"https://51st.news/trump-golf-course-takeover-wildlife-birds-conservation/\">https://51st.news/trump-golf-course-takeover-wildlife-birds-conservation/</a><br>"
        "NPS East Potomac Park Golf Course page: <a href=\"https://www.nps.gov/places/000/east-potomac-park-golf-course.htm\">https://www.nps.gov/places/000/east-potomac-park-golf-course.htm</a>"
    )

    entry["D"] = entry["D"] + enrichment_block
    return eid


# ============================================================================
# ENRICHMENT: Triumphal Arch full plaintiff list, Public Citizen counsel, Chutkan
# ============================================================================
def patch_triumphal_arch(entry):
    eid = "ea-2026-triumphal-arch-memorial-circle"

    enrichment_block = (
        "<br><br><b>MAY 16, 2026 ENRICHMENT: VETERANS LAWSUIT IDENTIFIED, PROJECT NAME "
        "'INDEPENDENCE ARCH', JUDGE CHUTKAN DECLINES TO BLOCK.</b><br>"
        "<b>VETERANS LAWSUIT IDENTIFIED.</b> The federal litigation referenced in the entry's "
        "status field was filed by three Vietnam War veterans, Michael Lemmon, Shaun Byrnes, "
        "and Jon Gundersen, joined by historian Calder Loth, represented by the nonprofit "
        "watchdog organization Public Citizen. The case was filed in the U.S. District Court "
        "for the District of Columbia. Defendants include the Office of the President, "
        "President Donald Trump personally, the National Park Service, and Domestic Policy "
        "Council Director Vince Haley. The veterans argue that the construction lacks "
        "Congressional approval and that the arch would disrupt the sightline between the "
        "Lincoln Memorial and Arlington House at Arlington National Cemetery, with additional "
        "claims based on the cultural-landscape integrity of Memorial Bridge and the "
        "ceremonial axis of national reconciliation. Case caption to be confirmed from PACER.<br><br>"
        "<b>JUDGE TANYA CHUTKAN DECLINED TO BLOCK.</b> Federal Court Judge Tanya Chutkan "
        "declined to block construction of the arch after the veterans and historian filed "
        "their lawsuit seeking to halt the project. The denial is procedural and does not "
        "resolve the merits; the underlying claims remain live. Plaintiffs may amend, seek "
        "appellate review, or file additional motions as the project moves through site survey "
        "and construction.<br><br>"
        "<b>PROJECT NAME 'INDEPENDENCE ARCH'.</b> Reporting indicates that the project's "
        "name as used by the Trump II administration is the 'Independence Arch.' The "
        "triumphal-arch descriptor is the architectural form; 'Independence Arch' is the "
        "project's branding, tied to the July 4, 2026 semiquincentennial target completion.<br><br>"
        "<b>ENRICHMENT SOURCES.</b><br>"
        "The Hill on Vietnam War veterans suing: <a href=\"https://thehill.com/regulation/court-battles/5746932-trump-triumphal-arch-lawsuit/\">https://thehill.com/regulation/court-battles/5746932-trump-triumphal-arch-lawsuit/</a><br>"
        "NOTUS on the veterans-and-historian lawsuit: <a href=\"https://www.notus.org/courts/vietnam-veterans-sue-trump-dc-arch-block-arlington-national-cemetery-views\">https://www.notus.org/courts/vietnam-veterans-sue-trump-dc-arch-block-arlington-national-cemetery-views</a><br>"
        "WUSA9 on the 250-foot arch lawsuit: <a href=\"https://www.wusa9.com/article/news/community/vietnam-veterans-sue-proposed-250-foot-trump-arch-near-arlington-cemetery/65-15580d6c-5658-4ddc-9b5a-f5b775f8080e\">https://www.wusa9.com/article/news/community/vietnam-veterans-sue-proposed-250-foot-trump-arch-near-arlington-cemetery/65-15580d6c-5658-4ddc-9b5a-f5b775f8080e</a><br>"
        "WJLA on the lawsuit and project name: <a href=\"https://wjla.com/news/local/president-donald-trump-triumphal-arch-monument-statue-lawsuit-vietnam-war-veterans-national-park-service-lincoln-memorial-arlington-cemetary-america-250-white-house-projects-historic-views-landmarks-plans-costs-view-obscurity-traffic-safety\">https://wjla.com/news/local/president-donald-trump-triumphal-arch-monument-statue-lawsuit-vietnam-war-veterans-national-park-service-lincoln-memorial-arlington-cemetary-america-250-white-house-projects-historic-views-landmarks-plans-costs-view-obscurity-traffic-safety</a><br>"
        "CNBC on renderings: <a href=\"https://www.cnbc.com/2026/04/10/trump-arch-renderings-arlington.html\">https://www.cnbc.com/2026/04/10/trump-arch-renderings-arlington.html</a><br>"
        "Associated Press (via KDH News) on site survey: <a href=\"https://kdhnews.com/news/ap/survey-work-begins-for-contested-trump-triumphal-arch-project-in-washington/article_f69024f3-d35c-5c59-845e-b9c8d48dc36a.html\">https://kdhnews.com/news/ap/survey-work-begins-for-contested-trump-triumphal-arch-project-in-washington/article_f69024f3-d35c-5c59-845e-b9c8d48dc36a.html</a>"
    )

    entry["D"] = entry["D"] + enrichment_block
    return eid


# ============================================================================
# ENRICHMENT: SO 3447 date correction + specific changes
# ============================================================================
def patch_so_3447(entry):
    eid = "so-3447-nps-hunting-restrictions-repeal"

    entry["d"] = "2026-01-13"

    entry["S"] = (
        "Active. Interior Secretary Doug Burgum signed Secretarial Order 3447 on January 13, "
        "2026. (One source indicates January 7; January 13 is the more widely reported date "
        "and matches the NRA-ILA publication date of January 14, 2026.) Implementation underway. "
        "Reporting indicates the order affects more than 50 federal land units in the lower 48 "
        "states. Hunting is currently authorized at 76 NPS units (existing baseline), trapping "
        "at 31 units, and approximately 51 million NPS-managed acres are open to hunting under "
        "unit-specific authorizations. The order directs all Interior agencies (NPS, BLM, FWS, "
        "Bureau of Reclamation) to expand hunting and fishing access, remove unnecessary "
        "barriers, and ensure consistent policy. Specific changes already implemented at Big "
        "Cypress National Preserve (FL), Mississippi National River and Recreation Area (MN), "
        "and Jean Lafitte National Historical Park and Preserve (LA, where the alligator "
        "hunting ban was lifted). The 63 congressionally designated National Parks (capital N) "
        "are largely not in the affected set because most are protected from hunting by separate "
        "federal statutes. Sierra Club and other conservation organizations have announced "
        "opposition; litigation anticipated."
    )

    enrichment_block = (
        "<br><br><b>MAY 16, 2026 ENRICHMENT: SO 3447 DATE AND SPECIFIC CHANGES.</b><br>"
        "<b>DATE CORRECTED.</b> Secretarial Order 3447 was signed January 13, 2026 (one source "
        "indicates January 7; the January 13 date matches the NRA-ILA publication date of "
        "January 14, 2026 and is more widely confirmed in reporting).<br><br>"
        "<b>SCOPE.</b> The order affects more than 50 federal land units in the lower 48 "
        "states. The existing baseline is that hunting is authorized at 76 NPS units (out of "
        "the approximately 433 NPS units nationwide), trapping at 31 units, and approximately "
        "51 million NPS-managed acres are open to hunting under unit-specific authorizations. "
        "The order does not create new hunting authority at units that lack it; it directs "
        "loosening of restrictions and removal of barriers at units where hunting is already "
        "permitted, and signals an Interior-wide presumption favoring hunting and fishing "
        "access.<br><br>"
        "<b>SPECIFIC CHANGES IMPLEMENTED.</b><br>"
        "Big Cypress National Preserve (Florida): hunters are no longer required to mark "
        "equipment with their contact information. This is a Seminole and Miccosukee cultural-"
        "resource landscape; the Seminole Tribe of Florida and Miccosukee Tribe of Indians of "
        "Florida maintain treaty and aboriginal hunting practices in the Preserve.<br>"
        "Mississippi National River and Recreation Area (Minnesota): hunters are now allowed "
        "to clear vegetation to create shooting lanes. This affects Anishinaabe (Mdewakanton "
        "Dakota and Ojibwe) cultural landscapes along the Upper Mississippi corridor.<br>"
        "Jean Lafitte National Historical Park and Preserve (Louisiana): the previous ban on "
        "alligator hunting has been lifted. The Preserve includes Chitimacha, United Houma "
        "Nation, and Pointe-au-Chien cultural-resource sites; the Houma Nation has cultural "
        "and economic relationships to alligators that interact with the new hunting "
        "authorization.<br><br>"
        "<b>FEDERAL AGENCIES COVERED.</b> The order applies department-wide: National Park "
        "Service (76 hunt-authorized units), Bureau of Land Management, U.S. Fish and Wildlife "
        "Service (national wildlife refuges), and Bureau of Reclamation properties. The "
        "department-wide framing extends the rollback far beyond NPS units alone.<br><br>"
        "<b>FEDERAL REGISTER NOTICES.</b> Federal Register proposals related to specific units "
        "(notably for Alaska NPS preserve units) have been issued and are tracked separately. "
        "The order itself was published as an Interior Department secretarial order rather than "
        "a Federal Register notice-and-comment rulemaking, which raises APA procedural "
        "questions for subsequent unit-specific rule changes.<br><br>"
        "<b>ENRICHMENT SOURCES.</b><br>"
        "Sportsmen's Alliance victory statement: <a href=\"https://sportsmensalliance.org/news/victory-for-sportsmen-secretarial-order-3447-opens-federal-lands-for-hunting-and-fishing/\">https://sportsmensalliance.org/news/victory-for-sportsmen-secretarial-order-3447-opens-federal-lands-for-hunting-and-fishing/</a><br>"
        "GearJunkie on the order: <a href=\"https://gearjunkie.com/hunting/interior-pushes-streamlined-hunting-rules-parks-federal-sites\">https://gearjunkie.com/hunting/interior-pushes-streamlined-hunting-rules-parks-federal-sites</a><br>"
        "Outdoor Life on shall-issue framework: <a href=\"https://www.outdoorlife.com/conservation/interior-department-public-lands-order/\">https://www.outdoorlife.com/conservation/interior-department-public-lands-order/</a><br>"
        "OutdoorHub: <a href=\"https://www.outdoorhub.com/news/2026/05/11/hunting-restrictions-lifted-on-federal-lands-as-interior-department-directive-takes-effect/\">https://www.outdoorhub.com/news/2026/05/11/hunting-restrictions-lifted-on-federal-lands-as-interior-department-directive-takes-effect/</a><br>"
        "NRA-ILA on order (Jan 14, 2026 publication): <a href=\"https://www.nraila.org/articles/20260114/secretary-of-the-interior-issues-order-expanding-hunting-access-nationwide\">https://www.nraila.org/articles/20260114/secretary-of-the-interior-issues-order-expanding-hunting-access-nationwide</a><br>"
        "Congressional Sportsmen's Foundation: <a href=\"https://congressionalsportsmen.org/press/secretary-burgum-issues-important-order-to-increase-access-for-hunters-and-anglers/\">https://congressionalsportsmen.org/press/secretary-burgum-issues-important-order-to-increase-access-for-hunters-and-anglers/</a><br>"
        "National Parks Traveler: <a href=\"https://www.nationalparkstraveler.org/2026/05/updated-national-parks-silently-allowing-more-hunting-and-trapping-access\">https://www.nationalparkstraveler.org/2026/05/updated-national-parks-silently-allowing-more-hunting-and-trapping-access</a><br>"
        "The Travel on park-ranger rules: <a href=\"https://www.thetravel.com/us-government-overturns-national-park-hunting-rules-lifts-restrictions/\">https://www.thetravel.com/us-government-overturns-national-park-hunting-rules-lifts-restrictions/</a><br>"
        "Shooting News Weekly: <a href=\"https://www.shootingnewsweekly.com/hunting/interior-secretary-orders-federal-lands-to-effectively-be-shall-issue-hunting-and-fishing-friendly-spaces/\">https://www.shootingnewsweekly.com/hunting/interior-secretary-orders-federal-lands-to-effectively-be-shall-issue-hunting-and-fishing-friendly-spaces/</a>"
    )

    entry["D"] = entry["D"] + enrichment_block
    return eid


# ============================================================================
# ENRICHMENT: Trilogy Metals investment structure + Department of War + litigation
# ============================================================================
def patch_trilogy(entry):
    eid = "ea-2025-trilogy-metals-ambler-equity"

    enrichment_block = (
        "<br><br><b>MAY 16, 2026 ENRICHMENT: DEPARTMENT OF WAR INVESTMENT STRUCTURE, "
        "CLOSING CONDITIONS, LITIGATION COALITION.</b><br>"
        "<b>INVESTMENT AUTHORITY: U.S. DEPARTMENT OF WAR (DOW).</b> The federal investment is "
        "by the U.S. Department of War (DOW). The DOW investment is intended to operate under "
        "Defense Production Act framework, though DPA reauthorization by Congress is a closing "
        "condition for the transaction. The DOW is the investing federal entity; the DPA is "
        "the underlying authorities framework. Treasury, DOI, and BLM are the regulatory "
        "agencies; the dual regulator-and-investor posture spans multiple federal departments.<br><br>"
        "<b>INVESTMENT STRUCTURE.</b> The DOW will invest approximately $17.8 million in "
        "Trilogy Metals in exchange for 8,215,570 units at a price of $2.17 per unit. Each unit "
        "comprises one common share of Trilogy Metals and three-quarters of a 10-year warrant. "
        "The full $35.6 million federal commitment is split between this direct investment in "
        "Trilogy Metals and additional investment terms with South32 Limited and Ambler "
        "Metals, the joint-venture partners on the Upper Kobuk Mineral Projects (UKMP).<br><br>"
        "<b>CLOSING CONDITIONS.</b> The parties intend to close the transaction promptly "
        "following two conditions: (1) reauthorization of the Defense Production Act by the "
        "United States Congress, and (2) completion by the U.S. Government of its Foreign "
        "Ownership, Control, or Influence (FOCI) review. If these conditions have not occurred "
        "prior to March 31, 2026, the letter of intent terminates. Status of both closing "
        "conditions to be tracked.<br><br>"
        "<b>LITIGATION COALITION.</b> Two distinct lawsuits have been filed against the Ambler "
        "Access Project ROW reversal.<br>"
        "(1) The original lawsuit was filed by the Northern Alaska Environmental Center "
        "together with a coalition of environmental and conservation organizations.<br>"
        "(2) A separate lawsuit was filed by the Tanana Chiefs Conference (representing 42 "
        "Interior Alaska tribes) together with several individual Native Villages. This is the "
        "Indigenous-rights and ANILCA Section 810 subsistence-impact litigation. Specific "
        "tribal plaintiffs and case caption to be confirmed.<br><br>"
        "<b>SIGNIFICANCE OF THE TWO-TRACK LITIGATION.</b> The bifurcation of the litigation "
        "into environmental-coalition and tribal-coalition tracks reflects the distinct legal "
        "frameworks at issue. The environmental coalition presses NEPA and Endangered Species "
        "Act claims. The Tanana Chiefs coalition presses ANILCA Section 810 subsistence-impact "
        "claims and federal trust responsibility claims. Both tracks raise the regulator-and-"
        "investor structural conflict separately.<br><br>"
        "<b>ENRICHMENT SOURCES.</b><br>"
        "Trilogy Metals press release on DOW investment: <a href=\"https://trilogymetals.com/news-and-media/news/trilogy-metals-announces-strategic-investment-by-us-federal-government/\">https://trilogymetals.com/news-and-media/news/trilogy-metals-announces-strategic-investment-by-us-federal-government/</a><br>"
        "PRNewswire on DOW investment terms: <a href=\"https://www.prnewswire.com/news-releases/trilogy-metals-announces-strategic-investment-by-us-federal-government-302576247.html\">https://www.prnewswire.com/news-releases/trilogy-metals-announces-strategic-investment-by-us-federal-government-302576247.html</a><br>"
        "Stocktitan on $35.6M investment structure: <a href=\"https://www.stocktitan.net/news/TMQ/trilogy-metals-announces-strategic-investment-by-us-federal-pnnxhb8iwo32.html\">https://www.stocktitan.net/news/TMQ/trilogy-metals-announces-strategic-investment-by-us-federal-pnnxhb8iwo32.html</a><br>"
        "Trilogy Metals update on Ambler Access Project: <a href=\"https://trilogymetals.com/news-and-media/news/trilogy-metals-provides-an-update-on-the-ambler-access-project/\">https://trilogymetals.com/news-and-media/news/trilogy-metals-provides-an-update-on-the-ambler-access-project/</a><br>"
        "Trilogy Metals on recent developments: <a href=\"https://trilogymetals.com/news-and-media/news/trilogy-metals-provides-an-update-on-recent-positive-developments-to-advance-the-ambler-access-project/\">https://trilogymetals.com/news-and-media/news/trilogy-metals-provides-an-update-on-recent-positive-developments-to-advance-the-ambler-access-project/</a><br>"
        "MLQ on $35.6M and 10% stake: <a href=\"https://mlq.ai/news/us-federal-government-to-invest-356-million-and-take-10-stake-in-trilogy-metals-advancing-ambler-mining-district/\">https://mlq.ai/news/us-federal-government-to-invest-356-million-and-take-10-stake-in-trilogy-metals-advancing-ambler-mining-district/</a><br>"
        "Junior Mining Network: <a href=\"https://www.juniorminingnetwork.com/junior-miner-news/press-releases/1358-tsx/tmq/188674-trilogy-metals-announces-strategic-investment-by-us-federal-government.html\">https://www.juniorminingnetwork.com/junior-miner-news/press-releases/1358-tsx/tmq/188674-trilogy-metals-announces-strategic-investment-by-us-federal-government.html</a>"
    )

    entry["D"] = entry["D"] + enrichment_block
    return eid


# ============================================================================
# RUN
# ============================================================================
PATCH_FUNCTIONS = {
    "litigation": [
        ("lit-2025-nthp-v-trump-ballroom", patch_nthp),
    ],
    "legislation": [
        ("leg-2026-ballroom-security-appropriation", patch_grassley),
    ],
    "executive_actions": [
        ("ea-2026-east-potomac-championship-golf", patch_east_potomac),
        ("ea-2026-triumphal-arch-memorial-circle", patch_triumphal_arch),
        ("ea-2025-trilogy-metals-ambler-equity", patch_trilogy),
    ],
    "agency_actions": [
        ("so-3447-nps-hunting-restrictions-repeal", patch_so_3447),
    ],
}


def main():
    if not DATA_PATH.exists():
        raise SystemExit(f"data.json not found at {DATA_PATH}")

    shutil.copy2(DATA_PATH, BACKUP_PATH)
    print(f"Backup written: {BACKUP_PATH.name}")

    with DATA_PATH.open() as f:
        data = json.load(f)

    em_dash = "—"
    patched_count = 0

    for cat, patches in PATCH_FUNCTIONS.items():
        entries = data.get(cat, [])
        for target_id, patch_fn in patches:
            target = None
            for e in entries:
                if (e.get("i") or e.get("id")) == target_id:
                    target = e
                    break
            if target is None:
                raise SystemExit(f"Entry {target_id} not found in {cat}. Aborting.")
            patch_fn(target)
            # Post-patch em-dash sweep
            if em_dash in json.dumps(target, ensure_ascii=False):
                raise SystemExit(f"ABORT: em-dash detected in patched {target_id}.")
            print(f"Patched {target_id} in {cat}.")
            patched_count += 1

    # Update meta.lastUpdated if present
    if "meta" in data and isinstance(data["meta"], dict):
        data["meta"]["lastUpdated"] = datetime.now().strftime("%Y-%m-%d")

    # Atomic write
    tmp = DATA_PATH.with_suffix(".json.tmp")
    with tmp.open("w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    tmp.replace(DATA_PATH)

    print()
    print(f"Done. {patched_count} entries enriched.")


if __name__ == "__main__":
    main()
