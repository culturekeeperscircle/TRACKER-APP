#!/usr/bin/env python3
"""TCKC Critical Review Audit
==============================

Audits tracker entries through four lenses tied to Prince Albert III's
scholarship and the project's framework:

1. PPPT FRAMEWORK CONSISTENCY (People / Places / Practices / Treasures)
   Are the four dimensions applied correctly and consistently? Are
   community-tag assignments defensible? Is the threat level (SEVERE /
   HARMFUL / WATCH / PROTECTIVE) calibrated against the cultural-
   continuity rubric documented in CLAUDE.md?

2. CULTURAL SUSTAINABILITY SCHOLARSHIP
   Does the analysis center cultural-continuity logic and intergenerational
   transmission? Does it engage with Indigenous-led approaches and
   Free, Prior, and Informed Consent (FPIC)? Does it avoid extractive
   academic framings? Does it treat cultures as living rather than
   frozen-in-time? Does it integrate cultural-rights-as-human-rights
   frameworks (UNESCO conventions, UNDRIP)?

3. CRITICAL LEGAL SCHOLARSHIP
   Does the analysis engage with law as a vehicle of power? Does it name
   doctrinal harms accurately? Does it avoid liberal-legalist framings
   that obscure power dynamics? Does it engage with intersectionality
   (CRT, LatCrit, TWAIL, Indigenous Critical Theory)? Does it recognize
   law's complicity with settler colonialism, racial capitalism, and
   patriarchy where applicable? Does it acknowledge Indigenous and
   community legal orders as parallel-or-competing rather than subsidiary?

4. SELF-DETERMINATION OF ALL COMMUNITIES
   Does the entry respect that communities are not monolithic? Does it
   acknowledge intra-community diversity and intercommunity tensions?
   Does it avoid zero-sum framings that pit one community's interests
   against another's? Does it recognize when one community's federal
   gain is another community's federal loss (e.g., HBCU funding boost
   funded by HSI cuts)? Does it avoid privileging state-mediated
   recognition over community self-determination? Does it engage with
   UNDRIP Article 3 (all peoples' right to self-determination)?

USAGE:
    python scripts/audit_critical_review.py --sample 10
    python scripts/audit_critical_review.py --sample 50 --model sonnet
    python scripts/audit_critical_review.py --category litigation
    python scripts/audit_critical_review.py --community Indigenous
    python scripts/audit_critical_review.py --since 2026-04-01
    python scripts/audit_critical_review.py --full --model haiku  # ALL entries
    python scripts/audit_critical_review.py --dry-run              # preview only

OUTPUT:
    audit-reports/audit-critical-review-YYYY-MM-DD-HHMMSS.md

COST CONTROLS:
    Default sample size is 10 entries. Default model is haiku-4.5
    (cheapest). Prompt caching is used to amortize the framework-context
    block across all entries in a run. Use --dry-run to preview entries
    and estimate cost before spending tokens.
"""
import argparse
import json
import os
import random
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

try:
    from anthropic import Anthropic
except ImportError:
    print("ERROR: anthropic package not installed. Run: pip install anthropic")
    sys.exit(1)

TRACKER_DIR = Path(__file__).parent.parent
DATA_FILE = TRACKER_DIR / "data" / "data.json"
REPORTS_DIR = TRACKER_DIR / "audit-reports"
CATEGORIES = ['executive_actions', 'agency_actions', 'legislation',
              'litigation', 'other_domestic', 'international']

MODEL_MAP = {
    'haiku': 'claude-haiku-4-5-20251001',
    'sonnet': 'claude-sonnet-4-6',
    'opus': 'claude-opus-4-7',
}


