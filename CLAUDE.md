# TCKC Cultural Threats Tracker — AI Operating Instructions

Every AI agent working on this project reads this file first.

---

## WRITING STYLE RULES (MANDATORY)

All prose produced for Prince must follow the six enshrined rules in [WRITING_STYLE_RULES.md](../../WRITING_STYLE_RULES.md):

1. No run-on sentences.
2. No awkward uses of the colon.
3. No em-dashes, ever.
4. No "not X, but Y" constructions in any form.
5. Argumentative writing must be logically sound and valid.
6. Explanatory text uses strong, epistemically grounded, declarative sentences.

Run the self-check before submitting writing. Violations are regressions.

---

## What This Project Is

A **FEDERAL** government action tracker monitoring threats to the cultural resources of five primary ethnic communities. It powers The Culture Keepers Circle's public advocacy and Prince's law review article.

**Current state (2026-04-23):**
- ~755 entries across 6 categories
- Single source of truth: `data/data.json` (~58 MB)
- Frontend: `index.html` (self-contained single-page app, 6.2 MB)
- Public URL: www.culturekeeperscircle.org/tracker
- Automation: Python pipeline + GitHub Actions daily cron

## The Canonical Research Question (locked 2026-04-23)

Every entry, every pipeline screening call, and every analytical pass answers the same question:

> **Which laws and policies from [GOVERNMENT ENTITY] will severely harm the cultural resources (People, Places, Practices, and Treasures) paramount to the cultural continuity of [CULTURAL COMMUNITY], moderately harm those same cultural resources, or protect those same cultural resources?**

Where:

- **[GOVERNMENT ENTITY]** is a U.S. federal entity identified by the tracker's source pipeline: White House, federal agency, Congress, federal court, or international body.
- **[CULTURAL COMMUNITY]** is one of the **five primary ethnic communities**:
  1. **Indigenous** — Native American nations, Alaska Native, Native Hawaiian
  2. **African-descendant** — African American, Afro-Caribbean, Afro-Latiné, African diaspora
  3. **Latiné** — Latin American, Chicano, Hispanic, Latinx
  4. **Asian** — Asian American, AANHPI, South Asian, Southeast Asian, East Asian
  5. **Pacific Islander** — Native Hawaiian, Samoan, Tongan, Chamorro, Polynesian, Micronesian, Melanesian

The three valid answers are:

- **SEVERE** — direct, immediate, often irreversible harm to PPPT resources paramount to cultural continuity
- **HARMFUL** — significant but reversible harm
- **PROTECTIVE** — safeguards, restores, funds, or defends those resources

**"Cultural continuity"** is the **severity rubric** — the test that tells you why something earns SEVERE, HARMFUL, or PROTECTIVE. A law or policy is paramount when it shapes the community's capacity to persist across generations as a distinct cultural entity along one of the four PPPT dimensions.

**Writing style for impact analysis.** Cultural continuity is the theoretical anchor, but PPPT prose should lean into **imminent, immediate, concrete harms** — specific places being razed, specific ceremonies being suppressed, specific funding being rescinded, specific families being separated. Abstract generational or continuity rhetoric is not required. A strong entry describes harm that is already happening or about to happen with named facts, real places, and identifiable people. The continuity framing justifies severity; the prose makes the harm visible.

- **People** — demographic survival, civil rights, dignified existence, leadership, migration and assembly, health and education access, immigration status, safety.
- **Places** — sacred sites, heritage sites, tribal lands, historic districts, cultural neighborhoods, diaspora homelands, museums, archives, cultural centers.
- **Practices** — religious and spiritual observance, language transmission, foodways, folk arts, ceremonies, dance and music, oral histories, traditional ecological knowledge.
- **Treasures** — material culture, artifacts, archives, intellectual property, historic documents, ancestral remains, sacred objects, artistic works, inherited land and assets.

Items may also touch secondary communities (LGBTQ+, immigrants, women, disabled, faith communities, federal employees, environmental-justice communities, etc.). Code those as additional affected communities. The PRIMARY focus stays on the five ethnic communities above.

---

## Scope Rules (locked 2026-04-23)

### 1. FEDERAL ACTIONS ONLY

State legislation, state regulations, state executive orders, municipal ordinances, campus-level resolutions, and local events are **out of scope** unless they are federal-law-implementing actions by a federal actor. Entries on state/local actions that slip into the tracker must be **muted** (`muted: true` plus `_mutedReason` and `_mutedDate`), **never deleted**. They may be useful for sibling state-layer projects (e.g., the BGHPN storymap five-state layer).

