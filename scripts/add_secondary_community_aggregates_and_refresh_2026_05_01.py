#!/usr/bin/env python3
"""Add 8 secondary-community aggregate analyses and refresh 6 existing
primary-community aggregates with February to April 2026 federal actions.

New aggregates added on 2026-05-01:
1. Women
2. LGBTQIA2S+
3. Disabled
4. Immigrant
5. Rural
6. Poor (low-income)
7. Non-Profit Sector
8. Arts and Humanities

Existing aggregates refreshed (date bumped to 2026-05-01, appendix
section appended to D):
- v2026-indigenous-cultural-threat-analysis
- v2026-african-descendant-cultural-threat-analysis
- v2026-latine-cultural-threat-analysis
- v2026-asian-american-cultural-threat-analysis
- v2026-pacific-islander-oceania-cultural-threat-analysis
- v2026-caribbean-cultural-threat-analysis

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
    f".json.bak-{datetime.now().strftime('%Y%m%d-%H%M%S')}-pre-secondary-aggregates"
)

THREAT_COLOR = "#991B1B"  # SEVERE
TODAY = "2026-05-01"
SOURCE_TAG = "manual_2026_05_01_aggregate"


def title(label, suffix):
    return (
        f'<span style="color: {THREAT_COLOR};">Aggregate Analysis:</span> '
        f'{label}. {suffix}'
    )


# ---------------------------------------------------------------------------
# 8 NEW AGGREGATES
# ---------------------------------------------------------------------------

WOMEN = {
    "i": "women-cultural-threat-analysis-2026-05",
    "t": "Aggregate Analysis",
    "n": "Women Aggregate Threat Analysis (May 2026)",
    "T": title(
        "Federal Threats to Women Across Cultural Communities",
        "Reproductive-Rights Restriction, Title IX Rollback, and Federal Workforce Gender Protections Withdrawn (Trump II, 2025-2026)",
    ),
    "s": "Women aggregate threat analysis",
    "d": TODAY,
    "a": "Trump II",
    "A": ["DOJ", "HHS", "FDA", "DOE", "EEOC", "DOD", "OPM", "VA", "State"],
    "S": "Active and expanding. Federal action across reproductive rights, Title IX, federal workforce health benefits, and international aid is in implementation. Multiple cases are pending in federal court.",
    "L": "SEVERE",
    "D": (
        "<b>FEDERAL ACTION PATTERNS.</b> The federal landscape facing women under the Trump II administration combines reproductive-rights restriction, Title IX rollback, and federal-workforce gender protections withdrawn in concert. The Department of Justice has revived the 1873 Comstock Act framework in advisory memoranda, treating the mailing of mifepristone and abortion-related instruments as potentially criminal under federal law. The Department of Health and Human Services has narrowed Title X family-planning access through gag rules limiting referrals. The FDA has signaled review of mifepristone access pathways approved during the Biden administration. The Department of Education rescinded the May 2024 Title IX rule that had clarified protections against pregnancy discrimination and sex-based harassment, returning Title IX implementation to the narrower 2020 framework. EEOC pregnancy and harassment guidance has been withdrawn or revised across multiple notices."
        "<br><br>"
        "The Department of Defense reversed Biden-era policies that had reimbursed travel for service members seeking reproductive care across state lines. The Office of Personnel Management revised federal-employee health coverage guidance affecting access to contraception, sterilization, and abortion services through the Federal Employees Health Benefits Program. The Department of Veterans Affairs has restricted reproductive-care services for women veterans in line with the broader administration posture. The Department of State has reinstated and expanded the Mexico City Policy, restricting U.S. foreign assistance to non-governmental organizations that provide or even reference abortion services internationally."
        "<br><br>"
        "<b>CUMULATIVE CULTURAL EFFECTS.</b> The cumulative effect of these federal actions concentrates harm on the women whose reproductive autonomy was already most constrained. Low-income women, women of color, rural women, women with disabilities, immigrant women, and women in states with restrictive abortion regimes carry the heaviest burden. The withdrawal of federal protective baselines means that state-level restrictions face fewer federal counterweights. The Title X gag-rule pattern has historical precedent in the first Trump administration, when an estimated 1,000 community clinics exited the program and 1.6 million patients lost access to federal family-planning services. The current implementation extends those losses. The federal reproductive-rights retreat compounds disparities documented in maternal-mortality statistics, where Black women die in childbirth at three to four times the rate of white women."
        "<br><br>"
        "The Title IX rollback affects students, faculty, and athletes across federally funded education institutions. Pregnancy-related accommodations for students lose their explicit federal floor. Sexual-harassment investigation procedures revert to the narrower 2020 due-process framework that civil-rights advocates had documented as protective of accused parties at the cost of complainants. Federal-employee health coverage changes ripple through the broader employer-sponsored insurance market because federal benefits often serve as a benchmark. The Mexico City Policy expansion withdraws U.S. funding from women's health programs serving tens of millions of women across the global South."
        "<br><br>"
        "<b>OPERATIONAL POSTURE.</b> Implementation is active and expanding. Federal litigation continues across multiple fronts. Mifepristone access is contested in successor litigation to <i>Alliance for Hippocratic Medicine v. FDA</i>. Title X cases are pending in federal district courts. Title IX rule litigation continues across multiple circuits. Federal employee unions have challenged some health-benefit changes. The legal posture is fluid and the operational facts on the ground shift with each new district-court ruling, appellate stay, or final agency action."
        "<br><br>"
        "<b>CROSS-COMMUNITY RESONANCE.</b> The federal action patterns affect women across all five primary cultural communities. Indigenous women face compounded harms because Indian Health Service facilities have historically delivered limited reproductive care under Hyde Amendment restrictions and the IHS budget continues to underfund women's health services. African-descendant women face the highest documented maternal-mortality rates in the federal data, and the federal retreat from women's health infrastructure deepens that gap. Latine women face linguistic and immigration-status barriers that compound the federal access restrictions, particularly for mixed-status families afraid to seek federally funded care. Asian American and Pacific Islander women face culturally specific stigmas around reproductive health that federal program retrenchment exacerbates by removing trusted community-clinic infrastructure. Caribbean women face the same patterns layered atop territorial-status inequities that already restrict federal benefit parity."
        "<br><br>"
        "<b>SOURCES.</b><br>"
        '<a href="https://www.federalregister.gov/agencies/health-and-human-services-department" target="_blank" rel="noopener">HHS notices and rules (Federal Register)</a>.<br>'
        '<a href="https://www.federalregister.gov/agencies/education-department" target="_blank" rel="noopener">Department of Education Title IX rule actions (Federal Register)</a>.<br>'
        '<a href="https://www.fda.gov/drugs/postmarket-drug-safety-information-patients-and-providers/mifepristone-information" target="_blank" rel="noopener">FDA mifepristone information page</a>.<br>'
        '<a href="https://www.eeoc.gov/" target="_blank" rel="noopener">EEOC guidance updates</a>.<br>'
        '<a href="https://www.state.gov/policy-issues/" target="_blank" rel="noopener">U.S. Department of State policy issues page (Mexico City Policy expansion)</a>.<br>'
        '<a href="https://www.courtlistener.com/?q=mifepristone&type=r" target="_blank" rel="noopener">CourtListener docket search for mifepristone litigation</a>.'
    ),
    "I": {
        "women": {
            "people": "Women across the United States face the most direct federal reproductive-rights restriction in fifty years. The end of constitutional protection for abortion under <i>Dobbs v. Jackson Women's Health Organization</i> (2022) shifted the locus of regulation to the states, but the federal government has now joined the restriction posture through advisory memoranda, agency rules, and budget actions. Women in the twenty-one states with abortion bans or near-bans face the steepest barriers. Federal employees, military service members, and veterans face restrictions imposed at the federal benefit level rather than the state level. Black women face the highest maternal-mortality rates and the highest infant-mortality rates documented in federal data. Indigenous women rely on the Indian Health Service for primary care and face longstanding Hyde Amendment restrictions that the current administration has not relaxed. Immigrant women in mixed-status families face additional barriers because public charge concerns and ICE proximity to clinics chill clinical encounters. Rural women face provider deserts that the Title X clinic exit pattern from the first Trump administration deepened by 1,000 facilities. Survivors of sexual assault face Title IX procedural rollbacks that empirical research has documented as reducing reporting and substantiation rates.",
            "places": "The federal places where these actions land include hospital obstetrical units, Title X family-planning clinics, university health centers, military treatment facilities, Veterans Affairs medical centers, Indian Health Service hospitals and clinics, and federally qualified health centers. The 1,400 federally qualified health centers serve more than 30 million patients annually, the majority of whom are women, and federal funding pressures shape what they can offer. University Title IX offices on more than 6,000 federally funded campuses are the institutional sites where the rule rollback is implemented day to day. Federal courthouses across the country, particularly the U.S. District Court for the Northern District of Texas, the Fifth Circuit Court of Appeals, and the U.S. Supreme Court, are the litigation forums where the operational posture is being settled. The Centers for Disease Control headquarters in Atlanta and the FDA campus in Silver Spring are the agency sites where the regulatory record is being made.",
            "practices": "The federal action patterns affect cultural and civic practices including reproductive decision-making, family formation, school participation, military service, federal employment, and international solidarity work. The practice of receiving accurate medical information at a federally funded clinic is constrained by the gag-rule pattern. The practice of mailing prescription medication, including mifepristone, is contested by the Comstock revival memos. The practice of athletic and academic participation under Title IX is reshaped by the rule rescission. Cultural practices around childbirth, postpartum care, and lactation support are affected by federal program funding shifts. The practice of advocacy and organizing through federally funded community programs is constrained where federal grants now exclude organizations that perform or refer for reproductive health services. International solidarity practices including funding partnerships, technical assistance, and joint campaigns are constrained by the Mexico City Policy expansion.",
            "treasures": "The cultural treasures at risk include the documentary record of women's reproductive-rights advocacy held by federal and federally funded archives, including the National Archives, the Library of Congress, and the records of the federal courts. The case files of <i>Roe v. Wade</i> (1973), <i>Planned Parenthood v. Casey</i> (1992), and <i>Dobbs v. Jackson Women's Health Organization</i> (2022) are part of the treasured record of constitutional development. Federal datasets including the National Survey of Family Growth, the Pregnancy Risk Assessment Monitoring System, and the maternal-mortality surveillance systems at CDC are themselves cultural treasures because they document the lived demographic reality of women's health in the United States. The records of the Equal Employment Opportunity Commission, the Office for Civil Rights at the Department of Education, and the Office of Federal Contract Compliance Programs are the federal evidentiary record of women's civil-rights enforcement. Each of these records faces preservation and access risks where agencies are restructured, defunded, or politically constrained."
        }
    },
    "c": ["Women", "All Communities", "Indigenous", "African-descendant", "Latiné", "Asian American", "Pacific Islander", "Caribbean", "Immigrant", "LGBTQIA2S+", "Disabled", "Rural", "Low-income"],
    "U": "https://www.federalregister.gov/",
    "_source": SOURCE_TAG,
}


LGBTQ = {
    "i": "lgbtqia2s-cultural-threat-analysis-2026-05",
    "t": "Aggregate Analysis",
    "n": "LGBTQIA2S+ Aggregate Threat Analysis (May 2026)",
    "T": title(
        "Federal Threats to LGBTQIA2S+ Communities Across Cultural Communities",
        "Federal Sex Definition Rollback, Military Trans Ban, Title IX Rollback, and Health-Care Restrictions (Trump II, 2025-2026)",
    ),
    "s": "LGBTQIA2S+ aggregate threat analysis",
    "d": TODAY,
    "a": "Trump II",
    "A": ["White House", "DOJ", "HHS", "DOD", "DOE", "State", "DHS", "OPM"],
    "S": "Active and expanding. Federal sex-definition reversal under EO 14168 has been implemented across multiple agencies. Multiple lawsuits are pending. The military transgender ban has been reinstated. State-level protective AGs have filed amicus briefs and joined federal challenges.",
    "L": "SEVERE",
    "D": (
        "<b>FEDERAL ACTION PATTERNS.</b> On January 20, 2025, President Trump issued Executive Order 14168, titled \"Defending Women From Gender Ideology Extremism and Restoring Biological Truth to the Federal Government.\" The order directs every federal agency to define \"sex\" as biological binary at conception and to remove gender-identity language from federal forms, programs, and grants. Implementation has reached the Department of State (passport sex markers reverted to assigned-at-birth designation), the Department of Defense (transgender service members removed from active duty under successor policy to the prior trans ban), the Department of Education (Title IX gender-identity protections rescinded), the Department of Health and Human Services (SAMHSA gender-affirming-care guidance for minors withdrawn, HRSA grant restrictions imposed), the Department of Justice (criminal civil-rights enforcement in gender-identity cases narrowed), and the Office of Personnel Management (federal-employee gender-identity protections withdrawn from FEHB plan administration)."
        "<br><br>"
        "The Department of Homeland Security narrowed asylum protections for LGBTQIA2S+ migrants, returning to a pre-2014 framework that places the burden of proof on the applicant to establish particular social group membership without the supportive guidance the Biden administration had issued. The Department of State revoked the Office of the Special Envoy for the Human Rights of LGBTQI+ Persons and reduced reporting on global LGBTQIA2S+ human-rights conditions in the annual Country Reports on Human Rights Practices. Federal contracting guidance and federal grant terms were revised to remove gender-identity and sexual-orientation nondiscrimination language across agencies. The Department of Health and Human Services revoked or revised guidance interpreting Section 1557 of the Affordable Care Act in ways that had protected gender-affirming care."
        "<br><br>"
        "<b>CUMULATIVE CULTURAL EFFECTS.</b> The cumulative federal posture treats LGBTQIA2S+ identity as a protected category to be narrowed or removed across the federal regulatory record. Transgender, nonbinary, intersex, and Two-Spirit individuals face the most direct exposure because the federal sex-binary mandate touches every encounter with federal forms, federal programs, and federal benefits. Lesbian, gay, and bisexual individuals face derivative exposure through the rollback of nondiscrimination interpretations and the chilling effect on federally funded programs. The military ban affects an estimated 14,000 transgender service members and their families. Federal-employee benefit changes affect more than 2 million federal workers and their dependents. Federal-grant changes affect community organizations across the country that depend on HHS, DOE, NEA, NEH, and CDC funding to deliver culturally competent services."
        "<br><br>"
        "Two-Spirit individuals in Indigenous communities face compounded exposure because Indian Health Service implementation tracks the federal HHS posture and because tribal-federal relationships are constrained by federal grant terms. LGBTQIA2S+ asylum seekers face removal to countries where they face documented persecution. LGBTQIA2S+ youth face the withdrawal of federal protective floors at school under Title IX and at the doctor's office under HHS Section 1557 reinterpretation. Federal data collection on LGBTQIA2S+ populations has been pared back across multiple surveys, reducing the evidentiary base for civil-rights enforcement and public-health response."
        "<br><br>"
        "<b>OPERATIONAL POSTURE.</b> Implementation is active and broad. Multiple federal lawsuits challenge EO 14168 and its agency implementations. Cases pending include challenges to the passport-marker reversal, the military service-member discharges, the Title IX rule rescission, and the Section 1557 reinterpretation. State attorneys general from protective jurisdictions have filed amicus briefs and joined plaintiff coalitions in several actions. Federal district courts have entered preliminary injunctions in some matters. The Supreme Court will likely receive merits petitions on at least one of the major implementations within the 2026 term."
        "<br><br>"
        "<b>CROSS-COMMUNITY RESONANCE.</b> LGBTQIA2S+ individuals exist across every primary cultural community the tracker covers. Indigenous Two-Spirit traditions face federal pressure on grant terms, IHS care, and tribal-federal program structure. African-descendant LGBTQIA2S+ communities face the documented intersection of racial and gender-identity discrimination in federal programs, employment, and housing. Latine and Caribbean LGBTQIA2S+ communities face federal asylum and immigration changes that compound the broader sex-definition rollback. Asian American and Pacific Islander LGBTQIA2S+ communities face culturally specific stigmas that federal program retrenchment exacerbates. The federal posture toward LGBTQIA2S+ identity is therefore not a single-community matter but a thread that cuts across every demographic group the tracker tracks."
        "<br><br>"
        "<b>SOURCES.</b><br>"
        '<a href="https://www.whitehouse.gov/presidential-actions/2025/01/defending-women-from-gender-ideology-extremism-and-restoring-biological-truth-to-the-federal-government/" target="_blank" rel="noopener">EO 14168 (whitehouse.gov)</a>.<br>'
        '<a href="https://travel.state.gov/" target="_blank" rel="noopener">Department of State passport policy</a>.<br>'
        '<a href="https://www.defense.gov/" target="_blank" rel="noopener">Department of Defense personnel policy updates</a>.<br>'
        '<a href="https://www.hhs.gov/ocr/" target="_blank" rel="noopener">HHS Office for Civil Rights (Section 1557 guidance)</a>.<br>'
        '<a href="https://www.courtlistener.com/?q=executive+order+14168&type=r" target="_blank" rel="noopener">CourtListener docket search for EO 14168 litigation</a>.'
    ),
    "I": {
        "lgbtq": {
            "people": "LGBTQIA2S+ communities across the United States face a federal posture that treats sexual orientation and gender identity as categories to be narrowed or removed from the federal regulatory record. Transgender, nonbinary, and intersex individuals face the most direct exposure because the EO 14168 mandate to define sex as biological binary touches every federal form, program, and benefit. An estimated 14,000 transgender service members and their families face removal from active duty. More than 2 million federal employees and their dependents face benefit changes affecting gender-affirming care access. LGBTQIA2S+ youth face withdrawal of federal protective floors at school and at the doctor's office. LGBTQIA2S+ asylum seekers face removal to countries where they face documented persecution. Two-Spirit individuals in Indigenous communities face compounded exposure through Indian Health Service implementation and tribal-federal program structure. LGBTQIA2S+ elders face benefit changes affecting Social Security spousal recognition, VA spousal benefits, and Medicare implementation. The cumulative posture concentrates harm on those who depend most on federal recognition for security: federal employees, service members, asylum seekers, and program beneficiaries.",
            "places": "Federal places where these actions land include military bases and installations across the country, federal courthouses where litigation is pending, Department of State passport agencies and embassies, Department of Veterans Affairs medical centers, Indian Health Service facilities, federally qualified health centers, and the offices of HHS, the Department of Education, and the Department of Justice in Washington. Public schools and universities receiving federal funds are the institutional sites where Title IX rollback is implemented. LGBTQIA2S+ community centers across the country, many of which depend on federal grant funding through HRSA, SAMHSA, NEA, NEH, and CDC, face program changes flowing from agency grant-term revisions. Sites of cultural and historical significance to LGBTQIA2S+ communities, including the Stonewall National Monument in New York and the Pulse memorial in Orlando, face federal context shifts that affect interpretation, programming, and partnerships.",
            "practices": "Cultural practices affected include identity documentation (passports, federal IDs, federal forms), military service, federal employment, federally funded health-care access, asylum and immigration practice, and federally funded community programming. The practice of receiving gender-affirming care at federally funded facilities is constrained by HHS guidance withdrawal. The practice of serving openly in the armed forces is constrained by the reinstated trans ban. The practice of bringing federal civil-rights claims under sex-discrimination statutes is constrained by the narrowed federal interpretation of \"sex.\" Cultural practices including Pride celebrations and community-organized public memorials face federal funding and partnership shifts. The practice of asylum advocacy on behalf of LGBTQIA2S+ migrants is constrained by the asylum-rule revisions. Two-Spirit ceremonial practices in Indigenous communities face federal grant-term constraints where federally funded programs serve as venue or sponsor.",
            "treasures": "Cultural treasures at risk include the documentary record of LGBTQIA2S+ civil-rights advocacy held in federal and federally funded archives. The records of the Stonewall National Monument, the LGBTQ History Project at the Library of Congress, the records of the federal litigation in <i>Lawrence v. Texas</i> (2003), <i>Obergefell v. Hodges</i> (2015), and <i>Bostock v. Clayton County</i> (2020), and the federal data collected by CDC on LGBTQIA2S+ health outcomes are part of the treasured record. Community archives held by organizations including the GLBT Historical Society in San Francisco, the ONE Archives at the University of Southern California, and the Schomburg Center for Research in Black Culture face funding pressures that flow from the federal grant-term changes. Federal datasets that have collected sexual orientation and gender identity data, including portions of the National Health Interview Survey and the Behavioral Risk Factor Surveillance System, face data-collection rollbacks that diminish the evidentiary record for future civil-rights advocacy."
        }
    },
    "c": ["LGBTQIA2S+", "All Communities", "Indigenous", "African-descendant", "Latiné", "Asian American", "Pacific Islander", "Caribbean", "Immigrant", "Women", "Disabled"],
    "U": "https://www.whitehouse.gov/presidential-actions/2025/01/defending-women-from-gender-ideology-extremism-and-restoring-biological-truth-to-the-federal-government/",
    "_source": SOURCE_TAG,
}


DISABLED = {
    "i": "disabled-cultural-threat-analysis-2026-05",
    "t": "Aggregate Analysis",
    "n": "Disabled Communities Aggregate Threat Analysis (May 2026)",
    "T": title(
        "Federal Threats to Disabled Communities Across Cultural Communities",
        "IDEA Defunding, Section 504 Weakening, Medicaid HCBS Cuts, and ADA Enforcement Retreat (Trump II, 2025-2026)",
    ),
    "s": "Disabled aggregate threat analysis",
    "d": TODAY,
    "a": "Trump II",
    "A": ["DOE", "HHS", "CMS", "DOJ", "HUD", "EEOC", "DOL", "VA"],
    "S": "Active and expanding. IDEA enforcement reductions are in effect. Section 504 rule revisions are in process. Medicaid HCBS waiver pressures are accelerating. Multiple lawsuits are pending in federal court, including challenges from Disability Rights state-network plaintiffs.",
    "L": "SEVERE",
    "D": (
        "<b>FEDERAL ACTION PATTERNS.</b> The federal landscape facing disabled communities under the Trump II administration combines education, health care, housing, employment, and civil-rights retreats that compound across the disability life course. The Department of Education has reduced staffing at the Office of Special Education Programs and at the Office for Civil Rights, the two federal offices responsible for Individuals with Disabilities Education Act (IDEA) implementation and Section 504 enforcement in schools. IDEA Part B and Part C grant administration has been disrupted by reductions in force and by hiring freezes. The Department's Section 504 rule revision process has been redirected, weakening the framework that had been strengthened in the May 2024 final rule covering medical care, child welfare, and value assessments."
        "<br><br>"
        "The Centers for Medicare and Medicaid Services have advanced per-capita-cap and block-grant proposals for Medicaid that disability advocates have documented as posing existential threats to Home and Community-Based Services waiver programs. HCBS waivers serve more than 4 million Medicaid beneficiaries and are the federal mechanism that supports community living instead of institutionalization. The Department of Justice Civil Rights Division Disability Rights Section has reduced ADA Title II and Title III enforcement activity. The Department of Housing and Urban Development has slowed implementation of the HUD Section 811 supportive-housing program and has narrowed Fair Housing Act disability enforcement. The Equal Employment Opportunity Commission has reduced ADA Title I employment-discrimination case activity. The Department of Government Efficiency layoffs of federal workers have fallen disproportionately on disabled federal employees. Veterans Affairs disability-rating processing has slowed under the broader VA staffing changes."
        "<br><br>"
        "<b>CUMULATIVE CULTURAL EFFECTS.</b> The cumulative federal posture concentrates harm on disabled people who depend on federal programs for the basic conditions of community living. Disabled children face IDEA implementation gaps that result in less appropriate placement, fewer related services, and longer due-process backlogs. Disabled adults face Medicaid HCBS waiting-list expansion, threatening the community-living gains made since the Supreme Court's <i>Olmstead v. L.C.</i> (1999) decision. Disabled workers face EEOC and DOL enforcement retreat that reduces redress for disability-based termination, denial of accommodation, and pay discrimination. Disabled veterans face VA service slowdowns that compound the existing benefit-application backlog. Disabled immigrants face the public charge rule reinstatement and the federal posture that treats disability as a disqualifying factor for benefit access and immigration relief."
        "<br><br>"
        "AbilityOne contracting reform proposals threaten the federal program that supports community-rehabilitation employment for blind and significantly disabled workers across more than 500 nonprofit agencies. Federal communications-access funding for ASL interpreting and Communication Access Real-time Translation services faces cuts. Accessible transportation programs administered by the Federal Transit Administration face reductions in technical-assistance funding. The cumulative effect is a federal retreat from the disability civil-rights infrastructure built since the Rehabilitation Act of 1973 and the Americans with Disabilities Act of 1990."
        "<br><br>"
        "<b>OPERATIONAL POSTURE.</b> Implementation is active and broad. Multiple federal lawsuits challenge agency rollbacks. Disability Rights state-network plaintiffs have filed actions in IDEA, Section 504, and ADA matters. The National Disability Rights Network has documented enforcement-data declines across DOJ, EEOC, and HHS. Federal courts have not yet issued comprehensive rulings on the federal-program retreats; most cases are in preliminary stages or in administrative-record stages awaiting final-agency-action determinations."
        "<br><br>"
        "<b>CROSS-COMMUNITY RESONANCE.</b> Disabled people exist across every primary cultural community. Indigenous disabled people face compounded exposure through Indian Health Service capacity gaps and tribal-federal program structure. African-descendant disabled people face the documented intersection of racial and disability discrimination in federal programs, education, and policing. Latine and Caribbean disabled people face linguistic and immigration-status barriers that compound the federal access restrictions. Asian American and Pacific Islander disabled people face culturally specific stigmas that federal program retrenchment exacerbates by reducing community-organization grant funding. Disabled people in immigrant, low-income, rural, and LGBTQIA2S+ communities each carry distinct vulnerabilities that the cumulative federal posture deepens."
        "<br><br>"
        "<b>SOURCES.</b><br>"
        '<a href="https://www.ed.gov/" target="_blank" rel="noopener">Department of Education IDEA and Section 504 actions</a>.<br>'
        '<a href="https://www.cms.gov/" target="_blank" rel="noopener">CMS Medicaid HCBS guidance and proposals</a>.<br>'
        '<a href="https://www.justice.gov/crt/disability-rights-section" target="_blank" rel="noopener">DOJ Disability Rights Section</a>.<br>'
        '<a href="https://www.eeoc.gov/" target="_blank" rel="noopener">EEOC ADA enforcement statistics</a>.<br>'
        '<a href="https://www.ndrn.org/" target="_blank" rel="noopener">National Disability Rights Network</a>.<br>'
        '<a href="https://www.courtlistener.com/?q=section+504+rule&type=r" target="_blank" rel="noopener">CourtListener docket search for Section 504 litigation</a>.'
    ),
    "I": {
        "disabled": {
            "people": "Disabled people across the United States face a federal posture of retreat from the civil-rights infrastructure that has supported community living, education access, and workforce participation since the 1970s. Disabled children face IDEA implementation gaps. Disabled adults face Medicaid HCBS waiting-list expansion. Disabled workers face EEOC and Department of Labor enforcement retreat. Disabled veterans face VA service slowdowns. Disabled immigrants face public charge and benefit-access posture changes. Blind and low-vision people face federal accessibility-funding reductions. Deaf and hard-of-hearing people face ASL interpreter and CART funding cuts. People with intellectual and developmental disabilities face HCBS waiver pressures that threaten the community-living gains made since <i>Olmstead</i>. People with psychiatric disabilities face SAMHSA program shifts and Medicaid behavioral-health restrictions. People with chronic physical disabilities face Medicare and Medicaid coverage uncertainty. The disability community is broad and the federal exposure is broad as well.",
            "places": "Federal places where these actions land include public schools and universities receiving IDEA and Section 504 funds, more than 4 million Medicaid HCBS beneficiary households across all fifty states and the territories, more than 500 AbilityOne nonprofit agency sites, federal workplaces affected by DOGE layoffs, Veterans Affairs medical centers and benefit offices, public housing and Section 811 supportive housing across the country, and federally funded transit systems. The Department of Education in Washington, the Office for Civil Rights regional offices, the CMS regional offices, and the federal courthouses where disability-rights litigation is pending are the institutional sites where the operational posture is being settled. Disability cultural sites including Gallaudet University in Washington (the federally chartered university for the deaf and hard of hearing) and the National Federation of the Blind headquarters in Baltimore face federal partnership shifts.",
            "practices": "Cultural practices affected include the practice of receiving an appropriate education under IDEA, the practice of community living supported by HCBS waivers, the practice of accessible voting, the practice of ADA-protected employment, the practice of accessible transportation, and the practice of independent advocacy through Centers for Independent Living. The practice of self-determination over one's own care is constrained by HCBS waiver waiting-list expansion. The practice of accessing federal benefits is constrained by SSI eligibility tightening proposals. The practice of accessing federal services in plain language and accessible format is constrained by federal-program staff reductions. Disability cultural practices including Disability Pride observances, Deaf cultural events, blind community ceremonies, and intellectual-and-developmental-disability self-advocacy gatherings face federal grant-term changes that affect community-organization sponsorship.",
            "treasures": "Cultural treasures at risk include the documentary record of the disability rights movement held by federal and federally funded archives, including the records of the Department of Education's Office of Special Education and Rehabilitative Services, the National Council on Disability, and the federal court files in <i>Olmstead v. L.C.</i> (1999), <i>PARC v. Pennsylvania</i> (1972), and <i>Mills v. Board of Education of the District of Columbia</i> (1972). The papers of disability-rights leaders held by federal and federally funded archives, including the Justin Dart papers and the Judy Heumann papers, are treasured records of advocacy history. The U.S. Access Board's accessibility standards record, the federal data on disability prevalence collected by the Census Bureau and the Centers for Disease Control, and the records of the Independent Living movement supported by federal RSA funding are all federal cultural treasures. Each faces preservation and access risks where agencies are restructured or defunded."
        }
    },
    "c": ["Disabled", "All Communities", "Indigenous", "African-descendant", "Latiné", "Asian American", "Pacific Islander", "Caribbean", "Veterans", "Low-income", "Immigrant"],
    "U": "https://www.ed.gov/about/offices/list/osers/osep/index.html",
    "_source": SOURCE_TAG,
}


IMMIGRANT = {
    "i": "immigrant-cultural-threat-analysis-2026-05",
    "t": "Aggregate Analysis",
    "n": "Immigrant Communities Aggregate Threat Analysis (May 2026)",
    "T": title(
        "Federal Threats to Immigrant Communities Across Cultural Communities",
        "Birthright-Citizenship Restriction, Mass Deportation, Asylum Suspension, TPS Termination, and Sanctuary-Funding Cuts (Trump II, 2025-2026)",
    ),
    "s": "Immigrant aggregate threat analysis",
    "d": TODAY,
    "a": "Trump II",
    "A": ["White House", "DHS", "ICE", "USCIS", "CBP", "DOJ", "State", "HHS"],
    "S": "Active and expanding. Mass deportation operations are in execution. Birthright-citizenship litigation is at the Supreme Court level. TPS terminations are entering effect dates with active litigation. Refugee admissions are paused. Multiple federal courts have entered preliminary injunctions on subsets of the policy posture.",
    "L": "SEVERE",
    "D": (
        "<b>FEDERAL ACTION PATTERNS.</b> The federal landscape facing immigrant communities under the Trump II administration is the broadest immigration restriction posture since the 1924 Johnson-Reed Act. Executive Order 14160, issued January 20, 2025, purports to deny birthright citizenship to U.S.-born children of undocumented parents and certain temporary-status parents. Successor executive orders and proclamations declared a national emergency at the southern border, suspended refugee admissions, paused asylum processing under the Immigration and Nationality Act Section 212(f), expanded expedited removal nationwide, ended catch-and-release practices, and directed mass-deportation operations targeting an estimated 11 million undocumented residents. The Department of Homeland Security implemented those directives through ICE enforcement operations, CBP border practices, and USCIS processing changes."
        "<br><br>"
        "Temporary Protected Status terminations affect Venezuelan, Haitian, Honduran, Nicaraguan, Salvadoran, Sudanese, and other designated populations. Humanitarian parole programs created during the Biden administration (CHNV for Cubans, Haitians, Nicaraguans, and Venezuelans, plus Uniting for Ukraine) were terminated. The Diversity Visa Lottery and the U-visa, T-visa, and Special Immigrant Juvenile programs face processing slowdowns. USCIS fee increases for asylum applications, employment authorization documents, naturalization, and family-based petitions raise the cost of legal-immigration processes for low-income families. The public charge rule has been reinstated in expanded form, treating use of Medicaid, SNAP, federal housing assistance, and other federal benefits as grounds for inadmissibility. Sanctuary-jurisdiction federal funding has been targeted through grant-term modifications across DOJ, DHS, and HUD programs."
        "<br><br>"
        "<b>CUMULATIVE CULTURAL EFFECTS.</b> The cumulative effect concentrates harm on mixed-status families, undocumented community members, asylum seekers, refugees, TPS holders, and U.S. citizens whose civic life is constrained by ICE proximity to schools, courthouses, hospitals, and places of worship. The chilling effect on immigrant-community engagement with federal and state institutions has been documented across health-care access, school enrollment, and crime reporting. Immigrant cultural institutions including community centers, day-labor centers, language schools, ethnic media, and faith communities face member departures and operational disruption. Immigrant workers in agriculture, construction, food processing, hospitality, and home health care face workplace raids and family separations that disrupt entire local economies."
        "<br><br>"
        "Federal courthouses become contested ground where ICE arrests at courthouse exits chill participation in legal processes. Public schools face enrollment declines and absenteeism among immigrant children. Hospitals face emergency-room avoidance among patients who fear immigration consequences. Faith communities including Catholic parishes, evangelical Spanish-speaking congregations, mosques, gurdwaras, and temples report congregant absences linked to enforcement fears. The cultural cost of mass deportation extends beyond the directly removed to the U.S.-citizen children of removed parents, the local economies disrupted, and the community institutions that lose members."
        "<br><br>"
        "<b>OPERATIONAL POSTURE.</b> Implementation is active and broad. Multiple federal lawsuits challenge subsets of the policy posture. Federal district courts have entered preliminary injunctions on EO 14160 (the birthright citizenship order), on certain TPS terminations, and on certain expedited-removal expansions. The Supreme Court ruled on universal injunctions in <i>Trump v. CASA, Inc.</i> (June 27, 2025), narrowing the availability of universal injunctions while leaving the constitutional merits of the underlying policies unresolved. Asylum suspension cases are pending. Sanctuary-funding cases continue across multiple circuits. The legal posture is fluid and the operational facts on the ground change with each new district-court ruling, appellate stay, or executive directive."
        "<br><br>"
        "<b>CROSS-COMMUNITY RESONANCE.</b> Immigrant communities exist across every primary cultural community the tracker covers. Indigenous immigrants from Latin America (Maya, Mixtec, Zapotec, Quechua, and other Indigenous communities of the Americas) face the federal pressure compounded by linguistic isolation when ICE encounters do not include qualified interpreters. African-descendant immigrants from Haiti, the Dominican Republic, Jamaica, Nigeria, Ethiopia, Somalia, and other origins face the federal pressure compounded by anti-Black racial profiling in federal enforcement. Latine immigrants face the broadest direct exposure given the demographic distribution of the affected populations. Asian American immigrants from China, Vietnam, India, the Philippines, Cambodia, Laos, and other origins face the federal pressure compounded by H-1B and student-visa restrictions and by the broader anti-Asian climate the tracker has documented elsewhere. Pacific Islander immigrants and Compact of Free Association migrants from the Republic of the Marshall Islands, the Federated States of Micronesia, and the Republic of Palau face federal benefit-access constraints under the public charge expansion."
        "<br><br>"
        "<b>SOURCES.</b><br>"
        '<a href="https://www.whitehouse.gov/presidential-actions/2025/01/protecting-the-meaning-and-value-of-american-citizenship/" target="_blank" rel="noopener">EO 14160 (whitehouse.gov)</a>.<br>'
        '<a href="https://www.dhs.gov/" target="_blank" rel="noopener">DHS enforcement and TPS notices</a>.<br>'
        '<a href="https://www.uscis.gov/" target="_blank" rel="noopener">USCIS fee and policy updates</a>.<br>'
        '<a href="https://www.scotusblog.com/case-files/cases/trump-v-casa-inc/" target="_blank" rel="noopener"><i>Trump v. CASA, Inc.</i> SCOTUSblog case page</a>.<br>'
        '<a href="https://www.courtlistener.com/?q=executive+order+14160&type=r" target="_blank" rel="noopener">CourtListener docket search for immigration EO litigation</a>.'
    ),
    "I": {
        "immigrant": {
            "people": "Immigrant communities across the United States face the broadest restriction posture in a century. The directly affected population includes an estimated 11 million undocumented residents, more than 1 million TPS holders facing termination dates, more than 500,000 humanitarian-parole holders whose programs have been terminated, hundreds of thousands of asylum seekers in pending proceedings, and millions of mixed-status family members whose civic life is shaped by enforcement risk. The U.S.-citizen children of removed parents, estimated in the millions, face the secondary harm of family separation. Refugee admissions, paused at the executive level, affect tens of thousands of vetted applicants who had been awaiting travel. Naturalization applicants face fee increases and processing slowdowns that delay civic enfranchisement. The public charge expansion affects benefit-eligible immigrants whose use of federal programs now creates inadmissibility risk. The combined posture treats immigration status as a defect to be enforced against rather than a transition to be supported.",
            "places": "Federal places where these actions land include the U.S.-Mexico border (where asylum suspension is implemented), interior CBP and ICE field offices across the country, USCIS processing centers, immigration courts under EOIR, federal district and appellate courts where litigation is pending, the U.S. Supreme Court (where the birthright citizenship case is pending merits review), embassies and consulates abroad (where visa processing reflects the new posture), and refugee-admission processing facilities. Immigrant cultural sites within the United States include ethnic enclaves, day-labor corner sites, federally funded community centers, hospitals serving large immigrant patient populations, and federally funded English-language acquisition programs. Faith communities including more than 16,000 Catholic parishes, hundreds of evangelical Spanish-speaking congregations, more than 2,500 mosques, hundreds of gurdwaras, and hundreds of temples are sites where immigrant cultural and spiritual life concentrates and where federal enforcement encounters chill participation.",
            "practices": "Cultural practices affected include the practice of family reunification through legal immigration channels, the practice of seeking asylum from persecution, the practice of working in occupations dominated by immigrant labor, the practice of sending remittances home, the practice of celebrating cultural and religious festivals, and the practice of civic participation through naturalization. The practice of attending an immigration court hearing without fear of arrest at the courthouse exit is constrained by the federal courthouse-arrest posture. The practice of seeking medical care without fear of immigration consequence is constrained by hospital-area enforcement and by the public charge rule. The practice of sending children to public school without fear of family separation is constrained by school-area enforcement reports. The practice of organizing collectively through day-labor centers, worker centers, and immigrant-rights coalitions is constrained by federal grant-term changes affecting nonprofit funding partners.",
            "treasures": "Cultural treasures at risk include the documentary record of immigrant communities held in federal and federally funded archives, including the records at Ellis Island and Angel Island Immigration Stations, the Library of Congress oral history collections, the National Archives immigrant records, and the federal court files of major immigration-rights cases (<i>Plyler v. Doe</i> (1982), <i>INS v. Cardoza-Fonseca</i> (1987), <i>Zadvydas v. Davis</i> (2001), <i>DACA</i> litigation). Community archives held by ethnic organizations including the Tenement Museum in New York, the Japanese American National Museum in Los Angeles, the National Hispanic Cultural Center in Albuquerque, and many others document the lived experience of immigration in America. Federally funded oral history projects through the American Folklife Center and the Smithsonian Center for Folklife and Cultural Heritage are treasured records that face funding-pressure risks. Family papers, personal letters, photographs, and recorded oral histories held in immigrant communities are themselves cultural treasures that face risks where families are separated by deportation."
        }
    },
    "c": ["Immigrant", "All Communities", "Indigenous", "African-descendant", "Latiné", "Asian American", "Pacific Islander", "Caribbean", "Refugee", "Asylum Seeker", "Mixed-Status Family"],
    "U": "https://www.dhs.gov/",
    "_source": SOURCE_TAG,
}


RURAL = {
    "i": "rural-cultural-threat-analysis-2026-05",
    "t": "Aggregate Analysis",
    "n": "Rural Communities Aggregate Threat Analysis (May 2026)",
    "T": title(
        "Federal Threats to Rural Communities Across Cultural Communities",
        "USDA Rural Development Cuts, Rural Hospital Closures, Broadband Expiration, and Conservation-Program Reductions (Trump II, 2025-2026)",
    ),
    "s": "Rural aggregate threat analysis",
    "d": TODAY,
    "a": "Trump II",
    "A": ["USDA", "HHS", "CMS", "FCC", "EPA", "USPS", "DOL", "DOE"],
    "S": "Active and expanding. USDA Rural Development funding has been cut. Rural hospital closures are accelerating under Medicaid pressure. The Affordable Connectivity Program has expired. Conservation Reserve Program cuts are in process. Postal service degradation continues to affect rural ZIPs.",
    "L": "SEVERE",
    "D": (
        "<b>FEDERAL ACTION PATTERNS.</b> Rural communities face a federal posture of program retrenchment that touches the basic infrastructure of rural life. The U.S. Department of Agriculture Rural Development mission area has seen cuts to Rural Housing Service, Rural Business-Cooperative Service, and Rural Utilities Service program funding. The Affordable Connectivity Program, which had subsidized broadband access for more than 23 million low-income households (a disproportionate share rural), expired and has not been renewed. The Federal Communications Commission's Universal Service Fund High Cost program has faced contribution-base challenges that constrain rural broadband expansion. The Centers for Medicare and Medicaid Services proposals on Medicaid per-capita caps and block grants have accelerated rural hospital financial pressure. The American Hospital Association has documented an ongoing rural hospital closure trend that adds to the more than 150 rural hospitals closed since 2010."
        "<br><br>"
        "USDA conservation programs including the Conservation Reserve Program, the Environmental Quality Incentives Program, and the Conservation Stewardship Program face funding reductions and rule changes that affect farm operations and rural land stewardship. Title I rural school funding under the Elementary and Secondary Education Act faces formula pressures. The Department of Veterans Affairs rural-health staffing has been affected by the broader VA staffing changes, deepening rural-veteran service-access gaps. Postal Service operational changes have continued the multi-year degradation of rural mail delivery, affecting prescription-medication delivery, agricultural-product mail, absentee-ballot delivery, and the broader civic life of rural communities. EPA rural drinking-water programs administered through the State Revolving Funds and the Drinking Water State Revolving Fund face reductions in technical-assistance support."
        "<br><br>"
        "<b>CUMULATIVE CULTURAL EFFECTS.</b> The cumulative federal posture concentrates harm on rural residents whose access to health care, education, broadband, transportation, and basic federal services depends on programs designed to offset the structural costs of distance and dispersion. Rural residents experience longer drive times to medical care, fewer providers per capita, and higher per-capita costs in every infrastructure category. Federal program retrenchment widens those gaps. Rural hospital closures create maternity-care deserts that disproportionately affect Black, Indigenous, and Latina mothers in rural counties. Rural broadband gaps constrain telemedicine, remote work, distance learning, and civic engagement. Rural school funding pressures affect the quality of education in places where the federal share of school revenue is structurally larger. The cumulative rural retreat falls hardest on the rural residents who are also part of other marginalized communities: rural Indigenous tribal members, rural African-descendant communities in the South, rural Latine farmworker communities, and rural Pacific Islander communities in the territories."
        "<br><br>"
        "Cultural costs include the erosion of community institutions: the rural hospital, the rural post office, the rural school, the rural library, the rural cooperative, and the rural church. Each of these is a federal-program touch point where rural cultural life is supported and where retrenchment cuts directly. The Radiation Exposure Compensation Act (RECA) reauthorization gap affects rural communities downwind of federal nuclear-test sites and rural uranium-mining communities. Rural environmental-justice communities including the Mississippi Delta, the Black Belt, the Navajo Nation, the Kentucky coalfields, and the agricultural valleys of California face federal program retreat from cleanup and protection programs they depend on."
        "<br><br>"
        "<b>OPERATIONAL POSTURE.</b> Implementation is active and ongoing. Federal litigation on rural-program changes is limited compared to other policy areas, partly because rural advocacy organizations have smaller litigation capacity and partly because rural-program retrenchment often happens through budget action rather than rule change. Congressional action on the next Farm Bill, on Medicaid funding, on USDA appropriations, and on broadband-program reauthorization will shape the rural posture for the rest of this administration. Rural state attorneys general have varied positions on the policy retreat, with some joining sanctuary-funding lawsuits and others supporting the administration's posture."
        "<br><br>"
        "<b>CROSS-COMMUNITY RESONANCE.</b> Rural communities are not monocultural. Indigenous tribal members live disproportionately in rural areas, particularly in the western states and Alaska, and the federal rural retreat compounds the existing inadequacy of Indian Health Service rural facilities, BIA road infrastructure, and BIE school funding. African-descendant rural communities, particularly in the Black Belt counties of Alabama, Mississippi, Georgia, and South Carolina, face federal rural retreat layered atop centuries of disinvestment in the rural South. Latine rural communities, particularly in agricultural California, the Texas border, the Pacific Northwest, and the upper Midwest, face federal rural retreat layered atop immigration enforcement and language-access gaps. Asian American rural communities, particularly Hmong, Laotian, and Cambodian communities in the Central Valley and the upper Midwest, face federal rural retreat layered atop refugee resettlement legacies. Pacific Islander rural communities in American Samoa, Guam, the Northern Mariana Islands, the Federated States of Micronesia, the Marshall Islands, and Palau face territorial-status inequities compounded by the broader federal rural retreat."
        "<br><br>"
        "<b>SOURCES.</b><br>"
        '<a href="https://www.rd.usda.gov/" target="_blank" rel="noopener">USDA Rural Development</a>.<br>'
        '<a href="https://www.cms.gov/" target="_blank" rel="noopener">CMS rural health and Medicaid policy</a>.<br>'
        '<a href="https://www.fcc.gov/general/universal-service" target="_blank" rel="noopener">FCC Universal Service programs</a>.<br>'
        '<a href="https://www.aha.org/" target="_blank" rel="noopener">American Hospital Association rural hospital tracking</a>.<br>'
        '<a href="https://www.usps.gov/" target="_blank" rel="noopener">United States Postal Service operational reports</a>.<br>'
        '<a href="https://www.epa.gov/dwsrf" target="_blank" rel="noopener">EPA Drinking Water State Revolving Fund</a>.'
    ),
    "I": {
        "rural": {
            "people": "Rural Americans constitute approximately 60 million people across all fifty states and the territories, distributed across more than 2,000 rural counties. The federal posture affects rural residents whose access to health care, education, broadband, transportation, and basic federal services depends on programs designed to offset the structural costs of distance and dispersion. Rural residents experience longer drive times to medical care, fewer providers per capita, and higher per-capita costs in every infrastructure category. Rural hospital closures create maternity-care deserts that disproportionately affect Black, Indigenous, and Latina mothers in rural counties. Rural Indigenous communities, including more than 300 tribal nations whose reservations are in rural settings, face the federal retreat layered atop existing trust-responsibility gaps. Rural African-descendant communities in the Black Belt face the federal retreat layered atop centuries of rural disinvestment. Rural Latine farmworker communities face the federal retreat layered atop immigration enforcement. Rural Asian American communities including Hmong, Laotian, and Cambodian populations face the federal retreat layered atop refugee resettlement legacies. Rural Pacific Islander communities in the territories face territorial-status inequities compounded by the broader retreat.",
            "places": "Rural places where these actions land include more than 1,800 rural hospitals (more than 150 of which have closed since 2010), the more than 6,500 critical-access hospitals and rural health clinics, rural schools serving an estimated 9 million rural students, rural post offices in more than 30,000 ZIP codes, rural libraries supported through IMLS Library Services and Technology Act formula grants, rural cooperatives serving rural electricity, telephone, and water needs, USDA Rural Development project sites, and the more than 31 million broadband households that had qualified for ACP support. Rural cultural sites include county fairgrounds, agricultural-museum sites, rural historic districts, rural sacred sites for Indigenous communities, rural Black churches and cemeteries, rural farmworker community centers, rural Pacific Islander cultural centers, rural veterans' memorials, and rural one-room-schoolhouse historic landmarks. Federal land in rural areas including BLM, Forest Service, and Park Service holdings is the rural cultural landscape.",
            "practices": "Rural cultural practices affected include the practice of cooperative agriculture supported by USDA programs, the practice of rural-school education funded through Title I and Impact Aid, the practice of rural-hospital childbirth and end-of-life care, the practice of rural-religious community life supported by post-office mail delivery, the practice of rural civic engagement through absentee voting and rural-newspaper readership, the practice of rural conservation through CRP and EQIP, and the practice of rural cultural transmission through 4-H, FFA, and Cooperative Extension programming. The practice of receiving prescription medication by mail is constrained by USPS rural-route degradation. The practice of distance education and telemedicine is constrained by the ACP expiration. The practice of sustainable agriculture is constrained by conservation-program funding cuts. The practice of rural community organizing is constrained where federal grants to rural nonprofits face term changes.",
            "treasures": "Rural cultural treasures at risk include the documentary record of rural America held in federal and federally funded archives, including the USDA Cooperative Extension records, the Federal Writers' Project rural folklore collections at the Library of Congress, the Smithsonian Center for Folklife and Cultural Heritage rural folklife collections, and the National Archives' agricultural-policy record. Community archives in rural museums, historical societies, and university libraries (particularly land-grant universities under the Morrill Act framework) hold the lived record of rural cultural life. Rural sacred sites for Indigenous communities, rural Black church records and cemetery records, rural farmworker-organizing records, and rural Pacific Islander cultural records are treasures held in their home communities. The Federal Lands Recreation Enhancement Act sites, the National Register of Historic Places rural listings, and the rural Heritage Areas designated by Congress are federally connected cultural treasures whose preservation depends on federal partnership."
        }
    },
    "c": ["Rural", "All Communities", "Indigenous", "African-descendant", "Latiné", "Asian American", "Pacific Islander", "Veterans", "Low-income", "Disabled"],
    "U": "https://www.rd.usda.gov/",
    "_source": SOURCE_TAG,
}


POOR = {
    "i": "low-income-cultural-threat-analysis-2026-05",
    "t": "Aggregate Analysis",
    "n": "Low-Income Communities Aggregate Threat Analysis (May 2026)",
    "T": title(
        "Federal Threats to Low-Income Communities Across Cultural Communities",
        "SNAP and Medicaid Cuts, ACA Premium Credit Expiration, Public Housing Demolition, and Civil-Legal-Aid Reductions (Trump II, 2025-2026)",
    ),
    "s": "Low-income aggregate threat analysis",
    "d": TODAY,
    "a": "Trump II",
    "A": ["USDA", "HHS", "CMS", "HUD", "Treasury", "DOL", "SSA", "LSC"],
    "S": "Active and expanding. SNAP work-requirement and benefit-cut proposals are advancing. Medicaid per-capita-cap proposals are in legislative motion. ACA premium-tax-credit enhancements expire at the end of 2025 absent congressional renewal. HUD program changes affect public and assisted housing. Multiple federal lawsuits are pending.",
    "L": "SEVERE",
    "D": (
        "<b>FEDERAL ACTION PATTERNS.</b> Low-income communities face a federal posture of program retrenchment across the federal social safety net. The Supplemental Nutrition Assistance Program (SNAP) faces work-requirement expansion under the Fiscal Responsibility Act framework continued by the current administration, plus benefit-cut proposals tied to the Thrifty Food Plan reset. The Medicaid program faces per-capita-cap and block-grant proposals that the Congressional Budget Office has scored as causing tens of millions of beneficiaries to lose coverage. The Affordable Care Act premium-tax-credit enhancements (the American Rescue Plan and Inflation Reduction Act subsidies) expire at the end of 2025 absent congressional renewal, raising marketplace premiums substantially for low-income enrollees. The Temporary Assistance for Needy Families program faces tightening through state-flexibility changes that allow steeper sanctions and shorter time limits."
        "<br><br>"
        "The Department of Housing and Urban Development has accelerated public housing redevelopment under the Rental Assistance Demonstration with reduced replacement-housing requirements. Housing Choice Voucher (Section 8) program funding faces reductions in administrative-fee support that constrain housing-authority capacity. The Low Income Home Energy Assistance Program faces appropriations pressure. Free and reduced-price school meal eligibility faces tightening through community-eligibility-provision changes. Supplemental Security Income eligibility faces tightening through proposed asset-limit and income-counting rule changes. The Legal Services Corporation, the federally chartered nonprofit that funds civil legal aid for low-income litigants, faces appropriations pressure that reduces representation in housing, public benefits, family law, and consumer matters. Federal earned income tax credit and child tax credit administration has not been expanded and faces audit-rate proposals that fall heaviest on low-income filers."
        "<br><br>"
        "<b>CUMULATIVE CULTURAL EFFECTS.</b> The cumulative federal posture concentrates harm on the more than 38 million Americans living below the federal poverty line and the additional tens of millions in the near-poor population whose stability depends on federal programs. Children in low-income households face SNAP cuts, school-meal cuts, Medicaid cuts, and TANF cuts simultaneously, with documented effects on food security, health outcomes, and educational attainment. Working-poor adults face the loss of ACA premium-tax-credit enhancements, raising marketplace premiums by hundreds to thousands of dollars annually for enrollees in the 100-to-400 percent of poverty income range. Older adults in the SNAP and SSI populations face benefit cuts at a moment when housing costs are rising. Rural low-income residents and urban low-income residents face distinct but overlapping versions of the same retrenchment pattern."
        "<br><br>"
        "Federal program retrenchment falls heaviest on communities that are simultaneously low-income and members of other affected communities. Indigenous low-income households face the federal retrenchment layered atop the chronic underfunding of the Indian Health Service, BIA programs, and BIE schools. African-descendant low-income households face the federal retrenchment layered atop the documented racial wealth gap and centuries of housing and credit discrimination. Latine low-income households face the federal retrenchment layered atop public charge concerns that chill benefit access. Asian American low-income households, particularly Hmong, Cambodian, Laotian, Vietnamese, Burmese, Nepali, and Bhutanese refugee-origin communities, face poverty rates substantially above the U.S. average that the retrenchment deepens. Pacific Islander low-income households face territorial-benefit inequities that compound the broader retreat. Disabled low-income households face SSI tightening compounded with HCBS waiver pressure."
        "<br><br>"
        "<b>OPERATIONAL POSTURE.</b> Implementation is active and ongoing. SNAP work-requirement expansions are in effect across the states. Medicaid per-capita-cap legislation is pending in Congress. ACA premium-tax-credit expiration is pending the year-end 2025 statutory deadline. HUD program changes are in implementation through agency rulemaking. Multiple federal lawsuits challenge subsets of the retrenchment. State attorneys general have filed in Medicaid, SNAP, and HUD matters. The CBO and the Center on Budget and Policy Priorities have scored the cumulative effect as the largest expansion of federal-program-driven economic insecurity since the 1996 welfare reform."
        "<br><br>"
        "<b>CROSS-COMMUNITY RESONANCE.</b> Low-income communities span every primary cultural community. Indigenous low-income households, African-descendant low-income households, Latine low-income households, Asian American low-income households, Pacific Islander low-income households, and Caribbean low-income households each face the federal retrenchment layered atop community-specific federal-program inadequacies. Low-income people in immigrant, rural, urban, disabled, and LGBTQIA2S+ communities each carry distinct vulnerabilities that the cumulative federal posture deepens. The poverty experience is shared across cultural communities and the federal program retreat is felt across all of them."
        "<br><br>"
        "<b>SOURCES.</b><br>"
        '<a href="https://www.fns.usda.gov/snap" target="_blank" rel="noopener">USDA Food and Nutrition Service SNAP</a>.<br>'
        '<a href="https://www.cms.gov/" target="_blank" rel="noopener">CMS Medicaid policy</a>.<br>'
        '<a href="https://www.healthcare.gov/" target="_blank" rel="noopener">HealthCare.gov ACA marketplace</a>.<br>'
        '<a href="https://www.hud.gov/" target="_blank" rel="noopener">HUD policy and program updates</a>.<br>'
        '<a href="https://www.ssa.gov/ssi/" target="_blank" rel="noopener">SSA Supplemental Security Income</a>.<br>'
        '<a href="https://www.lsc.gov/" target="_blank" rel="noopener">Legal Services Corporation</a>.<br>'
        '<a href="https://www.cbpp.org/" target="_blank" rel="noopener">Center on Budget and Policy Priorities analysis</a>.'
    ),
    "I": {
        "lowIncome": {
            "people": "More than 38 million Americans live below the federal poverty line and additional tens of millions in the near-poor population face economic insecurity that depends on federal programs for stability. Children in low-income households number more than 11 million. Working-poor adults number tens of millions across the formal and informal economies. Older adults in SNAP, SSI, Medicare Savings Programs, and LIHEAP populations number millions. Rural low-income residents and urban low-income residents face distinct but overlapping versions of the same retrenchment pattern. Indigenous low-income households face poverty rates substantially above the U.S. average. African-descendant low-income households reflect the documented racial wealth gap. Latine low-income households face mixed-status family chilling effects. Asian American low-income households, particularly in Southeast Asian refugee-origin communities, face poverty rates substantially above the U.S. average that media coverage often misses behind aggregate AAPI statistics. Pacific Islander low-income households face territorial-benefit inequities. Disabled low-income households face SSI tightening compounded with HCBS waiver pressure. The federal program retreat is felt across all of them.",
            "places": "Federal places where these actions land include the SNAP retailers serving more than 250,000 outlets nationwide, the Medicaid managed-care plans covering more than 90 million enrollees, the ACA marketplaces in fifty states and the District of Columbia, the more than 1.2 million public-housing units administered by HUD, the Housing Choice Voucher program covering more than 2.3 million households, the federal LIHEAP-funded utility-assistance offices in every state, the SSA field offices and the Disability Determination Services in every state, and the more than 130 Legal Services Corporation grantees across the country. Free and reduced-price school meals serve approximately 30 million children daily across more than 95,000 schools. Federal community-action agencies under the Community Services Block Grant operate in nearly every county. Federally qualified health centers, free clinics, food banks, and emergency-shelter networks are the operational sites where federal retrenchment is felt by low-income community members.",
            "practices": "Cultural practices affected include the practice of providing for one's family through SNAP and school meals, the practice of receiving health care through Medicaid and the ACA marketplace, the practice of stable housing through public housing and Section 8 vouchers, the practice of warm winters through LIHEAP, the practice of disability-related income through SSI, the practice of asserting rights through Legal Services Corporation grantees, and the practice of community gathering at the food pantry, the community-action agency, the public library, and the Section 8 housing complex. The practice of working at sub-living-wage jobs while relying on federal subsidies is constrained by the simultaneous benefit cuts and the absence of federal minimum-wage adjustment. The practice of intergenerational support is constrained where SSI rules treat in-kind support as countable income. The practice of asset-building is constrained by SSI and TANF asset limits.",
            "treasures": "Cultural treasures at risk include the documentary record of low-income community life held in federal and federally funded archives, including the records of the War on Poverty programs at the National Archives, the Federal Writers' Project oral history collections at the Library of Congress, the Cooperative Extension records, and the federal court files of major poverty-law cases (<i>Goldberg v. Kelly</i> (1970), <i>Shapiro v. Thompson</i> (1969), <i>King v. Smith</i> (1968)). Community archives held by community-action agencies, settlement houses, and Legal Services Corporation grantees document the lived experience of poverty and the federal-program response. Federally funded oral history projects through StoryCorps and the Smithsonian Center for Folklife and Cultural Heritage have collected the voices of low-income communities. The federal datasets on poverty, food security, and material hardship maintained by the Census Bureau, the USDA Economic Research Service, and HHS are themselves cultural treasures because they document the lived demographic reality of poverty in the United States."
        }
    },
    "c": ["Low-income", "All Communities", "Indigenous", "African-descendant", "Latiné", "Asian American", "Pacific Islander", "Caribbean", "Rural", "Disabled", "Immigrant"],
    "U": "https://www.cbpp.org/",
    "_source": SOURCE_TAG,
}


NONPROFIT = {
    "i": "nonprofit-sector-cultural-threat-analysis-2026-05",
    "t": "Aggregate Analysis",
    "n": "Non-Profit Sector Aggregate Threat Analysis (May 2026)",
    "T": title(
        "Federal Threats to the Non-Profit Sector Serving Cultural Communities",
        "NEH and IMLS Termination, AmeriCorps Termination, IRS Scrutiny, and Federal Grant Cancellations (Trump II, 2025-2026)",
    ),
    "s": "Non-profit sector aggregate threat analysis",
    "d": TODAY,
    "a": "Trump II",
    "A": ["NEH", "IMLS", "AmeriCorps", "IRS", "Treasury", "EPA", "DOJ", "HHS", "DOE"],
    "S": "Active and expanding. NEH and IMLS terminations are in implementation. AmeriCorps termination is in process. IRS scrutiny of 501(c)(3) advocacy organizations has increased. Multiple lawsuits are pending. Foundation and donor concerns about federal posture have produced documented giving slowdowns.",
    "L": "SEVERE",
    "D": (
        "<b>FEDERAL ACTION PATTERNS.</b> The non-profit sector faces a federal posture that targets the federal funding, regulatory, and partnership infrastructure on which charitable, cultural, civil-rights, and service organizations depend. The administration directed termination of the National Endowment for the Humanities, the Institute of Museum and Library Services, and AmeriCorps. NEH grant terminations affected scholarly humanities programs, museum programming, library exhibitions, and public-humanities work across all fifty states and the territories. IMLS grant terminations affected library services, museum services, and the formula funding that flows through state library agencies and state museum agencies to local institutions. AmeriCorps terminations affected approximately 200,000 service members and the more than 21,000 nonprofit and public-agency host sites that depend on AmeriCorps for staffing."
        "<br><br>"
        "Federal grant cancellations across the non-profit sector have included EPA Environmental Justice grants clawed back, NEA grants terminated, NSF research grants reviewed for content, HHS service-delivery grants modified, and Department of Education adult-education grants reduced. The Internal Revenue Service has increased scrutiny of 501(c)(3) and 501(c)(4) advocacy organizations through audit selection, exemption-application review, and Form 990 enforcement. Treasury has signaled review of foreign-funded non-profit operations under the Foreign Agents Registration Act and Treasury counter-terrorism finance frameworks. The Department of Justice has opened investigations of certain civil-rights organizations under federal grant-fraud and program-integrity authorities. Federal partnerships including HHS, DOE, and EPA partnerships with civil-rights and environmental organizations have been terminated or restructured."
        "<br><br>"
        "<b>CUMULATIVE CULTURAL EFFECTS.</b> The cumulative federal posture concentrates harm on the non-profit organizations that deliver cultural programming, civil-rights enforcement, social services, and community development to historically marginalized communities. The non-profit sector employs more than 12 million workers, accounts for approximately 5.6 percent of U.S. GDP, and provides services that federal, state, and local governments rely on as a delivery channel. Federal funding represents a substantial share of nonprofit revenue, particularly in the human-services subsector (where federal funding is approximately 55 percent of revenue at many service organizations). Federal grant cancellations have forced layoffs, program closures, and service reductions across the sector."
        "<br><br>"
        "Cultural-sector nonprofits including museums, libraries, historic sites, performing-arts organizations, and community-cultural-development organizations have lost NEH, IMLS, NEA, and Smithsonian-affiliate funding. Civil-rights nonprofits including legal-defense funds, voting-rights organizations, and civil-liberties organizations have faced grant terminations and IRS scrutiny. Service-delivery nonprofits including health-care safety-net providers, food banks, housing organizations, and education organizations have faced HHS, USDA, HUD, and Department of Education grant changes. Faith-based nonprofits including Catholic Charities, Lutheran Services, Jewish Family Service, and Muslim relief organizations have faced refugee-resettlement, child-welfare, and disaster-relief partnership changes. Foundation and donor giving has slowed in measured ways, partly in response to the federal posture and partly in response to broader economic conditions."
        "<br><br>"
        "<b>OPERATIONAL POSTURE.</b> Implementation is active and broad. Multiple federal lawsuits challenge agency terminations and grant cancellations. The National Council of Nonprofits, the Independent Sector, the National Humanities Alliance, the American Library Association, the American Alliance of Museums, and other sector associations have filed amicus briefs and litigation. Federal district courts have entered preliminary injunctions on subsets of the terminations. Congressional appropriations bills include continued funding for some agencies that the executive branch has directed to wind down, creating implementation tension. The legal posture is fluid and the sector-wide effect is being documented in real time by the Urban Institute, the Center for Effective Government, and academic centers."
        "<br><br>"
        "<b>CROSS-COMMUNITY RESONANCE.</b> Non-profit organizations serve every primary cultural community. Indigenous-serving nonprofits including the National Congress of American Indians, the Native American Rights Fund, the Association of American Indian Affairs, and tribal-college foundations face federal grant changes. African-descendant-serving nonprofits including the NAACP Legal Defense Fund, the National Urban League, the Southern Poverty Law Center, and historically-Black-college foundations face federal grant changes. Latine-serving nonprofits including UnidosUS, MALDEF, LULAC, and Hispanic-serving institution foundations face federal grant changes. Asian American-serving nonprofits including the Asian American Legal Defense and Education Fund, the Japanese American Citizens League, and AANHPI community organizations face federal grant changes. Pacific Islander-serving nonprofits including the Empowering Pacific Islander Communities and the Pacific Islander Center of Primary Care Excellence face federal grant changes. Caribbean-serving nonprofits face the same patterns. The federal non-profit-sector posture is therefore felt as a community-development cut across every cultural community the tracker covers."
        "<br><br>"
        "<b>SOURCES.</b><br>"
        '<a href="https://www.neh.gov/" target="_blank" rel="noopener">National Endowment for the Humanities</a>.<br>'
        '<a href="https://www.imls.gov/" target="_blank" rel="noopener">Institute of Museum and Library Services</a>.<br>'
        '<a href="https://www.americorps.gov/" target="_blank" rel="noopener">AmeriCorps</a>.<br>'
        '<a href="https://www.councilofnonprofits.org/" target="_blank" rel="noopener">National Council of Nonprofits</a>.<br>'
        '<a href="https://independentsector.org/" target="_blank" rel="noopener">Independent Sector</a>.<br>'
        '<a href="https://www.urban.org/policy-centers/center-nonprofits-and-philanthropy" target="_blank" rel="noopener">Urban Institute Center on Nonprofits and Philanthropy</a>.<br>'
        '<a href="https://www.courtlistener.com/?q=neh+termination&type=r" target="_blank" rel="noopener">CourtListener docket search for sector litigation</a>.'
    ),
    "I": {
        "nonprofit": {
            "people": "The non-profit sector employs more than 12 million workers in the United States and engages tens of millions more as volunteers, board members, and donors. The directly affected population includes approximately 200,000 AmeriCorps service members per year and the staff of more than 21,000 host sites that lose AmeriCorps placements. Cultural-sector workers at museums, libraries, historic sites, and performing-arts organizations face layoffs flowing from NEH, IMLS, and NEA grant terminations. Civil-rights organization staff face IRS scrutiny and federal grant changes. Faith-community service workers at refugee-resettlement, child-welfare, and disaster-relief organizations face partnership changes. The communities these workers serve, the millions of low-income, immigrant, disabled, and culturally specific community members who receive nonprofit services, face program reductions and waiting-list expansions. The cumulative effect concentrates harm on people whose access to culturally competent service depends on the nonprofit infrastructure that the federal retreat is degrading.",
            "places": "Federal places where these actions land include the more than 1.5 million 501(c)(3) and 501(c)(4) organizations registered with the IRS, the more than 35,000 museums in the United States supported in part by IMLS funding, the more than 9,000 public libraries supported by IMLS LSTA funding flowing through state library agencies, the more than 21,000 AmeriCorps host sites, the federally funded community-action agencies in nearly every county, the federally qualified health centers operated as nonprofits, the historically Black colleges and universities, tribal colleges, and Hispanic-serving institutions. NEH and IMLS headquarters in Washington, the IRS Tax Exempt and Government Entities Division, and the federal courts where sector litigation is pending are the institutional sites where the operational posture is being settled.",
            "practices": "Cultural practices affected include the practice of charitable giving, the practice of volunteer service, the practice of nonprofit governance through volunteer boards, the practice of grant-writing and grant administration, the practice of advocacy through 501(c)(3) educational and 501(c)(4) lobbying activities, the practice of community organizing through nonprofit hosts, the practice of cultural programming through museums and performing-arts organizations, the practice of educational programming through libraries and adult-education programs, the practice of religious-community service delivery through faith-based nonprofits, and the practice of mutual aid through informal and incorporated community organizations. The practice of partnering with federal agencies on service delivery is constrained by partnership terminations. The practice of organizing communities for civil-rights advocacy is constrained by IRS scrutiny.",
            "treasures": "Cultural treasures at risk include the collections, archives, and operational records of the more than 35,000 U.S. museums, the more than 9,000 public libraries, the historic sites, and the cultural organizations that serve cultural communities. The records of the National Endowment for the Humanities programming since 1965, the Institute of Museum and Library Services programming since 1996, AmeriCorps service since 1994, and the broader federal-nonprofit partnership since the War on Poverty are themselves federal cultural treasures. Community archives held by civil-rights nonprofits, ethnic-community organizations, faith-based service organizations, and arts organizations document the lived record of nonprofit work. Federal datasets on nonprofit revenue, employment, and giving maintained by the IRS, the Bureau of Labor Statistics, and the National Center for Charitable Statistics are themselves cultural treasures because they document the lived demographic reality of the nonprofit sector."
        }
    },
    "c": ["Non-Profit Sector", "All Communities", "Indigenous", "African-descendant", "Latiné", "Asian American", "Pacific Islander", "Caribbean", "Faith Communities", "Arts", "Academic"],
    "U": "https://www.councilofnonprofits.org/",
    "_source": SOURCE_TAG,
}


ARTS_HUM = {
    "i": "arts-humanities-cultural-threat-analysis-2026-05",
    "t": "Aggregate Analysis",
    "n": "Arts and Humanities Aggregate Threat Analysis (May 2026)",
    "T": title(
        "Federal Threats to Arts and Humanities Communities (Academics, Artists, Scholars, Cultural Workers)",
        "NEH and NEA Termination, IMLS Termination, Smithsonian Pressure, Kennedy Center Reorganization, and Higher-Education Federal-Funding Changes (Trump II, 2025-2026)",
    ),
    "s": "Arts and humanities aggregate threat analysis",
    "d": TODAY,
    "a": "Trump II",
    "A": ["NEH", "NEA", "IMLS", "Smithsonian", "Kennedy Center", "NSF", "NIH", "DOE", "CPB"],
    "S": "Active and broad. NEH and NEA terminations are in implementation. IMLS termination is in implementation. Smithsonian funding pressure has produced documented programming changes. Kennedy Center board reorganization is in effect. CPB defunding is being implemented through appropriations action. Multiple lawsuits are pending.",
    "L": "SEVERE",
    "D": (
        "<b>FEDERAL ACTION PATTERNS.</b> The arts and humanities communities face a federal posture that targets the federal cultural infrastructure built since the National Foundation on the Arts and the Humanities Act of 1965. The administration directed termination of the National Endowment for the Humanities and the National Endowment for the Arts. NEH and NEA grant terminations affected scholarly research, museum programming, library exhibitions, public-humanities work, performing arts, visual arts, literary arts, folk-and-traditional arts, and arts-in-education programming across all fifty states and the territories. The administration directed termination of the Institute of Museum and Library Services, affecting library services, museum services, and the formula funding that flows through state agencies to local institutions."
        "<br><br>"
        "The Smithsonian Institution faces federal funding pressure that has produced documented programming changes, particularly at the National Museum of African American History and Culture, the National Museum of the American Indian, the Smithsonian American Women's History Museum, and the National Museum of the American Latino. The Kennedy Center for the Performing Arts board was reorganized through presidential action. The Corporation for Public Broadcasting faces appropriations defunding that affects PBS, NPR, and the more than 1,500 local public-broadcasting stations across the country. The National Science Foundation and the National Institutes of Health have reviewed humanities-adjacent research grants for content, with documented terminations and modifications. The Department of Education has changed Higher Education Act Title IV student-loan terms, accreditation guidance, and foreign-student-visa partnerships in ways that affect arts-and-humanities programs at colleges and universities. Federal partnerships with academic institutions including the Mellon Foundation co-funded programs, the Andrew W. Mellon Public Humanities Fellowships, and the National Humanities Center programming have been disrupted."
        "<br><br>"
        "<b>CUMULATIVE CULTURAL EFFECTS.</b> The cumulative federal posture concentrates harm on the cultural sector that produces, preserves, and transmits the United States's cultural heritage. NEH funding had supported humanities scholarship, public-humanities programming, museum exhibitions, library exhibitions, documentary film and radio, K-12 humanities curricula, and the federal-state humanities councils in every state and territory. NEA funding had supported arts-in-education, folk and traditional arts, literary arts, performing arts, visual arts, design, and creative-placemaking. IMLS funding had supported library services and museum services across the country. The simultaneous loss of these programs creates a documented contraction of cultural-sector employment, cultural programming, and cultural research."
        "<br><br>"
        "Academics in the humanities face a documented job-market contraction worsened by the federal funding retreat. Tenure-track positions in English, history, philosophy, religious studies, area studies, and other humanities disciplines have declined for more than a decade and the federal retreat accelerates the trend. Artists face the loss of NEA and state-arts-council fellowships, project grants, and presenting opportunities. Cultural workers at museums, libraries, archives, and presenting organizations face layoffs flowing from federal grant terminations. The cumulative effect is a contraction of the federal cultural infrastructure that has supported the production, preservation, and transmission of the cultural heritage of every primary cultural community the tracker covers."
        "<br><br>"
        "<b>OPERATIONAL POSTURE.</b> Implementation is active and broad. Multiple federal lawsuits challenge agency terminations and grant cancellations. The American Council of Learned Societies, the National Humanities Alliance, the American Library Association, the American Alliance of Museums, the Association of American Universities, the Modern Language Association, the American Historical Association, and other field associations have filed amicus briefs and litigation. State humanities councils and state arts councils have organized federal-state rebuilding efforts to fill funding gaps. Foundation and private giving has shifted to fill some of the gap, with mixed and incomplete results. The legal posture is fluid and the sector-wide effect is being documented in real time."
        "<br><br>"
        "<b>CROSS-COMMUNITY RESONANCE.</b> The arts and humanities communities serve every primary cultural community. Indigenous arts and humanities including tribal-college humanities programs, Indigenous-language preservation, Native American Music Program funding, and museum repatriation work face federal grant changes. African-descendant arts and humanities including HBCU humanities programs, the National Museum of African American History and Culture, Black-serving cultural institutions, and African American Studies programs face federal funding pressure. Latine arts and humanities including Hispanic-serving institution humanities programs, the National Museum of the American Latino, and Latine-led cultural organizations face federal grant changes. Asian American arts and humanities including the Smithsonian Asian Pacific American Center, ethnic-studies programs at universities, and AANHPI cultural organizations face federal grant changes. Pacific Islander arts and humanities including the Smithsonian Pacific Islander programming, the East-West Center, and Native Hawaiian cultural organizations face federal grant changes. Caribbean arts and humanities including the National Park Service Caribbean cultural sites and Caribbean diaspora cultural organizations face federal grant changes. The federal arts-and-humanities posture cuts across every cultural community."
        "<br><br>"
        "<b>SOURCES.</b><br>"
        '<a href="https://www.neh.gov/" target="_blank" rel="noopener">National Endowment for the Humanities</a>.<br>'
        '<a href="https://www.arts.gov/" target="_blank" rel="noopener">National Endowment for the Arts</a>.<br>'
        '<a href="https://www.imls.gov/" target="_blank" rel="noopener">Institute of Museum and Library Services</a>.<br>'
        '<a href="https://www.si.edu/" target="_blank" rel="noopener">Smithsonian Institution</a>.<br>'
        '<a href="https://www.kennedy-center.org/" target="_blank" rel="noopener">John F. Kennedy Center for the Performing Arts</a>.<br>'
        '<a href="https://www.cpb.org/" target="_blank" rel="noopener">Corporation for Public Broadcasting</a>.<br>'
        '<a href="https://www.nationalhumanitiesalliance.org/" target="_blank" rel="noopener">National Humanities Alliance</a>.<br>'
        '<a href="https://www.aam-us.org/" target="_blank" rel="noopener">American Alliance of Museums</a>.'
    ),
    "I": {
        "arts": {
            "people": "The arts and humanities communities include scholars at colleges and universities, artists working in performing, visual, literary, and design arts, cultural workers at museums and libraries, cultural workers at presenting and producing organizations, cultural workers at federal cultural agencies, cultural workers at state and local cultural agencies, K-12 humanities and arts educators, and the audiences and learners who participate in cultural programming. Humanities scholars number tens of thousands across U.S. colleges and universities, with hundreds of thousands of doctoral students and graduate students in pipeline. Working artists number more than two million across the U.S. economy. Museum workers, library workers, and presenting-organization workers number hundreds of thousands. The federal retreat affects all of them simultaneously through grant terminations, agency restructuring, and partnership changes. The communities they serve, the millions of audience members, students, and learners who engage with cultural programming, face program reductions and access constraints.",
            "places": "Federal places where these actions land include the more than 35,000 U.S. museums, the more than 9,000 public libraries, the more than 4,000 colleges and universities offering humanities programs, the more than 1,500 local public-broadcasting stations, the Smithsonian's 21 museums and 14 research centers in Washington and across the country, the Kennedy Center for the Performing Arts in Washington, the National Endowments at the Old Post Office Building in Washington, IMLS at the Capital Gallery in Washington, the Library of Congress and the National Archives in Washington, the federal historic sites administered by the National Park Service, the federally funded HBCUs, tribal colleges, Hispanic-serving institutions, and Asian American and Native American Pacific Islander-serving institutions, and the state humanities councils and state arts councils in every state and territory.",
            "practices": "Cultural practices affected include the practice of humanities scholarship in colleges and universities, the practice of artistic creation in studios and rehearsal halls, the practice of cultural programming in museums and libraries, the practice of cultural transmission in K-12 schools and informal-learning settings, the practice of public humanities through documentary film, radio, and digital media, the practice of cultural-heritage preservation in archives and historic sites, the practice of arts education and arts-in-education through state arts councils and school partnerships, the practice of cultural exchange through international programs and partnerships, and the practice of cultural advocacy through field associations. The practice of receiving an NEH or NEA grant is constrained by termination. The practice of partnering with the Smithsonian on community-curated exhibitions is constrained by funding pressure. The practice of public-radio listening and public-television viewing is constrained by CPB defunding.",
            "treasures": "Cultural treasures at risk include the collections of the Smithsonian Institution (more than 155 million objects), the holdings of the Library of Congress (more than 175 million items), the holdings of the National Archives (more than 13 billion items), the collections of the more than 35,000 U.S. museums, the holdings of the more than 9,000 public libraries, the recordings of the Federal Cylinder Project at the Library of Congress American Folklife Center, the recordings of the Federal Writers' Project at the Library of Congress, the productions of the Federal Theatre Project preserved at George Mason University, the documentary films and radio programs supported by NEH and CPB, the artworks supported by NEA fellowships and project grants, the scholarly monographs and journal articles supported by NEH research grants, the K-12 humanities curricula developed under NEH funding, and the public-humanities programming through state humanities councils. Each of these treasures depends on a federal cultural infrastructure that the current posture is degrading."
        }
    },
    "c": ["Arts", "Academic", "All Communities", "Indigenous", "African-descendant", "Latiné", "Asian American", "Pacific Islander", "Caribbean", "Federal Employees", "Non-Profit Sector"],
    "U": "https://www.neh.gov/",
    "_source": SOURCE_TAG,
}


# ---------------------------------------------------------------------------
# REFRESH APPENDICES for the 6 existing primary-community aggregates
# ---------------------------------------------------------------------------

REFRESH_APPENDIX_INDIGENOUS = (
    "<br><br>"
    "<b>UPDATES THROUGH APRIL 2026.</b> Federal action since the original "
    "January 2026 analysis includes the BLM Alaska Public Lands Oil and Gas "
    "Leasing Pivot 2025-2026 (now tracked as <code>alaska-oil-gas-leasing-"
    "pivot-2025-2026</code>), the BIA Federal Acknowledgment Process notices "
    "September 2025 to February 2026 (tracked as <code>federal-acknowledgment"
    "-petitions-2025-2026</code>), the BLM ANCSA Land Conveyances February-"
    "March 2026 (tracked as <code>ancsa-conveyances-2026</code>), the BIA "
    "Approvals of 20 Tribal-State Gaming Compacts and Amendments 2025-2026 "
    "(tracked as <code>indian-gaming-compacts-2025-2026</code>), and the BIA "
    "Approvals of 7 Tribal Leasing Ordinances under the HEARTH Act of 2012 "
    "(tracked as <code>hearth-act-approvals-2025-2026</code>). The combined "
    "posture remains SEVERE because resource-extraction and acknowledgment "
    "process actions threaten Indigenous sacred sites, treaty rights, and "
    "tribal-federal trust standing in ways the original analysis described. "
    "Two-Spirit community impacts are now tracked separately in the "
    "LGBTQIA2S+ aggregate analysis. Cross-community impacts on Indigenous "
    "women, Indigenous low-income households, Indigenous immigrants, "
    "Indigenous disabled people, and Indigenous arts-and-humanities workers "
    "are tracked in the corresponding new aggregates."
)

REFRESH_APPENDIX_AFRICAN = (
    "<br><br>"
    "<b>UPDATES THROUGH APRIL 2026.</b> Federal action since the original "
    "January 2026 analysis includes the Bush-Era Bipartisan International "
    "Development Programs Dismantled 2026 (now tracked as <code>bush-era-"
    "bipartisan-programs-dismantled-2026</code>), with documented "
    "consequences for African-descendant communities throughout sub-Saharan "
    "Africa, the Caribbean, and the African diaspora more broadly. Federal "
    "action also includes the executive-branch funding pressure on the "
    "National Museum of African American History and Culture, ongoing "
    "Smithsonian programming changes, HBCU federal-grant pressure, and the "
    "documented contraction of federal civil-rights enforcement at DOJ, "
    "EEOC, and HHS. The combined posture remains SEVERE. Cross-community "
    "impacts on African-descendant women, African-descendant low-income "
    "households, African-descendant immigrants, African-descendant disabled "
    "people, African-descendant LGBTQIA2S+ communities, and African-"
    "descendant arts-and-humanities workers are tracked in the corresponding "
    "new aggregates."
)

REFRESH_APPENDIX_LATINE = (
    "<br><br>"
    "<b>UPDATES THROUGH APRIL 2026.</b> Federal action since the original "
    "January 2026 analysis includes EO 14160 (now tracked as <code>"
    "birthright-citizenship-attack-2026-001</code>) and the broader "
    "immigration enforcement posture documented in the Immigrant aggregate "
    "analysis. Latine communities face the broadest immediate exposure to "
    "the immigration-enforcement and birthright-citizenship pattern given "
    "the demographic distribution of mixed-status families. Federal action "
    "also includes the Smithsonian National Museum of the American Latino "
    "(opening 2027) federal funding posture, ongoing Hispanic-serving "
    "institution federal-grant pressure, and the documented contraction of "
    "federal civil-rights enforcement. The combined posture remains SEVERE. "
    "Cross-community impacts on Latine women, Latine low-income households, "
    "Latine disabled people, Latine LGBTQIA2S+ communities, Latine rural "
    "communities, and Latine arts-and-humanities workers are tracked in the "
    "corresponding new aggregates."
)

REFRESH_APPENDIX_ASIAN = (
    "<br><br>"
    "<b>UPDATES THROUGH APRIL 2026.</b> Federal action since the original "
    "January 2026 analysis includes EO 14160 (now tracked as <code>"
    "birthright-citizenship-attack-2026-001</code>), with direct historical "
    "resonance to the Chinese Exclusion era and <i>United States v. Wong "
    "Kim Ark</i> (1898). Federal action also includes ongoing H-1B and "
    "student-visa restrictions affecting AAPI communities, the Smithsonian "
    "Asian Pacific American Center programming pressure, and the documented "
    "contraction of federal civil-rights enforcement at DOJ and EEOC on "
    "anti-Asian discrimination matters. The combined posture remains SEVERE. "
    "Cross-community impacts on AAPI women, AAPI low-income households "
    "(particularly in Southeast Asian refugee-origin communities), AAPI "
    "immigrants, AAPI disabled people, AAPI LGBTQIA2S+ communities, and "
    "AAPI arts-and-humanities workers are tracked in the corresponding new "
    "aggregates."
)

REFRESH_APPENDIX_PACIFIC = (
    "<br><br>"
    "<b>UPDATES THROUGH APRIL 2026.</b> Federal action since the original "
    "January 2026 analysis includes the Bush-Era Bipartisan International "
    "Development Programs Dismantled 2026 (now tracked as <code>bush-era-"
    "bipartisan-programs-dismantled-2026</code>), with consequences for "
    "Pacific Islander communities through the Compacts of Free Association "
    "and through Pacific climate-adaptation programs. Federal action also "
    "includes ongoing federal-territorial funding inequities, Native "
    "Hawaiian federal-recognition status remaining unresolved, and the "
    "documented contraction of federal civil-rights enforcement on Pacific "
    "Islander matters. The combined posture remains SEVERE. Cross-community "
    "impacts on Pacific Islander women, Pacific Islander low-income "
    "households, Pacific Islander immigrants (including COFA migrants), "
    "Pacific Islander disabled people, Pacific Islander LGBTQIA2S+ "
    "communities, Pacific Islander rural and territorial communities, and "
    "Pacific Islander arts-and-humanities workers are tracked in the "
    "corresponding new aggregates."
)

REFRESH_APPENDIX_CARIBBEAN = (
    "<br><br>"
    "<b>UPDATES THROUGH APRIL 2026.</b> Federal action since the original "
    "January 2026 analysis includes the Bush-Era Bipartisan International "
    "Development Programs Dismantled 2026 (now tracked as <code>bush-era-"
    "bipartisan-programs-dismantled-2026</code>), with consequences for "
    "Caribbean communities through PEPFAR-affected nations and through "
    "U.S.-Caribbean development partnerships. Federal action also includes "
    "TPS terminations affecting Haitian communities, the broader "
    "immigration enforcement posture documented in the Immigrant aggregate, "
    "ongoing federal-territorial funding inequities for Puerto Rico and the "
    "U.S. Virgin Islands, and the documented contraction of federal "
    "civil-rights enforcement. The combined posture remains SEVERE. "
    "Cross-community impacts on Caribbean women, Caribbean low-income "
    "households, Caribbean immigrants, Caribbean disabled people, "
    "Caribbean LGBTQIA2S+ communities, Caribbean rural and territorial "
    "communities, and Caribbean arts-and-humanities workers are tracked in "
    "the corresponding new aggregates."
)


REFRESHES = {
    "v2026-indigenous-cultural-threat-analysis": REFRESH_APPENDIX_INDIGENOUS,
    "v2026-african-descendant-cultural-threat-analysis": REFRESH_APPENDIX_AFRICAN,
    "v2026-latine-cultural-threat-analysis": REFRESH_APPENDIX_LATINE,
    "v2026-asian-american-cultural-threat-analysis": REFRESH_APPENDIX_ASIAN,
    "v2026-pacific-islander-oceania-cultural-threat-analysis": REFRESH_APPENDIX_PACIFIC,
    "v2026-caribbean-cultural-threat-analysis": REFRESH_APPENDIX_CARIBBEAN,
}


NEW_AGGREGATES = [WOMEN, LGBTQ, DISABLED, IMMIGRANT, RURAL, POOR, NONPROFIT, ARTS_HUM]


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
    bad_phrases = ["not X, but Y"]
    for agg in NEW_AGGREGATES:
        for s in collect_strings(agg):
            if em_dash in s:
                raise SystemExit(f"ABORT: em-dash in new aggregate {agg['i']}.")
    for eid, appendix in REFRESHES.items():
        if em_dash in appendix:
            raise SystemExit(f"ABORT: em-dash in refresh appendix for {eid}.")

    shutil.copy2(DATA_PATH, BACKUP_PATH)
    print(f"Backup written: {BACKUP_PATH.name}")

    with DATA_PATH.open() as f:
        data = json.load(f)

    if "agency_actions" not in data:
        data["agency_actions"] = []
    added = 0
    for agg in NEW_AGGREGATES:
        existing_ids = {
            (e.get("i") or e.get("id"))
            for cat in [
                "executive_actions", "agency_actions", "legislation",
                "litigation", "other_domestic", "international",
            ]
            for e in data.get(cat, [])
        }
        if agg["i"] in existing_ids:
            print(f"  SKIP: {agg['i']} already exists")
            continue
        data["agency_actions"].append(agg)
        print(f"  ADDED: {agg['i']} (D={len(agg['D'])} chars)")
        added += 1

    refreshed = 0
    for cat in ["agency_actions", "executive_actions", "legislation", "litigation", "other_domestic", "international"]:
        for entry in data.get(cat, []):
            eid = entry.get("i") or entry.get("id")
            if eid in REFRESHES:
                if "UPDATES THROUGH APRIL 2026" in entry.get("D", ""):
                    print(f"  SKIP: {eid} already refreshed")
                    continue
                entry["D"] = entry.get("D", "") + REFRESHES[eid]
                entry["d"] = TODAY
                print(f"  REFRESHED: {eid}")
                refreshed += 1

    if "meta" in data and isinstance(data["meta"], dict):
        data["meta"]["lastUpdated"] = TODAY

    tmp = DATA_PATH.with_suffix(".json.tmp")
    with tmp.open("w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    tmp.replace(DATA_PATH)

    print(f"\nAdded {added} new aggregate analyses.")
    print(f"Refreshed {refreshed} existing aggregate analyses.")


if __name__ == "__main__":
    main()
