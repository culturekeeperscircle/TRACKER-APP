# Supabase internal dashboard setup

**Date:** 2026-05-06
**Author:** A. Prince Albert III, with Claude
**Status:** live

## What was built

The TCKC Threat Tracker now mirrors itself into Supabase Postgres at project `xsqdjhjcqbawghuaqqwj`. All 806 unique entries and the meta snapshot from `data/data.json` are queryable from Supabase Studio. Seven dashboard views give Prince and the board a SQL-driven internal dashboard without any frontend work and without changing the public tracker at `culturekeeperscircle.org/tracker`.

This is path A from the May 6 design conversation. Path B (re-back the public tracker) and path C (new analyst dashboard) remain open and can build on this foundation.

## How to access

1. Sign in to Supabase: https://supabase.com/dashboard/project/xsqdjhjcqbawghuaqqwj
2. Use the **Table Editor** to browse `entries` and `tracker_meta` directly.
3. Use the **SQL Editor** to run any of the queries below or write your own. Save useful queries as **Reports** so they show up in the left nav.

## The seven views

| View | Question it answers |
|---|---|
| `v_dashboard_snapshot` | Headline scoreboard. Total entries, severity counts, new in last 7 / 30 days, distinct agencies, latest action date. |
| `v_severity_by_category` | How does each of the six categories break down by SEVERE / HARMFUL / PROTECTIVE / WATCH. |
| `v_monthly_volume` | Monthly action volume by severity, the time-series for trend tracking. |
| `v_top_agencies` | Federal agencies ranked by entry count, with severity split. |
| `v_recent_severe` | Active watchlist. SEVERE entries from the last 60 days. |
| `v_admin_breakdown` | Administration × severity matrix. Trump II vs prior administrations. |
| `v_crossref_inventory` | Domestic entries that also surface in international scope. |

Every view uses `security_invoker = on`, so RLS applies to the role running the query.

## Current numbers (2026-05-06 load)

- 806 unique entries across six categories.
- 400 SEVERE, 238 HARMFUL, 159 PROTECTIVE, 9 WATCH.
- 23 new entries in the last 7 days, 138 in the last 30 days.
- 142 distinct agencies referenced across all entries.
- Top agencies by volume: DOI (191), DHS (120), DOJ (90), ED (71), EPA (64).
- Latest action date in the data: 2026-05-01.

## Security posture

Both tables (`entries`, `tracker_meta`) have RLS enabled with no policies. The anon and authenticated roles cannot read or write. Only the service role (Studio internal) has access. Two `INFO` advisor notices about "RLS Enabled No Policy" are expected and intentional for path A.

The bulk loader runs through a temporary anon policy (`tckc_load_temp_*`) that is opened immediately before the load and dropped immediately after. The policy never lives outside a load window.

The `update_updated_at` trigger function pins `search_path = ''` to satisfy the function-search-path advisor.

## Refresh cadence

`data.json` is rewritten daily by the existing pipeline (`pipeline/main.py` driven by `.github/workflows/`). The Supabase mirror does not auto-refresh yet. Re-run the loader manually after major updates, or wire it into the daily workflow as a follow-up. See `pipeline/supabase/README.md` for the open-policy / load / close-policy steps.

## Pinned reports

Open the SQL Editor in Studio and save each of these as a named report so they appear under **Reports** in the left nav.

```sql
-- Headline scoreboard
SELECT * FROM v_dashboard_snapshot;

-- Severity matrix
SELECT * FROM v_severity_by_category;

-- 12-month action volume
SELECT month, severity, n
FROM v_monthly_volume
WHERE month >= (current_date - INTERVAL '12 months')
ORDER BY month, severity;

-- Top 20 agencies
SELECT * FROM v_top_agencies LIMIT 20;

-- Active watchlist
SELECT id, action_date, official_name, agencies, status_text
FROM v_recent_severe
ORDER BY action_date DESC;

-- Full-text search example (substitute the search term)
SELECT id, action_date, official_name, severity
FROM entries
WHERE to_tsvector('english',
        coalesce(official_name,'') || ' ' ||
        coalesce(summary,'')       || ' ' ||
        coalesce(description_html,'')
      ) @@ plainto_tsquery('english', 'Smithsonian')
ORDER BY action_date DESC
LIMIT 25;
```

## What was built where

```
TCKC Threat Tracker/
├── pipeline/supabase/
│   ├── README.md       open-policy / load / close-policy workflow
│   ├── chunker.py      data.json → /tmp/tckc_chunks/
│   └── load.py         /tmp/tckc_chunks/ → PostgREST upserts
└── docs/
    └── 2026 05 06 - [INFRA] - Supabase Internal Dashboard Setup.md   (this file)
```

The migrations applied to the project (in order):

1. `tckc_tracker_init_schema` (enums, tables, indexes, triggers, RLS on)
2. `tckc_temp_anon_load_policies` (opened for first load)
3. `tckc_drop_temp_load_policies`
4. `tckc_temp_anon_load_policies_v2` (opened for description backfill)
5. `tckc_drop_temp_load_policies_v2`
6. `tckc_dashboard_views` (seven views)
7. `tckc_harden_views_and_function` (security_invoker on, search_path pinned)

## Next steps, in priority order

1. Decide whether to automate the loader inside the existing daily workflow.
2. Pin the six reports above in Studio so the dashboard renders the moment Prince logs in.
3. Pick path B or C when ready to extend beyond internal use. Both inherit this schema.
