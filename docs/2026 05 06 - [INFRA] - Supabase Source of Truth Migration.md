# Supabase as source of truth: path B migration

**Date:** 2026-05-06
**Status:** code shipped, awaiting GitHub Actions secret + first automated run

## Decision recap

Earlier today the tracker got a Supabase mirror (path A: read-only dashboard).
Then the working model shifted: Supabase becomes the source of truth, `data.json` becomes a generated artifact. This doc captures the full migration in one place.

## What changed in the codebase

```
pipeline/supabase/
├── __init__.py
├── client.py     credential resolution (service role preferred)
├── mapping.py    bidirectional JSON ↔ row mapping, single source of truth
├── load.py       full upsert of data.json into Supabase
├── sync.py       insert-only wrapper for the daily pipeline
├── export.py     Supabase → data.json, regenerates legacy shape
└── README.md     module reference

.github/workflows/daily-update.yml   <- new export → pipeline → sync → export steps
.env.example                          <- adds SUPABASE_PROJECT_REF, SUPABASE_SERVICE_ROLE_KEY
```

Schema additions in Supabase (migrations applied today):

```
tckc_extend_for_full_fidelity   adds I/c/U/_source/mute/aggregate/cross-ref columns
                                plus extras jsonb catch-all
```

The full table now mirrors every key seen in `data.json`. Round-trip diff against production data is clean: 834 entries in, 834 out, zero value mismatches.

## What you must do once

1. **Get the service role key.**
   Studio → Settings → API → copy the `service_role` key. Treat it like a database password.

2. **Add it as a GitHub Actions secret.**
   GitHub repo → Settings → Secrets and variables → Actions → New repository secret.
   Name: `SUPABASE_SERVICE_ROLE_KEY`
   Value: the service role key.

3. **(Optional) Mirror it locally for ad-hoc operations.**
   Add to `.env`:
   ```
   SUPABASE_PROJECT_REF=xsqdjhjcqbawghuaqqwj
   SUPABASE_SERVICE_ROLE_KEY=...
   ```

After step 2, the next time `Daily Tracker Update` runs (manually via `gh workflow run` or via the Actions UI), the new Supabase steps execute automatically.

## How a daily run now works

```
1. checkout repo
2. python -m pipeline.supabase.export    pull canonical Supabase state into data.json
3. python -m pipeline                     ingest pipeline runs against fresh data.json
4. python -m pipeline.supabase.sync       insert-only push to Supabase (preserves Studio edits)
5. python -m pipeline.supabase.export     re-export so data.json matches Supabase exactly
6. validate data.json
7. commit data/data.json data/state.json index.html
8. push
```

Manual edits made in Studio between runs survive step 4 because `sync` uses
`Prefer: resolution=ignore-duplicates`. Only entries with a brand-new `id` are
inserted.

## Operating model going forward

- **Add or correct entries**: edit in Studio Table Editor, or write SQL in the SQL Editor. The next workflow run propagates to data.json and git.
- **Bulk QA**: SQL Editor against `entries` and the dashboard views.
- **Cite a snapshot**: tag a release in git as before. The committed `data.json` is the snapshot. Zenodo and SWHID flows are unchanged.
- **Debug a discrepancy**: run `python -m pipeline.supabase.export --pretty --out /tmp/diff.json` and diff against `data/data.json`. Any drift means the Supabase state and the committed JSON disagree, which a fresh workflow run will reconcile.

## What was deliberately not changed

- `pipeline/main.py` and the source connectors. The pipeline still writes to `data.json`. The new architecture wraps the pipeline rather than refactoring it. This keeps the ingest logic stable while shifting the system of record.
- The static `index.html` dashboard. It still reads `data.json` over the wire. Whether to migrate the public dashboard onto Supabase (path B-public) is a separate decision and unblocked by today's work.

## Verifying after the first automated run

```sql
-- Headline numbers should match the Studio dashboard.
SELECT * FROM v_dashboard_snapshot;

-- Entry count should match data.json's meta.total in the latest commit.
SELECT count(*) FROM entries;

-- Cross-refs preserved as full rows.
SELECT count(*) FROM entries WHERE is_cross_ref = true;
```

If those three numbers track `data.json` after each commit, the round-trip is healthy.

## Rollback

If something goes wrong:

1. Revert the workflow to the prior commit. The pipeline reverts to writing only `data.json`.
2. Drop or ignore the new Supabase steps in `pipeline/supabase/`. They are additive; nothing in the legacy pipeline depends on them.
3. The Supabase database remains intact and queryable for QA. It just stops auto-updating.

## Open follow-ups (not blocking)

- Re-enable the daily cron in `daily-update.yml` once the first automated run succeeds.
- Consider an audit table (`entry_revisions`) to capture every UPDATE for accountability.
- Migrate the public-facing tracker (path B-public or path C) when the data layer is fully proven.