# Framework context block. This is sent as a cacheable prefix so the
# cost is paid once per run rather than once per entry.
FRAMEWORK_CONTEXT = """You are conducting a critical review audit of TCKC Cultural Threats Tracker entries on behalf of Prince Albert III. Your audit is to be conducted through four lenses, each grounded in Prince's scholarly orientation and the project's operating framework.

# PRINCE'S SCHOLARLY ORIENTATION

Prince is a cultural sustainability scholar (drawing on the Indigenous-led, intergenerational-continuity, FPIC-grounded tradition that places living cultural practice at the center of analysis) and a critical legal scholar (drawing on CRT, LatCrit, TWAIL, and Indigenous Critical Theory, treating law as a vehicle of power rather than a neutral framework). He supports the self-determination of ALL communities and refuses zero-sum framings that privilege one community's interests at the expense of another's.

# THE PPPT FRAMEWORK

The tracker codes federal-action impact across four dimensions:

- People: demographic survival, civil rights, dignified existence, leadership, migration and assembly, health and education access, immigration status, safety
- Places: sacred sites, heritage sites, tribal lands, historic districts, cultural neighborhoods, diaspora homelands, museums, archives, cultural centers
- Practices: religious and spiritual observance, language transmission, foodways, folk arts, ceremonies, dance and music, oral histories, traditional ecological knowledge
- Treasures: material culture, artifacts, archives, intellectual property, historic documents, ancestral remains, sacred objects, artistic works, inherited land and assets

The five primary cultural communities are:
1. Indigenous (Native American nations, Alaska Native, Native Hawaiian)
2. African-descendant (African American, Afro-Caribbean, Afro-Latine, African diaspora)
3. Latine (Latin American, Chicano, Hispanic, Latinx)
4. Asian (AANHPI, South Asian, Southeast Asian, East Asian)
5. Pacific Islander (Native Hawaiian, Samoan, Tongan, Chamorro, Polynesian, Micronesian, Melanesian)

Threat levels: SEVERE (direct, immediate, often irreversible harm), HARMFUL (significant but reversible harm), WATCH (monitoring), PROTECTIVE (safeguards, restores, funds, defends).

# THE FOUR AUDIT LENSES

## Lens 1: PPPT framework consistency
Are the four dimensions applied correctly? Is content placed in People that should be in Places (or vice versa)? Does the entry use all four dimensions for each affected community, or does it skip dimensions that should be populated? Is the threat-level classification calibrated against comparable entries in the tracker? Are community-tag assignments defensible against the entry's actual content?

## Lens 2: Cultural sustainability scholarship
Does the analysis center cultural-continuity logic? Does it engage with intergenerational transmission, Indigenous-led approaches, and FPIC? Does it avoid extractive academic framings (treating communities as objects of study rather than co-producers of knowledge)? Does it treat cultures as living rather than frozen-in-time? Does it integrate cultural-rights-as-human-rights frameworks where relevant?

## Lens 3: Critical legal scholarship
Does the analysis engage with law as a vehicle of power? Does it name doctrinal harms accurately? Does it avoid liberal-legalist framings that obscure power dynamics? Does it engage with intersectionality? Does it recognize law's complicity with settler colonialism, racial capitalism, and patriarchy where applicable? Does it acknowledge Indigenous and community legal orders as parallel-or-competing rather than subsidiary to federal law?

## Lens 4: Self-determination of all communities
Does the entry respect that communities are not monolithic? Does it acknowledge intra-community diversity and intercommunity tensions? Does it avoid zero-sum framings? Does it recognize when one community's federal gain is another community's federal loss? Does it avoid privileging state-mediated recognition over community self-determination? Does it engage with UNDRIP Article 3 where applicable?

# YOUR OUTPUT

For each entry you audit, produce a JSON object with this structure:

{
  "entry_id": "the entry's i or id field",
  "overall_severity": "HIGH | MEDIUM | LOW | OK",
  "findings": [
    {
      "lens": "PPPT | Cultural Sustainability | Critical Legal | Self-Determination",
      "severity": "HIGH | MEDIUM | LOW",
      "issue": "concise description of the concern",
      "evidence": "specific quotation or reference from the entry",
      "recommended_action": "concrete fix or further-review action"
    }
  ],
  "strengths": ["short list of what the entry does well, if anything notable"],
  "audit_notes": "any cross-cutting observation"
}

Severity calibration:
- HIGH: substantive concern that likely warrants editing the entry. Examples: framing that contradicts FPIC; treating an Indigenous-led action as state-mediated; zero-sum framing that pits one TCKC primary community against another; PPPT placement that misclassifies content; threat-level classification that diverges sharply from comparable tracker entries.
- MEDIUM: worth reviewing. Examples: a missed intersectional angle; a cross-reference that should exist but doesn't; a community tag that could be expanded; a phrasing that is defensible but could be strengthened.
- LOW: note for future improvement. Examples: a stylistic choice that could be more precise; a source that could be added; a minor PPPT-dimension expansion opportunity.
- OK: no concerns; entry is well-formed and consistent.

If the entry is well-formed, return overall_severity OK with an empty findings list. Do not invent concerns.

WRITING-STYLE COMPLIANCE: Your audit prose follows the same style rules the tracker uses (no em-dashes, no run-on sentences, no awkward colons, no 'not X, but Y' constructions, strong declarative prose). Your output is JSON; the prose-style rules apply to the field values.
"""


