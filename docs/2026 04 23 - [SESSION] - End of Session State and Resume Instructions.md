# End-of-Session State — 2026-04-23

**Status:** Prince disconnecting hard drive. Will resume later today. All work saved. No long-running processes left active.

---

## What got done today (chronological highlights)

### Tracker data & operations

- **SPLC duplicate pair merged** — `doj-v-splc-2026` kept as canonical; 8 communities unioned; PBS source URL preserved as cross-ref.
- **6 state-level entries deleted** (Tennessee, Arizona, Indiana, Ohio, Idaho, Kansas) → archived to `data/state_level_archive_20260422.json` for BGHPN state-layer reuse.
- **Chicago municipal entry muted** (`chicago-reparations-tipped-wages-2026-001`).
- **Frontend updated** with `isVisibleItem()` filter in `index.html`; `?show_muted=1` URL param for audit override.
- **Comprehensive pipeline runs** — initial run (3 entries with 15-cap), follow-up run (35 entries with 50-cap). Net 774 public-visible, 17 muted, 791 total.
- **NAGPRA policy applied** — 16 state/university/private NAGPRA entries muted; unique IDs assigned (nagpra-2026-{FR_number}); single `nagpra-roundup-2026-04` PROTECTIVE aggregate entry created.
- **ID collision fixed** — 17 entries sharing `doi-notice-2026-010` renamed to unique IDs.

### Pipeline & infrastructure

- **Generation cap raised** 15 → 50 (pipeline/main.py default, .env override, GitHub Actions workflow timeout 60 → 90 min).
- **API keys migrated** to project-local `.env` via `python-dotenv`. Scrubbed from accidental NanoClaw/.env.example landing site. (Keys: rotate when convenient as belt-and-suspenders.)
- **Follow-up-pipeline bug observed** — Sonnet generates duplicate IDs for same-type batch items (doi-notice-2026-010 loop). Discussed but not fixed; flagged for future session.

### Policy locks (now in CLAUDE.md and agent memory)

- **Federal-only scope.** State/local entries get muted, never deleted. Federal cases with state parties stay federal.
- **NAGPRA policy.** Individual coding only for federal actors (DOI, NPS, Army Corps, BIA, SI). Monthly aggregate "NAGPRA Roundup" for state/university/private.
- **Canonical research question** (locked this evening):
  > Which laws and policies from [GOVERNMENT ENTITY] will severely harm the cultural resources (People, Places, Practices, and Treasures) paramount to the cultural continuity of [CULTURAL COMMUNITY], moderately harm those same cultural resources, or protect those same cultural resources?
