# Beat-agents Phase 1 scaffold

**Date:** 2026-05-07
**Status:** scaffold shipped, pilot agent stubbed, Render not yet deployed

## Decisions locked

| Decision | Choice |
|---|---|
| Beat granularity | 20 beats by agency cluster, plus a second pass of cross-cutting agents that read the augmented data. |
| Verification posture | All agent edits land in `pending_edits` for the first month. After that, low-risk fields auto-approve, severity / new-entry / category changes stay quarantined. |
| Cost ceiling | 50 augmentations per beat per week. Enforced by `MAX_AUGMENTATIONS_PER_RUN` in `pipeline/tracker/agents/base.py`. |
| Hosting | Render cron jobs, one per beat, rotating across the week. |

## What was built

```
pipeline/tracker/
├── __init__.py             public SDK surface
├── sdk.py                  Tracker: search, propose_augment, propose_new_entry, approve, reject, record_gap_report
├── runner.py               CLI entry point: python -m pipeline.tracker.runner --beat doi
├── approve.py              quarantine reviewer CLI
└── agents/
    ├── __init__.py         REGISTRY dict mapping beat name → agent class
    ├── base.py             BeatAgent base class + BeatRunResult dataclass
    └── doi.py              pilot DOI cluster agent (stubbed augment for now)

render.yaml                 Render Blueprint with one cron job for the DOI beat
```

Migrations applied to the Supabase project:

```
tckc_beat_agents_phase1
  ALTER entries: legal_authorities, affected_programs, personnel, dollar_impacts,
                 procedural_status, cited_quotes, source_documents, explicit_related_ids,
                 research_depth, last_deep_researched_at, deep_research_notes
  CREATE TABLE pending_edits      quarantine queue
  CREATE TABLE gap_reports        per-run reports
  CREATE VIEW v_research_depth_progress
  CREATE VIEW v_pending_review_queue
```

## How it works end to end

```
Render cron fires (Monday 03:00 ET for DOI)
  → python -m pipeline.tracker.runner --beat doi
  → DOIBeatAgent.run(window_start, window_end)
      ├── discover()  pulls source candidates  (Phase 1: stub returning [])
      ├── reconcile() finds gaps               (Phase 1: stub)
      ├── augment()   proposes edits to `pending_edits` via Tracker.propose_augment
      └── record_gap_report()  writes one row to `gap_reports`

You review the queue:
  python -m pipeline.tracker.approve list --beat land-tribal
  python -m pipeline.tracker.approve approve 42 --by prince
  # or, after the first month, for trusted low-risk edits:
  python -m pipeline.tracker.approve bulk-approve --agent doi-beat-v1 --risk low --by auto-approver
```

## What is real and what is stubbed

**Real:**
- Schema, indexes, views in Supabase.
- Tracker SDK with proposal-only writes (proven path through `pending_edits`).
- Quarantine reviewer CLI with list / approve / reject / bulk-approve.
- Runner CLI that constructs and runs an agent for a given window.
- Render blueprint with the DOI cron slot wired.
- Risk auto-classification (low / medium / high) based on which fields the proposal touches.

**Stubbed (Phase 2 work):**
- `BeatAgent.discover()` returns `[]`. Real source connectors (Federal Register, regs.gov, OIG/GAO RSS, agency newsrooms) still need to be wired.
- `BeatAgent.reconcile()` returns `[]`. Gap detection logic still needs to be written.
- `BeatAgent.augment()` only flags shallow entries with a placeholder note. The real research call (Claude reads entry + source document, proposes structured fills) is the central Phase 2 task.

The scaffold proves the path. The next pass replaces the stubs with real research logic for the DOI beat, validates against ten entries by hand, then templates that pattern across the remaining 19 beats.

## What you must do once

1. **Set Render secrets.** From the Render dashboard for the new Blueprint:
   - `ANTHROPIC_API_KEY` (your existing one)
   - `SUPABASE_SERVICE_ROLE_KEY` (Studio → Settings → API → service_role)
   - `SUPABASE_PROJECT_REF` (already defaulted to `xsqdjhjcqbawghuaqqwj`)
   - `TCKC_AGENT_CAP` (defaulted to 50)
