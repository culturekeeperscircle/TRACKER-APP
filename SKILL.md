---
name: tckc-threat-tracker
description: >
  The TCKC Cultural Threats Tracker is an AI-powered monitoring and research
  system that tracks U.S. FEDERAL government actions affecting the cultural
  resources of Indigenous, African-descendant, Latiné, Asian American, Pacific
  Islander, and other marginalized communities. Use this skill whenever Prince
  mentions: the tracker, threat tracker, TCKC, tracker entries, tracker
  pipeline, adding entries, enrichment, impact analysis, 4Ps or PPPT analysis,
  People Places Practices Treasures, tracker data, tracker audit, tracker
  export, community impact, threat levels, SEVERE / HARMFUL / PROTECTIVE /
  WATCH entries, federal-actions tracking, Congress.gov, Federal Register,
  CourtListener, NewsAPI, tracker HTML, tracker updates, pipeline runs, NAGPRA
  Roundup, state-level mute, muted entries, cap / MAX_ENTRIES_PER_RUN,
  historical backfill since Jan 19 2025, or the law review article's empirical
  backbone. Also trigger for work on the TCKC website's tracker page, any
  partner integration pulling Tracker data (BGHPN storymap, Cultural Heritage
  Partners, NPCA NCRC), or the BGHPN storymap five-state layer (which is a
  sibling project that consumes muted state-level entries).
---

# TCKC Cultural Threats Tracker — Skill File

This skill file is the agent-triggered entry point. For operating rules, scope, and NAGPRA policy, read [CLAUDE.md](CLAUDE.md). For full workflow, read [docs/AUTOMATION.md](docs/AUTOMATION.md).

---

## WRITING STYLE RULES (MANDATORY)

All prose must follow the six rules in [WRITING_STYLE_RULES.md](../../WRITING_STYLE_RULES.md):

1. No run-on sentences.
2. No awkward uses of the colon.
3. No em-dashes, ever.
4. No "not X, but Y" constructions.
5. Argumentative writing must be logically sound and valid.
6. Explanatory text uses strong, epistemically grounded, declarative sentences.

---

## The Canonical Research Question (locked 2026-04-23)

> **Which laws and policies from [GOVERNMENT ENTITY] will severely harm the cultural resources (People, Places, Practices, and Treasures) paramount to the cultural continuity of [CULTURAL COMMUNITY], moderately harm those same cultural resources, or protect those same cultural resources?**

- **[GOVERNMENT ENTITY]** = U.S. federal entity (White House, agency, Congress, federal court, international body).
- **[CULTURAL COMMUNITY]** = one of five primary ethnic communities: **Indigenous** / **African-descendant** / **Latiné** / **Asian** / **Pacific Islander**.
- Answers: **SEVERE** / **HARMFUL** / **PROTECTIVE** (with `WATCH` for developing threats).

**Writing style for impact analysis.** Cultural continuity is the **severity rubric** — the reason an entry earns SEVERE, HARMFUL, or PROTECTIVE. The PROSE in `impactByCommunity` leans into **imminent, immediate, concrete harms** already happening or about to happen (specific places being razed, specific ceremonies suppressed, specific funding rescinded, specific families separated, specific leaders targeted). Do NOT use formulaic generational rhetoric as a substitute for analysis. The continuity framing justifies severity; the prose makes the harm visible through named facts, real places, and identifiable people.

