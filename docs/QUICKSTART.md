# TCKC Tracker — Quick Start

One page. Everything you need to run, update, or audit the tracker.

---

## Run the automated pipeline

```bash
cd "Culture Keepers Circle/TCKC Threat Tracker"
python3 -m pipeline
```

Fetches from 4 APIs since last run, screens with Claude, generates up to 50 entries, writes to `data/data.json`, pushes state. Takes 20–50 min.

**Common overrides:**
```bash
MAX_ENTRIES_PER_RUN=200 python3 -m pipeline      # Big catch-up run
DRY_RUN=true python3 -m pipeline                  # Preview only
LOOKBACK_DAYS=30 python3 -m pipeline              # Force 30-day window
SOURCE_FILTER=federal_register python3 -m pipeline  # Single source
```

## Push manually drafted entries

```bash
# 1. Drop entries JSON into tracker root: NEW_ENTRIES_APRIL_2026.json
# 2. Run:
./scripts/update.sh --auto      # Fully automated
./scripts/update.sh              # Interactive confirmation
./scripts/update.sh --dry-run    # Preview only
```

## Audit data quality

```bash
python3 scripts/audit_toolkit.py --full                          # Full audit
python3 scripts/audit_toolkit.py --summary                       # Quick counts
python3 scripts/audit_toolkit.py --word-counts --period 2025-Q1  # Specific period
python3 scripts/audit_toolkit.py --structure --since 2025-10
```

## Enrich existing entries

```bash
python3 scripts/enrich_entries.py --community indigenous --dry-run
python3 scripts/enrich_entries.py --community african-descendant --all
python3 scripts/enrich_entries.py --community targeted-gaps --all
```

## Canonical files

| File | Purpose |
|---|---|
| `data/data.json` | Single source of truth. ~58 MB. Do not hand-edit. |
| `data/state.json` | Pipeline state (last run, dedup IDs). |
| `index.html` | Self-contained public UI (6.2 MB). |
| `CLAUDE.md` | AI operating rules (scope, NAGPRA policy, style). |
| `SKILL.md` | Agent skill frontmatter and overview. |
| `README.md` | Public-facing overview. |
| `docs/AUTOMATION.md` | Full update workflow guide. |

## Entry schema (15 fields)

| Field | Key | What |
|---|---|---|
| ID | `i` | `eo-{num}`, `hr-{num}-{congress}`, `{agency}-{type}-{year}-{seq}` |
| Type | `t` | "Executive Order", "Public Law", "Court Opinion", etc. |
| Number | `n` | Official designation |
| Title | `T` | HTML color span per threat level |
| Summary | `s` | 2–5 word slug |
| Date | `d` | `YYYY-MM-DD` |
| Administration | `a` | "Trump II", "Biden", etc. |
| Agencies | `A` | Array of abbreviations |
| Status | `S` | Description |
| Threat level | `L` | `SEVERE`, `HARMFUL`, `PROTECTIVE`, or `WATCH` |
| Description | `D` | 500–1500 words, HTML |
| Impact | `I` | Community keys → {people, places, practices, treasures} × 150–300 words each |
| Communities | `c` | Array of community names |
| Source URL | `U` | Official government / court URL |
| Source tag | `_source` | e.g., `federal_register_2026` |

## Threat-level colors (HTML spans in `T` field)

- SEVERE: `#991B1B` (red)
- HARMFUL: `#CA8A04` (amber)
- PROTECTIVE: `#065F46` (green)

## Categories (6)

`executive_actions`, `agency_actions`, `legislation`, `litigation`, `other_domestic`, `international`

## Scope rules (as of 2026-04-23)

1. **FEDERAL ACTIONS ONLY.** State/local gets muted (`muted: true`), never deleted.
2. **Federal cases with state parties stay federal.** Forum matters.
3. **NAGPRA notices:** keep only federal-actor notices (DOI, NPS, Army Corps, BIA, SI); aggregate state/university notices into monthly "NAGPRA Roundup" PROTECTIVE entries.

## When things go wrong

| Symptom | Fix |
|---|---|
| Pipeline blocks on "uncommitted changes" | `git stash -u` or commit first |
| Pipeline returns 0 entries | Check dedup — items likely in `processed_ids`. Clear them or set `LOOKBACK_DAYS` |
| Cap hit, entries dropped | `MAX_ENTRIES_PER_RUN=N python3 -m pipeline` with higher N, or reset state |
| `python-dotenv` import error | `pip install -r requirements.txt` |
| API key missing | Check `.env` file in tracker root |

## Related docs

- `docs/AUTOMATION.md` — Full workflow guide
- `docs/2026 04 23 - [METHODOLOGY] - Pipeline Queries and Research Questions Full Disclosure.md` — All queries and research questions
- `docs/2026 04 23 - [STRATEGY] - Historical Backfill and QA Plan Since Jan 19 2025.md` — Backfill strategy

---

*Last updated 2026-04-23.*
