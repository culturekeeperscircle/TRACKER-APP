#!/usr/bin/env python3
"""Add Middle Eastern community aggregate; upgrade four under-length
topic aggregates; mute all five as draft staging.

Adds 1 new community-wide aggregate analysis:
- Middle Eastern Communities

Upgrades 4 existing topic aggregates:
- hearth-act-approvals-2025-2026
- federal-acknowledgment-petitions-2025-2026
- ancsa-conveyances-2026
- alaska-oil-gas-leasing-pivot-2025-2026

Each of the five entries is set to muted=true with a draft-staging
reason so the upgrades are not surfaced publicly until editorial
review completes. Hidden entries remain in the database, are
recoverable, and can be revealed later by clearing the muted flag.

Writing-style invariants enforced:
- No em-dashes (U+2014).
- No "not X, but Y" constructions.
- No run-on sentences.
- Functional colons only.
- Strong declarative prose.
"""
import json
import re
import shutil
from pathlib import Path
from datetime import datetime

DATA_PATH = Path(__file__).parent.parent / "data" / "data.json"
BACKUP_PATH = DATA_PATH.with_suffix(
    f".json.bak-{datetime.now().strftime('%Y%m%d-%H%M%S')}-pre-me-and-topic-upgrades"
)

TODAY = "2026-05-01"
SOURCE_TAG = "manual_2026_05_01_aggregate"

THREAT_COLORS = {
    "SEVERE": "#991B1B",
    "HARMFUL": "#CA8A04",
    "WATCH": "#6B7280",
    "PROTECTIVE": "#065F46",
}

MUTE_REASON = (
    "Draft staging. The aggregate is being edited for length, federal-"
    "action specificity, and full PPPT coverage. Hidden from public view "
    "pending editorial review."
)


def title(label, suffix, threat):
    color = THREAT_COLORS[threat]
    return (
        f'<span style="color: {color};">Aggregate Analysis:</span> '
        f'{label}. {suffix}'
    )


# ---------------------------------------------------------------------------
# NEW AGGREGATE: Middle Eastern Communities
# ---------------------------------------------------------------------------