Full framing (including what "cultural continuity" and "paramount" mean, and the writing-style standard) lives in [CLAUDE.md](CLAUDE.md#the-canonical-research-question-locked-2026-04-23).

## System at a Glance

**Purpose.** Federal government action tracker used for CKC public advocacy and Prince's law review article. Provides the empirical backbone for his "dual inventory" of Attack Vectors and Defense Vectors.

**Public URL.** www.culturekeeperscircle.org/tracker

**Current state (2026-04-23).**
- ~755 entries across 6 categories
- `data/data.json` (~58 MB single source of truth)
- `index.html` (6.2 MB self-contained public UI)
- GitHub Actions daily cron + manual pipeline runs

**Three purposes.**
1. **Research tool** — empirical foundation for the law review article's 5-Attack / 4-Defense dual inventory.
2. **Advocacy tool** — public-facing resource used by community members, advocates, policymakers.
3. **Monitoring system** — automated pipeline fetching from Federal Register, Congress.gov, CourtListener, NewsAPI.

---

## Scope (locked 2026-04-23)

**FEDERAL ACTIONS ONLY.** State, municipal, and campus-level actions are out of scope. Entries that slip through get muted (`muted: true`), never deleted. Federal cases with state parties stay federal.

**NAGPRA policy.** Code individually only federal-actor NAGPRA notices (DOI, NPS, Army Corps, BIA, Smithsonian). Aggregate state and university notices into one monthly "NAGPRA Roundup" PROTECTIVE entry.

Full scope rules: [CLAUDE.md § Scope Rules](CLAUDE.md#scope-rules-locked-2026-04-23).

---

## Entry Categories (6)

| Category | Count (approx.) |
|---|---|
| `executive_actions` | ~100 |
| `agency_actions` | ~255 |
| `legislation` | ~194 |
| `litigation` | ~127 |
| `other_domestic` | ~19 (post-mute) |
| `international` | ~60 |

---

## Entry Schema (compact keys)

| Field | Key | Purpose |
|---|---|---|
| ID | `i` | Unique identifier (per-category format) |
| Type | `t` | e.g., "Executive Order", "Final Rule" |
| Number | `n` | Official designation |
| Title | `T` | HTML with color span for threat level |
| Summary | `s` | 2–5 word slug |
| Date | `d` | `YYYY-MM-DD` |
| Administration | `a` | "Trump II", "Biden", etc. |
| Agencies | `A` | Array of abbreviations |
| Status | `S` | Current status description |
| Threat level | `L` | SEVERE / HARMFUL / PROTECTIVE / WATCH |
| Description | `D` | 500–1500 words HTML |
| Impact (PPPT) | `I` | Community-keyed 4-field analysis (people/places/practices/treasures) at 150–300 words each |
| Communities | `c` | Affected-community array |
| Source URL | `U` | Official government / court URL |
| Source tag | `_source` | Provenance tag |
| Muted | `muted` | `true` if hidden from public view |
| Muted reason | `_mutedReason` | Plain-English rationale |
| Muted date | `_mutedDate` | `YYYY-MM-DD` |
| Cross-ref | `_crossRef` | Array for merged-duplicate provenance |

---

## Processing Pipeline

```
Sources (4 APIs)
    ↓
Keyword filter (Federal Register) + Direct fetch (others)
    ↓
Claude Haiku relevance screening (confidence ≥ 0.6)
    ↓
Claude Sonnet full entry generation
    ↓
Deduplication (source-ID + entry-ID)
    ↓
Schema validation
    ↓
data.json + state.json
```

Detailed methodology: [docs/2026 04 23 - [METHODOLOGY] - Pipeline Queries and Research Questions Full Disclosure.md](docs/2026%2004%2023%20-%20%5BMETHODOLOGY%5D%20-%20Pipeline%20Queries%20and%20Research%20Questions%20Full%20Disclosure.md).

---

## Key Commands

```bash
# Run the full pipeline (fetch → screen → generate → dedup → save)
python3 -m pipeline

# Big catch-up run (raised cap)
MAX_ENTRIES_PER_RUN=200 python3 -m pipeline

# Dry run (no writes)
DRY_RUN=true python3 -m pipeline

# Single source
SOURCE_FILTER=federal_register python3 -m pipeline

# Push manually drafted entries
./scripts/update.sh --auto

# Data quality audit
python3 scripts/audit_toolkit.py --full
python3 scripts/audit_toolkit.py --summary

# Targeted enrichment
python3 scripts/enrich_entries.py --community indigenous --dry-run
python3 scripts/enrich_entries.py --community african-descendant --all
```

One-page cheat sheet: [docs/QUICKSTART.md](docs/QUICKSTART.md).

---

## Pipeline Caps

| Setting | Default | Override |
|---|---|---|
| `MAX_ENTRIES_PER_RUN` | 50 | Env var or `.env` |
| `SCREENING_TIME_BUDGET` | 1200s | Env var |
| `LOOKBACK_DAYS` | 0 (use state.json) | Env var |
| `DRY_RUN` | false | Env var |
| `SOURCE_FILTER` | all | Env var |

Raised from 15 to 50 on 2026-04-23. See `docs/archive/UPDATE_SUMMARY_2026_04_22.md`.

---

## Community Keys (canonical 27)

```
africanAmerican, indigenous, latine, asianAmerican, pacificIslander,
alaskaNative, nativeHawaiian, immigrant, lgbtq, women, disabled,
muslim, jewish, sikh, rural, urban, lowIncome, environmentalJustice,
academicCommunity, faithCommunities, arts, nonprofit, federalEmployees,
allCommunities
```

Some legacy entries also use display forms like "Indigenous/Tribal", "African-descendant", "Latiné". Both coexist.

---

## What Triggers This Skill

Any mention of: tracker, threat tracker, TCKC, tracker entries, tracker pipeline, adding entries, enrichment, impact analysis, PPPT or 4Ps, community impact, threat levels, SEVERE / HARMFUL / PROTECTIVE / WATCH, Congress.gov source, Federal Register source, CourtListener, NewsAPI, NAGPRA roundup, state-level mute, cap / MAX_ENTRIES_PER_RUN, historical backfill, BGHPN storymap state-level layer, Cultural Heritage Partners partnership, NPCA NCRC coalition, or any work on the law review article's empirical backbone.

---

## Relationship to Sibling Projects

- **Law Review Article** (*Redefining Culture*) — consumes Tracker data as empirical backbone.
- **Book — Against the Peoples Who Built the Nation** — uses Tracker scope for hegemonic-encounter documentation.
- **BGHPN Storymap Partnership** — consumes muted state-level entries as data layer over Black heritage sites (five-state pilot: FL, AL, MD, NY, MS, due 2026-05-28).
- **Cultural Heritage Partners partnership** — litigation firm that uses Tracker as case-identification pipeline; their *Fight Back* litigation targets Section 106 emergency-procedure bypasses that the Tracker codes.
- **NPCA National Cultural Resource Coalition (NCRC)** — CKC is a founding member; Tracker feeds NCRC coordination.

---

## Related Documents

- [CLAUDE.md](CLAUDE.md) — AI operating rules (scope, style, NAGPRA policy)
- [README.md](README.md) — Public-facing overview
- [docs/AUTOMATION.md](docs/AUTOMATION.md) — Full update-workflow guide
- [docs/QUICKSTART.md](docs/QUICKSTART.md) — One-page reference
- [docs/2026 04 23 - [METHODOLOGY] - Pipeline Queries and Research Questions Full Disclosure.md](docs/2026%2004%2023%20-%20%5BMETHODOLOGY%5D%20-%20Pipeline%20Queries%20and%20Research%20Questions%20Full%20Disclosure.md)
- [docs/2026 04 23 - [STRATEGY] - Historical Backfill and QA Plan Since Jan 19 2025.md](docs/2026%2004%2023%20-%20%5BSTRATEGY%5D%20-%20Historical%20Backfill%20and%20QA%20Plan%20Since%20Jan%2019%202025.md)
- [scripts/README.md](scripts/README.md) — Per-script usage

---

*Last updated 2026-04-23. Replaces the earlier SKILL.md that referenced stale entry counts (666) and 5 categories.*
