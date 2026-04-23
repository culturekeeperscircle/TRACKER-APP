---
name: tckc-threat-tracker
description: >
  The TCKC Cultural Threats Tracker — an AI-powered monitoring and research system that tracks federal government actions affecting the cultural resources of Indigenous, African-descendant, and other marginalized communities in the United States. Use this skill whenever Prince mentions: the tracker, threat tracker, tracker entries, tracker pipeline, adding entries, enrichment, impact analysis, 4Ps analysis, tracker data, tracker audit, tracker export, community impact, threat levels, SEVERE/HARMFUL/PROTECTIVE entries, federal actions tracking, Congress.gov, Federal Register, CourtListener, tracker HTML, tracker updates, or pipeline runs. Also trigger when working on the law review article's empirical backbone (630+ entries) or the TCKC website's tracker page.
---
## WRITING STYLE RULES (MANDATORY)

Every piece of prose produced for Prince in this project must follow the six enshrined rules in [WRITING_STYLE_RULES.md](../../WRITING_STYLE_RULES.md). Summary:

1. No run-on sentences.
2. No awkward uses of the colon.
3. No em-dashes, ever.
4. No "not X, but Y" constructions in any form.
5. Argumentative writing must be logically sound and valid.
6. Explanatory text uses strong, epistemically grounded, declarative sentences.

Run the self-check in the canonical file before submitting any writing. Violations are regressions.


# TCKC Cultural Threats Tracker

## System Overview

The TCKC Cultural Threats Tracker is the empirical backbone of Prince's law review article and The Culture Keepers Circle's public advocacy. It is a comprehensive, searchable database that catalogs federal government actions — executive orders, legislation, litigation, agency actions, and international developments — that affect the cultural resources of marginalized communities in the United States.

**Public URL**: www.culturekeeperscircle.org/tracker
**Current state (as of April 2, 2026)**: 666 entries across 5 categories

The tracker serves three purposes:
1. **Research tool** — Provides the empirical foundation for Prince's law review article (the "dual inventory" of harm and defense)
2. **Advocacy tool** — Public-facing resource for CKC's mission, used by community members, advocates, and policymakers
3. **Monitoring system** — Automated pipeline that scans federal sources for new relevant actions

## Architecture

```
TCKC Threat Tracker/
├── pipeline/                    # Python automated ingestion pipeline
│   ├── main.py                 # Pipeline entry point
│   ├── config.py               # API keys, model config, relevance keywords
│   ├── __main__.py             # Module runner
│   ├── sources/                # Data source connectors (all inherit from base)
│   │   ├── base.py             # BaseSourceConnector + MultiQuerySourceConnector ABCs
│   │   ├── congress_gov.py     # Congress.gov API (bills, resolutions)
│   │   ├── federal_register.py # Federal Register API (EOs, rules, notices)
│   │   ├── courtlistener.py    # CourtListener API (litigation)
│   │   └── news_api.py         # News API (implementation coverage)
│   ├── processing/             # Analysis and validation
│   │   ├── relevance_filter.py # Keyword + Claude screening
│   │   ├── claude_analyzer.py  # Claude-powered entry generation + 4Ps analysis
│   │   ├── deduplicator.py     # Cross-source deduplication
│   │   └── validator.py        # Schema validation
│   ├── data/                   # Data management
│   │   ├── schema.py           # Entry field definitions
│   │   └── data_manager.py     # JSON I/O, merging
│   ├── utils/                  # Shared utilities
│   │   ├── logger.py
│   │   ├── rate_limiter.py
│   │   └── retry.py
│   ├── prompts/                # Claude prompt templates
│   │   ├── relevance_screening.txt
│   │   ├── entry_generation.txt
│   │   └── quality_check.txt
│   └── logs/                   # Pipeline run logs
├── scripts/                    # Automation and enrichment scripts
│   ├── comprehensive_update.py # Core automation engine (JSON merge + git push)
│   ├── update.sh               # Shell wrapper (interactive/auto/dry-run)
│   ├── enrich_entries.py       # Unified enrichment (--community indigenous|african-descendant|targeted-gaps|fix-impacts|all)
│   ├── audit_toolkit.py        # Unified audit (--word-counts|--structure|--full|--summary, --period, --since)
│   ├── add_legislation_batch.py
│   ├── validate_forms.py
│   └── README.md
├── index.html                  # Public tracker UI (deployed to website, self-contained)
└── Archive/                    # Legacy scripts and historical versions
```

