#!/usr/bin/env python3
"""TCKC Agency Coverage Audit
================================

Comprehensive gap analysis: for each TCKC-relevant federal agency,
fetch Federal Register actions since 2025-01-19 (the start of the
Trump II administration), cross-reference against existing tracker
entries, and identify untracked items that may belong in the tracker.

Output: per-agency markdown gap report plus corpus-wide summary.

WHAT THIS AUDIT DOES
- Pulls Federal Register actions per agency via the public FR API
  (no API key required; rate-limited but generous)
- Cross-references each FR action against existing tracker entries
  by canonical URL, document number, and title fuzzy match
- For untracked items: uses Claude Haiku to screen relevance against
  the TCKC research question (which laws and policies severely harm,
  moderately harm, or protect the cultural resources of the five
  primary cultural communities)
- Categorizes each untracked item: HIGH-PRIORITY (likely belongs in
  tracker), MEDIUM-PRIORITY (worth review), LOW-PRIORITY (note),
  NOT_RELEVANT (skip)
- Optionally drafts tracker entries for HIGH-PRIORITY items

WHAT THIS AUDIT DOES NOT DO
- Court rulings (use --include-courts when added; CourtListener API)
- Congressional actions (use --include-congress when added)
- Agency press releases that are not Federal Register actions
- Executive orders are in Federal Register, but presidential
  statements at events are not
- Smithsonian and National Park Service interpretive material removals
  are typically NOT in the Federal Register; they require separate
  sourcing

USAGE
  python scripts/audit_agency_coverage.py --agency DOI --dry-run
  python scripts/audit_agency_coverage.py --agency-list DOI,DOJ,ED
  python scripts/audit_agency_coverage.py --all-priority-agencies
  python scripts/audit_agency_coverage.py --since 2025-01-19 --until 2025-06-30
  python scripts/audit_agency_coverage.py --draft-entries  # auto-draft HIGH items

OUTPUT
  audit-reports/agency-coverage-YYYY-MM-DD-HHMMSS-AGENCY.md (per agency)
  audit-reports/agency-coverage-YYYY-MM-DD-HHMMSS-summary.md (corpus rollup)
  audit-reports/agency-coverage-YYYY-MM-DD-HHMMSS.json (machine-readable)

COST CONTROLS
  Default: Federal Register API only (no API cost), Haiku screening for
  untracked items. A typical agency has 50-500 FR actions per year, of
  which 80%+ are routinely tracked or routine; the LLM only screens
  untracked items. Cost per agency typically $0.05-$0.50 with Haiku.
"""
import argparse
import json
import os
import re
import ssl
import sys
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone, date
from pathlib import Path

# Build a robust SSL context. macOS Python ships without certifi by
# default; fall back to the system default if certifi is unavailable.
try:
    import certifi
    _SSL_CONTEXT = ssl.create_default_context(cafile=certifi.where())
except ImportError:
    _SSL_CONTEXT = ssl.create_default_context()

try:
    from anthropic import Anthropic
except ImportError:
    print("ERROR: anthropic package not installed. Run: pip install anthropic")
    sys.exit(1)

TRACKER_DIR = Path(__file__).parent.parent
DATA_FILE = TRACKER_DIR / "data" / "data.json"
REPORTS_DIR = TRACKER_DIR / "audit-reports"

# Federal Register API base
FR_API_BASE = "https://www.federalregister.gov/api/v1/documents.json"