def load_entries():
    with open(DATA_FILE, 'r') as f:
        data = json.load(f)
    rows = []
    for cat in CATEGORIES:
        for entry in data.get(cat, []):
            entry_id = entry.get('id') or entry.get('i')
            if entry_id:
                rows.append((cat, entry_id, entry))
    return rows


def filter_entries(entries, args):
    rows = entries
    if args.category:
        rows = [r for r in rows if r[0] == args.category]
    if args.community:
        rows = [r for r in rows
                if args.community.lower() in [c.lower() for c in r[2].get('c', [])]]
    if args.threat_level:
        rows = [r for r in rows if r[2].get('L', '').upper() == args.threat_level.upper()]
    if args.since:
        rows = [r for r in rows if r[2].get('d', '') >= args.since]
    return rows


def estimate_cost(rows, model_id):
    # Rough estimates per entry; numbers are intentionally conservative.
    total_input_tokens = len(rows) * 8000  # framework block + entry payload
    cached_input_tokens = (len(rows) - 1) * 5000  # framework block re-read cached
    fresh_input_tokens = total_input_tokens - cached_input_tokens
    output_tokens = len(rows) * 1500  # audit JSON output
    if 'haiku' in model_id:
        cost = (fresh_input_tokens * 1.0e-6) + (cached_input_tokens * 0.1e-6) + (output_tokens * 5.0e-6)
    elif 'sonnet' in model_id:
        cost = (fresh_input_tokens * 3.0e-6) + (cached_input_tokens * 0.3e-6) + (output_tokens * 15.0e-6)
    elif 'opus' in model_id:
        cost = (fresh_input_tokens * 15.0e-6) + (cached_input_tokens * 1.5e-6) + (output_tokens * 75.0e-6)
    else:
        cost = 0
    return cost


def audit_entry(client, model_id, cat, entry_id, entry):
    # Strip HTML for cleaner reading by the model
    desc = entry.get('D') or entry.get('d', '')
    raw = json.dumps(entry, ensure_ascii=False, indent=2)
    user_msg = f"AUDIT THIS ENTRY (category: {cat}):\n\n```json\n{raw}\n```\n\nReturn your audit as a single JSON object per the structure described in the system prompt."

    response = client.messages.create(
        model=model_id,
        max_tokens=2048,
        system=[
            {
                "type": "text",
                "text": FRAMEWORK_CONTEXT,
                "cache_control": {"type": "ephemeral"},
            },
        ],
        messages=[{"role": "user", "content": user_msg}],
    )
    text = "".join(block.text for block in response.content if hasattr(block, 'text'))
    # Try to parse JSON. Strip any markdown code fences.
    m = re.search(r'\{[\s\S]*\}', text)
    if not m:
        return None, text, response.usage
    try:
        parsed = json.loads(m.group(0))
        return parsed, text, response.usage
    except json.JSONDecodeError:
        return None, text, response.usage


