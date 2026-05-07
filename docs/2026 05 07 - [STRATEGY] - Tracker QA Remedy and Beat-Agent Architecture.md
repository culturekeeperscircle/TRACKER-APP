# Tracker QA Remedy and Beat-Agent Architecture

**Date:** 2026-05-07
**Status:** Canonical strategy doc. Supersedes prior partial framings.
**Author:** A. Prince Albert III
**Scope:** Diagnosis of the three gaps that limit the TCKC Cultural Resource Threat Tracker, and the four-piece architecture that closes them.

---

## What this supersedes

This is the single source of truth for the tracker's QA strategy and the beat-agent architecture going forward. The following earlier doc is now historical and has been moved to `docs/archive/`:

- `2026 05 06 - [INFRA] - Supabase Internal Dashboard Setup.md` (Path A, "internal-only mirror"; still technically accurate for views and Studio Reports, but the operating model has moved past it).

Still authoritative for their narrower implementation scope (read alongside this doc, not in place of it):

- `2026 05 06 - [INFRA] - Supabase Source of Truth Migration.md` — Path B implementation: how `data.json` round-trips through Supabase.
- `2026 05 07 - [INFRA] - Beat-Agents Phase 1 Scaffold.md` — the schema migration, tracker SDK, BeatAgent base class, runner CLI, quarantine reviewer, and Render blueprint that implement Architecture pieces 1-3 below.

---

## Diagnosis

### Coverage gap

Four sources catch the front page of federal action (Federal Register, Congress.gov, CourtListener, NewsAPI). They miss agency guidance documents, OIG reports, GAO reports, regs.gov dockets, agency newsroom releases, IG memos, dear-colleague letters, congressional testimony, state-AG actions, and most subagency-level moves. A lot of what affects cultural communities lives in those gaps.

### Granularity gap

The schema captures WHAT happened, WHEN, WHO, and IMPACT. It does not capture the legal substructure that makes deep policy research possible: statute and regulation citations, named programs affected, personnel involved, dollar amounts, procedural posture, direct quotes with page citations, the authority chain that an action invokes or cancels.

### Queryability gap

SQL handles aggregations, but end-users get no faceted UI, no saved views, no topic graph, no per-entry "related actions" panel. The data is queryable in theory; it's not queryable to a journalist or an LDF lawyer in practice.

The fix is to layer beat-agents and a richer schema on top of the existing pipeline, not replace it. The pipeline's job is breadth-first ingest. The agents' job is depth-first research and augmentation.

---

## Architecture

Four pieces.

### 1. Schema extension for granular legal detail

Add structured columns for the substructure that makes legal and policy research possible. Existing rows stay valid. Agents fill in the new fields incrementally.

```sql
ALTER TABLE entries
  ADD COLUMN legal_authorities       jsonb,    -- [{citation, type, role}]
  ADD COLUMN affected_programs       text[],   -- ["Title VI compliance", "Section 106"]
  ADD COLUMN personnel               jsonb,    -- [{name, title, role}]
  ADD COLUMN dollar_impacts          jsonb,    -- [{amount, period, description}]
  ADD COLUMN procedural_status       text,     -- "comment period open through ..."
  ADD COLUMN cited_quotes            jsonb,    -- [{text, source_url, page}]
  ADD COLUMN source_documents        jsonb,    -- [{url, title, type, sha256}]
  ADD COLUMN related_entry_ids       text[],   -- explicit graph edges
  ADD COLUMN research_depth          text      -- 'shallow' | 'deep' | 'expert'
    CHECK (research_depth IN ('shallow','deep','expert')) DEFAULT 'shallow',
  ADD COLUMN last_deep_researched_at timestamptz,
  ADD COLUMN deep_research_notes     text;     -- agent's working notes
```

Now `research_depth` becomes the dial. The current 834 entries are `shallow`. Agents promote them to `deep` as they augment. Humans (you, an LOR student, an LDF associate) promote to `expert` after review.

### 2. A Python tracker SDK

A small library that wraps Supabase reads and writes so agents have one stable surface to call. Three operations cover 90% of needs:

```python
from tracker import client

t = client()
hits = t.search(agency="DOI", since="2025-01-20", min_severity="HARMFUL")
t.augment(entry_id="eo-14154", legal_authorities=[...], cited_quotes=[...])
t.add_entry({...})  # for actions the pipeline missed
```

