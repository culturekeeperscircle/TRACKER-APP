# TCKC Tracker - Automated Comprehensive Update Guide

## Quick Start

### Option 1: Shell Script (Easiest)
```bash
cd "Culture Keepers Circle/TRACKER APP"
./scripts/update.sh              # Interactive mode
./scripts/update.sh --auto       # Fully automated
./scripts/update.sh --dry-run    # Preview only
```

### Option 2: Python Script (Direct)
```bash
python3 scripts/comprehensive_update.py              # Interactive
python3 scripts/comprehensive_update.py --auto       # Automated
python3 scripts/comprehensive_update.py --dry-run    # Preview
```

### Option 3: VS Code Task
Pre-configured in `.vscode/tasks.json` — use Terminal > Run Task menu

---

## What The Script Does

**Complete Workflow in One Command:**

1. ✅ **Git Sync** - Fetches latest from GitHub
2. ✅ **Validation** - Checks repository status
3. ✅ **Entry Integration** - Loads NEW_ENTRIES_APRIL_2026.json and merges into data.json
4. ✅ **Metadata Update** - Updates data/state.json with timestamps and counts
5. ✅ **Commit** - Creates git commit with entry count in message
6. ✅ **Push** - Pushes to origin/main with automatic rebase if needed
7. ✅ **Verification** - Confirms publication to GitHub

---

## Usage Modes

### Interactive Mode (Default)
```bash
./scripts/update.sh
```
- Prompts before each major step
- Confirms git status issues
- Safe for manual review

### Automated Mode
```bash
./scripts/update.sh --auto
```
- No prompts
- Skips confirmations (requires clean repo)
- Ideal for CI/CD integration

### Dry-Run Mode
```bash
./scripts/update.sh --dry-run
```
- Performs all steps EXCEPT commit/push
- Shows what would happen
- Safe to test before full run

---

## Workflow for Creating New Entries

### Step 1: Create NEW_ENTRIES_APRIL_2026.json
File should be in root of TRACKER APP directory with this structure:

```json
{
  "executive_actions": [
    {
      "i": "eo-unique-id-2026",
      "t": "Executive Order",
      "n": "Short name",
      "T": "<span style=\"color: #991B1B;\">Full title</span>",
      "s": "One-line summary",
      "d": "2026-04-02",
      "a": "Trump II",
      "A": ["OMB", "DOJ"],
      "S": "Status",
      "L": "SEVERE",
      "D": "<b>Full description</b>...",
      "c": ["africanAmerican", "indigenous", ...],
      "U": "https://source-url.gov",
      "_source": "federal_register",
      "I": {
        "africanAmerican": {
          "people": "...",
          "places": "...",
          "practices": "...",
          "treasures": "..."
        }
      }
    }
  ],
  "legislation": [...],
  "litigation": [...],
  "agency_actions": [...],
  "international": [...]
}
```

### Step 2: Run the Update Script
```bash
./scripts/update.sh --auto
```

### Step 3: Verify on GitHub
Check https://github.com/culturekeeperscircle/TRACKER-APP to confirm entries appear

---

## Advanced Usage

### Running from Python Directly
```python
from scripts.comprehensive_update import TrackerUpdate

updater = TrackerUpdate(auto_mode=True, dry_run=False)
success = updater.run()
updater.save_log()
```

### Scheduled Updates (Cron)
```bash
# Add to crontab: Run daily at 5 AM Eastern
0 10 * * 1-5 cd /path/to/TRACKER_APP && ./scripts/update.sh --auto >> logs/cron.log 2>&1
```

### GitHub Actions Integration
Create `.github/workflows/comprehensive-update.yml` to trigger script on schedule

---

## Troubleshooting

### "Repository has uncommitted changes"
```bash
git status               # See what's changed
git stash               # Temporarily save changes
./scripts/update.sh     # Run update
git stash pop          # Restore changes
```

### "Push failed: non-fast-forward"
Script will automatically attempt rebase. If it still fails:
```bash
git pull --rebase origin main
./scripts/update.sh --auto
```