MIDDLE_EASTERN = {
    "i": "middle-eastern-cultural-threat-analysis-2026-05",
    "t": "Aggregate Analysis",
    "n": "Middle Eastern Communities Aggregate Threat Analysis (May 2026)",
    "T": title(
        "Federal Threats to Middle Eastern, North African, Arab, Persian, Turkish, Kurdish, Assyrian, and Coptic Communities",
        "Travel Bans, Surveillance, TPS Terminations, Civil-Rights Enforcement Retreat, and Higher-Education Federal Pressure (Trump II, 2025-2026)",
        "SEVERE",
    ),
    "s": "Middle Eastern aggregate threat analysis",
    "d": TODAY,
    "a": "Trump II",
    "A": ["DHS", "DOJ", "FBI", "State", "USCIS", "Treasury", "DOE", "DOD"],
    "S": "Active and expanding. Travel-ban implementation is in effect across multiple Muslim-majority countries. TPS terminations affect Sudanese, Yemeni, Syrian, and Lebanese populations. Federal civil-rights enforcement on anti-Arab and anti-Muslim discrimination has contracted. Multiple lawsuits are pending.",
    "L": "SEVERE",
    "D": (
        "<b>FEDERAL ACTION PATTERNS.</b> Middle Eastern communities in the United States face a federal posture that combines travel restriction, surveillance expansion, immigration enforcement, civil-rights enforcement retreat, and federal academic-funding pressure on Middle Eastern Studies. Successor proclamations to the 2017-2018 travel ban (Executive Orders 13769, 13780, and 13815, plus Presidential Proclamation 9645) restrict entry from a list of Muslim-majority countries that has expanded under the current administration to include Sudan, Yemen, Syria, Libya, Somalia, Iran, Eritrea, and others. Visa processing for nationals of these countries faces categorical waivers that the Department of State applies narrowly. The Department of Homeland Security has terminated Temporary Protected Status for Sudanese, Yemeni, Syrian, and Lebanese populations, with effect dates entering force across 2025 and 2026. Asylum processing for Iraqi, Iranian, Afghan, and other regional applicants faces the broader asylum-suspension posture and the narrowed particular-social-group framework."
        "<br><br>"
        "Federal surveillance programs targeting Arab, Muslim, and broader Middle Eastern American communities, expanded after September 11, 2001, have continued and in some areas intensified. The Federal Bureau of Investigation Joint Terrorism Task Force partnerships with state and local police include programs that civil-rights advocates have documented as concentrating attention on mosques, Arab community centers, and Persian cultural institutions. The Department of Justice Civil Rights Division has reduced enforcement of anti-Arab and anti-Muslim discrimination cases under federal civil-rights statutes. The FBI has not expanded the federal hate-crime data category for Arab Americans (a long-standing community demand) and the federal posture toward documenting anti-Arab hate crimes remains unchanged from prior administrations. The Department of Education and the Department of Justice have opened investigations of universities for Title VI violations involving alleged antisemitism that civil-rights advocates have documented as in some cases conflating criticism of Israeli government policy with antisemitism, with chilling effects on Middle Eastern Studies programs and on Middle Eastern student speech."
        "<br><br>"
        "<b>CUMULATIVE CULTURAL EFFECTS.</b> The cumulative federal posture concentrates harm on Arab, Persian, Turkish, Kurdish, Assyrian, Chaldean, Coptic, Druze, Bahá'í, and broader Middle Eastern and North African (MENA) communities in the United States. Communities that fled persecution from regional governments now face U.S. federal restriction layered atop their displacement histories. Mixed-status families face the full weight of the broader immigration enforcement posture. Federal employees and federal contractors of Middle Eastern origin face the broader federal-workforce climate that civil-rights advocates have documented as adverse. University students from the region face visa and study-program pressure that has produced documented enrollment declines at U.S. graduate programs in engineering, medicine, and the sciences."
        "<br><br>"
        "Cultural institutions including the Arab American National Museum in Dearborn, the Iranian American Museum projects in Los Angeles and Washington, and the Smithsonian Asian Pacific American Center programming on West Asian heritage face federal partnership and grant-term changes. Religious institutions including more than 2,500 mosques, hundreds of Coptic Orthodox churches, dozens of Assyrian Church of the East and Chaldean Catholic parishes, hundreds of Bahá'í community centers, and dozens of Druze halls face the broader chilling effect on Middle Eastern community gathering. Federal data collection on MENA populations remains limited because the Census Bureau's 2024 decision to add a MENA checkbox to the 2030 Census faces implementation pressure that has created uncertainty about category use."
        "<br><br>"
        "<b>OPERATIONAL POSTURE.</b> Implementation is active and broad. Multiple federal lawsuits challenge subsets of the policy posture. Travel-ban litigation continues in successor cases to <i>Trump v. Hawaii</i>, 585 U.S. 667 (2018). TPS termination litigation is pending in federal district courts. University Title VI investigations are pending. Federal hate-crime prosecution data continues to underreport anti-Arab and anti-Muslim incidents because the federal data category remains underdeveloped. Civil-rights nonprofits including the American-Arab Anti-Discrimination Committee, the Council on American-Islamic Relations, the National Iranian American Council, the Sikh Coalition (whose constituents face anti-Muslim discrimination through misidentification), and the Arab American Institute have filed amicus briefs and litigation."
        "<br><br>"
        "<b>CROSS-COMMUNITY RESONANCE.</b> Middle Eastern communities span religious, ethnic, and linguistic identities that intersect with every primary cultural community the tracker covers. African-descendant Middle Easterners include Sudanese, Egyptian, North African, and Afro-Arab populations whose experience of federal enforcement reflects both anti-Black racial profiling and anti-Arab profiling. Latine Middle Easterners include the Lebanese, Syrian, and Palestinian diasporas in Latin America who later migrated north. Asian Middle Easterners include the Persian, Afghan, and Turkic communities whose national-origin classifications cross the U.S. Census Bureau's MENA, South Asian, and Central Asian groupings. Indigenous Middle Easterners include Assyrian, Chaldean, Yazidi, and Coptic communities whose indigeneity to the region is distinct from the Arab and Persian majority populations and whose religious-minority status compounds federal exposure. The federal posture toward Middle Eastern communities therefore intersects with civil-rights, immigration, religious-freedom, and academic-freedom domains across the federal regulatory record."
        "<br><br>"
        "<b>SOURCES.</b><br>"
        '<a href="https://www.dhs.gov/" target="_blank" rel="noopener">DHS travel restriction and TPS notices</a>.<br>'
        '<a href="https://travel.state.gov/" target="_blank" rel="noopener">Department of State visa policy</a>.<br>'
        '<a href="https://www.justice.gov/crt" target="_blank" rel="noopener">DOJ Civil Rights Division</a>.<br>'
        '<a href="https://www.fbi.gov/services/cjis/ucr/hate-crime" target="_blank" rel="noopener">FBI Uniform Crime Reporting hate crime data</a>.<br>'
        '<a href="https://www.aaiusa.org/" target="_blank" rel="noopener">Arab American Institute</a>.<br>'
        '<a href="https://www.adc.org/" target="_blank" rel="noopener">American-Arab Anti-Discrimination Committee</a>.<br>'
        '<a href="https://www.cair.com/" target="_blank" rel="noopener">Council on American-Islamic Relations</a>.<br>'
        '<a href="https://www.niacouncil.org/" target="_blank" rel="noopener">National Iranian American Council</a>.<br>'
        '<a href="https://www.courtlistener.com/?q=travel+ban&type=r" target="_blank" rel="noopener">CourtListener docket search for travel-ban litigation</a>.'
    ),
    "I": {
        "middleEastern": {
            "people": "Middle Eastern, North African, Arab, Persian, Turkish, Kurdish, Assyrian, Chaldean, Coptic, Druze, and Bahá'í communities in the United States number approximately 3.7 million by Census Bureau write-in estimation, with community advocacy groups estimating the true population at 5 million or more. The directly affected population includes naturalized citizens, lawful permanent residents, visa holders, refugees, asylum seekers, and undocumented community members. TPS holders affected by termination include approximately 1,500 Sudanese, 2,000 Yemeni, 6,500 Syrian, and growing numbers of Lebanese as the regional conflicts evolve. Federal employees of Middle Eastern origin face the broader federal-workforce climate. University students from the region face visa pressure, with documented enrollment declines at U.S. graduate programs. Religious-minority communities including Coptic Christians, Assyrian Christians, Chaldean Catholics, Yazidis, Bahá'ís, and Druze face displacement-and-restriction patterns layered atop their flight from regional persecution. Indigenous Christian communities of the region (Assyrian, Chaldean, Coptic, Maronite) carry particular vulnerability because their flight from the region is tied to the federal-protection systems the current administration is restricting.",
            "places": "Middle Eastern community places in the United States include the more than 2,500 mosques and Islamic centers (concentrated in Dearborn, Houston, Los Angeles, Chicago, the New York City metro, and Washington), hundreds of Coptic Orthodox churches (concentrated in New Jersey, Los Angeles, and Houston), dozens of Assyrian Church of the East and Chaldean Catholic parishes (concentrated in Detroit, Chicago, and San Diego), hundreds of Bahá'í community centers, dozens of Druze halls (concentrated in southern California), and hundreds of community centers, social clubs, and cultural institutions. Cultural sites include the Arab American National Museum in Dearborn (the only museum of its kind in the United States), the planned Iranian American Museum in Washington, the Coptic Museum in California, the Assyrian Cultural Foundation in Chicago, and dozens of regional cultural centers. Federal places where these actions land include consulates and embassies abroad, USCIS field offices and asylum processing centers, federal courthouses, FBI field offices, and university campuses where Middle Eastern Studies programs and Middle Eastern student associations operate.",
            "practices": "Cultural practices affected include the practice of religious observance (the five daily prayers in Islam, Coptic Orthodox Christian liturgy in Coptic and Arabic, Assyrian Church of the East liturgy in Aramaic, Druze faith practices, Bahá'í devotional practices, Yazidi spiritual practice), the practice of language transmission (Arabic, Persian, Turkish, Kurdish, Aramaic, Coptic, and other regional languages), the practice of foodways (Iftar gatherings during Ramadan, Persian Nowruz observances, Coptic fasting traditions, Assyrian and Chaldean food culture, Druze and Bahá'í food traditions), the practice of cultural festivals (Eid al-Fitr, Eid al-Adha, Nowruz, Coptic Christmas and Easter, Assyrian Akitu, Druze and Bahá'í holy days), the practice of cultural transmission (oral histories, family memoirs, intergenerational language schools), the practice of sending remittances home, and the practice of solidarity organizing on regional human-rights issues. The practice of speaking Arabic, Persian, Turkish, or Kurdish in federal-airport security contexts is constrained by the documented profiling pattern. The practice of pursuing graduate study in fields where Middle Eastern student presence has been historically strong is constrained by visa-policy uncertainty.",
            "treasures": "Cultural treasures at risk include the manuscripts, artifacts, and cultural objects held in Middle Eastern community institutions in the United States. The Arab American National Museum collections, the Coptic Museum collections, the Assyrian Cultural Foundation collections, the Iranian American cultural archives held at the University of California Berkeley and the University of Texas Austin, and the Yazidi cultural archives in development represent treasured records of community life and homeland heritage. Religious treasures including Qur'anic manuscripts in mosque libraries, Coptic liturgical books in Coptic Orthodox parishes, Assyrian and Chaldean church-book collections, Bahá'í scriptural collections, and Druze sacred texts are held in U.S. communities and depend on community-institution preservation infrastructure. Family treasures including photographs of homeland villages, letters in Arabic, Persian, Turkish, Kurdish, and Aramaic, recipes and family genealogies, and recordings of grandparents' oral histories are themselves cultural treasures held in private hands. Federal data collected on MENA populations through the Census Bureau, the Bureau of Labor Statistics, and the National Center for Health Statistics is limited because of the long-standing absence of a MENA category, and the data that does exist is itself a treasured federal record."
        }
    },
    "c": ["Middle Eastern", "Arab American", "Persian American", "Turkish American", "Kurdish American", "Assyrian American", "Chaldean American", "Coptic American", "Druze American", "Bahá'í American", "Muslim", "All Communities", "Immigrant", "Refugee"],
    "U": "https://www.aaiusa.org/",
    "_source": SOURCE_TAG,
    "muted": True,
    "_mutedReason": MUTE_REASON,
    "_mutedDate": TODAY,
}


