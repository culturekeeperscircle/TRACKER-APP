"""CourtListener API client — federal litigation, court opinions."""
import requests
import logging
from ..config import COURTLISTENER_TOKEN
from ..utils.retry import retry_with_backoff
from .base import MultiQuerySourceConnector

logger = logging.getLogger('tckc_pipeline')

API_BASE = 'https://www.courtlistener.com/api/rest/v4'


@retry_with_backoff(max_retries=3, exceptions=(requests.RequestException,))
def search_opinions(query, filed_after, page=1):
    """Search court opinions."""
    headers = {'Authorization': f'Token {COURTLISTENER_TOKEN}'} if COURTLISTENER_TOKEN else {}
    params = {
        'q': query,
        'filed_after': filed_after,
        'order_by': 'dateFiled desc',
        'type': 'o',  # opinions
        'page': page,
    }
    resp = requests.get(f'{API_BASE}/search/', params=params, headers=headers, timeout=30)
    resp.raise_for_status()
    return resp.json()


class CourtListenerConnector(MultiQuerySourceConnector):
    source_name = 'courtlistener'
    category = 'litigation'
    max_per_query = 20

    # Replaced 2026-05-07. The previous 13 queries used implicit AND across all
    # terms, which silently narrowed results to opinions containing every word.
    # The new set uses explicit Boolean operators (OR / AND / parens) and
    # crosses each top-15 federal agency with cultural-community relevance.
    # See docs/[METHODOLOGY] Pipeline Queries and Research Questions Full
    # Disclosure for the full mapping and rationale.
    search_queries = [
        # ───── INDIGENOUS / TRIBAL ─────
        # DOI cluster (BIA, BLM, NPS, FWS, BIE, OSM)
        '("Bureau of Indian Affairs" OR BIA) AND (sovereignty OR consultation OR reservation OR treaty)',
        '("Bureau of Land Management" OR BLM) AND (tribal OR sacred OR "traditional cultural property")',
        '("National Park Service" OR NPS) AND ("sacred site" OR "tribal land" OR "co-management" OR consultation)',
        '("Fish and Wildlife Service" OR FWS) AND (tribal OR subsistence OR "incidental take")',
        '("Bureau of Indian Education" OR BIE OR "tribal college" OR TCU) AND (funding OR governance)',
        # Statutes
        'NAGPRA AND (regulation OR "Review Committee" OR enforcement OR amendment)',
        '("Indian Child Welfare Act" OR ICWA) AND (custody OR placement OR jurisdiction)',
        '("Indian Self-Determination" OR "638 contracting" OR "Public Law 93-638") AND tribe',
        '("Antiquities Act" OR "national monument") AND (designation OR rescission OR boundary OR review)',
        # Health, treaty, Hawaii, Alaska
        '("Indian Health Service" OR IHS) AND (funding OR contracting OR self-determination)',
        '"treaty rights" AND (hunting OR fishing OR water OR gathering OR usufructuary)',
        '"tribal sovereignty" AND (immunity OR jurisdiction OR taxation OR Public Law 280)',
        '"Native Hawaiian" AND (homestead OR "ceded lands" OR "Hawaiian Home Lands" OR Kanaiolowalu)',
        '("Alaska Native" OR ANCSA OR ANILCA) AND (subsistence OR corporation OR village)',

        # ───── AFRICAN-DESCENDANT ─────
        # Civil rights enforcement
        '("Civil Rights Division" OR DOJ) AND ("pattern or practice" OR "Title VII" OR "Title VI")',
        '("Voting Rights Act" OR VRA) AND ("Section 2" OR "Section 5" OR redistricting OR preclearance)',
        '("Equal Employment Opportunity Commission" OR EEOC) AND (race OR "national origin")',
        '("Department of Housing" OR HUD) AND ("fair housing" OR "disparate impact" OR redlining)',
        # Cultural institutions and education
        '(HBCU OR "historically Black college") AND (funding OR "Title III" OR accreditation)',
        '("National Museum of African American History" OR NMAAHC) AND (funding OR governance OR programming)',
        '(Gullah OR Geechee OR "Reconstruction Era") AND (preservation OR "national park" OR "national monument")',
        '(reparations OR "racial equity" OR "racial justice") AND (federal OR Congress OR appropriation)',

        # ───── LATINÉ ─────
        # Immigration
        '(DACA OR "Deferred Action") AND (rescission OR injunction OR rule)',
        '(TPS OR "Temporary Protected Status") AND (designation OR termination OR renewal)',
        '(asylum OR refugee) AND (border OR "credible fear" OR "Title 8" OR DHS)',
        '("U.S. Citizenship and Immigration Services" OR USCIS) AND (naturalization OR "public charge" OR fee)',
        '("Immigration and Customs Enforcement" OR ICE) AND (detention OR "sensitive locations" OR enforcement)',
        '("Customs and Border Protection" OR CBP) AND (border OR detention OR "family separation")',
        # Language, labor
        '("language access" OR "English Learner" OR "bilingual education" OR "Title III") AND (ED OR HHS OR "Title VI")',
        '(farmworker OR "H-2A" OR "agricultural worker") AND (DOL OR USDA OR OSHA OR wage)',
        '(Latino OR Hispanic OR Latiné) AND (Census OR redistricting OR "Title VI")',

        # ───── ASIAN / AAPI ─────
        '("Asian American" OR AAPI OR AANHPI) AND ("hate crime" OR discrimination OR "Title VI")',
        '("Japanese American" OR Manzanar OR "incarceration camp") AND (preservation OR redress)',
        '("South Asian" OR Sikh OR Hindu OR "anti-Muslim") AND ("hate crime" OR profiling OR FBI)',
        '("disaggregated data" OR "data disaggregation") AND (Asian OR Census OR HHS)',
        '("Chinese Exclusion" OR "Asian American history" OR "Filipino American history") AND education',

        # ───── PACIFIC ISLANDER ─────
        '("Compact of Free Association" OR COFA OR "Marshall Islands" OR Micronesia OR Palau) AND (federal OR Medicaid OR education)',
        '("Pacific Islander" OR "Native Hawaiian") AND ("climate displacement" OR "military base" OR sovereignty)',

        # ───── CULTURAL INSTITUTIONS ─────
        '(Smithsonian OR "National Museum") AND (funding OR governance OR programming OR DEI)',
        '("National Endowment for the Arts" OR NEA OR "National Endowment for the Humanities" OR NEH) AND (grant OR rescission OR injunction)',
        '("Institute of Museum and Library Services" OR IMLS) AND (funding OR elimination OR rule)',
        '("Kennedy Center" OR "John F. Kennedy Center") AND (board OR programming OR appropriation)',
        '("Corporation for Public Broadcasting" OR CPB OR PBS OR NPR) AND (funding OR "First Amendment")',
        '("Library of Congress" OR LOC OR "National Archives" OR NARA) AND (record OR access OR removal)',
        '("Advisory Council on Historic Preservation" OR ACHP OR "Section 106") AND (review OR consultation)',

        # ───── ENVIRONMENT / LAND / WATER ─────
        '("Environmental Protection Agency" OR EPA) AND ("environmental justice" OR "Title VI" OR "cumulative impact")',
        '("National Environmental Policy Act" OR NEPA) AND ("environmental review" OR consultation OR impact)',
        '("Clean Water Act" OR CWA) AND (tribe OR "treatment as state" OR "water rights")',
        '("Endangered Species Act" OR ESA) AND (consultation OR listing OR habitat OR tribal)',
        '("National Oceanic and Atmospheric Administration" OR NOAA) AND ("fishing rights" OR sanctuary OR Indigenous)',

        # ───── EDUCATION / RELIGION / HERITAGE ─────
        '("Department of Education" OR "Office for Civil Rights" OR OCR) AND ("Title VI" OR "Title IX" OR DEI)',
        '("Religious Freedom Restoration Act" OR RFRA OR "Free Exercise") AND ("sacred site" OR ceremony OR practice)',
        '("National Historic Preservation Act" OR NHPA OR "National Register") AND (consultation OR listing)',

        # ───── CIVIL RIGHTS / WORKFORCE ─────
        '("Diversity Equity Inclusion" OR DEI) AND (rescission OR ban OR contractor OR Executive)',
        '("Affirmative Action" OR "Executive Order 11246" OR OFCCP) AND (rescission OR contractor)',
        '("hate crime" OR "Matthew Shepard") AND (FBI OR DOJ OR statistics)',
        '("birthright citizenship" OR "Fourteenth Amendment" OR "14th Amendment") AND (citizenship OR "jus soli")',

        # ───── FOREIGN / INTERNATIONAL ─────
        '("Department of State" OR DOS) AND (visa OR refugee OR "human rights" OR sanctions)',
        '("USAID" OR "U.S. Agency for International Development") AND (development OR culture OR Indigenous)',
    ]

    def _search(self, query, since_date):
        data = search_opinions(query, since_date)
        return data.get('results', [])

    def _get_id(self, raw):
        return str(raw.get('id', ''))

    def _parse_result(self, result):
        return {
            'source_id': str(result.get('id', '')),
            'title': result.get('caseName', ''),
            'court': result.get('court', ''),
            'date': (result.get('dateFiled') or '')[:10],
            'docket_number': result.get('docketNumber', ''),
            'snippet': result.get('snippet', ''),
            'citation': result.get('citation', []),
            'url': f"https://www.courtlistener.com{result.get('absolute_url', '')}",
            'status': result.get('status', ''),
        }


# Backwards-compatible module-level functions
_connector = CourtListenerConnector()
fetch_since = _connector.fetch_since
get_category = _connector.get_category