def render_report(args, model_id, results, total_usage, total_cost, started_at):
    lines = []
    lines.append("# TCKC Critical Review Audit")
    lines.append("")
    lines.append(f"**Run start (UTC)**: {started_at.strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append(f"**Run duration**: {(datetime.now(timezone.utc) - started_at).total_seconds():.0f} seconds")
    lines.append(f"**Model**: `{model_id}`")
    lines.append(f"**Entries audited**: {len(results)}")
    lines.append(f"**Filters applied**: category={args.category or 'all'}, community={args.community or 'all'}, threat-level={args.threat_level or 'all'}, since={args.since or 'all'}")
    lines.append(f"**Sampling**: {'full' if args.full else f'random sample of {args.sample}'}")
    lines.append(f"**Total tokens**: input={total_usage.get('input_tokens', 0):,} (cached={total_usage.get('cache_read_input_tokens', 0):,}), output={total_usage.get('output_tokens', 0):,}")
    lines.append(f"**Approximate cost**: ${total_cost:.4f}")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Tally
    tally = {"HIGH": 0, "MEDIUM": 0, "LOW": 0, "OK": 0}
    by_severity = {"HIGH": [], "MEDIUM": [], "LOW": [], "OK": []}
    for r in results:
        sev = (r.get('audit') or {}).get('overall_severity', 'UNKNOWN')
        if sev in tally:
            tally[sev] += 1
            by_severity[sev].append(r)
        else:
            tally['OK'] = tally.get('OK', 0)

    lines.append(f"## Summary tally")
    lines.append("")
    lines.append(f"- HIGH-severity findings: {tally['HIGH']}")
    lines.append(f"- MEDIUM-severity findings: {tally['MEDIUM']}")
    lines.append(f"- LOW-severity findings: {tally['LOW']}")
    lines.append(f"- OK (no concerns): {tally['OK']}")
    lines.append("")

    for severity_label in ['HIGH', 'MEDIUM', 'LOW']:
        if not by_severity[severity_label]:
            continue
        lines.append(f"## {severity_label}-priority concerns")
        lines.append("")
        for r in by_severity[severity_label]:
            audit = r.get('audit') or {}
            lines.append(f"### `{r['entry_id']}` ({r['category']})")
            lines.append("")
            entry_title = r['entry'].get('T', '')
            entry_title_clean = re.sub(r'<[^>]+>', '', entry_title)
            if entry_title_clean:
                lines.append(f"**Entry title**: {entry_title_clean}")
                lines.append("")
            lines.append(f"**Threat level (current)**: {r['entry'].get('L', '')}")
            lines.append(f"**Date**: {r['entry'].get('d', '')}")
            lines.append("")
            findings = audit.get('findings', [])
            if findings:
                lines.append("**Findings**:")
                lines.append("")
                for f in findings:
                    lines.append(f"- **[{f.get('severity','?')}] {f.get('lens','?')}**: {f.get('issue','')}")
                    if f.get('evidence'):
                        lines.append(f"  - *Evidence*: {f['evidence']}")
                    if f.get('recommended_action'):
                        lines.append(f"  - *Recommended action*: {f['recommended_action']}")
                lines.append("")
            strengths = audit.get('strengths', [])
            if strengths:
                lines.append(f"**Strengths**: {'; '.join(strengths)}")
                lines.append("")
            audit_notes = audit.get('audit_notes')
            if audit_notes:
                lines.append(f"**Audit notes**: {audit_notes}")
                lines.append("")
            lines.append("---")
            lines.append("")

    if by_severity['OK']:
        lines.append(f"## OK (no concerns) ({len(by_severity['OK'])} entries)")
        lines.append("")
        for r in by_severity['OK']:
            lines.append(f"- `{r['entry_id']}` ({r['category']})")
        lines.append("")

    # Errors
    errors = [r for r in results if r.get('error')]
    if errors:
        lines.append(f"## Audit errors ({len(errors)} entries)")
        lines.append("")
        for r in errors:
            lines.append(f"- `{r['entry_id']}`: {r['error']}")
        lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="TCKC Critical Review Audit")
    parser.add_argument('--sample', type=int, default=10,
                        help='Random sample size (default 10). Ignored if --full.')
    parser.add_argument('--full', action='store_true',
                        help='Audit ALL filtered entries. Use with care.')
    parser.add_argument('--category', choices=CATEGORIES, default=None)
    parser.add_argument('--community', default=None,
                        help='Filter by community tag (case-insensitive)')
    parser.add_argument('--threat-level', dest='threat_level',
                        choices=['SEVERE', 'HARMFUL', 'WATCH', 'PROTECTIVE'],
                        default=None)
    parser.add_argument('--since', default=None,
                        help='Filter to entries with d >= YYYY-MM-DD')
    parser.add_argument('--model', choices=list(MODEL_MAP.keys()), default='haiku')
    parser.add_argument('--dry-run', action='store_true',
                        help='Preview entries and cost estimate without calling the API')
    parser.add_argument('--seed', type=int, default=None,
                        help='Random seed for reproducible sampling')
    args = parser.parse_args()

    if not DATA_FILE.exists():
        print(f"ERROR: data.json not found at {DATA_FILE}")
        sys.exit(1)

    entries = load_entries()
    rows = filter_entries(entries, args)
    print(f"Filtered entries: {len(rows)}")

    if not args.full:
        if args.seed is not None:
            random.seed(args.seed)
        if len(rows) > args.sample:
            rows = random.sample(rows, args.sample)
    print(f"Entries to audit: {len(rows)}")

    model_id = MODEL_MAP[args.model]
    estimated = estimate_cost(rows, model_id)
    print(f"Model: {model_id}")
    print(f"Estimated cost (rough): ${estimated:.4f}")

    if args.dry_run:
        print("\nDRY RUN. Would audit:")
        for cat, eid, _e in rows:
            print(f"  - {cat}: {eid}")
        return

    api_key = os.environ.get('ANTHROPIC_API_KEY')
    if not api_key:
        print("ERROR: ANTHROPIC_API_KEY not set in environment.")
        sys.exit(1)

    client = Anthropic(api_key=api_key)
    started_at = datetime.now(timezone.utc)
    results = []
    total_usage = {'input_tokens': 0, 'output_tokens': 0, 'cache_read_input_tokens': 0, 'cache_creation_input_tokens': 0}

    for i, (cat, eid, entry) in enumerate(rows, 1):
        print(f"[{i}/{len(rows)}] Auditing {eid}...", flush=True)
        try:
            parsed, raw_text, usage = audit_entry(client, model_id, cat, eid, entry)
            results.append({
                'category': cat,
                'entry_id': eid,
                'entry': entry,
                'audit': parsed,
                'raw_text': raw_text if not parsed else None,
                'error': None if parsed else 'JSON parse failed; raw text preserved',
            })
            for k in total_usage:
                total_usage[k] += getattr(usage, k, 0) or 0
        except Exception as e:
            results.append({
                'category': cat,
                'entry_id': eid,
                'entry': entry,
                'audit': None,
                'error': str(e),
            })
        # Mild pacing to avoid rate limits
        time.sleep(0.5)

    total_cost = estimate_cost(rows, model_id)

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = started_at.strftime('%Y%m%d-%H%M%S')
    report_path = REPORTS_DIR / f"audit-critical-review-{timestamp}.md"
    json_path = REPORTS_DIR / f"audit-critical-review-{timestamp}.json"

    report = render_report(args, model_id, results, total_usage, total_cost, started_at)
    report_path.write_text(report)
    json_path.write_text(json.dumps({
        'meta': {
            'started_at': started_at.isoformat(),
            'model': model_id,
            'sample': args.sample if not args.full else 'full',
            'category': args.category,
            'community': args.community,
            'threat_level': args.threat_level,
            'since': args.since,
            'total_usage': total_usage,
            'total_cost_usd': total_cost,
        },
        'results': results,
    }, default=str, ensure_ascii=False, indent=2))

    print(f"\nReport: {report_path}")
    print(f"JSON: {json_path}")
    print(f"Total cost (rough): ${total_cost:.4f}")


if __name__ == '__main__':
    main()