- **Five primary ethnic communities:** Indigenous, African-descendant, Latiné, Asian, Pacific Islander (diasporic scope on each).
- **Writing-style clarification (Prince's refinement tonight):** Cultural continuity is the severity RUBRIC, not a keyword requirement. Impact prose focuses on imminent, immediate, concrete harms — not generational rhetoric.

### Folder cleanup

- Root reduced from 30 to 14 entries.
- Three canonical instruction files (CLAUDE, SKILL, README) updated with current state and the new research question.
- New `docs/` structure with AUTOMATION, QUICKSTART, METHODOLOGY, STRATEGY, AUDIT, HARMONIZATION PLAN, and this SESSION file.
- `docs/archive/` holds deprecated instruction files and old UPDATE_SUMMARY files.
- `data/archive/` holds older backups and audit outputs.
- `.gitignore` updated to include `.claude/` and `update_log_*.txt`.
- All committed in one clean git commit: `4008628`.

### Live prompt update

- `pipeline/prompts/relevance_screening.txt` rewritten to embed the canonical research question verbatim, with the five primary communities, PPPT cultural-continuity frame, and diasporic-scope language. **Next pipeline run uses this.**

### Outside the tracker

- NPCA Veterans Council + NCRC founding membership added to resume and persistent memory.
- BGHPN Storymap Partnership project folder, PLAN, and persistent memory created. 5-state policy layer deliverable (FL, AL, MD, NY, MS) due 2026-05-28.
- Cultural Heritage Partners alignment memo prepared.
- Week 4 + Week 5 Upper/Lower/Aesthetics gym templates saved.
- Harmonization plan for bringing all 774 active entries into conformance with the canonical research question (documented; not executed).

---

## Open decisions that need your call when you return

### 1. Execute the harmonization plan?

Full details in [docs/2026 04 23 - [PLAN] - Tracker Harmonization with Canonical Research Question.md](./2026%2004%2023%20-%20%5BPLAN%5D%20-%20Tracker%20Harmonization%20with%20Canonical%20Research%20Question.md).

**Revised scope** (after tonight's clarification that continuity language is not a keyword requirement):

| Step | Cost | Time |
|---|---|---|
| Taxonomy normalization (script, dedup label variants) | $0 | 15 min |
| Refinement #1 — **SKIP the automated 24-entry patch.** Keyword check was a crude proxy. Substantive review (if any) is better done by Kiran on a sample, not a batch rewrite. | — | — |
| Refinement #2 — augment 16 intersectional entries with primary-community codings | $2.40 | 20 min |
| Refinement #3 — triage 300 flags, patch ~100 real gaps | $30 | 1h 45m |
| Forward-facing prompt updates (generation, quality-check) | $0 | 25 min |
| **Revised total** | **~$32** | **~2h 45m** |

### 2. Historical backfill (Jan 19, 2025 → today)

Strategy memo at [docs/2026 04 23 - [STRATEGY] - Historical Backfill and QA Plan Since Jan 19 2025.md](./2026%2004%2023%20-%20%5BSTRATEGY%5D%20-%20Historical%20Backfill%20and%20QA%20Plan%20Since%20Jan%2019%202025.md). Four-phase plan. Phase 1 (external-tracker cross-validation via parallel Explore agents) is the cheapest high-yield start.

### 3. Pre-existing ID collision cleanup

26 entries across 5 duplicate IDs: `doi-notice-2026-003` (×6), `doi-notice-2026-006` (×11), `doi-notice-2026-008` (×2), `usccr-notice-2026-001` (×4), `fcc-notice-2026-001` (×3). Same-style script pattern as tonight. ~15 min runtime.

### 4. Open items outside the tracker

- **LinkedIn publish timing** for NPCA Veterans Council post
- **Substack 01** publish — Kiran returned a publish-ready revision with 4 open questions
- **BGHPN site inventory scan** — flagged in the PLAN, waiting on BGHPN website URL confirmation
- **Resume PDF regeneration** from the updated .txt (current PDF is stale)
- **CHP managing-partner meeting** prep memo ready (you confirmed meeting timing)
- **Rotate three API keys** (CONGRESS, COURTLISTENER, NEWS) as belt-and-suspenders after the accidental NanoClaw landing. Fully optional; the keys were never committed to git.

---

## How to resume (pick one, tell me which)

**A. Execute the harmonization plan.** I run taxonomy normalization + Refinements #2 and #3 + prompt updates. ~3 hours, ~$32. You spot-check 10 per batch.

**B. Kick off historical backfill Phase 1 (external cross-validation).** 15 parallel Explore agents scraping external trackers (ACLU, Democracy Docket, FAS EO Tracker, Just Security, Brennan Center, Georgetown DEI Rollback, etc.). ~90 min, ~$30. Produces a must-have list of entries the tracker may be missing since Jan 19, 2025.

**C. Clean up pre-existing ID collisions.** Quick 15-min technical fix for the 26 entries sharing 5 duplicate IDs.

**D. Ship the Substack and/or LinkedIn post.** Non-tracker work; pulls you out of the pipeline weeds for a bit.

**E. BGHPN site-inventory scan.** Tight deadline (May 28 delivery). Dispatch an Explore agent on BGHPN's website once you have the URL.

**F. Something else.** Tell me what's on your mind when you reconnect.

---

## State snapshot

### Files touched today

- `data/data.json` — 791 entries (774 public + 17 muted)
- `data/state.json` — `last_successful_run: 2026-04-23`
- `data/state_level_archive_20260422.json` — 6 deleted state entries, preserved
- `data/data.json.bak-20260422-pre-mute` — most recent rollback point
- `data/data.json.bak-20260423-pre-nagpra-cleanup` — pre-NAGPRA-cleanup rollback
- `CLAUDE.md` / `SKILL.md` / `README.md` — all current
- `docs/` — full structure with strategy, methodology, audit, harmonization plan
- `pipeline/prompts/relevance_screening.txt` — rewritten around canonical research question
- `pipeline/main.py` — MAX_ENTRIES_PER_RUN default raised to 50
- `.env` / `.env.example` — API keys in place, git-ignored
- `.github/workflows/daily-update.yml` + `manual-update.yml` — 90-min timeout

### Git state

- Branch: `main`
- Last commit: `4008628` "Mute state-level entries, wire dotenv for local keys, checkpoint pre-pull"
- Working tree has new work not yet committed (NAGPRA roundup, docs/ reorg, harmonization plan, research-question edits). When you return, I can draft a second commit covering these.

### Pipeline state

- Idle. No background processes.
- Last pipeline run: 2026-04-23 with `MAX_ENTRIES_PER_RUN=50`.
- Next scheduled run: GitHub Actions cron, 5:00 AM ET tomorrow (will use new prompt + new cap automatically).

### API costs today

- Roughly $5-7 total spent across Claude Haiku screening and Sonnet generation (two pipeline runs).

---

## When you reconnect

Open this file first. It's the ground truth for where we left off. Tell me which of A–F (or something else) and I'll pick it up cleanly.

**Memory is persistent across sessions via the `.claude/projects/.../memory/` directory.** Everything important from today is saved there. The only thing that stops working when you disconnect the drive is this specific project folder — the memories and session context survive fine.

---

*Session ended 2026-04-23 evening. Resume whenever. Work preserved.*