## Data Sources

| Source | API | What It Provides | Key Config |
|--------|-----|-----------------|------------|
| **Congress.gov** | `congress_gov.py` | Bills, resolutions, legislative actions | `CONGRESS_API_KEY` |
| **Federal Register** | `federal_register.py` | Executive orders, agency rules, notices | Public API (no key) |
| **CourtListener** | `courtlistener.py` | Litigation filings, court orders | `COURTLISTENER_TOKEN` |
| **News API** | `news_api.py` | Implementation coverage, reactions | `NEWS_API_KEY` |

## Processing Pipeline

Data flows through five stages:

1. **Source Fetch** — Each source module queries its API for new items since `last_successful_run` (stored in `state.json`). Returns raw documents.

2. **Relevance Filtering** (`relevance_filter.py`) — Two-pass filter:
   - **Keyword pre-filter**: Matches against ~200 relevance keywords in `config.py` (cultural heritage, ethnic communities, specific agencies, bill topics)
   - **Claude screening** (Haiku model): Classifies borderline items as relevant/irrelevant with confidence score

3. **Entry Generation** (`claude_analyzer.py`) — Claude Sonnet generates full tracker entries:
   - Assigns threat level (SEVERE, HARMFUL, or PROTECTIVE)
   - Writes description (500-1500 words)
   - Generates 4Ps impact analysis per affected community (People, Places, Practices, Treasures — 200-300 words each)
   - Maps to community taxonomy
   - Assigns agency codes

4. **Deduplication** (`deduplicator.py`) — Cross-source matching to prevent duplicate entries for the same action

5. **Validation** (`validator.py`) — Schema compliance check against `ENTRY_SCHEMA`

## Data Schema

### Entry Fields (15 required)

| Field | Key | Type | Description |
|-------|-----|------|-------------|
| Unique ID | `i` | string | e.g., `"eo-policy-name-2026"` |
| Document type | `t` | string | e.g., `"Executive Order"`, `"Public Law"` |
| Number | `n` | string | e.g., `"EO 13933"`, `"H.R. 7822"` |
| Full title | `T` | string | HTML with color span |
| Summary | `s` | string | 2-5 word slug |
| Date | `d` | string | ISO format `YYYY-MM-DD` |
| Administration | `a` | string | `"Trump II"`, `"Biden"`, etc. |
| Agencies | `A` | array | Agency abbreviation strings |
| Status | `S` | string | Current status description |
| Threat level | `L` | string | `"SEVERE"`, `"HARMFUL"`, or `"PROTECTIVE"` |
| Description | `D` | string | 500-1500 words, HTML formatted |
| Impact analysis | `I` | object | Community keys → 4Ps fields |
| Communities | `c` | array | Affected community identifiers |
| Source URL | `U` | string | Official source |

### Impact Analysis Structure (4Ps / PPPT)
```json
"I": {
  "communityKey": {
    "people": "200-300 words on impact to People",
    "places": "200-300 words on impact to Places",
    "practices": "200-300 words on impact to Practices",
    "treasures": "200-300 words on impact to Treasures"
  }
}
```

### Threat Levels
- **SEVERE** — Direct, immediate harm to cultural resources
- **HARMFUL** — Indirect or delayed harm
- **PROTECTIVE** — Defensive action (judicial intervention, protective legislation, etc.)

### Entry Categories
- `executive_actions` (100 entries)
- `agency_actions` (201 entries)
- `legislation` (179 entries)
- `litigation` (125 entries)
- `international` (60 entries)

## Frontend / UI

- **`index.html`** — The primary public-facing tracker deployed to CKC website. Single-page app with search, filtering by category/threat level/community, expandable entries with full impact analysis. Self-contained (all JS/CSS inline).

## Key Scripts