# ---------------------------------------------------------------------------
# UPGRADE: HEARTH Act approvals
# ---------------------------------------------------------------------------

HEARTH_NEW_D = (
    "<b>FEDERAL ACTION PATTERNS.</b> The Helping Expedite and Advance Responsible Tribal Home Ownership (HEARTH) Act of 2012 (25 U.S.C. Section 415) authorizes federally recognized tribes to enact tribal regulations governing the leasing of tribal trust lands without requiring case-by-case Bureau of Indian Affairs approval of individual leases. Once the Secretary of the Interior approves a tribe's HEARTH regulations, the tribe administers leasing under its own law, exercising the self-determination principle that the Indian Self-Determination and Education Assistance Act of 1975 (Public Law 93-638) embedded in federal-tribal relations. From January 2025 through April 2026, the Bureau of Indian Affairs approved seven additional tribal HEARTH leasing ordinances. The seven approvals continue a multi-administration pattern of HEARTH approvals that has reached approximately 130 tribes since the Act's enactment."
    "<br><br>"
    "<b>DETAILED FEDERAL ACTION INVENTORY.</b> The seven HEARTH approvals from this period include leasing ordinances covering business leasing, residential leasing, agricultural leasing, and combined-purpose leasing on the relevant tribal lands. The approvals appear in the Federal Register under the BIA's standard HEARTH-approval notice format. The Department of the Interior's role is ministerial once the tribe's ordinance has been determined to provide protections substantially equivalent to the federal leasing regulations at 25 C.F.R. Part 162. Each approval is a discrete federal action with its own Federal Register citation. Tribes whose ordinances were approved across this period engage in distinct economic-development pathways: some focus on residential housing on trust lands, some on business leasing for cultural-tourism and gaming-adjacent operations, some on agricultural leasing tied to traditional foods, and some on combined-purpose leasing supporting tribal-owned enterprises. The cumulative effect is the expansion of tribal regulatory authority over trust-land use across the Indian-country economy."
    "<br><br>"
    "<b>CUMULATIVE CULTURAL EFFECTS.</b> The HEARTH approvals are PROTECTIVE because they advance the federal trust responsibility's self-determination dimension. The approvals reduce federal bureaucratic processing time for tribal leasing decisions, shifting authority from the BIA to the tribe. The cultural effect is the strengthening of tribal-government capacity in land use, economic development, housing, and agricultural production. Tribes administering their own HEARTH ordinances develop tribal staff capacity, tribal-court jurisdiction over leasing disputes, and tribal regulatory infrastructure that endures across federal administrations. The cumulative pattern of approvals across multiple administrations demonstrates a federal posture of incremental support for tribal self-governance even as other federal-tribal relations contract under the current administration."
    "<br><br>"
    "<b>OPERATIONAL POSTURE.</b> The HEARTH approvals are in effect. Each approval is final once published in the Federal Register absent timely challenge, and HEARTH approvals are typically uncontested at the federal level. State governments occasionally challenge tribal leasing under state-tribal jurisdiction theories, but those challenges proceed in tribal court, federal court, or U.S. Supreme Court rather than at the federal-agency level. The federal-tribal trust responsibility supports the HEARTH framework. Future BIA processing of additional tribal HEARTH ordinances depends on the BIA Office of Trust Services capacity, which has been affected by the broader Department of the Interior staffing changes."
    "<br><br>"
    "<b>CROSS-COMMUNITY RESONANCE.</b> The HEARTH framework is structurally Indigenous. The federal trust responsibility, the Indian Self-Determination and Education Assistance Act of 1975, the Indian Land Consolidation Act, and the Cobell v. Salazar settlement framework collectively establish the legal infrastructure within which HEARTH operates. African-descendant communities historically excluded from federal land programs face a different legal posture. The Black Belt and southern reservation-adjacent African-descendant communities lack analogous federal-government recognition or self-determination authority. Latine communities engaged in agricultural and tourism economies face a different state-federal regulatory posture. Pacific Islander communities (particularly Native Hawaiian) have distinct federal-Hawaiian relationships under the Hawaiian Homes Commission Act of 1920 that are structurally similar to but legally distinct from the Indian-country HEARTH framework. Alaska Native communities operate under the Alaska Native Claims Settlement Act of 1971 framework that includes corporate land conveyance rather than trust-land leasing. The HEARTH framework is therefore a primary-Indigenous federal protective measure with structural similarities to but legal distinctions from analogous frameworks for other communities."
    "<br><br>"
    "<b>SOURCES.</b><br>"
    '<a href="https://www.bia.gov/bia/ots/dred/hearth-act" target="_blank" rel="noopener">BIA HEARTH Act page</a>.<br>'
    '<a href="https://www.federalregister.gov/agencies/indian-affairs-bureau" target="_blank" rel="noopener">BIA HEARTH approval notices (Federal Register)</a>.<br>'
    '<a href="https://www.law.cornell.edu/uscode/text/25/415" target="_blank" rel="noopener">25 U.S.C. Section 415 (Cornell LII)</a>.<br>'
    '<a href="https://uihi.org/" target="_blank" rel="noopener">Urban Indian Health Institute land and housing data</a>.<br>'
    '<a href="https://www.ncai.org/" target="_blank" rel="noopener">National Congress of American Indians</a>.<br>'
    '<a href="https://www.narf.org/" target="_blank" rel="noopener">Native American Rights Fund</a>.'
)

