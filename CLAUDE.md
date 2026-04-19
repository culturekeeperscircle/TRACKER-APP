# TCKC Cultural Threats Tracker — AI Tool Instructions

## What This Project Is

A federal government action tracker monitoring threats to cultural resources of Indigenous, African-descendant, Latine, Asian American, Pacific Islander, and other marginalized communities. It powers The Culture Keepers Circle's public advocacy and Prince's law review article.

- **666 entries** across 5 categories (executive_actions, legislation, litigation, agency_actions, international)
- **Single source of truth**: `data/data.json` (~58 MB JSON)
- **Frontend**: `index.html` (self-contained single-page app, 6.2 MB)
- **Automation**: Python pipeline + shell scripts + GitHub Actions

## Key Entry Points

| Task | Command / File |
|------|---------------|
| Run pipeline | `python3 -m pipeline` |
| Push updates | `./scripts/update.sh --auto` |
| Enrich entries | `python3 scripts/enrich_entries.py --community <type> --dry-run` |
| Audit data | `python3 scripts/audit_toolkit.py --full` |
| Edit tracker UI | `index.html` (inline JS/CSS) |
| Modify schema | `pipeline/data/schema.py` |
| Add API source | Inherit from `pipeline/sources/base.py` |

## Data Format

Entries use **abbreviated single-letter keys** for compact JSON:

```
i = ID, t = type, n = number, T = title (HTML), s = summary,
d = date, a = administration, A = agencies[], S = status,
L = threat level, D = description (HTML), I = impact analysis,
c = communities[], U = source URL, _source = data source tag
```

Impact analysis (`I`) nests community keys containing 4Ps objects:
```json
"I": { "indigenous": { "people": "...", "places": "...", "practices": "...", "treasures": "..." } }
```

## Threat Levels

- `SEVERE` — Irreversible harm (red)
- `HARMFUL` — Significant but reversible (orange)
- `WATCH` — Monitoring level
- `PROTECTIVE` — Defensive/positive action (green)

## Community Keys (27)

```
africanAmerican, indigenous, latine, asianAmerican, pacificIslander,
alaskaNative, nativeHawaiian, immigrant, lgbtq, women, disabled,
muslim, jewish, sikh, rural, urban, lowIncome, environmentalJustice,
academicCommunity, faithCommunities, arts, nonprofit, federalEmployees,
allCommunities
```

## Pipeline Architecture

```
Sources (4 APIs) → Relevance Filter → Claude Analysis → Dedup → Validate → data.json
```

Source connectors inherit from `pipeline/sources/base.py`:
- `BaseSourceConnector` — paginated APIs (Congress.gov, Federal Register)
- `MultiQuerySourceConnector` — multi-query APIs (CourtListener, NewsAPI)

All connectors expose backwards-compatible `fetch_since()` and `get_category()` module-level functions.

## Claude Models Used

| Stage | Model | Config Key |
|-------|-------|-----------|
| Relevance screening | Haiku 4.5 | `CLAUDE_SCREENING_MODEL` |
| Entry generation | Sonnet 4.6 | `CLAUDE_GENERATION_MODEL` |
| Quality validation | Haiku 4.5 | `CLAUDE_VALIDATION_MODEL` |

## Environment Variables Required

```
ANTHROPIC_API_KEY    — Claude API (required for pipeline)
CONGRESS_API_KEY     — Congress.gov API
COURTLISTENER_TOKEN  — CourtListener API
NEWS_API_KEY         — NewsAPI.org
```

## File Conventions

- Scripts in `scripts/` operate on `data/data.json` directly
- Enrichment logs go to `pipeline/logs/enrichment/`
- Legacy/archived files live in `Archive/legacy/`
- The comprehensive_update.py script (309 KB) contains large reference databases (INDIGENOUS_PEOPLES_BY_JURISDICTION, AFRICAN_DESCENDANT_PEOPLES_BY_JURISDICTION, etc.) that enrichment scripts import from

## Things NOT to Do

- Do not modify `data/data.json` by hand — use scripts or pipeline
- Do not create new top-level dated files (e.g., `2026 04 05 - [SCRIPT] - ...`) — put scripts in `scripts/` and logs in `pipeline/logs/`
- Do not create duplicate enrichment scripts — use `enrich_entries.py --community <type>`
- Do not create duplicate audit scripts — use `audit_toolkit.py` with flags
- Do not reference `tckc-tracker.html`, `nonprofit_tracker.db`, or individual `enrich_*.py` scripts — these are archived

## Related Documentation

- `SKILL.md` — Full system documentation with schema details
- `AUTOMATION_GUIDE.md` — Pipeline architecture and CI/CD
- `SYSTEM_SUMMARY.md` — High-level system overview
- `scripts/README.md` — Script usage guide
- `QUICKSTART.md` — Quick reference cheat sheet