# TCKC-relevant agency slug mappings. Federal Register uses slugs;
# this dict maps short labels to FR slugs and back to display names.
AGENCY_REGISTRY = {
    # White House and Office of the President
    "WH":     {"fr_slug": "executive-office-of-the-president", "label": "White House and EOP"},
    "OMB":    {"fr_slug": "management-and-budget-office", "label": "Office of Management and Budget"},
    "USTR":   {"fr_slug": "trade-representative-office-of-united-states", "label": "U.S. Trade Representative"},
    # Justice
    "DOJ":    {"fr_slug": "justice-department", "label": "Department of Justice"},
    "DEA":    {"fr_slug": "drug-enforcement-administration", "label": "Drug Enforcement Administration"},
    "FBI":    {"fr_slug": "federal-bureau-of-investigation", "label": "Federal Bureau of Investigation"},
    # Interior and natural resources
    "DOI":    {"fr_slug": "interior-department", "label": "Department of the Interior"},
    "BIA":    {"fr_slug": "indian-affairs-bureau", "label": "Bureau of Indian Affairs"},
    "BIE":    {"fr_slug": "indian-education-bureau", "label": "Bureau of Indian Education"},
    "NPS":    {"fr_slug": "national-park-service", "label": "National Park Service"},
    "BLM":    {"fr_slug": "land-management-bureau", "label": "Bureau of Land Management"},
    "FWS":    {"fr_slug": "fish-and-wildlife-service", "label": "Fish and Wildlife Service"},
    "USGS":   {"fr_slug": "geological-survey", "label": "U.S. Geological Survey"},
    "ONHIR":  {"fr_slug": "navajo-and-hopi-indian-relocation-office", "label": "Office of Navajo and Hopi Indian Relocation"},
    # Education
    "ED":     {"fr_slug": "education-department", "label": "Department of Education"},
    "OCR":    {"fr_slug": "civil-rights-office-education-department", "label": "ED Office for Civil Rights"},
    # Health and Human Services
    "HHS":    {"fr_slug": "health-and-human-services-department", "label": "Department of Health and Human Services"},
    "FDA":    {"fr_slug": "food-and-drug-administration", "label": "Food and Drug Administration"},
    "CDC":    {"fr_slug": "centers-for-disease-control-and-prevention", "label": "Centers for Disease Control"},
    "NIH":    {"fr_slug": "national-institutes-of-health", "label": "National Institutes of Health"},
    "IHS":    {"fr_slug": "indian-health-service", "label": "Indian Health Service"},
    "ACF":    {"fr_slug": "children-and-families-administration", "label": "Administration for Children and Families"},
    # Homeland Security
    "DHS":    {"fr_slug": "homeland-security-department", "label": "Department of Homeland Security"},
    "ICE":    {"fr_slug": "immigration-and-customs-enforcement-bureau", "label": "Immigration and Customs Enforcement"},
    "CBP":    {"fr_slug": "u-s-customs-and-border-protection", "label": "Customs and Border Protection"},
    "USCIS":  {"fr_slug": "u-s-citizenship-and-immigration-services", "label": "USCIS"},
    "FEMA":   {"fr_slug": "federal-emergency-management-agency", "label": "FEMA"},
    "TSA":    {"fr_slug": "transportation-security-administration", "label": "TSA"},
    # State and international
    "State":  {"fr_slug": "state-department", "label": "Department of State"},
    "USAID":  {"fr_slug": "agency-for-international-development", "label": "USAID"},
    # Agriculture
    "USDA":   {"fr_slug": "agriculture-department", "label": "Department of Agriculture"},
    "FNS":    {"fr_slug": "food-and-nutrition-service", "label": "Food and Nutrition Service (SNAP, WIC)"},
    "NRCS":   {"fr_slug": "natural-resources-conservation-service", "label": "Natural Resources Conservation Service"},
    # Housing and Urban Development
    "HUD":    {"fr_slug": "housing-and-urban-development-department", "label": "Department of Housing and Urban Development"},
    # Labor
    "DOL":    {"fr_slug": "labor-department", "label": "Department of Labor"},
    "EEOC":   {"fr_slug": "equal-employment-opportunity-commission", "label": "Equal Employment Opportunity Commission"},
    # Environment and energy
    "EPA":    {"fr_slug": "environmental-protection-agency", "label": "Environmental Protection Agency"},
    "DOE":    {"fr_slug": "energy-department", "label": "Department of Energy"},
    "FERC":   {"fr_slug": "federal-energy-regulatory-commission", "label": "FERC"},
    "NRC":    {"fr_slug": "nuclear-regulatory-commission", "label": "Nuclear Regulatory Commission"},
    # Cultural and academic agencies
    "Smithsonian": {"fr_slug": "smithsonian-institution", "label": "Smithsonian Institution"},
    "NEA":    {"fr_slug": "national-endowment-for-the-arts", "label": "National Endowment for the Arts"},
    "NEH":    {"fr_slug": "national-endowment-for-the-humanities", "label": "National Endowment for the Humanities"},
    "IMLS":   {"fr_slug": "institute-of-museum-and-library-services", "label": "Institute of Museum and Library Services"},
    "NARA":   {"fr_slug": "national-archives-and-records-administration", "label": "National Archives"},
    "ACHP":   {"fr_slug": "advisory-council-on-historic-preservation", "label": "Advisory Council on Historic Preservation"},
    # Communications
    "FCC":    {"fr_slug": "federal-communications-commission", "label": "FCC"},
    "FTC":    {"fr_slug": "federal-trade-commission", "label": "FTC"},
    # Civil rights commission
    "USCCR":  {"fr_slug": "civil-rights-commission", "label": "U.S. Commission on Civil Rights"},
    # Commerce
    "Commerce": {"fr_slug": "commerce-department", "label": "Department of Commerce"},
    "Census":   {"fr_slug": "census-bureau", "label": "Census Bureau"},
    "NOAA":     {"fr_slug": "national-oceanic-and-atmospheric-administration", "label": "NOAA"},
    # Treasury
    "Treasury": {"fr_slug": "treasury-department", "label": "Department of the Treasury"},
    "IRS":      {"fr_slug": "internal-revenue-service", "label": "Internal Revenue Service"},
    # Defense
    "DoD":     {"fr_slug": "defense-department", "label": "Department of Defense"},
    "VA":      {"fr_slug": "veterans-affairs-department", "label": "Department of Veterans Affairs"},
}