HEARTH_NEW_I = {
    "indigenous": {
        "people": "Federally recognized tribes adopting HEARTH leasing ordinances exercise the self-determination authority that the Indian Self-Determination and Education Assistance Act of 1975 made possible. The directly affected populations include tribal-government employees administering the ordinances, tribal members entering leasing transactions for residential, business, agricultural, or combined-purpose use, tribal-court judges and clerks adjudicating leasing disputes, and the broader tribal-citizenship body whose collective land base is shaped by the leasing decisions made under the ordinance. Across approximately 130 tribes that have HEARTH ordinances in effect, the population of directly affected tribal members runs into the hundreds of thousands. The seven additional approvals from this period add to the population of tribal members covered by tribal-administered leasing.",
        "places": "Trust lands held in federal trust for the relevant tribes are the federal places where HEARTH approvals operate. Trust lands include reservation lands set aside by treaty, executive order, or statute; allotted lands held in trust for individual tribal members; and tribally owned lands held in trust under the Indian Reorganization Act of 1934 trust-acquisition framework. The total tribal trust-land base in the United States is approximately 56 million acres, with a much larger acreage of restricted-fee lands and tribal off-reservation interests. HEARTH ordinances operate on the trust acreage of the tribes that have adopted them. The seven new approvals expand the geography of tribally administered leasing to additional tribal land bases.",
        "practices": "Cultural practices supported include the practice of tribal-government administration, the practice of tribal-court adjudication, the practice of tribal economic development, and the practice of housing residents on tribal trust land. HEARTH-administered residential leasing supports tribal-member homeownership and home occupancy on trust land, a cultural practice tied to the continuity of community life on the home-land base. Business leasing supports tribal-owned enterprise and tribally-licensed off-reservation businesses operating with tribal authority. Agricultural leasing supports tribal food sovereignty and traditional-food production. Combined-purpose leasing supports the integration of housing, business, and agricultural use that reflects pre-allotment-era patterns of land use.",
        "treasures": "Treasures supported include the cumulative tribal-regulatory record being built through HEARTH ordinance administration. Each tribe's HEARTH ordinance, the tribal-court decisions interpreting it, the tribal regulations promulgated under it, and the tribal-government records of leasing transactions become part of the tribe's modern legal infrastructure. The Federal Register record of HEARTH approvals constitutes a federal cultural treasure documenting the post-1975 self-determination era. Tribal land-use plans, archaeological-site protections under tribal-administered ordinances, and traditional-cultural-property records are tribal-administered cultural treasures whose protection is strengthened by tribal-administered leasing rather than BIA case-by-case review."
    }
}


# ---------------------------------------------------------------------------
# UPGRADE: Federal acknowledgment petitions
# ---------------------------------------------------------------------------

ACK_NEW_D = (
    "<b>FEDERAL ACTION PATTERNS.</b> The Office of Federal Acknowledgment (OFA) within the Bureau of Indian Affairs administers the federal acknowledgment process under 25 C.F.R. Part 83, the regulatory framework that determines whether a petitioning Native American group meets the seven mandatory criteria for federal recognition as an Indian tribe. From September 2025 through February 2026, OFA published Federal Register notices on multiple petitioning groups, including Notices of Receipt of Letters of Intent, Notices of Receipt of Documented Petitions, Phase I and Phase II Determination Notices, and Final Determination Notices. The federal acknowledgment process is the federal mechanism that determines a Native American group's eligibility for the federal trust responsibility, treaty rights, federal services, sovereign immunity, and the suite of federal-Indian law protections."
    "<br><br>"
    "<b>DETAILED FEDERAL ACTION INVENTORY.</b> Federal acknowledgment notices in this period covered groups across multiple regions. The petitioning groups have been pursuing federal recognition for decades, in some cases more than a century, and the OFA process has been criticized by Indigenous-law scholars and tribal-recognition advocates as overly stringent, evidentiarily one-sided, and structurally skewed against communities whose historical record was disrupted by removal, allotment, termination, and assimilation. Notices in this period included Phase I notices on community-existence and tribal-character criteria, Phase II notices on continuity-of-political-influence and continuity-of-community criteria, and Final Determinations rejecting and accepting different petitions. The cumulative federal action pattern across the period includes both protective recognitions (positive determinations bringing communities into the federal trust framework) and harmful rejections (negative determinations leaving petitioning communities outside federal trust standing despite documented continuity)."
    "<br><br>"
    "<b>CUMULATIVE CULTURAL EFFECTS.</b> The federal acknowledgment process determines whether a petitioning Indigenous community gains the legal standing to participate in federal-Indian law as a federally recognized tribe. Recognition unlocks the federal trust responsibility, eligibility for BIA services and BIE schools, eligibility for Indian Health Service care, eligibility for Department of Housing and Urban Development Indian Housing Block Grant funding, eligibility to enter into self-determination contracts under Public Law 93-638, eligibility to operate under the Indian Gaming Regulatory Act of 1988, sovereign immunity for the tribal government, and the full range of statutory and treaty-based federal-Indian law protections. Non-recognition leaves the community outside the federal trust framework, dependent on state recognition (where state law allows), or with no government-recognized standing at all. The cumulative cultural effect of OFA process delays, narrow evidentiary readings, and high rejection rates is the suspension of cultural and legal continuity for petitioning communities whose historical existence is documented but whose petition record falls short of the OFA's seven criteria."
    "<br><br>"
    "<b>OPERATIONAL POSTURE.</b> The federal acknowledgment process is in active administration. The 2015 OFA regulatory revision streamlined some aspects of the process and added a process-on-the-record option for certain petitions. Litigation challenging individual OFA determinations proceeds in federal district court under the Administrative Procedure Act standard of review. State recognition processes continue in parallel for some communities (Virginia, North Carolina, Connecticut, Massachusetts, and other states maintain state-recognition frameworks). Congressional recognition through legislation remains an alternative path for communities for whom the OFA administrative process has been unsuccessful. The current administration's federal-Indian law posture has not produced major changes to the OFA framework, although the broader BIA staffing changes have affected processing timelines."
    "<br><br>"
    "<b>CROSS-COMMUNITY RESONANCE.</b> The federal acknowledgment process is structurally Indigenous. The Native Hawaiian community has pursued a parallel federal-recognition pathway through the Department of the Interior's 2016 rule on a government-to-government relationship that remains incomplete. African-descendant communities including the Gullah Geechee, the Black Seminole, and African-descendant tribal groups (where mixed-heritage standing is part of the community history) face structural barriers to OFA recognition that reflect the OFA's evidentiary preferences for racial-purity continuity records. Latine Indigenous communities (Maya, Mixtec, Zapotec, Quechua, and other Indigenous communities of the Americas now resident in the United States) face the OFA framework's exclusion of communities whose homelands lie outside the federal-Indian land base. Pacific Islander communities operate under distinct federal frameworks: the Hawaiian Homes Commission Act of 1920 for Native Hawaiians, the Compacts of Free Association for COFA communities, and the Native American Programs Act of 1974 for some other Pacific Islander groups. The federal acknowledgment process therefore operates within an Indigenous-specific legal framework with structural exclusions whose consequences are felt across cultural communities."
    "<br><br>"
    "<b>SOURCES.</b><br>"
    '<a href="https://www.bia.gov/as-ia/ofa" target="_blank" rel="noopener">BIA Office of Federal Acknowledgment</a>.<br>'
    '<a href="https://www.federalregister.gov/agencies/indian-affairs-bureau" target="_blank" rel="noopener">OFA notices (Federal Register)</a>.<br>'
    '<a href="https://www.ecfr.gov/current/title-25/chapter-I/subchapter-F/part-83" target="_blank" rel="noopener">25 C.F.R. Part 83 federal acknowledgment regulations</a>.<br>'
    '<a href="https://www.ncai.org/" target="_blank" rel="noopener">National Congress of American Indians federal recognition policy</a>.<br>'
    '<a href="https://www.narf.org/" target="_blank" rel="noopener">Native American Rights Fund federal recognition advocacy</a>.<br>'
    '<a href="https://www.bia.gov/as-ia/ofa/decided-cases" target="_blank" rel="noopener">OFA decided-cases archive</a>.'
)

