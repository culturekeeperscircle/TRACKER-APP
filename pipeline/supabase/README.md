# Supabase integration (path B: Supabase is the source of truth)

Project: `xsqdjhjcqbawghuaqqwj`
Studio: https://supabase.com/dashboard/project/xsqdjhjcqbawghuaqqwj
REST endpoint: https://xsqdjhjcqbawghuaqqwj.supabase.co/rest/v1

This package implements the operating model decided on 2026-05-06:

- Supabase Postgres holds the canonical TCKC tracker dataset.
- `data/data.json` is a generated artifact, regenerated from Supabase each pipeline run, committed to git for citation, archival, and the static `index.html` dashboard.
- Manual edits made in Supabase Studio are preserved across pipeline runs because the daily workflow uses insert-only sync.

## Modules

| File | Role |
|---|---|
| `client.py` | Resolves Supabase URL and credentials from env. Service role preferred. |
| `mapping.py` | Bidirectional translation between data.json entry shape and Postgres rows. Single source of truth for field mappings. |
| `load.py` | Full upsert of `data/data.json` into Supabase. Supports `--insert-only`. |
| `sync.py` | Insert-only wrapper around `load.py`. Used in the daily workflow to push only new entries. |
| `export.py` | Pulls all rows + meta from Supabase, regenerates `data/data.json` in legacy shape. |

## Daily flow (automated in `.github/workflows/daily-update.yml`)

```
git pull
python -m pipeline.supabase.export    # 1. pull current Supabase state into data.json
python -m pipeline                     # 2. ingest pipeline appends new entries to data.json
python -m pipeline.supabase.sync       # 3. push only new entries to Supabase (preserves manual edits)
python -m pipeline.supabase.export     # 4. re-export to lock data.json to canonical Supabase state
git add data/ index.html && git commit && git push
```

The export-before-pipeline step is critical. It catches any manual edits made in Studio between runs and brings them into the local data.json the pipeline operates on. Without it, the pipeline would happily overwrite manual edits during step 2.

## Credentials

The workflow uses the **service role key** (Studio → Settings → API → `service_role`). Service role bypasses RLS, which is what automation needs. Add it to GitHub repository secrets as `SUPABASE_SERVICE_ROLE_KEY` exactly once.

For local runs, set the same value in `.env` (already in `.gitignore`):

```
SUPABASE_PROJECT_REF=xsqdjhjcqbawghuaqqwj
SUPABASE_SERVICE_ROLE_KEY=...
```

The anon key is supported as a fallback for one-off local loads but only works when a permissive policy is open. The default RLS posture (RLS on, no policies) blocks anon entirely.

## Schema

Two tables, both with RLS enabled and no policies. Service role bypasses; anon and authenticated have no access.

```
public.entries        full-fidelity entry rows, including cross-refs
public.tracker_meta   singleton meta snapshot
```

Plus seven `security_invoker = on` views: `v_dashboard_snapshot`, `v_severity_by_category`, `v_monthly_volume`, `v_top_agencies`, `v_recent_severe`, `v_admin_breakdown`, `v_crossref_inventory`.

The entries table mirrors every key found in `data.json`:

| JSON key | Postgres column |
|---|---|
| `i` or `id` | `id` (PK) plus `id_field_name` to remember which key the original used |
| `t` | `entry_type` |
| `n` | `official_name` |
| `T` | `title_html` |
| `s` | `summary` |
| `d` | `action_date` |
| `a` | `administration` |
| `A` | `agencies` (text[]) |
| `S` | `status_text` |
| `L` | `severity` (enum) |
| `D` | `description_html` |
| `I` | `community_impacts` (jsonb) |
| `c` | `communities` (text[]) |
| `U` | `source_url` |
| `_source` | `source_tag` |
| `_isRef`, `_primaryRef` | `is_cross_ref`, `primary_ref_id` |
| `_relatedActions`, `_derivedFrom` | `related_action_ids`, `derived_from_ids` |
| `keyQuotes`, `agencyMandates`, `impactByCommunity` | `key_quotes`, `agency_mandates`, `impact_by_community` (jsonb) |
| `_crossRef` | `cross_ref_payload` (jsonb) |
| `muted`, `_mutedReason`, `_mutedDate` | `is_muted`, `mute_reason`, `mute_date` |
| `_isAggregate` | `is_aggregate` |
| anything not modeled above | `extras` (jsonb) catch-all |

Round-trip fidelity has been validated against the production data.json. 0 entries lost, 0 value mismatches across all 834 rows. The only diffs are empty-array fields (`"A": []`, `"_derivedFrom": []`) that the original carried explicitly and the export omits. The static `index.html` dashboard treats absence and empty array identically.

## Editing in Studio

Use **Table Editor** for inline single-cell edits. Use the **SQL Editor** for bulk changes. The next daily run will pull the edits into data.json automatically.

Caveats:

- The pipeline does not currently read existing entries before generating new ones. If you delete an entry in Studio, the pipeline may re-detect it from the same federal source and re-insert it. This is a known edge case. Mark suspicious entries `is_muted = true` rather than deleting if you want them suppressed but remembered.
- Editing `id` is destructive. The id is the primary key and the linchpin for cross-references and `_relatedActions`. Don't.

## QA via SQL

The seven views give you canned analytics. For ad-hoc QA, hit `entries` directly. Examples in `docs/2026 05 06 - [INFRA] - Supabase Internal Dashboard Setup.md` and the follow-up handover doc.
