# TCKC Tracker Automation Guide

One canonical guide for every way the tracker gets updated. Replaces the prior three files (`AUTOMATION_GUIDE.md`, `SYSTEM_SUMMARY.md`, `VS_CODE_BUTTON_GUIDE.md`) archived in `docs/archive/`.

---

## The Two Update Paths

The tracker has two distinct update workflows. Use the one that matches your situation.

### Path A. Automated Pipeline (daily, AI-driven)

The pipeline fetches from four APIs, screens with Claude, generates entries, and writes them to `data/data.json`.

```bash
cd "Culture Keepers Circle/TCKC Threat Tracker"
python3 -m pipeline
```

**Runs on:**
- **GitHub Actions cron** (daily, 5:00 AM ET Mon–Fri, 90-min timeout).
- **Your laptop** for one-off catch-up runs.

**Options:**
```bash
python3 -m pipeline                          # Default: since last_successful_run, NO CAP
MAX_ENTRIES_PER_RUN=50 python3 -m pipeline   # Opt back into a cap (testing only)
LOOKBACK_DAYS=30 python3 -m pipeline         # Force a 30-day window
DRY_RUN=true python3 -m pipeline             # Preview without writing
SOURCE_FILTER=federal_register python3 -m pipeline  # Single source
```

**What it uses:**
- API keys from `.env` (local) or GitHub Secrets (Actions)
- Claude Haiku 4.5 for screening and validation
- Claude Sonnet 4.6 for entry generation
- 4 source connectors (Federal Register, Congress.gov, CourtListener, NewsAPI)

Full methodology documented in [`docs/2026 04 23 - [METHODOLOGY] - Pipeline Queries and Research Questions Full Disclosure.md`](./2026%2004%2023%20-%20%5BMETHODOLOGY%5D%20-%20Pipeline%20Queries%20and%20Research%20Questions%20Full%20Disclosure.md).

### Path B. Manual JSON + Comprehensive Update (ad-hoc, human-drafted)

When Prince or a staffer drafts entries by hand (JSON file in project root), use `scripts/comprehensive_update.py` to integrate, commit, and push.

```bash
# 1. Drop entries into a file like NEW_ENTRIES_APRIL_2026.json
# 2. Run:
./scripts/update.sh --auto
```

**Modes:**

| Flag | Behavior |
|---|---|
| `--auto` | Fully automated: sync → merge → commit → push → verify. ~30 seconds. |
| `(no flag)` | Interactive: prompts for confirmation at each step. |
| `--dry-run` | Preview without committing anything. |

**What it does:**

1. Fetches latest from GitHub (rebase on conflict).
2. Validates the new JSON file against schema.
3. Merges entries into `data/data.json` (skipping duplicates).
4. Updates `data/state.json` meta counts.
5. Commits with auto-generated message.
6. Pushes to `main`.
7. Verifies GitHub Pages deployment.

**Blocks on:** uncommitted changes in repo (safety rail). Commit or stash first.

---

## VS Code Button Shortcut (Path B)

If you prefer clicking to typing, Path B is available as VS Code tasks:

1. `Cmd+Shift+P` → `Tasks: Run Task`
2. Pick one:
   - **TCKC: Comprehensive Update (Interactive)**
   - **TCKC: Comprehensive Update (Auto)** ← most common
   - **TCKC: Update Preview (Dry-Run)**

**Or bind a keyboard shortcut:**

`Cmd+Shift+P` → `Preferences: Open Keyboard Shortcuts (JSON)` → add:

```json
{
  "key": "cmd+shift+u",
  "command": "workbench.action.tasks.runTask",
  "args": "TCKC: Comprehensive Update (Auto)"
}
```

Now `Cmd+Shift+U` launches the update.

---

## Environment Setup (One-Time)

### API keys

Create `.env` in the tracker root (git-ignored; template in `.env.example`):

```
ANTHROPIC_API_KEY=sk-ant-...
CONGRESS_API_KEY=...
COURTLISTENER_TOKEN=...
NEWS_API_KEY=...
# Source expansion 2026-05-07: register one key at https://api.data.gov/signup
# and use it for both regulations.gov v4 and govinfo.gov.
REGULATIONS_GOV_API_KEY=...
GOVINFO_API_KEY=...
# MAX_ENTRIES_PER_RUN is unset by default (no cap). Set a positive integer
# only for testing or to throttle a specific run.
```

Get keys from:
- Anthropic: console.anthropic.com
- Congress: api.congress.gov/sign-up/
- CourtListener: courtlistener.com/profile/api/
- NewsAPI: newsapi.org/register

### Python dependencies

```bash
pip install -r requirements.txt
```

Current deps: `anthropic`, `requests`, `python-dotenv`.

### Git authentication

If pushing manually:
- macOS Keychain: `git config --global credential.helper osxkeychain`
- SSH: add your key to `~/.ssh/` and clone via SSH URL

---

## State and Deduplication

`data/state.json` tracks:

- `last_successful_run` — drives fetch-window for next run
- `sources.*.last_fetched_date` — per-source cursors
- `processed_ids.*` — up to 1,000 most-recent source IDs per source (for dedup)
- `cumulative_stats` — lifetime run count and entries added

**To force a backfill** (e.g., re-fetch after a cap change):