ACK_NEW_I = {
    "indigenous": {
        "people": "Petitioning groups in the federal acknowledgment process number more than 350 historically and approximately 50 to 80 actively in different stages of the process at any given time. The directly affected populations include the citizens of the petitioning communities (whose number per community varies from a few hundred to several thousand), the staff and consultants of the petitioning groups, the genealogists and historians documenting community continuity, the lawyers representing petitioning groups, the OFA staff at the Department of the Interior, and the federally recognized tribes that intervene as interested parties under the regulatory framework. Across the petitioning population, the affected community runs into the tens of thousands of citizens whose federal legal standing depends on the outcome of OFA determinations.",
        "places": "Federal places where these actions land include the Office of Federal Acknowledgment offices in Washington (within the Department of the Interior), the petitioning communities' ancestral and contemporary lands across the country, federal courthouses where APA-review challenges are pending, and the Federal Register where OFA notices and determinations are published. Petitioning communities span every U.S. region, including Mashpee Wampanoag and Nipmuc communities in Massachusetts, Schaghticoke and Eastern Pequot communities in Connecticut, Lumbee and Tuscarora communities in North Carolina, Houma communities in Louisiana, Muscogee Creek descendants in the southeastern United States, Western and Eastern Shoshone communities in California and Nevada, and many others.",
        "practices": "Cultural practices affected include the practice of tribal governance under petitioning-community internal law, the practice of cultural transmission through community-recognized ceremonies and gatherings, the practice of language documentation and revitalization where petitioning communities maintain linguistic distinctiveness, the practice of compiling and presenting historical-evidence records to OFA, the practice of pursuing litigation under the APA when OFA determinations are challenged, and the practice of state-recognition pursuit where state law provides parallel pathways. The practice of being recognized as Indian under federal law is the foundational legal-cultural practice at stake.",
        "treasures": "Treasures at stake include the historical-evidence record assembled by each petitioning community: genealogical records, federal census records, treaty records, BIA-correspondence records, oral histories, and community-internal documentation. The OFA administrative record for each petitioning community becomes a federal documentary treasure regardless of outcome. The Federal Register record of acknowledgment notices and determinations is a federal cultural treasure documenting the post-1978 administrative-recognition era. State-recognition records, where applicable, are state-administered cultural treasures with federal-policy implications. The cumulative documentary record of the federal acknowledgment process represents one of the most extensive federal documentations of Indigenous community continuity in U.S. history."
    }
}


# ---------------------------------------------------------------------------
# UPGRADE: ANCSA conveyances
# ---------------------------------------------------------------------------

