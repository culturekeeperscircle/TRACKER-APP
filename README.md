# TCKC Cultural Threats Tracker

An AI-powered monitoring system tracking U.S. federal government actions affecting the cultural resources of five primary ethnic communities.

**Public URL:** [www.culturekeeperscircle.org/tracker](https://www.culturekeeperscircle.org/tracker)
**Current state (2026-04-23):** ~755 entries across 6 categories.

## The Canonical Research Question

Every entry answers the same question:

> **Which laws and policies from [GOVERNMENT ENTITY] will severely harm the cultural resources (People, Places, Practices, and Treasures) paramount to the cultural continuity of [CULTURAL COMMUNITY], moderately harm those same cultural resources, or protect those same cultural resources?**

- **[GOVERNMENT ENTITY]** = U.S. federal entity (White House, agency, Congress, federal court, international body).
- **[CULTURAL COMMUNITY]** = one of five primary ethnic communities: **Indigenous** / **African-descendant** / **Latiné** / **Asian** / **Pacific Islander**.
- **Answers:** SEVERE / HARMFUL / PROTECTIVE (with WATCH for developing threats).

**Writing style.** Cultural continuity is the **severity rubric**. Prose in impact analysis leans into **imminent, immediate, concrete harms** (specific places, ceremonies, funding, families, leaders) — not formulaic generational rhetoric.

Full framing in [CLAUDE.md](CLAUDE.md#the-canonical-research-question-locked-2026-04-23).

---

## Documentation Map

| Audience | Start here |
|---|---|
| I'm an AI agent working on this project | [CLAUDE.md](CLAUDE.md) |
| I want to run or update the tracker | [docs/AUTOMATION.md](docs/AUTOMATION.md) |
| I just need the commands | [docs/QUICKSTART.md](docs/QUICKSTART.md) |
| I'm evaluating the tracker's research methodology | [docs/2026 04 23 - [METHODOLOGY] - Pipeline Queries and Research Questions Full Disclosure.md](docs/2026%2004%2023%20-%20%5BMETHODOLOGY%5D%20-%20Pipeline%20Queries%20and%20Research%20Questions%20Full%20Disclosure.md) |
| I want to read about the historical-backfill plan | [docs/2026 04 23 - [STRATEGY] - Historical Backfill and QA Plan Since Jan 19 2025.md](docs/2026%2004%2023%20-%20%5BSTRATEGY%5D%20-%20Historical%20Backfill%20and%20QA%20Plan%20Since%20Jan%2019%202025.md) |
| I'm an agent / need trigger skill | [SKILL.md](SKILL.md) |

---

## Architecture

The tracker is a self-contained single-page web app backed by a JSON database and a Python automated ingestion pipeline.

```
TCKC Threat Tracker/
├── CLAUDE.md              # AI operating instructions
├── SKILL.md               # Agent-triggered skill file
├── README.md              # You are here
├── index.html             # Public UI (6.2 MB, self-contained HTML/CSS/JS)
├── data/
│   ├── data.json                                # Source of truth (~58 MB, ~755 entries)
│   ├── state.json                               # Pipeline state (dedup IDs, last-run)
│   ├── state_level_archive_20260422.json        # Exported state-level entries (recoverable)
│   ├── data.json.bak-20260422-pre-mute          # Most recent rollback point
│   └── archive/                                 # Older backups and audit outputs
├── pipeline/              # Automated ingestion
│   ├── main.py
│   ├── config.py                                # API keys, keywords, subject filters
│   ├── sources/                                 # Federal Register, Congress.gov,
│   │                                            #   CourtListener, NewsAPI connectors
│   ├── processing/                              # Relevance, dedup, validation
│   ├── prompts/                                 # Claude prompt templates
│   ├── data/                                    # Schema + data manager
│   └── utils/                                   # Logger, rate limiter, retry
├── scripts/               # Manual tools (update.sh, audit, enrichment)
├── docs/
│   ├── AUTOMATION.md                            # Full update-workflow guide
│   ├── QUICKSTART.md                            # One-page cheat sheet
│   ├── 2026 04 23 - [METHODOLOGY] - ...         # Full research-question disclosure
│   ├── 2026 04 23 - [STRATEGY] - ...            # Historical backfill plan
│   ├── 2026 04 23 - [AUDIT] - ...               # Most recent triage report
│   └── archive/                                 # Old update summaries + deprecated docs
├── .github/workflows/                           # Daily cron, manual update, deep-sweep
├── Archive/                                     # Pre-pipeline legacy files
├── Aesthetics/                                  # Branding, logos, CSS snippets
├── International/                               # Treaty/UN obligation sub-system
└── tckc-litigation-tracker/                     # Node.js sub-app
```

---

## Pipeline at a Glance

```
4 sources → keyword filter → Claude Haiku screening → Claude Sonnet generation → dedup → validate → data.json
```

- **Sources:** Federal Register (no key), Congress.gov (key), CourtListener (token), NewsAPI (key)
- **Cap:** 50 entries per run by default (configurable via `MAX_ENTRIES_PER_RUN`)
- **Screening budget:** 20 min max per run
- **Run locally:** `python3 -m pipeline`
- **Runs automatically:** GitHub Actions daily at 5:00 AM ET (Mon–Fri)

Detailed methodology: [docs/2026 04 23 - [METHODOLOGY]...](docs/2026%2004%2023%20-%20%5BMETHODOLOGY%5D%20-%20Pipeline%20Queries%20and%20Research%20Questions%20Full%20Disclosure.md).

---

## Entry Schema (compact JSON)

Each entry carries 14–17 fields using single-letter keys for compactness. Most important:

| Key | Field | Example |
|---|---|---|
| `i` | Unique ID | `eo-14173`, `hr-1234-119`, `doi-notice-2026-001` |
| `T` | Title (HTML colored by threat) | `<span style="color:#991B1B;">EO 14173:</span> …` |
| `L` | Threat level | `SEVERE` / `HARMFUL` / `PROTECTIVE` / `WATCH` |
| `I` | Impact by Community (PPPT) | `{"indigenous": {"people":…, "places":…, "practices":…, "treasures":…}}` |
| `U` | Official source URL | Federal Register, Congress.gov, courtlistener.com, etc. |
| `muted` | Hidden from public view | `true` (with `_mutedReason`, `_mutedDate`) |

Full schema: [CLAUDE.md § Entry Schema](CLAUDE.md#entry-schema-single-letter-abbreviated-keys).

---

## Entry Categories (6)

`executive_actions` · `agency_actions` · `legislation` · `litigation` · `other_domestic` · `international`

## Threat Levels

- **SEVERE** (`#991B1B` red) — direct, immediate, often irreversible harm
- **HARMFUL** (`#CA8A04` amber) — significant but reversible harm
- **WATCH** — monitoring level (rare)
- **PROTECTIVE** (`#065F46` green) — defensive or positive action

## Community Taxonomy (27)

```
africanAmerican, indigenous, latine, asianAmerican, pacificIslander,
alaskaNative, nativeHawaiian, immigrant, lgbtq, women, disabled,
muslim, jewish, sikh, rural, urban, lowIncome, environmentalJustice,
academicCommunity, faithCommunities, arts, nonprofit, federalEmployees,
allCommunities
```

---

## Scope (locked 2026-04-23)

**Federal actions only.** State/municipal/campus actions are out of scope; if they slip in, they get muted (`muted: true`), never deleted. Federal cases with state parties stay federal. NAGPRA notices: individual entries for federal-actor notices (DOI, NPS, Army Corps, BIA, SI); a single monthly "NAGPRA Roundup" PROTECTIVE aggregate for state/university/private-institution notices.

Full scope rules: [CLAUDE.md § Scope Rules](CLAUDE.md#scope-rules-locked-2026-04-23).

---

## Dependencies

```
anthropic>=0.40.0
requests>=2.31.0
python-dotenv>=1.0.0
```

Install with `pip install -r requirements.txt`.

## Environment Variables

| Variable | Purpose |
|---|---|
| `ANTHROPIC_API_KEY` | Claude screening, generation, validation |
| `CONGRESS_API_KEY` | Congress.gov source |
| `COURTLISTENER_TOKEN` | CourtListener source |
| `NEWS_API_KEY` | NewsAPI source |
| `MAX_ENTRIES_PER_RUN` | Optional cap override (default 50) |
| `SCREENING_TIME_BUDGET` | Optional Haiku screening budget override |
| `LOOKBACK_DAYS` | Optional lookback override (default: use state.json) |
| `DRY_RUN` | Preview mode (default false) |
| `SOURCE_FILTER` | Single-source filter (default: all) |

All loaded from `.env` (git-ignored) or shell exports. Template in `.env.example`.

---

## Partners

The Tracker is the empirical backbone for:

- **Prince Albert III's law review article** (*Redefining Culture*) — 9.3:1 ratio of SEVERE/HARMFUL to PROTECTIVE is a headline finding.
- **Prince's book** (*Against the Peoples Who Built the Nation*) — provides the hegemonic-encounter documentation.
- **BGHPN Storymap Partnership** — state-level data layer consuming muted state entries (first five-state pilot due 2026-05-28).
- **Cultural Heritage Partners** litigation firm — Tracker feeds their case-identification pipeline (overlaps with *Fight Back* litigation).
- **NPCA National Cultural Resource Coalition (NCRC)** — CKC founding member.

---

*Last updated 2026-04-23.*