```python
# Back up state first
cp data/state.json data/state.json.bak

# Edit state.json:
#   "last_successful_run": "2025-01-19"   # Or whatever start date
#   "sources.*.last_fetched_date": "2025-01-19"
#   "processed_ids.*": []                  # Clear to force re-process
```

Deduplication happens at TWO layers:

1. **Source-ID dedup** (in `state.json`) — prevents re-processing the same raw API item.
2. **Entry-ID dedup** (in `data.json`) — prevents adding the same tracker entry twice.

Both fire on every pipeline run.

---

## Pipeline Caps and Timeouts

| Setting | Default | Where | Purpose |
|---|---|---|---|
| `MAX_ENTRIES_PER_RUN` | **none (unlimited)** | `pipeline/main.py:161`; override via env var | Optional opt-in cap; positive int enforces, ≤0 or unset means no cap |
| `SCREENING_TIME_BUDGET` | **20 min (1200s)** | `pipeline/main.py`; override via env var | Max time spent in Claude Haiku screening |
| Actions workflow timeout (daily, manual) | **350 min** | `.github/workflows/daily-update.yml`, `manual-update.yml` | Hard kill if pipeline hangs; matches GitHub's 360-min job ceiling |
| Actions workflow timeout (deep-sweep) | **300 min** | `.github/workflows/deep-sweep.yml` | For big catch-up runs |
| Rate limiter | 5 req/sec | `pipeline/utils/rate_limiter.py` | Protects all API calls |

**History:** The cap was 15 from 2026-02-27 to 2026-04-23, raised to 50 on 2026-04-23 after a 50-item test run exposed silent drops, then **removed entirely on 2026-05-07** at Prince's directive after the 50-cap continued to drop legitimate high-impact entries on heavy news days. Workflow timeouts raised the same day from 90 to 350 minutes to accommodate unlimited runs.

---

## Deployment

The tracker deploys automatically via GitHub Pages on every commit to `main`:

- **Repo:** `github.com/culturekeeperscircle/TRACKER-APP`
- **Live URL:** `www.culturekeeperscircle.org/tracker`
- **Build:** GitHub Pages serves `index.html` + `data/data.json` directly (no build step)

---

## Scripts Reference

Located in `scripts/`:

| Script | Purpose |
|---|---|
| `comprehensive_update.py` | Core automation engine for Path B (JSON merge → git commit → push). |
| `update.sh` | Shell wrapper for `comprehensive_update.py`. |
| `enrich_entries.py` | Run targeted enrichment on existing entries (`--community indigenous\|african-descendant\|targeted-gaps\|fix-impacts\|all`). |
| `audit_toolkit.py` | Quality audit (`--word-counts\|--structure\|--full\|--summary`, with `--period`/`--since` date filters). |
| `add_legislation_batch.py` | Bulk-add legislation entries from a CSV or JSON. |
| `validate_forms.py` | Validate a single entry's schema compliance. |
| `clean_boilerplate.py` | Remove boilerplate text from descriptions. |
| `remediate_subfederal.py` | Flag and mute state/local entries that slipped through. |

---

## Troubleshooting

### Pipeline aborts with "Repository has uncommitted changes"

You have dirty local state. Either:
- `git status` → decide what to commit/stash
- `git stash -u` to tuck everything away temporarily

### Pipeline runs but adds 0 entries

Three possibilities:
1. All fetched items were in `processed_ids` (expected on a fresh same-day re-run).
2. The keyword filter / Haiku screening filtered everything (check log for `AI-relevant items:` count).
3. The generation cap was hit and items got sorted-by-threat but dropped (look for `Capping entry generation at N items (had M)`).

### Pipeline times out in GitHub Actions

Check Actions logs. Likely causes:
- Workflow timeout too low (currently 90 min; bump if needed)
- Anthropic API rate-limiting (rare)
- Source API outage (Federal Register / Congress / CourtListener / News)

### Entry generation fails with "schema errors"

Claude generated an entry that didn't match the schema. The pipeline will attempt AI repair; if that fails too, the entry is skipped and logged.

### `python-dotenv` not found

```bash
pip install -r requirements.txt
```

---

## Related Documents

- **[CLAUDE.md](../CLAUDE.md)** — AI operating instructions (scope rules, style rules, NAGPRA policy)
- **[SKILL.md](../SKILL.md)** — Agent-trigger skill file
- **[README.md](../README.md)** — Public-facing overview
- **[docs/QUICKSTART.md](./QUICKSTART.md)** — One-page cheat sheet
- **[docs/2026 04 23 - [METHODOLOGY] - Pipeline Queries and Research Questions Full Disclosure.md](./2026%2004%2023%20-%20%5BMETHODOLOGY%5D%20-%20Pipeline%20Queries%20and%20Research%20Questions%20Full%20Disclosure.md)** — All queries, prompts, and research questions
- **[docs/2026 04 23 - [STRATEGY] - Historical Backfill and QA Plan Since Jan 19 2025.md](./2026%2004%2023%20-%20%5BSTRATEGY%5D%20-%20Historical%20Backfill%20and%20QA%20Plan%20Since%20Jan%2019%202025.md)** — Gap analysis and backfill plan

---

*Consolidated 2026-04-23 from AUTOMATION_GUIDE.md + SYSTEM_SUMMARY.md + VS_CODE_BUTTON_GUIDE.md. Originals archived in `docs/archive/`.*