Builds on the same service-role-key plumbing already shipped in `pipeline/supabase/client.py`.

### 3. Beat-agents

Define ~20 beats, each owning a slice of the federal landscape. Each beat-agent is a Claude Agent SDK process with a beat-specific system prompt, the tracker SDK, web access for primary sources, and a target output (augmented entries plus gap reports).

A pragmatic beat split:

| Cluster | Beats |
|---|---|
| Land and tribal | DOI/BIA/BLM/NPS, USDA-Forest, ACHP |
| Civil rights | DOJ/Civil Rights Division, ED/OCR, EEOC, HHS/OCR |
| Immigration | DHS/ICE/CBP/USCIS, DOJ/EOIR, DOS visa |
| Cultural institutions | Smithsonian, NEA/NEH, IMLS, Kennedy Center, CPB, LOC |
| Environment | EPA, NOAA, CEQ, Energy |
| Health | HHS/CDC/NIH/IHS, FDA |
| Education | ED, NSF |
| Foreign | DOS, DOD, USAID |
| Cross-cutting | DOGE/personnel, OMB, GSA |
| Litigation | Federal courts, SCOTUS, AG |

Each beat-agent runs on a cycle (recommend weekly, one beat per day across the week) and does four jobs:

1. **Discover.** Pull RSS, Federal Register, agency newsroom, OIG, regs.gov dockets for the beat's date window.
2. **Reconcile.** Diff against existing tracker entries. Flag actions covered in the press but not yet in the tracker.
3. **Augment.** For existing entries, fill in `legal_authorities`, `affected_programs`, `personnel`, `cited_quotes`, `source_documents`. Bump `research_depth` to `deep`.
4. **Report.** Write a `gap_report` row covering "what's new this week, what's still missing, what needs human review."

### 4. Faceted queryability for end-users

This belongs in the chat-first landing page discussed previously. The chat is the primary surface; faceted browse is the secondary. Two additions:

- **Saved views** as a Supabase table: `(slug, name, description, sql_template, default_params)`. The chat backend translates "show me everything affecting Smithsonian" into a saved view. The browse UI surfaces views as named filters.
- **Topic taxonomy.** A two-axis tag system. One axis is communities (the existing five). One axis is institutional domain (cultural institutions, land, civil rights, etc.). Agents tag; humans review. Users browse by intersection.

---

## Build order

1. **Schema extension and the tracker SDK** (2 days). Apply the migration. Build `tracker.search/augment/add_entry`. Write unit tests against a few real entries.
2. **Pilot one beat-agent end to end** (3-5 days). Pick the noisiest beat (DOI or Smithsonian). Build the agent. Have it process one week of action. Measure: how many existing entries got augmented to `deep`, how many gaps did it find, how good were the augmentations on a 10-entry spot check.
3. **Iterate the agent prompt and the SDK** based on the pilot. The first pass will surface tooling friction.
4. **Roll out to all 20 beats** (2 weeks). Weekly cron schedule. One agent per beat per cycle.
5. **Source expansion** (concurrent). Wire up regs.gov, OIG/GAO RSS, agency newsrooms. Beat-agents inherit the wider source pool.
6. **Saved views + topic taxonomy + faceted browse** (1-2 weeks). Lands in the new chat-first landing page when it's built.

---

## Implementation status (2026-05-07)

| Build-order step | Status |
|---|---|
| 1. Schema extension | DONE. Migration `tckc_beat_agents_phase1` applied. |
| 1. Tracker SDK | DONE. Lives at `pipeline/tracker/sdk.py`. |
| 2. Pilot beat-agent | SCAFFOLDED. `pipeline/tracker/agents/doi.py` runs end to end with stubbed discover/reconcile and a placeholder augment. Real research logic is the next focused pass. |
| 3. Iterate | PENDING (after first real pilot run). |
| 4. Roll out 20 beats | PENDING. Each beat needs its own subclass + Render cron slot. |
| 5. Source expansion | PENDING. |
| 6. Faceted queryability | PENDING. Requires the chat landing page. |

For the implementation specifics (file map, deployment, quarantine workflow, cost discipline, rollback procedure), see the companion doc:

`docs/2026 05 07 - [INFRA] - Beat-Agents Phase 1 Scaffold.md`.