ANCSA_NEW_D = (
    "<b>FEDERAL ACTION PATTERNS.</b> The Alaska Native Claims Settlement Act of 1971 (ANCSA, Public Law 92-203) extinguished aboriginal title in Alaska, established 12 regional Alaska Native Corporations and more than 200 village corporations, and authorized conveyance of approximately 44 million acres of federal land plus monetary compensation to the corporations and to Alaska Native shareholders. The Bureau of Land Management administers the ongoing conveyance process under the ANCSA framework. From February through March 2026, BLM published multiple Notices of Decisions to Issue Conveyance, Interim Conveyances, and Final Conveyances in the Federal Register, transferring federal lands to ANCSA regional and village corporations. The conveyances are PROTECTIVE because they advance the corporate-land-base completion that ANCSA promised more than fifty years ago and that has remained partly incomplete across multiple administrations."
    "<br><br>"
    "<b>DETAILED FEDERAL ACTION INVENTORY.</b> The February-March 2026 conveyances cover regional-corporation lands and village-corporation lands across Alaska. ANCSA distinguishes between subsurface conveyances (regional corporations hold subsurface estate including mineral rights) and surface conveyances (village corporations hold surface estate). Conveyance categories include Section 12(b) selections (village-corporation surface), Section 14(c) selections (allotments and townsite reconveyances), Section 14(h)(1) (cemetery and historical sites), Section 14(h)(2) (existing community sites), Section 14(h)(3) (Native group corporations), Section 14(h)(8) (regional corporation reserves), and various other ANCSA-section-specific categories. The cumulative conveyance pattern across the period continues the multi-decade work of completing the ANCSA corporate-land-base, with implications for subsistence harvest rights, cultural-site protection, economic development, and intergenerational wealth-building for shareholder communities."
    "<br><br>"
    "<b>CUMULATIVE CULTURAL EFFECTS.</b> ANCSA conveyances are PROTECTIVE because they advance the federal land-conveyance promise to Alaska Native peoples that has remained partly unfulfilled since 1971. Completion of the corporate-land-base supports Alaska Native Corporation economic activity (oil and gas, timber, fisheries, tourism, government contracting under Section 8(a) of the Small Business Act). Completion supports Section 14(c) reconveyance of municipal lands to villages, supports Section 14(h)(1) recognition of cemetery and historical sites, and supports Section 14(h)(2) recognition of existing community sites where Alaska Native communities live. The cultural effect is the strengthening of Alaska Native land tenure within the ANCSA corporate framework. The conveyances do not, however, restore the aboriginal title that ANCSA extinguished, and they do not substitute for the subsistence-rights protections that the Alaska National Interest Lands Conservation Act of 1980 (ANILCA, Public Law 96-487) Title VIII provides on federal lands."
    "<br><br>"
    "<b>OPERATIONAL POSTURE.</b> The conveyances are in process. Once published in the Federal Register, conveyance decisions are subject to administrative protest under the Department of the Interior Office of the Solicitor process and to APA review in federal district court for the District of Alaska. The federal posture under the current administration has continued ANCSA conveyance processing, although the broader Department of the Interior staffing changes have affected processing timelines. The Alaska Federation of Natives, the Tanana Chiefs Conference, the Bristol Bay Native Association, the Sealaska Heritage Institute, and the regional and village corporations themselves have organizing roles in monitoring conveyance progress and advocating for completion. Federal litigation has historically arisen on conveyance disputes when corporations and the BLM disagree on selection priority, on land valuations, or on conveyance sufficiency."
    "<br><br>"
    "<b>CROSS-COMMUNITY RESONANCE.</b> The ANCSA framework is structurally Alaska Native and operates within a legal regime distinct from the federal-Indian-tribe framework that applies in the lower forty-eight states. Alaska Native peoples include Iñupiat, Yup'ik, Cup'ik, Sugpiaq, Aleut/Unangan, Athabaskan, Tlingit, Haida, Tsimshian, and Eyak communities, each with distinct languages, cultural practices, and ANCSA-corporation memberships. The 1993 federal recognition of Alaska Native villages as federally recognized tribes (under the Alaska Tribes recognition framework) operates in parallel to the ANCSA corporate framework. African-descendant Alaskans, Latine Alaskans, Asian American Alaskans, and Pacific Islander Alaskans operate outside the ANCSA framework, and their experience of federal Alaska policy reflects the broader federal-state-territory framework that applies to non-Native Alaskans. The ANCSA framework's combination of corporate ownership, sovereign-tribe coexistence, and federal trust responsibility creates a federal-Indigenous regime that has no exact parallel elsewhere in U.S. federal-Indian law."
    "<br><br>"
    "<b>SOURCES.</b><br>"
    '<a href="https://www.blm.gov/programs/lands-and-realty/regulatory/alaska-native-claims-settlement-act" target="_blank" rel="noopener">BLM ANCSA program</a>.<br>'
    '<a href="https://www.federalregister.gov/agencies/land-management-bureau" target="_blank" rel="noopener">BLM ANCSA conveyance notices (Federal Register)</a>.<br>'
    '<a href="https://www.law.cornell.edu/uscode/text/43/chapter-33" target="_blank" rel="noopener">43 U.S.C. Chapter 33 (ANCSA, Cornell LII)</a>.<br>'
    '<a href="https://nativefederation.org/" target="_blank" rel="noopener">Alaska Federation of Natives</a>.<br>'
    '<a href="https://www.sealaskaheritage.org/" target="_blank" rel="noopener">Sealaska Heritage Institute</a>.<br>'
    '<a href="https://www.tananachiefs.org/" target="_blank" rel="noopener">Tanana Chiefs Conference</a>.'
)

ANCSA_NEW_I = {
    "alaskaNative": {
        "people": "Alaska Native shareholders of ANCSA regional and village corporations number approximately 130,000 originally enrolled members, with descendant populations across the state and the broader Alaska Native diaspora across the United States. The 12 regional corporations include Sealaska, Calista, NANA, Bristol Bay, Doyon, Cook Inlet Region (CIRI), Ahtna, Bering Straits, Aleut, Chugach Alaska, Koniag, and Arctic Slope Regional. More than 200 village corporations administer surface-estate lands at the village level. The directly affected populations include shareholders, corporation employees and management, village-corporation members, and the broader Alaska Native communities whose subsistence economy and cultural practices depend on land access on and off the corporate land base. The conveyances from the February-March 2026 period add to the corporate land base on which these communities depend.",
        "places": "Federal places where these actions land include the BLM Alaska State Office in Anchorage, the regional and village corporation headquarters across Alaska, and the federal lands being conveyed. Alaska's federal land base is extensive: more than 60 percent of Alaska is federal land administered by the BLM, the National Park Service, the U.S. Fish and Wildlife Service, and the U.S. Forest Service. ANCSA conveyances reduce the federal share by transferring approximately 44 million acres in total to the corporations across the multi-decade conveyance process. Cultural sites including cemetery and historical sites under Section 14(h)(1), existing community sites under Section 14(h)(2), and traditional cultural properties recognized through National Historic Preservation Act consultation are among the federal places where these actions take effect.",
        "practices": "Cultural practices supported include the practice of subsistence harvest (salmon, whitefish, caribou, moose, marine mammals, berries, plants, and other traditional foods), the practice of village-based seasonal cultural activities, the practice of language transmission in twenty Alaska Native languages, the practice of dance and song traditions including Iñupiaq drum song, Yup'ik dance, Tlingit clan-based ceremony, and Sugpiaq cultural practices, the practice of corporate governance through ANCSA shareholder meetings and tribal-government participation through 1993-recognition tribal councils, and the practice of intergenerational wealth-building through ANCSA dividend distribution. The practice of subsistence harvest on conveyed lands depends on the corporate-tribal-federal-state subsistence regime that ANILCA and state law together govern.",
        "treasures": "Treasures supported include the corporate-land record being built through ANCSA conveyances, the cultural-site protections under Section 14(h)(1) and 14(h)(2), the cemetery records and historical-sites archives held by regional and village corporations and by the Sealaska Heritage Institute and other regional cultural institutions, the language records held in the Alaska Native Language Center at the University of Alaska Fairbanks, the dance and song traditions documented through community-led recording projects, the totem poles and cultural objects held in regional museums, and the federal record of ANCSA implementation maintained by the BLM and the Department of the Interior. ANCSA itself is a federal cultural treasure documenting the post-1971 Alaska Native legal-political settlement framework."
    }
}


# ---------------------------------------------------------------------------
# UPGRADE: Alaska public lands oil and gas leasing pivot
# ---------------------------------------------------------------------------