### "NEW_ENTRIES file not found"
Create the file in the TRACKER APP root directory before running script:
```bash
touch NEW_ENTRIES_APRIL_2026.json
# Then populate with new entries
```

### Check Logs
After each run, a timestamped log is saved:
```bash
ls update_log_*.txt        # View all logs
cat update_log_20260402_*.txt  # Check latest
```

---

## Entry Format Reference

### Required Fields for Every Entry:
- `i` - Unique ID (e.g., "eo-policy-name-2026")
- `t` - Type (Executive Order, Legislation, Litigation, Agency Action, International)
- `n` - Short name
- `T` - Full title (can include HTML color spans)
- `s` - One-line summary
- `d` - Date (ISO format: YYYY-MM-DD)
- `a` - Administration (e.g., "Trump II")
- `A` - Array of agencies
- `S` - Status string
- `L` - Threat level (SEVERE, HARMFUL, WATCH, PROTECTIVE)
- `D` - Full description (HTML formatted)
- `c` - Communities array (see taxonomy below)
- `U` - Primary source URL
- `_source` - Data source tag
- `I` - Impact analysis object with 4Ps per community

### Community Taxonomy (27 total)
```
africanAmerican, indigenous, latine, asianAmerican, pacificIslander,
alaskaNative, nativeHawaiian, immigrant, lgbtq, women, disabled,
muslim, jewish, sikh, rural, urban, lowIncome, environmentalJustice,
academicCommunity, faithCommunities, arts, nonprofit, federalEmployees,
allCommunities
```

### Threat Levels
```
SEVERE      - Irreversible loss, mass impact, critical harm
HARMFUL     - Significant but potentially reversible damage
WATCH       - Monitoring level, moderate concern
PROTECTIVE  - Positive action, rights-expanding, restoration
```

### 4Ps Framework (Impact Analysis)
Each community needs analysis in 4 dimensions:
- **people**: Who is affected (practitioners, vulnerable populations, etc.)
- **places**: Geographic/spatial impact (neighborhoods, institutions, sacred sites)
- **practices**: Cultural practices (traditions, ceremonies, education)
- **treasures**: Material/cultural resources (artifacts, collections, archives)

Each should be 200-300+ words for comprehensive coverage.

---

## Success Indicators

✅ Script completed without errors
✅ Entry count increased in output message
✅ Commit message shows "Added X new entries"
✅ Log shows "Successfully pushed to GitHub"
✅ New entries visible on https://github.com/culturekeeperscircle/TRACKER-APP
✅ Entries render correctly on public tracker website

---

## File Locations

```
TRACKER APP/
├── scripts/
│   ├── comprehensive_update.py    # Main automation script
│   ├── update.sh                  # Shell wrapper
│   ├── enrich_entries.py          # Unified enrichment tool
│   ├── audit_toolkit.py           # Unified audit tool
│   ├── add_legislation_batch.py   # Batch legislation import
│   ├── validate_forms.py          # Form validation
│   └── README.md                  # This file
├── data/
│   ├── data.json                  # Main tracker database (single source of truth)
│   └── state.json                 # Pipeline state metadata
└── NEW_ENTRIES_APRIL_2026.json   # Input file (create before running)
```

## Additional Tools

### Enrichment
```bash
python3 scripts/enrich_entries.py --community indigenous --dry-run
python3 scripts/enrich_entries.py --community african-descendant --all
python3 scripts/enrich_entries.py --community targeted-gaps --all
python3 scripts/enrich_entries.py --community all --dry-run
```

### Auditing
```bash
python3 scripts/audit_toolkit.py --full                            # Full audit
python3 scripts/audit_toolkit.py --word-counts --period 2025-01 2025-03
python3 scripts/audit_toolkit.py --structure --since 2025-10
python3 scripts/audit_toolkit.py --summary                         # Quick overview
```

---

## Next Steps

1. **Create entry data** in NEW_ENTRIES_APRIL_2026.json
2. **Run update script**: `./scripts/update.sh --auto`
3. **Verify on GitHub** within 30 seconds
4. **Monitor tracker website** for live entry visibility

That's it! The rest is automated.