# Priority order for --all-priority-agencies. These are the agencies
# whose actions most directly affect the five TCKC primary cultural
# communities.
PRIORITY_AGENCIES = [
    "WH", "DOJ", "DOI", "BIA", "NPS", "BLM", "ED", "OCR", "HHS", "IHS",
    "DHS", "ICE", "CBP", "State", "USAID", "USDA", "FNS", "HUD", "EPA",
    "NRC", "Smithsonian", "NEA", "NEH", "IMLS", "NARA", "USCCR",
]

DEFAULT_SINCE = "2025-01-19"
DEFAULT_UNTIL = date.today().isoformat()


def fetch_fr_actions(agency_slug, since_date, until_date, max_per_page=1000):
    """Fetch Federal Register documents for an agency in a date range.

    Returns a list of dicts with the relevant fields per FR document.
    Paginates automatically.
    """
    all_results = []
    page = 1
    while True:
        params = {
            "conditions[agencies][]": agency_slug,
            "conditions[publication_date][gte]": since_date,
            "conditions[publication_date][lte]": until_date,
            "per_page": max_per_page,
            "page": page,
        }
        url = FR_API_BASE + "?" + urllib.parse.urlencode(params, doseq=True)
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "TCKC-Tracker-Audit/1.0"})
            with urllib.request.urlopen(req, timeout=60, context=_SSL_CONTEXT) as response:
                data = json.loads(response.read().decode())
        except Exception as e:
            print(f"  ERROR fetching FR for {agency_slug} page {page}: {e}", file=sys.stderr)
            break

        results = data.get("results", [])
        all_results.extend(results)

        total_pages = data.get("total_pages", 1)
        if page >= total_pages or not results:
            break
        page += 1
        # Be polite to FR API
        time.sleep(0.5)

    return all_results


def load_tracker_data():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)


def build_tracker_index(tracker_data):
    """Build URL-set, document-number-set, and title-list for fast cross-reference."""
    urls = set()
    doc_numbers = set()
    titles = []
    categories = ['executive_actions', 'agency_actions', 'legislation',
                  'litigation', 'other_domestic', 'international']
    for cat in categories:
        for entry in tracker_data.get(cat, []):
            u = entry.get('U', '') or ''
            if u:
                urls.add(u.strip().rstrip('/'))
            n = entry.get('n', '') or ''
            if n:
                doc_numbers.add(n.strip())
            T = entry.get('T', '') or ''
            T_clean = re.sub(r'<[^>]+>', '', T).strip()
            if T_clean:
                titles.append(T_clean.lower())
            # Also collect any inline <a href> URLs from the description
            D = entry.get('D', '') or ''
            for href in re.findall(r'href=["\']([^"\']+)["\']', D, re.I):
                urls.add(href.strip().rstrip('/'))
    return {'urls': urls, 'doc_numbers': doc_numbers, 'titles': titles}


