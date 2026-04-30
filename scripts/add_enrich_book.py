#!/usr/bin/env python3
"""Add Nicholas Enrich's whistleblower memoir to the tracker.

Book: "Into the Wood Chipper: A Whistleblower's Account of How the
Trump Administration Shredded USAID" (Simon & Schuster / Summit Books,
April 14, 2026; introduction by Atul Gawande).

Author: Nicholas Enrich, former Acting Assistant Administrator for
Global Health at USAID, pushed out in early 2025.

Category: international. The book documents the dismantling of USAID
and projects the international mortality consequences.

Threat level: SEVERE. The federal actions the book documents have
already produced near-term mortality and project to ~14 million
preventable deaths by 2030 per peer-reviewed Lancet analysis.
"""
import json
import shutil
from pathlib import Path
from datetime import datetime

DATA_PATH = Path(__file__).parent.parent / "data" / "data.json"
BACKUP_PATH = DATA_PATH.with_suffix(
    f".json.bak-{datetime.now().strftime('%Y%m%d-%H%M%S')}-pre-enrich-book"
)

NEW_ID = "enrich-wood-chipper-book-2026"

ENTRY = {
    "i": NEW_ID,
    "t": "Whistleblower Memoir",
    "n": "Nicholas Enrich, \"Into the Wood Chipper: A Whistleblower's Account of How the Trump Administration Shredded USAID\" (Summit Books / Simon & Schuster, April 14, 2026; introduction by Atul Gawande)",
    "T": '<span style="color: #991B1B;">Whistleblower Memoir:</span> Nicholas Enrich, "Into the Wood Chipper." Former USAID Acting Assistant Administrator for Global Health Documents DOGE Shredding of the Agency',
    "s": "Enrich Wood Chipper memoir",
    "d": "2026-04-14",
    "a": "Trump II",
    "A": ["USAID", "DOGE", "State"],
    "S": "Published April 14, 2026 by Summit Books, an imprint of Simon & Schuster. New York Times bestseller. Introduction by Atul Gawande. ISBN 978-1668226957 (hardcover); 978-1668161982 (paperback); 978-1668161968 (audiobook). Author Nicholas Enrich previously served as Acting Assistant Administrator for Global Health at USAID and was pushed out in early 2025.",
    "L": "SEVERE",
    "D": (
        "<b>WHISTLEBLOWER MEMOIR.</b> On April 14, 2026, Summit Books (an imprint of Simon & Schuster) published \"Into the Wood Chipper: A Whistleblower's Account of How the Trump Administration Shredded USAID\" by Nicholas Enrich. The book carries an introduction by physician-author Atul Gawande and reached the New York Times bestseller list. Enrich previously served as Acting Assistant Administrator for Global Health at the United States Agency for International Development (USAID) and was pushed out of the agency in early 2025 during the Department of Government Efficiency (DOGE) takeover led by Elon Musk.<br><br>"
        "<b>BOOK TITLE PROVENANCE.</b> The title quotes Elon Musk's X post of February 3, 2025: \"We spent the weekend feeding USAID into the wood chipper. Could gone to some great parties. Did that instead.\" The morning after the post, USAID's doors were closed to employees, the agency's logos and photographs of aid work were stripped from the building's walls, and its website and social-media accounts were taken down. (Primary source: <a href=\"https://x.com/elonmusk/status/1886307316804263979\">https://x.com/elonmusk/status/1886307316804263979</a>.)<br><br>"
        "<b>PRINCIPAL CLAIMS DOCUMENTED IN THE BOOK.</b> Enrich provides first-person testimony of decisions made inside USAID between February and his ouster in early 2025. The book documents: (1) a February 5, 2025 meeting at the Reagan Building where political appointees told career staff \"in full transparency, we're drawing down USAID\" and asked staff to walk them through \"mission-critical functions so that we can close things out smoothly\" (Joel Borkert, USAID chief of staff); (2) Borkert's stated assumption that USAID's global-health portfolio was \"just, you know, abortions\"; (3) Adam Korzeniewski (White House liaison) requesting \"Barney-style\" slides to explain drug-resistant tuberculosis risks and proposing the term \"Super TB\"; (4) Paul Seong (senior advisor) instructing staff to focus only on \"lifesaving stuff\" and deprioritizing maternal health as a \"number two\" concern; (5) the dismantling of clinical-trial infrastructure for drug-resistant tuberculosis with thousands of enrolled patients mid-treatment; (6) the layoff of all but 611 of more than 10,000 USAID employees; (7) the broader pattern in which political appointees with no public-health background made categorical decisions over the objection of career experts. Career colleague Ramona Godbole's stated reaction in the book: \"They're asking us to dig our own grave.\"<br><br>"
        "<b>PROJECTED MORTALITY.</b> Enrich states in interviews accompanying the book that an estimated 14 million people are projected to die \"unnecessarily\" over the next five years due to the USAID cuts and that nearly a million people, mostly children, have already died. These projections track the peer-reviewed Lancet analysis (\"Evaluating the impact of two decades of USAID interventions and projecting the effects of defunding on mortality up to 2030\") which found that USAID interventions prevented an estimated 91 million deaths across 133 countries between 2001 and 2021 and projected more than 14 million avoidable deaths by 2030 from the cuts, including more than 4.5 million children under age five (approximately 700,000 child deaths per year).<br><br>"
        "<b>ENRICH'S OPERATIVE STATEMENT.</b> Enrich states: \"We pulled the rug out from under people around the world. We broke promises to millions who were relying on USAID services, and left them hanging out to dry. We broke promises to governments and broke partnerships that will have lasting effects for years to come.\"<br><br>"
        "<b>RELATIONSHIP TO TCKC PRIMARY COMMUNITIES.</b> USAID's global-health, food-security, and maternal-and-child-health programs operated in countries with deep diaspora ties to all five TCKC primary cultural communities. PEPFAR (the President's Emergency Plan for AIDS Relief) and USAID HIV/AIDS, malaria, and tuberculosis programs operated heavily across sub-Saharan Africa (African-descendant diaspora ties), in Latin America and the Caribbean (Latiné and African-descendant diaspora ties), in South and Southeast Asia (Asian diaspora ties), and across the Pacific (Pacific Islander diaspora ties). USAID Indigenous-peoples and tribal-rights programs supported Indigenous communities in Latin America and elsewhere. Cuts to these programs sever long-term federal commitments to communities whose diaspora kin live in the United States and constitute a measurable harm to transnational kinship and remittance economies that sustain cultural continuity.<br><br>"
        "<b>RELATIONSHIP TO RELATED TRACKER ENTRIES.</b> The underlying federal actions are tracked at intl-2026-usaid-shutdown-001 (USAID Shutdown Anniversary, March 18, 2026, projecting 9.4 million additional deaths) and intl-2026-pepfar-cuts-001 (PEPFAR $4.2 billion cut projecting 600,000 additional deaths). The DOGE one-year report on workforce purges including USAID is tracked at eo-2026-doge-anniversary. The Enrich memoir provides the first-person primary-source account of the decisions documented at those entries.<br><br>"
        "<b>CULTURAL RESOURCE THREAT ASSESSMENT.</b> The threat level is SEVERE. The federal actions Enrich documents have produced near-term mortality at the scale of nearly a million people in the first year and project to approximately 14 million deaths by 2030 under peer-reviewed analysis. The harms attack People (mortality and morbidity at scale), Practices (international public-health partnerships built over six decades), and Treasures (the institutional knowledge, programmatic infrastructure, and partner-government relationships that constituted USAID's operational capacity). The harms are partially irreversible. Patients enrolled in mid-treatment clinical trials cannot be returned to baseline. Children who die of untreated infection cannot be revived. Partner governments and partner NGOs that have lost funding mid-cycle cannot recover the operational continuity required to deliver life-saving services on the original timeline."
        "<br><br>"
        "<b>SOURCES.</b><br>"
        "Primary source: Nicholas Enrich (with introduction by Atul Gawande), \"Into the Wood Chipper: A Whistleblower's Account of How the Trump Administration Shredded USAID,\" Summit Books (Simon & Schuster), April 14, 2026. ISBN 978-1668226957 (hardcover); 978-1668161982 (paperback); 978-1668161968 (audiobook). Publisher page: <a href=\"https://www.simonandschuster.com/books/Into-the-Wood-Chipper/Nicholas-Enrich/9781668226957\">https://www.simonandschuster.com/books/Into-the-Wood-Chipper/Nicholas-Enrich/9781668226957</a><br>"
        "Primary social-media source for the title: Elon Musk on X, February 3, 2025. <a href=\"https://x.com/elonmusk/status/1886307316804263979\">https://x.com/elonmusk/status/1886307316804263979</a><br>"
        "Primary peer-reviewed mortality analysis: Cavalcanti et al., \"Evaluating the impact of two decades of USAID interventions and projecting the effects of defunding on mortality up to 2030,\" The Lancet (2025). <a href=\"https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(25)02016-1/fulltext\">https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(25)02016-1/fulltext</a>; authors' reply: <a href=\"https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(25)02203-2/fulltext?rss=yes\">https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(25)02203-2/fulltext?rss=yes</a><br>"
        "Author and book interviews: Democracy Now!, \"Into the Wood Chipper: Whistleblower's Inside Story of DOGE Shredding USAID, 14 Million May Die,\" April 16, 2026. <a href=\"https://www.democracynow.org/2026/4/16/usaid_whistleblower\">https://www.democracynow.org/2026/4/16/usaid_whistleblower</a>; "
        "MS NOW (Nicholas Enrich opinion), \"Why I blew the whistle on DOGE's reckless destruction of USAID.\" <a href=\"https://www.ms.now/opinion/usaid-whistleblower-doge-elon-musk-wood-chipper\">https://www.ms.now/opinion/usaid-whistleblower-doge-elon-musk-wood-chipper</a><br>"
        "Book exclusive: The Handbasket, \"Whistleblower says Trump officials thought USAID did 'just abortions,' asked for 'Barney-style' slides before gutting agency, per new book.\" <a href=\"https://www.thehandbasket.co/p/trump-usaid-abortions-barney-nicholas-enrich-into-the-wood-chipper-book-exclusive\">https://www.thehandbasket.co/p/trump-usaid-abortions-barney-nicholas-enrich-into-the-wood-chipper-book-exclusive</a><br>"
        "Secondary mortality coverage: NBC News, \"USAID cuts could lead to 14 million deaths over the next five years, researchers say.\" <a href=\"https://www.nbcnews.com/health/health-news/usaid-cuts-lead-14-million-deaths-five-years-researchers-say-rcna216095\">https://www.nbcnews.com/health/health-news/usaid-cuts-lead-14-million-deaths-five-years-researchers-say-rcna216095</a>; "
        "France 24, \"US foreign aid cuts could cause 14 million deaths by 2030, Lancet study finds.\" <a href=\"https://www.france24.com/en/americas/20250701-us-foreign-aid-cuts-could-cause-14-million-deaths-study-finds\">https://www.france24.com/en/americas/20250701-us-foreign-aid-cuts-could-cause-14-million-deaths-study-finds</a>; "
        "America Magazine, \"Trump closing U.S.A.I.D. could cost an estimated 14 million lives by 2030.\" <a href=\"https://www.americamagazine.org/politics-society/2025/07/02/usaid-lancet-humanitarian-aid-hunger-disease-14-million-deaths-251050/\">https://www.americamagazine.org/politics-society/2025/07/02/usaid-lancet-humanitarian-aid-hunger-disease-14-million-deaths-251050/</a>; "
        "UCLA Fielding School of Public Health, \"Research finds more than 14 million preventable deaths by 2030 if USAID defunding continues.\" <a href=\"https://ph.ucla.edu/news-events/news/research-finds-more-14-million-preventable-deaths-2030-if-usaid-defunding\">https://ph.ucla.edu/news-events/news/research-finds-more-14-million-preventable-deaths-2030-if-usaid-defunding</a>; "
        "Health Policy Watch, \"USAID Formally Shut Down - Days After Scientists Warn Closure Will Kill 2.4 Million People Every Year.\" <a href=\"https://healthpolicy-watch.news/usaid-shut-down-lancet-millions-deaths/\">https://healthpolicy-watch.news/usaid-shut-down-lancet-millions-deaths/</a><br>"
        "Vendor pages for legitimate acquisition: Politics and Prose Bookstore, <a href=\"https://politics-prose.com/nicolas-enrich41526\">https://politics-prose.com/nicolas-enrich41526</a>; Tattered Cover, <a href=\"https://www.tatteredcover.com/products/9781668226957\">https://www.tatteredcover.com/products/9781668226957</a>; Strand, <a href=\"https://www.strandbooks.com/into-the-wood-chipper-a-whistleblower-s-account-of-how-the-trump-administration-shredded-usaid-9781668226957.html\">https://www.strandbooks.com/into-the-wood-chipper-a-whistleblower-s-account-of-how-the-trump-administration-shredded-usaid-9781668226957.html</a>; Barnes & Noble, <a href=\"https://www.barnesandnoble.com/w/into-the-wood-chipper-nicholas-enrich/1149238610\">https://www.barnesandnoble.com/w/into-the-wood-chipper-nicholas-enrich/1149238610</a>.<br>"
        "Related tracker entries: intl-2026-usaid-shutdown-001 (USAID Shutdown Anniversary, March 18, 2026); intl-2026-pepfar-cuts-001 (PEPFAR $4.2 billion cut, March 1, 2026); eo-2026-doge-anniversary (DOGE one-year report, January 20, 2026)."
    ),
    "I": {
        "africanDescendant": {
            "people": "USAID's HIV/AIDS, malaria, tuberculosis, and maternal-and-child-health programs across sub-Saharan Africa served populations with deep diaspora ties to U.S.-based African-descendant communities. Enrich documents the categorical dismantling of these programs. Lancet analysis projects more than 4.5 million child deaths under age five by 2030 attributable to the cuts, with sub-Saharan Africa bearing the largest share. The harm to People is direct and quantified.",
            "places": "Health-systems infrastructure built across sub-Saharan Africa over six decades of USAID partnership, including clinics, supply chains, and laboratory networks, is being abandoned mid-cycle. The places where African-descendant diaspora kin receive care are being closed.",
            "practices": "International public-health practice between U.S. and African public-health institutions, including bilateral and multilateral partnerships, training programs, and clinical-trial collaborations, is being severed. Practices of cross-Atlantic public-health solidarity are losing their federal infrastructure.",
            "treasures": "The institutional knowledge embodied in USAID's career global-health staff, the partner-government relationships USAID built across decades, and the clinical and epidemiological data USAID maintained constitute cultural-and-scientific treasures whose loss Enrich documents."
        },
        "latine": {
            "people": "USAID's programs in Latin America and the Caribbean served populations with deep diaspora ties to U.S.-based Latiné communities. Programs supporting maternal health, child nutrition, infectious-disease control, food security, and disaster response have been dismantled. Mortality projections include avoidable deaths in Latin American partner countries.",
            "places": "USAID-supported clinics, food-distribution networks, and disaster-response infrastructure across Latin America and the Caribbean face closure. Partner-government health systems lose U.S. operational support mid-cycle.",
            "practices": "Hemispheric public-health practice between U.S. and Latin American institutions, including programs in Mexico, Central America, the Caribbean, and South America, is being severed.",
            "treasures": "Decades of Latin-American-U.S. public-health partnership institutional knowledge, including clinical-trial data, surveillance systems, and partner-government relationships, are being lost."
        },
        "asianAmerican": {
            "people": "USAID's programs in South Asia, Southeast Asia, and East Asia served populations with deep diaspora ties to U.S.-based Asian-American communities. Tuberculosis programs, including the drug-resistant TB clinical trials Enrich names specifically, have been dismantled mid-treatment.",
            "places": "Health infrastructure across South and Southeast Asia, including TB-treatment networks, malaria-control programs, and maternal-health systems, faces collapse.",
            "practices": "Trans-Pacific public-health practice and the global TB-control partnerships in which USAID was a foundational partner are being severed.",
            "treasures": "Clinical-trial data and partner-institution relationships in Asia, including with WHO regional offices and partner-country ministries of health, are being lost."
        },
        "pacificIslander": {
            "people": "USAID's programs in the Pacific served Pacific Islander populations with deep diaspora ties to U.S.-based Pacific Islander communities, including in COFA states (Marshall Islands, Federated States of Micronesia, Palau).",
            "places": "Climate-adaptation and public-health infrastructure across the Pacific Islands face collapse following USAID program cuts. Partner-government health systems in COFA states lose operational support.",
            "practices": "Pacific public-health and climate-resilience partnerships are being severed mid-cycle.",
            "treasures": "Pacific public-health institutional knowledge and partner-government relationships, including those tied to the U.S. trust relationship with COFA states, are being lost."
        },
        "indigenous": {
            "people": "USAID supported Indigenous-rights and Indigenous-health programs across Latin America, Africa, and Asia, including programs serving Indigenous communities in the Amazon basin, Mesoamerica, and other regions. Indigenous communities globally face direct harm from program cuts.",
            "places": "USAID-supported land-rights, forest-protection, and Indigenous-health-clinic networks face collapse.",
            "practices": "International Indigenous-rights solidarity practice between U.S. agencies and Indigenous-led organizations globally is being severed.",
            "treasures": "Indigenous-led documentation, traditional-medicine partnerships, and language-preservation programs that received USAID funding face the loss of operational support."
        },
        "lgbtq": {
            "people": "PEPFAR and USAID HIV/AIDS programs served LGBTQ+ populations in countries where domestic political environments make alternative funding sources scarce or impossible. The cuts disproportionately harm LGBTQ+ populations in the global south who depend on U.S.-funded harm-reduction, antiretroviral, and community-health services.",
            "places": "LGBTQ+-serving clinics and community-health centers funded by USAID and PEPFAR face closure across multiple regions.",
            "practices": "LGBTQ+-affirming public-health practice in countries hostile to it has depended on U.S. federal funding to insulate service delivery from domestic political backlash.",
            "treasures": "The institutional partnerships USAID built with LGBTQ+-led NGOs in the global south are being severed."
        }
    },
    "c": ["African-descendant", "Latiné", "Asian", "Pacific Islander", "Indigenous", "lgbtq", "All Communities"],
    "U": "https://www.simonandschuster.com/books/Into-the-Wood-Chipper/Nicholas-Enrich/9781668226957",
    "_source": "manual",
}


def main():
    if not DATA_PATH.exists():
        raise SystemExit(f"data.json not found at {DATA_PATH}")

    shutil.copy2(DATA_PATH, BACKUP_PATH)
    print(f"Backup written: {BACKUP_PATH.name}")

    em_dash = "—"
    if em_dash in json.dumps(ENTRY, ensure_ascii=False):
        raise SystemExit("ABORT: em-dash detected in entry.")

    with DATA_PATH.open() as f:
        data = json.load(f)

    international = data.get("international", [])
    if any((e.get("id") or e.get("i")) == NEW_ID for e in international):
        raise SystemExit(f"Entry {NEW_ID} already exists. Aborting.")

    international.append(ENTRY)
    data["international"] = international

    if "meta" in data and isinstance(data["meta"], dict):
        data["meta"]["lastUpdated"] = datetime.now().strftime("%Y-%m-%d")

    tmp = DATA_PATH.with_suffix(".json.tmp")
    with tmp.open("w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    tmp.replace(DATA_PATH)

    print(f"Inserted {NEW_ID} into international. Total international: {len(international)}.")


if __name__ == "__main__":
    main()