2. **Trigger a test run** from Render's UI ("Run now" on `tckc-beat-doi`).
3. **Review the quarantine queue:**
   ```
   python -m pipeline.tracker.approve list --beat land-tribal
   ```
   You should see ~50 placeholder proposals that just flag entries for deep research. Approve a couple, reject a couple, or `bulk-approve --risk low` the lot to confirm the workflow.
4. Once the workflow is exercised end-to-end, return to this doc and start Phase 2: real source connectors and a real `augment()` method for `DOIBeatAgent`.

## The 20 beats (planned)

Beats are agency clusters. Each gets its own subclass of `BeatAgent` and one cron slot in `render.yaml`.

| Cluster | Beat name | Agencies |
|---|---|---|
| Land and tribal | `land-tribal` (DONE) | DOI, BIA, BLM, NPS, ACHP, FWS, USDA-Forest |
| Civil rights | `civil-rights` | DOJ-CRD, ED-OCR, EEOC, HHS-OCR |
| Immigration | `immigration` | DHS, ICE, CBP, USCIS, DOJ-EOIR, DOS-visa |
| Cultural institutions | `cultural-institutions` | Smithsonian, NEA, NEH, IMLS, Kennedy Center, CPB, LOC |
| Environment | `environment` | EPA, NOAA, CEQ, DOE |
| Health | `health` | HHS, CDC, NIH, IHS, FDA |
| Education | `education` | ED, NSF |
| Foreign | `foreign` | DOS, DOD, USAID |
| Cross-cutting | `personnel-deregulation` | DOGE, OMB, GSA |
| Litigation | `courts` | Federal courts, SCOTUS, AG |
| ... | ... (10 more, finer agency splits as needed) | ... |

Add a beat by:
1. Subclassing `BeatAgent` in `pipeline/tracker/agents/<beat>.py`.
2. Registering it in `pipeline/tracker/agents/__init__.py`.
3. Adding a cron block in `render.yaml`.

## Cost discipline

- Cap of 50 proposals per beat per run is enforced in `BeatAgent.augment()`. Subclasses must respect `self.cap`.
- Each proposal uses ~5-15K tokens of Claude Sonnet input plus ~2-5K output. At Sonnet 4.6 rates that's ~$0.05-$0.15 per proposal. 50 × 20 beats × weekly = roughly $50-150 / week.
- Track actual spend in `gap_reports.cost_usd` so the reviewer view tells you when a beat is running hot.

## Verification posture transitions

- **Month 1 (2026-05-07 → 2026-06-07).** Every proposal stays in quarantine until you (or a delegate) approve it.
- **Month 2 onward.** Run a daily cron that calls:
  ```
  python -m pipeline.tracker.approve bulk-approve --risk low --by auto-approver
  ```
  Low-risk edits (statutes, programs, personnel, quotes, documents, deep_research_notes) auto-approve. Medium- and high-risk stay in quarantine.
- **High-risk forever.** Severity changes, category changes, title rewrites, mute toggles, and brand-new entries always require a human approver.

## Rollback

If a beat goes sideways:

```sql
-- Mark all of an agent's pending edits superseded
UPDATE pending_edits
SET status = 'superseded',
    resolved_at = now(),
    resolved_by = 'rollback',
    resolved_note = 'agent paused for review'
WHERE agent_id = 'doi-beat-v1' AND status = 'pending';

-- Disable the cron in Render UI for the beat.
```

Approved edits already in `entries` would need targeted `UPDATE` statements to revert, since we don't have a versioning table yet. Phase 3 follow-up adds an `entry_revisions` audit log.

## Related docs

- **Parent strategy:** `docs/2026 05 07 - [STRATEGY] - Tracker QA Remedy and Beat-Agent Architecture.md`. Read that first for the diagnosis (coverage / granularity / queryability gaps) and the four-piece architecture this scaffold implements.
- `docs/2026 05 06 - [INFRA] - Supabase Source of Truth Migration.md` — path B (Supabase round-trip) implementation.
- `pipeline/supabase/README.md` — load/export/sync workflow.
- `docs/archive/2026 05 06 - [INFRA] - Supabase Internal Dashboard Setup [SUPERSEDED].md` — early Path A framing, retained for history.