| Script | Purpose |
|--------|---------|
| `scripts/comprehensive_update.py` | Core automation: validates JSON, git sync, merges entries, commits, pushes, verifies |
| `scripts/update.sh` | User-friendly shell wrapper with interactive/auto/dry-run modes |
| `scripts/enrich_entries.py` | Unified enrichment engine (`--community indigenous\|african-descendant\|targeted-gaps\|fix-impacts\|all`) |
| `scripts/audit_toolkit.py` | Unified audit tool (`--word-counts\|--structure\|--full\|--summary`, with `--period`/`--since` date filters) |
| `scripts/add_legislation_batch.py` | Batch add legislation entries |
| `scripts/validate_forms.py` | Validate entry schema compliance |

## Enrichment & Audit History

Multiple enrichment passes have been run to improve data quality:
- **African-descendant enrichment** (April 3, 2026): Targeted gaps in 4Ps analysis for African-descendant communities
- **Indigenous enrichment**: Similar pass for Indigenous community impacts
- **Targeted gap enrichment**: Filled specific missing analyses identified by audit scripts
- **Word count audits**: Ensured impact analyses meet 200-300 word minimums per 4Ps field
- **Ongoing**: 156 entries still need dropdown analyses (per TCKC audit memory)

## Current State (April 2, 2026)

- **666 total entries** across 5 categories
- **9 entries added** in most recent update cycle (March 27 - April 2, 2026)
- **Pipeline**: Operational with all 4 sources configured
- **Claude models**: Haiku 4.5 for screening/validation, Sonnet 4.6 for entry generation
- **Data quality**: 100% schema compliant; some entries still need enriched 4Ps analyses
- **Automation**: Single-command update via `./scripts/update.sh --auto` (30 seconds)

## Workflow: Common Operations

### Adding New Entries
1. Create JSON file with new entries following schema
2. Run: `./scripts/update.sh --auto`
3. Verify on GitHub and public tracker

### Running the Pipeline
```bash
cd "Culture Keepers Circle/TCKC Threat Tracker"
python3 -m pipeline              # Full pipeline run
python3 -m pipeline --dry-run    # Preview only
python3 -m pipeline --source congress_gov  # Single source
```

### Running Enrichment
```bash
python3 scripts/enrich_entries.py --community indigenous --dry-run
python3 scripts/enrich_entries.py --community african-descendant --all
python3 scripts/enrich_entries.py --community targeted-gaps --all
python3 scripts/enrich_entries.py --community all --dry-run
```

### Auditing Data Quality
```bash
python3 scripts/audit_toolkit.py --full                            # All entries
python3 scripts/audit_toolkit.py --word-counts --period 2025-01 2025-03
python3 scripts/audit_toolkit.py --structure --since 2025-10
python3 scripts/audit_toolkit.py --summary
```

### Exporting Data
The tracker data is stored in:
- `data/data.json` (single source of truth — deployed to website, ~58 MB, 666 entries)
- `data/state.json` (pipeline metadata — last run, entry counts)

## Dependencies & Setup

### Requirements
```
anthropic>=0.40.0
requests>=2.31.0
```

### Environment Variables
```bash
ANTHROPIC_API_KEY=sk-ant-...     # Required for Claude analysis
CONGRESS_API_KEY=...              # Required for Congress.gov source
COURTLISTENER_TOKEN=...           # Required for CourtListener source
NEWS_API_KEY=...                  # Required for News API source
```

### Running
```bash
cd "Culture Keepers Circle/TCKC Threat Tracker"
pip install -r requirements.txt
export ANTHROPIC_API_KEY=...
python3 -m pipeline
```

## Relationship to Other Projects

The Tracker provides the empirical backbone for Prince's law review article. The article's "dual inventory" of 5 Attack Vectors (harm) and 4 Defense Vectors (defense) is directly derived from tracker data. The 9.3:1 ratio of SEVERE/HARMFUL to PROTECTIVE entries is a key finding.

### Connected Project SKILLs
- **Law Review Article**: `Academic Work/Law Review Article - Redefining Culture/SKILL.md`
- **Book — Against the Peoples**: `Academic Work/Book - Against the Peoples Who Built the Nation/book-writer-SKILL.md`
