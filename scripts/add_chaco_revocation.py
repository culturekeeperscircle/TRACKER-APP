#!/usr/bin/env python3
"""Add Chaco Canyon mineral-withdrawal revocation entry.

On March 31, 2026, the Bureau of Land Management opened a public
scoping period on a proposal to revoke Public Land Order 7923
(June 7, 2023), the Biden-era 20-year mineral withdrawal protecting
336,404.42 acres of public lands surrounding Chaco Culture National
Historical Park (a UNESCO World Heritage Site sacred to all 19
Pueblos, the Navajo Nation, the Hopi Tribe, and other Tribal Nations
of the Southwest). The scoping comment period was set at 7 days,
ending April 7, 2026, during Easter, Passover, and several traditional
Pueblo ceremonial periods.

NEPA project number: DOI-BLM-NM-F010-2026-0002-EA.
"""
import json
import shutil
from pathlib import Path
from datetime import datetime

DATA_PATH = Path(__file__).parent.parent / "data" / "data.json"
BACKUP_PATH = DATA_PATH.with_suffix(
    f".json.bak-{datetime.now().strftime('%Y%m%d-%H%M%S')}-pre-chaco-revocation"
)

NEW_ID = "blm-chaco-withdrawal-revocation-2026"

ENTRY = {
    "i": NEW_ID,
    "t": "Agency Notice",
    "n": "BLM NEPA Project DOI-BLM-NM-F010-2026-0002-EA: Evaluation of Potential Revocation of Chaco Withdrawal (March 31, 2026)",
    "T": '<span style="color: #991B1B;">BLM Chaco Withdrawal Revocation Scoping:</span> Bureau of Land Management Opens 7-Day Scoping Period to Revoke or Shrink Biden-Era 336,404-Acre Mineral Withdrawal Around Chaco Culture National Historical Park',
    "s": "BLM Chaco mineral withdrawal revocation scoping",
    "d": "2026-03-31",
    "a": "Trump II",
    "A": ["DOI", "BLM"],
    "S": "Active. Scoping notice opened March 31, 2026 by the Bureau of Land Management. Public comment period closed April 7, 2026 (7 days, including Easter, Passover, and several traditional Pueblo ceremonial periods). Project number DOI-BLM-NM-F010-2026-0002-EA, \"Evaluation of Potential Revocation of Chaco Withdrawal.\" The agency is considering full revocation or geographic reduction of the existing 336,404.42-acre withdrawal. Implementing executive authorities are EO 14154 (Unleashing American Energy, tracked at eo-14154) and Secretary's Order 3418 (tracked at so-3418). New Mexico Congressional delegation has filed objection.",
    "L": "SEVERE",
    "D": (
        "<b>BLM SCOPING NOTICE.</b> On March 31, 2026, the Bureau of Land Management opened a public scoping period on a proposal to revoke Public Land Order 7923 (June 7, 2023), the Biden-era 20-year mineral withdrawal that protects 336,404.42 acres of public lands surrounding Chaco Culture National Historical Park in San Juan, Sandoval, and McKinley counties, New Mexico. The NEPA project is designated DOI-BLM-NM-F010-2026-0002-EA, \"Evaluation of Potential Revocation of Chaco Withdrawal.\" The scoping notice asks the public whether BLM should repeal the withdrawal in full or reduce the size of the buffer area, including by approximately half.<br><br>"
        "<b>SEVEN-DAY SCOPING WINDOW.</b> The public-comment period was set at seven days, closing April 7, 2026. The window included Easter Sunday, Passover, and multiple traditional Pueblo ceremonial periods. Tribal leaders, the New Mexico Congressional delegation, and environmental organizations have characterized the abbreviated timeline as procedurally improper and as effectively excluding meaningful tribal consultation. The Biden-era withdrawal (PLO 7923) had been built on more than a decade of tribal advocacy, two years of environmental review, 150 days of public comment, eight public meetings, bipartisan Congressional support, and approximately 100,000 public submissions. The proposed revocation would unwind that record over a single week of comment.<br><br>"
        "<b>SITE SIGNIFICANCE.</b> Chaco Culture National Historical Park is a UNESCO World Heritage Site (inscribed 1987). The park preserves the cultural heart of the ancestral Pueblo civilization that flourished in the San Juan Basin between approximately AD 850 and 1250. Chaco Canyon and the surrounding landscape contain Great Houses, ceremonial roads, alignments, and outlier sites that constitute one of the densest archaeological landscapes in North America. The park is sacred to all 19 Pueblos of New Mexico, the Navajo Nation, the Hopi Tribe, and to other Tribal Nations of the Southwest. The 10-mile buffer protected by PLO 7923 is the cultural landscape surrounding the park unit itself, including the ceremonial-road corridors and outlier sites that connect the park to the wider Chacoan world.<br><br>"
        "<b>UNDERLYING POLICY ORDER.</b> Public Land Order 7923 was published in the Federal Register on June 7, 2023 (88 FR 37268). The order withdrew approximately 336,404.42 acres of public lands surrounding the park boundary from location and entry under the United States mining laws (30 U.S.C. §§ 22-54) and from leasing under the Mineral Leasing Act (30 U.S.C. §§ 181 et seq.) and the Geothermal Steam Act (30 U.S.C. §§ 1001 et seq.) for a 20-year period. The withdrawal does not affect existing valid leases, valid existing rights, or trust or restricted Indian lands. The withdrawal was issued under the Federal Land Policy and Management Act of 1976 (43 U.S.C. § 1714).<br><br>"
        "<b>EXECUTIVE-BRANCH AUTHORITY CHAIN.</b> The proposed revocation operates under EO 14154 (Unleashing American Energy, tracked at eo-14154) and Secretary's Order 3418 (Unleashing American Energy, tracked at so-3418), which together direct Interior to identify and unwind Biden-era public-lands protections that limit oil, gas, and mineral leasing. The Chaco scoping notice is one of multiple parallel BLM revocations under the same authority chain. The broader pattern is captured at v2025-doi-003 (BLM Proposed Rescission of Public Lands Rule) and at agency-action-nps-monument-designation-review-2026 (DOI review of national monument designations).<br><br>"
        "<b>CONGRESSIONAL OBJECTION.</b> The New Mexico federal delegation, including Senators Martin Heinrich and Ben Ray Luján and Representatives Melanie Stansbury, Gabe Vasquez, and Teresa Leger Fernández, submitted formal objection in October 2025 (when the administration first signaled intent) and again in April 2026 (when the scoping notice opened). The delegation characterized the action as a \"reckless race to allow drilling in Chaco Canyon.\" Polling reported in association with the objection shows over 70 percent of New Mexico voters oppose reversing the withdrawal.<br><br>"
        "<b>DOCUMENTED HARMS IF THE WITHDRAWAL IS REVOKED.</b> "
        "(1) <i>Sacred-site exposure.</i> Oil and gas leasing within the 10-mile buffer would expose ceremonial roads, outlier sites, alignments, and viewsheds connected to Chaco's UNESCO-recognized cultural landscape to drilling-pad construction, road construction, pipeline installation, induced seismicity, and methane and VOC emissions. The cultural landscape is contiguous and place-specific. Damage to the buffer is damage to the park.<br>"
        "(2) <i>Free, prior, and informed consent.</i> The 7-day scoping window during religious holidays violates the consultation standard articulated under the United Nations Declaration on the Rights of Indigenous Peoples (tracked at intl-undrip-implementation) and the federal-Indian-trust-responsibility framework articulated in Joint Secretary's Order 3403 (tracked at so-3403-co-stewardship).<br>"
        "(3) <i>Cumulative impact.</i> The San Juan Basin is one of the most heavily drilled oil-and-gas basins in the country. Lifting the buffer would compound an already documented cumulative-impact load on the Greater Chaco landscape, including air-quality degradation in the Four Corners region disproportionately affecting Diné (Navajo) communities (tracked under the Indigenous aggregate analysis at v2026-indigenous-cultural-threat-analysis).<br>"
        "(4) <i>UNESCO obligations.</i> Damage to the cultural landscape surrounding the World Heritage Site exposes the United States to UNESCO World Heritage Committee scrutiny and potential listing of the site as World Heritage in Danger. The United States's already complicated UNESCO relationship is tracked at intl-unesco-withdrawal-rejoined.<br><br>"
        "<b>RELATIONSHIP TO BROADER PATTERN.</b> The Chaco revocation is one component of a coordinated Trump II Interior strategy to unwind Biden-era Indigenous-sacred-landscape protections. Bears Ears (tracked at proc-9681 and bears-ears-10th-circuit) and Grand Staircase-Escalante (tracked at proc-10286) face parallel Antiquities Act review (tracked at agency-action-nps-monument-designation-review-2026). Coal-leasing expansion in the broader region is tracked at coal-leasing-13m-acres. The broader Indigenous cultural-resource threat synthesis is at v2026-indigenous-cultural-threat-analysis.<br><br>"
        "<b>CULTURAL RESOURCE THREAT ASSESSMENT.</b> The threat level is SEVERE. The cultural resources at risk are paramount to the cultural continuity of all 19 Pueblos of New Mexico, the Navajo Nation, the Hopi Tribe, and the broader Indigenous Southwest. The harm dimensions include sacred-site exposure (Places), severance of ceremonial-road and outlier-site networks (Practices), exposure of archaeological treasures across an unsurveyed cultural landscape to extraction-related disturbance (Treasures), and continued environmental-justice harm to Diné and Pueblo communities living within the affected airshed (People). The harm is partially irreversible. Once a drilling pad is constructed, the cultural landscape it replaces cannot be restored on a Chacoan-civilization timescale."
        "<br><br>"
        "<b>SOURCES.</b><br>"
        "Primary federal-action document (Biden-era withdrawal being revoked): Public Land Order No. 7923, 88 FR 37268, June 7, 2023. <a href=\"https://www.federalregister.gov/documents/2023/06/07/2023-12158/public-land-order-no-7923-for-public-lands-withdrawal-surrounding-chaco-culture-national-historical\">https://www.federalregister.gov/documents/2023/06/07/2023-12158/public-land-order-no-7923-for-public-lands-withdrawal-surrounding-chaco-culture-national-historical</a>; "
        "DOI PDF of the PLO 7923 Federal Register notice: <a href=\"https://www.doi.gov/sites/doi.gov/files/plo-chaco-fr-notice-6.2.23-508.pdf\">https://www.doi.gov/sites/doi.gov/files/plo-chaco-fr-notice-6.2.23-508.pdf</a><br>"
        "Congressional objection: U.S. Senate Energy Committee (NM Delegation), \"N.M. Delegation Denounces Trump Admin's Reckless Race to Allow Drilling in Chaco Canyon,\" April 2026. <a href=\"https://www.energy.senate.gov/2026/4/n-m-delegation-denounces-trump-admin-s-reckless-race-to-allow-drilling-in-chaco-canyon\">https://www.energy.senate.gov/2026/4/n-m-delegation-denounces-trump-admin-s-reckless-race-to-allow-drilling-in-chaco-canyon</a>; "
        "Senator Martin Heinrich, \"N.M. Delegation Responds to Trump Administration's New Actions to Undo Protections for the Greater Chaco Region.\" <a href=\"https://www.heinrich.senate.gov/newsroom/press-releases/nm-delegation-responds-to-trump-administrations-new-actions-to-undo-protections-for-the-greater-chaco-region\">https://www.heinrich.senate.gov/newsroom/press-releases/nm-delegation-responds-to-trump-administrations-new-actions-to-undo-protections-for-the-greater-chaco-region</a>; "
        "U.S. Senate Energy Committee (NM Delegation), October 2025 statement. <a href=\"https://www.energy.senate.gov/2025/10/n-m-delegation-condemns-trump-administration-s-move-to-begin-reversing-protections-for-chaco-canyon\">https://www.energy.senate.gov/2025/10/n-m-delegation-condemns-trump-administration-s-move-to-begin-reversing-protections-for-chaco-canyon</a><br>"
        "Tribal and Indigenous response: Native News Online, \"ACTION NEEDED to Save Chaco!\" <a href=\"https://nativenewsonline.net/environment/action-needed-to-save-chaco/\">https://nativenewsonline.net/environment/action-needed-to-save-chaco/</a>; "
        "Archaeology Southwest, \"Revoking Chaco Canyon Protections Ignores Pueblos, Tribes, and the Public,\" April 1, 2026. <a href=\"https://www.archaeologysouthwest.org/2026/04/01/revoking-chaco-canyon-protections-ignores-pueblos-tribes-and-the-public-repost/\">https://www.archaeologysouthwest.org/2026/04/01/revoking-chaco-canyon-protections-ignores-pueblos-tribes-and-the-public-repost/</a>; "
        "Source New Mexico, \"New Mexico officials, tribes accuse feds of rushing to reverse Chaco Canyon drilling ban,\" April 1, 2026. <a href=\"https://sourcenm.com/2026/04/01/new-mexico-officials-tribes-accuse-feds-of-rushing-efforts-to-reverse-chaco-canyon-drilling-ban/\">https://sourcenm.com/2026/04/01/new-mexico-officials-tribes-accuse-feds-of-rushing-efforts-to-reverse-chaco-canyon-drilling-ban/</a><br>"
        "Environmental and conservation response: Sierra Club, \"Indigenous and Environmental Groups Denounce Trump Administration Proposal to Revoke Greater Chaco Protections,\" April 2026. <a href=\"https://www.sierraclub.org/press-releases/2026/04/indigenous-and-environmental-groups-denounce-trump-administration-proposal\">https://www.sierraclub.org/press-releases/2026/04/indigenous-and-environmental-groups-denounce-trump-administration-proposal</a>; "
        "National Parks Traveler, \"Groups Voice Opposition To Trump Administration's Oil And Gas Leasing Plans Near Chaco Canyon,\" April 2026. <a href=\"https://www.nationalparkstraveler.org/2026/04/groups-voice-opposition-trump-administrations-oil-and-gas-leasing-plans-near-chaco-canyon\">https://www.nationalparkstraveler.org/2026/04/groups-voice-opposition-trump-administrations-oil-and-gas-leasing-plans-near-chaco-canyon</a>; "
        "Our Public Lands and Waters, \"BLM Wants to Allow Drilling on Lands Directly Bordering Chaco Culture National Historical Park.\" <a href=\"https://ourpubliclandsandwaters.substack.com/p/blm-wants-to-allow-drilling-on-lands\">https://ourpubliclandsandwaters.substack.com/p/blm-wants-to-allow-drilling-on-lands</a>; "
        "More Than Just Parks, \"Trump Administration To Reverse Chaco Canyon Protections.\" <a href=\"https://morethanjustparks.substack.com/p/trump-administration-to-reverse-chaco\">https://morethanjustparks.substack.com/p/trump-administration-to-reverse-chaco</a><br>"
        "News coverage: KJZZ, \"Trump proposal could roll back buffer zone around this UNESCO World Heritage Site,\" April 7, 2026. <a href=\"https://www.kjzz.org/tribal-natural-resources/2026-04-07/trump-proposal-could-roll-back-buffer-zone-around-this-unesco-world-heritage-site\">https://www.kjzz.org/tribal-natural-resources/2026-04-07/trump-proposal-could-roll-back-buffer-zone-around-this-unesco-world-heritage-site</a>; "
        "KSUT Public Radio, \"Trump proposal could roll back buffer zone around Chaco,\" April 8, 2026. <a href=\"https://www.ksut.org/news/2026-04-08/trump-proposal-could-roll-back-buffer-zone-around-chaco\">https://www.ksut.org/news/2026-04-08/trump-proposal-could-roll-back-buffer-zone-around-chaco</a>; "
        "High Country News, \"The public got one week to comment on Chaco Canyon drilling. It's almost over.\" <a href=\"https://www.hcn.org/articles/the-public-got-one-week-to-comment-on-chaco-canyon-drilling-its-almost-over/\">https://www.hcn.org/articles/the-public-got-one-week-to-comment-on-chaco-canyon-drilling-its-almost-over/</a>; "
        "Santa Fe New Mexican, \"Trump administration clearing the way for drilling around Chaco Canyon, N.M. Democrats say.\" <a href=\"https://www.santafenewmexican.com/news/local_news/trump-administration-clearing-the-way-for-drilling-around-chaco-canyon-n-m-democrats-say/article_207344ef-8455-40f9-959e-7828f0bcd7f0.html\">https://www.santafenewmexican.com/news/local_news/trump-administration-clearing-the-way-for-drilling-around-chaco-canyon-n-m-democrats-say/article_207344ef-8455-40f9-959e-7828f0bcd7f0.html</a>; "
        "Deseret News, \"Is the BLM opening up lands near Chaco Canyon for mining?\" April 11, 2026. <a href=\"https://www.deseret.com/environment/2026/04/11/land-near-chaco-canyon-new-mexico-lose-protections-open-mining-blm/\">https://www.deseret.com/environment/2026/04/11/land-near-chaco-canyon-new-mexico-lose-protections-open-mining-blm/</a><br>"
        "Related tracker entries: eo-14154 (EO 14154 Unleashing American Energy, 2025-01-20); so-3418 (Secretary's Order 3418 Unleashing American Energy, 2025-02-03); so-3403-co-stewardship (Joint Secretary's Order 3403 on Trust Responsibility); v2025-doi-003 (BLM Proposed Rescission of Public Lands Rule, 2025-09-10); coal-leasing-13m-acres (13.1M acres opened to coal mining, 2025-09-01); agency-action-nps-monument-designation-review-2026 (DOI monument designation review, 2026-03-28); v2026-indigenous-cultural-threat-analysis (Indigenous aggregate analysis); intl-undrip-implementation (UNDRIP Free, Prior and Informed Consent); intl-unesco-withdrawal-rejoined (U.S. UNESCO posture)."
    ),
    "I": {
        "indigenous": {
            "people": "All 19 Pueblos of New Mexico (Acoma, Cochiti, Isleta, Jemez, Laguna, Nambe, Ohkay Owingeh, Picuris, Pojoaque, Sandia, San Felipe, San Ildefonso, Santa Ana, Santa Clara, Santo Domingo, Taos, Tesuque, Zia, Zuni), the Navajo Nation, the Hopi Tribe, and other Tribal Nations of the Southwest hold ancestral and ceremonial relationships to the Chaco landscape. The proposal threatens those relationships through drilling-pad construction, ceremonial-road severance, and air-quality degradation. The 7-day comment window during religious holidays compounds the procedural harm by foreclosing meaningful consultation.",
            "places": "The 336,404.42-acre buffer surrounding Chaco Culture National Historical Park is the cultural landscape contiguous to the UNESCO World Heritage core. The buffer contains ceremonial roads, alignments, outlier Great Houses, viewsheds, and named landscape features whose integrity is part of the park's Outstanding Universal Value as recognized by UNESCO. Drilling-pad construction, road construction, pipeline installation, and induced ground disturbance would compromise place-based cultural-resource integrity that cannot be restored on a Chacoan-civilization timescale.",
            "practices": "Pilgrimage, ceremonial road traversal, and ritual observance practices of the Pueblos and Diné that depend on the integrity of the surrounding landscape are threatened by industrial development of the buffer. Diné communities living within the affected airshed face cumulative-impact harms to traditional land-based practices. Tribal historic-preservation and archaeological-survey practices, conducted under tribal historic preservation officer (THPO) authority, are foreclosed when industrial development outpaces survey.",
            "treasures": "The buffer holds an estimated thousands of archaeological sites, many unsurveyed. These constitute Treasures of the Chacoan world. Their exposure to extraction-related disturbance threatens irreplaceable material culture, ancestral remains, sacred objects, and inscribed and aligned features."
        },
        "latine": {
            "people": "Hispano communities in the Greater Chaco region of northwestern New Mexico share airshed and watershed with the affected lands and have historic and cultural ties to the landscape that intersect with Pueblo and Diné cultural geography.",
            "places": "Hispano land-grant communities and rural Hispano communities in San Juan, Sandoval, and McKinley counties face shared environmental-justice harms from intensified extraction.",
            "practices": "Hispano land-stewardship and cultural-tourism practices in the Greater Chaco region are threatened by intensified extraction.",
            "treasures": "Hispano cultural-historical sites in the Greater Chaco region share landscape integrity with the Pueblo and Diné cultural-heritage record."
        },
        "allCommunities": {
            "people": "U.S. national-park-system stakeholders, descendants of the Chacoan civilization globally, archaeologists, art historians, and members of the broader public lose access to and integrity of one of the most significant cultural-heritage sites in North America.",
            "places": "The U.S. national park system loses the integrity of a UNESCO World Heritage Site cultural landscape.",
            "practices": "U.S. cultural-heritage stewardship practice, articulated under the National Historic Preservation Act and federal Indian trust responsibilities, is undermined.",
            "treasures": "Chaco Culture is part of the inheritance of all peoples. Its degradation diminishes a cultural treasure of the Americas."
        }
    },
    "c": ["Indigenous", "Latiné", "All Communities", "environmentalJustice"],
    "U": "https://www.federalregister.gov/documents/2023/06/07/2023-12158/public-land-order-no-7923-for-public-lands-withdrawal-surrounding-chaco-culture-national-historical",
    "_source": "manual",
}


def main():
    if not DATA_PATH.exists():
        raise SystemExit(f"data.json not found at {DATA_PATH}")

    em_dash = "—"
    if em_dash in json.dumps(ENTRY, ensure_ascii=False):
        raise SystemExit("ABORT: em-dash detected in entry.")

    shutil.copy2(DATA_PATH, BACKUP_PATH)
    print(f"Backup written: {BACKUP_PATH.name}")

    with DATA_PATH.open() as f:
        data = json.load(f)

    agency = data.get("agency_actions", [])
    if any((e.get("id") or e.get("i")) == NEW_ID for e in agency):
        raise SystemExit(f"Entry {NEW_ID} already exists. Aborting.")

    agency.append(ENTRY)
    data["agency_actions"] = agency

    if "meta" in data and isinstance(data["meta"], dict):
        data["meta"]["lastUpdated"] = datetime.now().strftime("%Y-%m-%d")

    tmp = DATA_PATH.with_suffix(".json.tmp")
    with tmp.open("w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    tmp.replace(DATA_PATH)

    print(f"Inserted {NEW_ID} into agency_actions. Total agency_actions: {len(agency)}.")


if __name__ == "__main__":
    main()
