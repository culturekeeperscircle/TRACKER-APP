# TCKC Cultural Threats Tracker

A comprehensive monitoring system tracking 666+ federal government actions affecting the cultural resources of Indigenous, African-descendant, Latine, Asian American, Pacific Islander, and other marginalized communities in the United States.

**Public URL**: www.culturekeeperscircle.org/tracker
**Current state**: 666 entries across 5 categories (as of April 2, 2026)

## Architecture

The tracker is a **single-page HTML application** backed by a JSON database and a Python automation pipeline.

```
TRACKER APP/
├── index.html                  # Public tracker UI (6.2 MB, self-contained HTML/CSS/JS)
├── data/
│   ├── data.json               # Main database (666 entries, ~58 MB)
│   └── state.json              # Pipeline metadata (last run, entry counts)
├── pipeline/                   # Python automated ingestion pipeline
│   ├── main.py                 # Entry point (python -m pipeline)
│   ├── config.py               # API keys, models, relevance keywords
│   ├── sources/                # API connectors (Congress.gov, Federal Register,
│   │   ├── base.py             #   CourtListener, News API) with shared base class
│   │   ├── congress_gov.py
│   │   ├── federal_register.py
│   │   ├── courtlistener.py
│   │   └── news_api.py
│   ├── processing/             # Analysis chain
│   │   ├── relevance_filter.py #   Keyword + Claude screening
│   │   ├── claude_analyzer.py  #   Entry generation + 4Ps analysis
│   │   ├── deduplicator.py     #   Cross-source dedup
│   │   └── validator.py        #   Schema validation
│   ├── data/
│   │   ├── schema.py           # Entry field definitions + community taxonomy
│   │   └── data_manager.py     # JSON I/O
│   ├── prompts/                # Claude prompt templates
│   └── utils/                  # Logger, rate limiter, retry
├── scripts/
│   ├── comprehensive_update.py # Core automation (git sync + JSON merge + push)
│   ├── update.sh               # Shell wrapper (interactive/auto/dry-run)
│   ├── enrich_entries.py       # Unified enrichment (indigenous, african-descendant,
│   │                           #   targeted-gaps, fix-impacts)
│   ├── audit_toolkit.py        # Unified audit (word counts, structure, date ranges)
│   ├── add_legislation_batch.py
│   └── validate_forms.py
├── tckc-litigation-tracker/    # Node.js sub-app for litigation-specific tracking
├── International/              # Python sub-system for treaty/obligation extraction
├── Archive/                    # Legacy files and old script versions
├── .github/workflows/          # GitHub Actions (daily + manual + validation)
└── .vscode/tasks.json          # VS Code task buttons
```

## Data Schema

### Entry Fields (abbreviated keys for compact JSON)

| Key | Field | Type | Example |
|-----|-------|------|---------|
| `i` | Unique ID | string | `"eo-policy-name-2026"` |
| `t` | Document type | string | `"Executive Order"`, `"Public Law"` |
| `n` | Number/designation | string | `"EO 13933"`, `"H.R. 7822"` |
| `T` | Full title | string | HTML with color span for threat level |
| `s` | Summary slug | string | 2-5 word description |
| `d` | Date | string | ISO `YYYY-MM-DD` |
| `a` | Administration | string | `"Trump II"`, `"Biden"` |
| `A` | Agencies | array | `["DOI", "EPA"]` |
| `S` | Status | string | Current status description |
| `L` | Threat level | string | `"SEVERE"`, `"HARMFUL"`, `"PROTECTIVE"` |
| `D` | Description | string | 500-1500 words, HTML formatted |
| `I` | Impact analysis | object | Community keys -> 4Ps fields |
| `c` | Communities | array | `["indigenous", "africanAmerican"]` |
| `U` | Source URL | string | Official source link |
| `_source` | Data source | string | `"federal_register"`, `"congress_gov"` |

### Impact Analysis (4Ps / PPPT)

Each affected community gets four analysis dimensions (200-300 words each):

```json
"I": {
  "indigenous": {
    "people": "Who is affected...",
    "places": "Geographic/spatial impact...",
    "practices": "Cultural practices affected...",
    "treasures": "Material/cultural resources at risk..."
  }
}
```

### Threat Levels

| Level | Meaning |
|-------|---------|
| **SEVERE** | Direct, irreversible harm to cultural resources |
| **HARMFUL** | Significant but potentially reversible damage |
| **WATCH** | Monitoring level, moderate concern |
| **PROTECTIVE** | Defensive action (litigation, protective legislation) |

### Community Taxonomy (27 identifiers)

```
africanAmerican, indigenous, latine, asianAmerican, pacificIslander,
alaskaNative, nativeHawaiian, immigrant, lgbtq, women, disabled,
muslim, jewish, sikh, rural, urban, lowIncome, environmentalJustice,
academicCommunity, faithCommunities, arts, nonprofit, federalEmployees,
allCommunities
```

## Quick Start

### Run the pipeline
```bash
cd "Culture Keepers Circle/TRACKER APP"
pip install -r requirements.txt
export ANTHROPIC_API_KEY=... CONGRESS_API_KEY=... COURTLISTENER_TOKEN=... NEWS_API_KEY=...
python3 -m pipeline                          # Full run
python3 -m pipeline --dry-run                # Preview only
python3 -m pipeline --source congress_gov    # Single source
```

### Push updates
```bash
./scripts/update.sh              # Interactive
./scripts/update.sh --auto       # Fully automated
./scripts/update.sh --dry-run    # Preview
```

### Enrich entries
```bash
python3 scripts/enrich_entries.py --community indigenous --dry-run
python3 scripts/enrich_entries.py --community african-descendant --all
python3 scripts/enrich_entries.py --community targeted-gaps --all
python3 scripts/enrich_entries.py --community all --dry-run
```

### Audit data quality
```bash
python3 scripts/audit_toolkit.py --full                            # All entries
python3 scripts/audit_toolkit.py --word-counts --period 2025-01 2025-03
python3 scripts/audit_toolkit.py --structure --since 2025-10
python3 scripts/audit_toolkit.py --summary
```

## Dependencies

```
anthropic>=0.40.0    # Claude API for analysis
requests>=2.31.0     # HTTP API calls
```

## Environment Variables

| Variable | Required For | Notes |
|----------|-------------|-------|
| `ANTHROPIC_API_KEY` | Claude analysis | Set in GitHub Secrets or local env |
| `CONGRESS_API_KEY` | Congress.gov source | api.congress.gov |
| `COURTLISTENER_TOKEN` | CourtListener source | courtlistener.com API |
| `NEWS_API_KEY` | News API source | newsapi.org |

---

*The Culture Keepers Circle - Protecting Cultural Continuity Through Comprehensive Documentation*