### 2. Federal cases with state parties STAY FEDERAL

Lawsuits in federal courts where a state is a plaintiff or defendant (e.g., *Texas v. Kennedy*, *Oregon v. USDA*, *Doe v. State of Kansas* federal challenge) are in scope. The forum is what matters, not the party name.

### 3. NAGPRA notices — federal-actor-only + monthly aggregate

- **Code individually:** NAGPRA notices from **federal actors** (DOI, NPS, U.S. Army Corps of Engineers, BIA, Smithsonian).
- **Skip individually:** NAGPRA notices from state agencies, state universities, private universities, city/county museums, private institutions.
- **Aggregate instead:** One **"NAGPRA Roundup: <Month> <Year>"** PROTECTIVE entry per calendar month, summarizing all skipped state/university/private-institution notices published that month, with count and representative list.

---

## Categories (6)

| Category | Description |
|---|---|
| `executive_actions` | Executive Orders, Presidential Proclamations, Presidential Memoranda |
| `agency_actions` | Final Rules, Proposed Rules, Agency Notices, Secretary Orders, agency memoranda |
| `legislation` | Public Laws, Bills, Joint Resolutions, Continuing Resolutions |
| `litigation` | Court Opinions, Court Orders, Consent Decrees, Settlements, Amicus Briefs |
| `other_domestic` | Policy Directives, Advisory Reports, IG Reports, GAO Reports |
| `international` | Treaties, UN Resolutions, International Agreements, UNESCO Decisions |

---

## Threat Levels

- `SEVERE` — Direct, immediate, often irreversible harm (red `#991B1B`)
- `HARMFUL` — Significant but reversible harm (amber `#CA8A04`)
- `WATCH` — Monitoring level; rare
- `PROTECTIVE` — Defensive or positive action (green `#065F46`)

---

## Community Keys (27)

```
africanAmerican, indigenous, latine, asianAmerican, pacificIslander,
alaskaNative, nativeHawaiian, immigrant, lgbtq, women, disabled,
muslim, jewish, sikh, rural, urban, lowIncome, environmentalJustice,
academicCommunity, faithCommunities, arts, nonprofit, federalEmployees,
allCommunities
```

(Plus a handful of human-readable display forms used in some legacy entries: "African-descendant", "Indigenous/Tribal", "Latiné", etc. Both forms coexist.)

---

## Entry Schema (single-letter abbreviated keys)

```
i = ID          t = document type   n = official number    T = HTML title
s = short slug   d = date (ISO)      a = administration     A = agencies[]
S = status       L = threat level    D = 500–1500 word desc  I = PPPT by community
c = communities[] U = official source URL   _source = source tag
```

### Mute metadata (added 2026-04-23)
```
muted        = true                            # Hides from public view
_mutedReason = "why it's muted"                # Plain English
_mutedDate   = "YYYY-MM-DD"                    # When muted
```

### Cross-ref metadata
```
_crossRef = [{merged_from, merged_source_url, merged_date}]  # For merged duplicates
```

### PPPT (Impact by Community)
```json
"I": {
  "indigenous": {
    "people": "150–300 words",
    "places": "150–300 words",
    "practices": "150–300 words",
    "treasures": "150–300 words"
  }
}
```

---

## Pipeline Architecture

```
Sources (4 APIs) → Keyword Filter → Claude Haiku Screening → Claude Sonnet Generation → Dedup → Validate → data.json
```

| Source | Connector | API key env var |
|---|---|---|
| Federal Register | `pipeline/sources/federal_register.py` | (none; public) |
| Congress.gov | `pipeline/sources/congress_gov.py` | `CONGRESS_API_KEY` |
| CourtListener | `pipeline/sources/courtlistener.py` | `COURTLISTENER_TOKEN` |
| NewsAPI | `pipeline/sources/news_api.py` | `NEWS_API_KEY` |

All connectors inherit from `pipeline/sources/base.py`.

### Claude models

| Stage | Model | Config key |
|---|---|---|
| Relevance screening | Haiku 4.5 | `CLAUDE_SCREENING_MODEL` |
| Entry generation | Sonnet 4.6 | `CLAUDE_GENERATION_MODEL` |
| Quality validation | Haiku 4.5 | `CLAUDE_VALIDATION_MODEL` |

### Pipeline caps

| Setting | Default | Purpose |
|---|---|---|
| `MAX_ENTRIES_PER_RUN` | **50** | Entry-generation cap per run |
| `SCREENING_TIME_BUDGET` | **1200s (20 min)** | Max Haiku screening time per run |
| GitHub Actions workflow timeout | **90 min** (daily), **300 min** (deep-sweep) | Hard kill |