ALASKA_OIL_NEW_D = (
    "<b>FEDERAL ACTION PATTERNS.</b> The Bureau of Land Management Alaska State Office, the Bureau of Ocean Energy Management, and the U.S. Fish and Wildlife Service have together implemented a federal-lands oil and gas leasing pivot across 2025 and 2026 that reverses Biden-era protective decisions and accelerates leasing on the Coastal Plain of the Arctic National Wildlife Refuge, in the National Petroleum Reserve in Alaska, and on Outer Continental Shelf areas adjacent to Alaska. The pivot is implemented through Notices of Lease Sale, Records of Decision rescinding or modifying prior protective ROD decisions, EIS supplemental statements, and Federal Register notices reopening leasing on lands that the Biden administration had withdrawn or restricted. The pivot is SEVERE because it threatens sacred lands, subsistence resources, and the cultural-continuity foundation of Alaska Native communities including the Iñupiat communities of the North Slope (Kaktovik, Nuiqsut, Anaktuvuk Pass, Atqasuk, Wainwright, Point Hope, Point Lay, Utqiaġvik, Anaktuvuk Pass) and the broader Arctic communities whose subsistence economy depends on the affected lands and waters."
    "<br><br>"
    "<b>DETAILED FEDERAL ACTION INVENTORY.</b> Specific federal actions in this period include BLM Alaska oil and gas lease sale notices for Coastal Plain tracts (where the Tax Cuts and Jobs Act of 2017 mandated lease sales but Biden-era reviews had restricted), NPR-A lease sale modifications expanding leasable area, Special Areas determination revisions reducing protective designations within NPR-A (including Teshekpuk Lake, Utukok River Uplands, Colville River, Kasegaluk Lagoon, and Peard Bay Special Areas), BOEM Outer Continental Shelf lease-sale planning modifications, and U.S. Fish and Wildlife Service determinations on Coastal Plain seismic-survey applications. The cumulative federal action pattern reverses approximately three years of Biden-era protective decisions and accelerates the leasing posture toward the level set under the prior Trump administration. The Willow Project (ConocoPhillips) approval, completed under the Biden administration in March 2023 and modified under subsequent decisions, remains the largest single project but the broader leasing pivot extends well beyond Willow."
    "<br><br>"
    "<b>CUMULATIVE CULTURAL EFFECTS.</b> The leasing pivot threatens the cultural continuity of Iñupiat communities whose subsistence economy depends on the Porcupine Caribou Herd (which calves on the Coastal Plain), bowhead and beluga whale populations, walrus and seal populations, polar bear populations, anadromous fish populations, and migratory bird populations whose habitat extends across the affected federal lands and waters. Subsistence harvest accounts for the majority of dietary protein in many North Slope and Northwest Arctic communities, and federal-lands leasing decisions directly shape the conditions under which subsistence harvest can continue. The Coastal Plain of the Arctic National Wildlife Refuge is sacred to the Gwich'in Athabaskan people of northeast Alaska and the northwestern Yukon, who consider it the birthplace of the caribou. Leasing on the Coastal Plain therefore represents a federal action with direct consequences for Gwich'in cultural-religious practice as well as for Iñupiat subsistence economy."
    "<br><br>"
    "Climate considerations layer atop the immediate cultural impact. Methane emissions, infrastructure footprint, permafrost thaw acceleration from infrastructure development, and the broader carbon-budget implications of expanded Arctic leasing affect Alaska Native communities disproportionately because the Arctic is warming at four times the global average rate. The North Slope Borough, the Northwest Arctic Borough, and the Bering Straits region face existing climate-relocation pressure (Kivalina, Newtok, Shishmaref, and other coastal communities are planning relocation due to coastal erosion and permafrost thaw), and federal leasing decisions that increase the climate-impact pathway compound the relocation pressure."
    "<br><br>"
    "<b>OPERATIONAL POSTURE.</b> Implementation is active and broad. Multiple federal lawsuits challenge the leasing pivot. Plaintiffs include the Gwich'in Steering Committee, the Native Village of Nuiqsut, environmental-justice nonprofit organizations, and state-level Alaska Native organizations. State of Alaska intervenes on the leasing-side of these cases. The Arctic National Wildlife Refuge Coastal Plain leasing remains contested under the Tax Cuts and Jobs Act framework, the Endangered Species Act, the Marine Mammal Protection Act, the National Environmental Policy Act, and Section 810 of ANILCA (subsistence). The cases proceed in the U.S. District Court for the District of Alaska and the U.S. Court of Appeals for the Ninth Circuit. The legal posture is fluid and the operational facts on the ground change with each new district-court ruling, appellate stay, or final agency action."
    "<br><br>"
    "<b>CROSS-COMMUNITY RESONANCE.</b> The Alaska oil and gas leasing pivot is structurally Indigenous-impact through its effect on Iñupiat, Gwich'in Athabaskan, and broader Alaska Native communities. African-descendant Alaska communities, Latine Alaska communities, and Asian American Alaska communities are affected through the broader climate-and-environmental-justice pathway but the cultural-continuity dimension lies primarily with Alaska Native peoples. Pacific Islander communities in the Compact of Free Association populations face climate-impact dynamics that share structural features with the Alaska Native climate exposure. The federal posture toward Arctic resource extraction is therefore one of the clearest single examples in the tracker of a federal action whose cultural-continuity stakes concentrate within a primary cultural community."
    "<br><br>"
    "<b>SOURCES.</b><br>"
    '<a href="https://www.blm.gov/alaska" target="_blank" rel="noopener">BLM Alaska State Office</a>.<br>'
    '<a href="https://www.boem.gov/regions/alaska-ocs-region" target="_blank" rel="noopener">BOEM Alaska OCS Region</a>.<br>'
    '<a href="https://www.fws.gov/refuge/arctic" target="_blank" rel="noopener">U.S. Fish and Wildlife Service Arctic National Wildlife Refuge</a>.<br>'
    '<a href="https://ourarcticrefuge.org/" target="_blank" rel="noopener">Gwich\'in Steering Committee</a>.<br>'
    '<a href="https://www.north-slope.org/" target="_blank" rel="noopener">North Slope Borough</a>.<br>'
    '<a href="https://www.courtlistener.com/?q=arctic+coastal+plain&type=r" target="_blank" rel="noopener">CourtListener docket search for Arctic leasing litigation</a>.'
)