def is_tracked(fr_action, tracker_index):
    """Check if a FR action is already represented in the tracker.

    Match strategy (any one is sufficient):
    1. URL match (FR html_url or pdf_url against tracked URLs)
    2. Document number match (FR document_number against tracked n field)
    3. Title fuzzy match (first 50 chars of FR title against tracked titles)
    """
    html_url = (fr_action.get('html_url') or '').strip().rstrip('/')
    pdf_url = (fr_action.get('pdf_url') or '').strip().rstrip('/')
    if html_url and html_url in tracker_index['urls']:
        return True, 'url_match'
    if pdf_url and pdf_url in tracker_index['urls']:
        return True, 'url_match_pdf'

    doc_num = (fr_action.get('document_number') or '').strip()
    if doc_num and doc_num in tracker_index['doc_numbers']:
        return True, 'doc_number_match'

    title = (fr_action.get('title') or '').strip().lower()
    if title and len(title) >= 30:
        title_prefix = title[:50]
        for tracked_title in tracker_index['titles']:
            if title_prefix in tracked_title:
                return True, 'title_fuzzy_match'

    return False, None


SCREENING_PROMPT = """You are screening Federal Register actions for inclusion in the TCKC Cultural Threats Tracker, which tracks federal actions affecting the cultural resources of five primary cultural communities: Indigenous, African-descendant, Latine, Asian, and Pacific Islander.

The TCKC research question is: which laws and policies from the U.S. federal government will severely harm, moderately harm, or protect the cultural resources (People, Places, Practices, Treasures) paramount to the cultural continuity of these communities?

For the FR action below, classify its TCKC relevance and return JSON:

{
  "relevance": "HIGH | MEDIUM | LOW | NOT_RELEVANT",
  "primary_community": "Indigenous | African-descendant | Latine | Asian | Pacific Islander | All Communities | None",
  "secondary_communities": ["..."],
  "threat_direction": "SEVERE | HARMFUL | PROTECTIVE | WATCH | NEUTRAL",
  "reasoning": "two or three sentences explaining the classification",
  "draft_id_slug": "a short kebab-case slug suitable for a tracker entry id, only if relevance is HIGH"
}

Severity calibration:
- HIGH: clearly tracker-worthy. Direct, named impact on one or more TCKC primary cultural communities. Examples: BIA tribal-recognition action; ED civil rights resolution; DOI mineral-withdrawal action; HHS health-equity rule.
- MEDIUM: arguably tracker-worthy. Indirect or contingent impact. Worth human review.
- LOW: tangential to TCKC scope. Routine federal action with no direct cultural-community impact.
- NOT_RELEVANT: clearly out of scope. Examples: routine procurement notices, technical regulatory amendments with no cultural-community implications, agency information collections.

Be conservative on HIGH. Better to flag MEDIUM and let a human escalate than to over-score routine items."""


def screen_fr_action(client, model_id, fr_action):
    """Use the LLM to screen a FR action for TCKC relevance."""
    snippet = {
        "title": fr_action.get('title', ''),
        "type": fr_action.get('type', ''),
        "document_number": fr_action.get('document_number', ''),
        "publication_date": fr_action.get('publication_date', ''),
        "agency_names": fr_action.get('agency_names', []),
        "abstract": (fr_action.get('abstract') or '')[:1500],
    }
    user_msg = "FEDERAL REGISTER ACTION:\n\n" + json.dumps(snippet, indent=2) + "\n\nClassify per the system prompt schema."
    response = client.messages.create(
        model=model_id,
        max_tokens=512,
        system=[{"type": "text", "text": SCREENING_PROMPT, "cache_control": {"type": "ephemeral"}}],
        messages=[{"role": "user", "content": user_msg}],
    )
    text = "".join(b.text for b in response.content if hasattr(b, 'text'))
    m = re.search(r'\{[\s\S]*\}', text)
    if not m:
        return None, response.usage
    try:
        return json.loads(m.group(0)), response.usage
    except json.JSONDecodeError:
        return None, response.usage