Full methodology disclosure: `docs/2026 04 23 - [METHODOLOGY] - Pipeline Queries and Research Questions Full Disclosure.md`.

---

## Frontend Behavior

- `index.html` is self-contained (all JS/CSS inline) and loads `data/data.json` at runtime.
- Muted entries (`muted: true`) are hidden from public view.
- Auditors override via URL param: `?show_muted=1`.
- Search, filter, and sort are client-side.

---

## Key Commands

| Task | Command |
|---|---|
| Run pipeline | `python3 -m pipeline` |
| Run pipeline (big catch-up) | `MAX_ENTRIES_PER_RUN=200 python3 -m pipeline` |
| Push manual entries | `./scripts/update.sh --auto` |
| Audit data | `python3 scripts/audit_toolkit.py --full` |
| Enrich entries | `python3 scripts/enrich_entries.py --community <type> --dry-run` |
| Validate a single entry | `python3 scripts/validate_forms.py` |

Full guide: `docs/AUTOMATION.md`. One-page cheat sheet: `docs/QUICKSTART.md`.

---

## File Layout

```
├── CLAUDE.md              # This file. AI operating rules.
├── SKILL.md               # Agent skill frontmatter; triggers this skill.
├── README.md              # Public-facing overview.
├── index.html             # Self-contained public UI.
├── data/
│   ├── data.json                                # Source of truth. ~58 MB.
│   ├── state.json                               # Pipeline state; dedup IDs.
│   ├── state_level_archive_20260422.json        # Exported state-level entries (recoverable).
│   ├── data.json.bak-20260422-pre-mute          # Most recent rollback point.
│   └── archive/                                 # Older backups and audit outputs.
├── pipeline/              # Automated ingestion (sources, processing, prompts, utils).
├── scripts/               # Automation and enrichment scripts.
├── docs/
│   ├── AUTOMATION.md      # Full update-workflow guide.
│   ├── QUICKSTART.md      # One-page cheat sheet.
│   ├── 2026 04 23 - [METHODOLOGY] - ...     # Full query/research-question disclosure.
│   ├── 2026 04 23 - [STRATEGY] - ...        # Historical backfill plan.
│   ├── 2026 04 23 - [AUDIT] - ...           # Recent triage report.
│   └── archive/           # Old update summaries + deprecated instruction files.
├── .github/workflows/     # GitHub Actions for daily cron + deep-sweep.
├── .env                   # API keys (git-ignored).
├── .env.example           # Template.
└── Archive/               # Legacy project files (pre-pipeline).
```

---

## Things NOT to Do

- **Do not modify `data/data.json` by hand.** Use the pipeline, the scripts in `scripts/`, or a Python script that loads + saves the JSON atomically.
- **Do not delete entries.** Mute (`muted: true`) instead. Deletion loses recoverability.
- **Do not create new top-level dated files** (e.g., `2026 04 05 - [SCRIPT] - ...`). Scripts belong in `scripts/`; logs belong in `pipeline/logs/`; docs belong in `docs/`.
- **Do not create duplicate enrichment or audit scripts.** Use `enrich_entries.py` and `audit_toolkit.py` with flags.
- **Do not commit `.env`, `.DS_Store`, or `update_log_*.txt`.** The `.gitignore` blocks them; if any slip through, remove them.
- **Do not bypass the mute policy.** State/local entries get muted with reason + date, not deleted.

---

## Related Documents

- `SKILL.md` — Agent skill file (triggers this skill on the right requests)
- `README.md` — Public-facing overview
- `docs/AUTOMATION.md` — Full workflow guide
- `docs/QUICKSTART.md` — One-page cheat sheet
- `docs/2026 04 23 - [METHODOLOGY] - Pipeline Queries and Research Questions Full Disclosure.md` — Full transparency on every query and research question
- `docs/2026 04 23 - [STRATEGY] - Historical Backfill and QA Plan Since Jan 19 2025.md` — Backfill plan
- `scripts/README.md` — Per-script usage
- `docs/archive/` — Deprecated legacy instruction files (AUTOMATION_GUIDE.md, SYSTEM_SUMMARY.md, VS_CODE_BUTTON_GUIDE.md, INDEX.md), preserved for reference
- `docs/archive/UPDATE_SUMMARY_*.md` — Historical change logs per update cycle

---

*Last updated 2026-04-23 during folder cleanup and NAGPRA-policy lock.*