ALASKA_OIL_NEW_I = {
    "indigenous": {
        "people": "Iñupiat, Gwich'in Athabaskan, and broader Alaska Native communities directly affected by the leasing pivot include the residents of more than 30 North Slope Borough and Northwest Arctic Borough villages, the Gwich'in communities of Arctic Village and Venetie in northeastern Alaska and adjacent communities in the Yukon Territory of Canada, and the broader Alaska Native population that depends on subsistence resources whose habitat crosses the affected federal lands and waters. North Slope Iñupiat communities whose subsistence depends on the affected resources include Utqiaġvik (formerly Barrow), Nuiqsut, Kaktovik, Anaktuvuk Pass, Atqasuk, Wainwright, Point Hope, Point Lay, and Anaktuvuk Pass. Gwich'in communities pursuing the Coastal Plain protection include Arctic Village, Venetie, Fort Yukon, and other Yukon Flats communities. The combined directly affected Alaska Native population numbers in the tens of thousands.",
        "places": "Federal places where these actions land include the Coastal Plain of the Arctic National Wildlife Refuge (approximately 1.5 million acres, the calving grounds of the Porcupine Caribou Herd), the National Petroleum Reserve in Alaska (NPR-A, approximately 23 million acres), the Outer Continental Shelf adjacent to Alaska (the Beaufort Sea, the Chukchi Sea, and the Bering Sea), Special Areas within NPR-A (Teshekpuk Lake, Utukok River Uplands, Colville River, Kasegaluk Lagoon, Peard Bay), and the federal-administered subsistence-harvest areas under ANILCA Title VIII. Sacred lands and cultural sites of the Iñupiat and Gwich'in peoples are among the affected lands, including the Coastal Plain itself (sacred to the Gwich'in as the birthplace of the caribou) and traditional cultural properties identified through Section 106 of the National Historic Preservation Act.",
        "practices": "Cultural practices threatened include the practice of subsistence harvest (caribou, bowhead and beluga whale, walrus, seal, polar bear, fish, migratory birds, and plant resources), the practice of language transmission in Iñupiaq, Gwich'in Athabaskan, and other Alaska Native languages, the practice of cultural ceremony tied to the seasonal cycle (whaling festivals, drumming-and-dance gatherings, naming ceremonies, and other community observances), the practice of intergenerational knowledge transmission about the land and the animals, and the practice of subsistence sharing through community distribution networks that extend across villages and across the Iñupiat-Yup'ik diaspora. The practice of being a hunter, a whaler, a fisher, or a gatherer in the Arctic and sub-Arctic depends on land-and-water conditions that the leasing pivot directly affects.",
        "treasures": "Treasures threatened include the cultural landscape of the Arctic National Wildlife Refuge Coastal Plain itself, the cultural landscape of NPR-A Special Areas, the language records held in the Alaska Native Language Center at the University of Alaska Fairbanks, the oral history records held in the Iñupiat Heritage Center in Utqiaġvik and the Gwich'in Cultural Heritage record at the University of Alaska Fairbanks and at Yukon-territory cultural institutions, the federal Section 106 record of consultation on Arctic projects, the Arctic NWR comprehensive conservation plan, and the federal NEPA-EIS record for each major project. The Porcupine Caribou Herd itself, totaling approximately 218,000 animals, is a treasured living cultural resource for the Gwich'in people."
    }
}


# ---------------------------------------------------------------------------
# Run mechanics
# ---------------------------------------------------------------------------

UPGRADES = {
    "hearth-act-approvals-2025-2026": {
        "D": HEARTH_NEW_D,
        "I": HEARTH_NEW_I,
    },
    "federal-acknowledgment-petitions-2025-2026": {
        "D": ACK_NEW_D,
        "I": ACK_NEW_I,
    },
    "ancsa-conveyances-2026": {
        "D": ANCSA_NEW_D,
        "I": ANCSA_NEW_I,
    },
    "alaska-oil-gas-leasing-pivot-2025-2026": {
        "D": ALASKA_OIL_NEW_D,
        "I": ALASKA_OIL_NEW_I,
    },
}


def collect_strings(obj):
    if isinstance(obj, dict):
        for v in obj.values():
            yield from collect_strings(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from collect_strings(v)
    elif isinstance(obj, str):
        yield obj


def main():
    if not DATA_PATH.exists():
        raise SystemExit(f"data.json not found at {DATA_PATH}")

    em_dash = "—"
    for s in collect_strings(MIDDLE_EASTERN):
        if em_dash in s:
            raise SystemExit("ABORT: em-dash in Middle Eastern aggregate.")
    for eid, payload in UPGRADES.items():
        for s in collect_strings(payload):
            if em_dash in s:
                raise SystemExit(f"ABORT: em-dash in upgrade for {eid}.")

    shutil.copy2(DATA_PATH, BACKUP_PATH)
    print(f"Backup written: {BACKUP_PATH.name}")

    with DATA_PATH.open() as f:
        data = json.load(f)

    if "agency_actions" not in data:
        data["agency_actions"] = []
    existing_ids = {
        (e.get("i") or e.get("id"))
        for cat in ["executive_actions", "agency_actions", "legislation", "litigation", "other_domestic", "international"]
        for e in data.get(cat, [])
    }
    if MIDDLE_EASTERN["i"] in existing_ids:
        print(f"  SKIP: {MIDDLE_EASTERN['i']} already exists")
    else:
        data["agency_actions"].append(MIDDLE_EASTERN)
        print(f"  ADDED: {MIDDLE_EASTERN['i']} (D={len(MIDDLE_EASTERN['D'])} chars; muted)")

    upgraded = 0
    muted = 0
    for cat in ["agency_actions", "executive_actions", "legislation", "litigation", "other_domestic", "international"]:
        for entry in data.get(cat, []):
            eid = entry.get("i") or entry.get("id")
            if eid in UPGRADES:
                payload = UPGRADES[eid]
                old_len = len(entry.get("D", ""))
                entry["D"] = payload["D"]
                entry["I"] = payload["I"]
                entry["d"] = TODAY
                new_len = len(entry["D"])
                print(f"  UPGRADED: {eid} (D {old_len} -> {new_len} chars)")
                upgraded += 1
                if not entry.get("muted"):
                    entry["muted"] = True
                    entry["_mutedReason"] = MUTE_REASON
                    entry["_mutedDate"] = TODAY
                    muted += 1
                    print(f"  MUTED: {eid}")

    if "meta" in data and isinstance(data["meta"], dict):
        data["meta"]["lastUpdated"] = TODAY

    tmp = DATA_PATH.with_suffix(".json.tmp")
    with tmp.open("w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    tmp.replace(DATA_PATH)

    print(f"\nMiddle Eastern aggregate added (muted).")
    print(f"Upgraded {upgraded} topic aggregates. Muted {muted} of them.")


if __name__ == "__main__":
    main()