def render_agency_report(agency_label, agency_key, fr_actions, results, started_at, since_date, until_date):
    lines = []
    lines.append(f"# Agency Coverage Gap Report: {agency_label}")
    lines.append("")
    lines.append(f"**Agency code**: `{agency_key}`")
    lines.append(f"**Period**: {since_date} to {until_date}")
    lines.append(f"**FR actions found**: {len(fr_actions)}")

    tracked = [r for r in results if r.get('tracked')]
    untracked_high = [r for r in results if not r.get('tracked') and r.get('screening', {}).get('relevance') == 'HIGH']
    untracked_med = [r for r in results if not r.get('tracked') and r.get('screening', {}).get('relevance') == 'MEDIUM']
    untracked_low = [r for r in results if not r.get('tracked') and r.get('screening', {}).get('relevance') == 'LOW']
    untracked_skip = [r for r in results if not r.get('tracked') and r.get('screening', {}).get('relevance') == 'NOT_RELEVANT']
    untracked_unscreened = [r for r in results if not r.get('tracked') and not r.get('screening')]

    lines.append(f"**Already tracked**: {len(tracked)}")
    lines.append(f"**Untracked HIGH-priority**: {len(untracked_high)}")
    lines.append(f"**Untracked MEDIUM-priority**: {len(untracked_med)}")
    lines.append(f"**Untracked LOW-priority**: {len(untracked_low)}")
    lines.append(f"**Untracked NOT_RELEVANT (skip)**: {len(untracked_skip)}")
    if untracked_unscreened:
        lines.append(f"**Untracked unscreened**: {len(untracked_unscreened)}")
    lines.append("")
    lines.append(f"**Run start (UTC)**: {started_at.strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("")
    lines.append("---")
    lines.append("")

    if untracked_high:
        lines.append("## HIGH-priority untracked actions (likely belong in tracker)")
        lines.append("")
        for r in untracked_high:
            fr = r['fr_action']
            s = r['screening']
            lines.append(f"### {fr.get('title','(untitled)')[:200]}")
            lines.append("")
            lines.append(f"- **Type**: {fr.get('type','')}")
            lines.append(f"- **Document number**: {fr.get('document_number','')}")
            lines.append(f"- **Date**: {fr.get('publication_date','')}")
            lines.append(f"- **URL**: {fr.get('html_url','')}")
            lines.append(f"- **Primary community**: {s.get('primary_community','')}")
            lines.append(f"- **Threat direction**: {s.get('threat_direction','')}")
            lines.append(f"- **Reasoning**: {s.get('reasoning','')}")
            if s.get('draft_id_slug'):
                lines.append(f"- **Suggested entry id**: `{s['draft_id_slug']}`")
            lines.append("")

    if untracked_med:
        lines.append("## MEDIUM-priority untracked actions (worth review)")
        lines.append("")
        for r in untracked_med:
            fr = r['fr_action']
            s = r['screening']
            lines.append(f"- **{fr.get('title','(untitled)')[:160]}**")
            lines.append(f"  - {fr.get('type','')} | {fr.get('publication_date','')} | {fr.get('document_number','')}")
            lines.append(f"  - {fr.get('html_url','')}")
            lines.append(f"  - {s.get('reasoning','')[:200]}")
        lines.append("")

    if untracked_low:
        lines.append(f"## LOW-priority untracked actions ({len(untracked_low)} items)")
        lines.append("")
        for r in untracked_low:
            fr = r['fr_action']
            lines.append(f"- {fr.get('title','(untitled)')[:140]} ({fr.get('publication_date','')}, {fr.get('document_number','')})")
        lines.append("")

    if tracked:
        lines.append(f"## Already tracked ({len(tracked)} items)")
        lines.append("")
        for r in tracked[:50]:
            fr = r['fr_action']
            lines.append(f"- {fr.get('title','(untitled)')[:140]} ({fr.get('publication_date','')}) — matched via {r.get('match_method','')}")
        if len(tracked) > 50:
            lines.append(f"- ... ({len(tracked) - 50} more)")
        lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="TCKC Agency Coverage Audit")
    agency_group = parser.add_mutually_exclusive_group(required=True)
    agency_group.add_argument('--agency', help='Single agency code (e.g., DOI, DOJ)')
    agency_group.add_argument('--agency-list', help='Comma-separated agency codes')
    agency_group.add_argument('--all-priority-agencies', action='store_true',
                              help='Run all priority agencies (~26 agencies)')
    agency_group.add_argument('--list-agencies', action='store_true',
                              help='Print available agency codes and exit')
    parser.add_argument('--since', default=DEFAULT_SINCE,
                        help=f'Start date (default {DEFAULT_SINCE})')
    parser.add_argument('--until', default=DEFAULT_UNTIL,
                        help='End date (default today)')
    parser.add_argument('--model', choices=['haiku', 'sonnet', 'opus'], default='haiku',
                        help='Model for relevance screening (default haiku)')
    parser.add_argument('--dry-run', action='store_true',
                        help='Fetch FR actions and cross-reference; skip LLM screening')
    parser.add_argument('--max-screen-per-agency', type=int, default=200,
                        help='Cap LLM-screening calls per agency (default 200)')
    args = parser.parse_args()

    if args.list_agencies:
        print("Available agency codes:")
        for code, info in sorted(AGENCY_REGISTRY.items()):
            print(f"  {code:12s} = {info['label']} ({info['fr_slug']})")
        return

    if args.agency:
        agencies = [args.agency]
    elif args.agency_list:
        agencies = [a.strip() for a in args.agency_list.split(',') if a.strip()]
    elif args.all_priority_agencies:
        agencies = PRIORITY_AGENCIES
    else:
        parser.error("must specify --agency, --agency-list, or --all-priority-agencies")

    for a in agencies:
        if a not in AGENCY_REGISTRY:
            print(f"ERROR: unknown agency code '{a}'. Use --list-agencies to see options.")
            sys.exit(1)

    model_id = {'haiku': 'claude-haiku-4-5-20251001',
                'sonnet': 'claude-sonnet-4-6',
                'opus': 'claude-opus-4-7'}[args.model]

    print(f"Agencies to audit: {agencies}")
    print(f"Period: {args.since} to {args.until}")
    print(f"Model: {model_id}")
    print(f"Dry run: {args.dry_run}")
    print()

    print("Loading tracker data...")
    tracker_data = load_tracker_data()
    tracker_index = build_tracker_index(tracker_data)
    print(f"  Tracker URLs: {len(tracker_index['urls'])}")
    print(f"  Tracker doc numbers: {len(tracker_index['doc_numbers'])}")
    print(f"  Tracker titles: {len(tracker_index['titles'])}")
    print()

    started_at = datetime.now(timezone.utc)
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = started_at.strftime('%Y%m%d-%H%M%S')

    client = None
    if not args.dry_run:
        api_key = os.environ.get('ANTHROPIC_API_KEY')
        if not api_key:
            print("ERROR: ANTHROPIC_API_KEY not set. Use --dry-run to skip LLM screening.")
            sys.exit(1)
        client = Anthropic(api_key=api_key)

    all_summary = []

    for agency_code in agencies:
        info = AGENCY_REGISTRY[agency_code]
        print(f"=== {agency_code}: {info['label']} ===")

        print(f"  Fetching FR actions for slug '{info['fr_slug']}'...")
        fr_actions = fetch_fr_actions(info['fr_slug'], args.since, args.until)
        print(f"  Found {len(fr_actions)} FR actions in period")

        # Cross-reference with tracker
        results = []
        tracked_count = 0
        for fr in fr_actions:
            tracked, match_method = is_tracked(fr, tracker_index)
            results.append({'fr_action': fr, 'tracked': tracked, 'match_method': match_method})
            if tracked:
                tracked_count += 1
        print(f"  Already tracked: {tracked_count}")
        print(f"  Untracked: {len(fr_actions) - tracked_count}")

        # Screen untracked items
        untracked_results = [r for r in results if not r['tracked']]
        if not args.dry_run and untracked_results:
            to_screen = untracked_results[:args.max_screen_per_agency]
            print(f"  Screening {len(to_screen)} untracked items with {model_id}...")
            for i, r in enumerate(to_screen, 1):
                if i % 10 == 0:
                    print(f"    [{i}/{len(to_screen)}]", flush=True)
                try:
                    screening, _usage = screen_fr_action(client, model_id, r['fr_action'])
                    r['screening'] = screening
                except Exception as e:
                    r['screening'] = {'relevance': 'UNSCREENED', 'error': str(e)}
                time.sleep(0.3)  # rate-limit pacing
            if len(untracked_results) > args.max_screen_per_agency:
                print(f"  Note: {len(untracked_results) - args.max_screen_per_agency} untracked items left unscreened (cap: {args.max_screen_per_agency})")

        # Render per-agency report
        report = render_agency_report(info['label'], agency_code, fr_actions, results, started_at, args.since, args.until)
        report_path = REPORTS_DIR / f"agency-coverage-{timestamp}-{agency_code}.md"
        report_path.write_text(report)
        print(f"  Wrote: {report_path}")

        # Tally for summary
        high = sum(1 for r in results if not r['tracked'] and (r.get('screening') or {}).get('relevance') == 'HIGH')
        med = sum(1 for r in results if not r['tracked'] and (r.get('screening') or {}).get('relevance') == 'MEDIUM')
        low = sum(1 for r in results if not r['tracked'] and (r.get('screening') or {}).get('relevance') == 'LOW')
        skip = sum(1 for r in results if not r['tracked'] and (r.get('screening') or {}).get('relevance') == 'NOT_RELEVANT')
        all_summary.append({
            'agency_code': agency_code,
            'agency_label': info['label'],
            'fr_actions': len(fr_actions),
            'tracked': tracked_count,
            'untracked_high': high,
            'untracked_medium': med,
            'untracked_low': low,
            'untracked_skip': skip,
            'report_path': str(report_path.relative_to(TRACKER_DIR)),
            'results': results,
        })
        print()

    # Render corpus-wide summary
    summary_lines = []
    summary_lines.append(f"# Agency Coverage Audit Summary")
    summary_lines.append("")
    summary_lines.append(f"**Run start (UTC)**: {started_at.strftime('%Y-%m-%d %H:%M:%S')}")
    summary_lines.append(f"**Period**: {args.since} to {args.until}")
    summary_lines.append(f"**Agencies audited**: {len(agencies)}")
    summary_lines.append(f"**Model**: `{model_id}`")
    summary_lines.append(f"**Dry run**: {args.dry_run}")
    summary_lines.append("")
    summary_lines.append("| Agency | FR actions | Tracked | HIGH | MED | LOW | Skip | Report |")
    summary_lines.append("|---|---|---|---|---|---|---|---|")
    for s in all_summary:
        summary_lines.append(f"| {s['agency_code']} ({s['agency_label']}) | {s['fr_actions']} | {s['tracked']} | {s['untracked_high']} | {s['untracked_medium']} | {s['untracked_low']} | {s['untracked_skip']} | [{s['agency_code']}]({s['report_path']}) |")
    summary_path = REPORTS_DIR / f"agency-coverage-{timestamp}-summary.md"
    summary_path.write_text("\n".join(summary_lines))

    json_path = REPORTS_DIR / f"agency-coverage-{timestamp}.json"
    json_path.write_text(json.dumps({
        'started_at': started_at.isoformat(),
        'since': args.since,
        'until': args.until,
        'model': model_id,
        'dry_run': args.dry_run,
        'agencies': all_summary,
    }, default=str, ensure_ascii=False, indent=2))

    print(f"Summary report: {summary_path}")
    print(f"JSON: {json_path}")


if __name__ == '__main__':
    main()
