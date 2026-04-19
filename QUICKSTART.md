# TCKC Tracker - Quick Start Cheat Sheet

## One-Command Update

```bash
cd "Culture Keepers Circle/TRACKER APP" && ./scripts/update.sh --auto
```

**What you need:**
1. File named `NEW_ENTRIES_APRIL_2026.json` in tracker root (with new entries)
2. Git credentials configured (happens once)

**What happens:**
- Fetches from GitHub ✓
- Integrates new entries ✓
- Commits changes ✓
- Pushes to GitHub ✓
- Entries live in ~30 seconds ✓

---

## Setup (First Time Only)

### 1. Configure Git
```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

### 2. Make Scripts Executable
```bash
chmod +x scripts/update.sh scripts/comprehensive_update.py
```

✅ Done! Now just run: `./scripts/update.sh --auto`

---

## Usage Methods

### Command Line (Fastest)
```bash
./scripts/update.sh --auto              # No prompts, fully automated
./scripts/update.sh                     # Interactive mode with confirmations
./scripts/update.sh --dry-run           # Preview without committing
./scripts/update.sh --help              # Show help
```

### VS Code (Most Convenient)
- Press `Cmd+Shift+P`
- Type "Tasks: Run Task"
- Select a TCKC task:
  - **TCKC: Comprehensive Update (Auto)** ← Use this
  - TCKC: Comprehensive Update (Interactive)
  - TCKC: Update Preview (Dry-Run)

---

## Entry File Format (Quick Reference)

Create `NEW_ENTRIES_APRIL_2026.json`:

```json
{
  "executive_actions": [
    {
      "i": "eo-unique-id-2026",
      "t": "Executive Order",
      "n": "Short name",
      "T": "<span style=\"color: #991B1B;\">Full Title</span>",
      "s": "One-sentence summary",
      "d": "2026-04-02",
      "a": "Trump II",
      "A": ["OMB", "DOJ"],
      "S": "Status description",
      "L": "SEVERE",
      "D": "<b>Full description with impact...</b>",
      "c": ["africanAmerican", "indigenous", "latine"],
      "U": "https://source-url.gov",
      "_source": "federal_register",
      "I": {
        "africanAmerican": {
          "people": "Who is affected...",
          "places": "Where it impacts...",
          "practices": "Cultural practices affected...",
          "treasures": "Cultural resources at risk..."
        }
      }
    }
  ],
  "legislation": [],
  "litigation": [],
  "agency_actions": [],
  "international": []
}
```

---

## Threat Levels

Use ONE:
- `SEVERE` - Irreversible loss, mass impact
- `HARMFUL` - Significant reversible damage
- `WATCH` - Monitoring level concern
- `PROTECTIVE` - Positive action, rights-expanding

---

## Communities (Pick Multiple)

```
africanAmerican         indigenous           latine
asianAmerican           pacificIslander      alaskaNative
nativeHawaiian          immigrant            lgbtq
women                   disabled             muslim
jewish                  sikh                 rural
urban                   lowIncome            environmentalJustice
academicCommunity       faithCommunities     arts
nonprofit               federalEmployees     allCommunities
```

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| "Repository has uncommitted changes" | `git stash` before running, `git stash pop` after |
| "Push failed" | Script auto-rebases, if it fails: `git pull --rebase origin main` |
| "NEW_ENTRIES file not found" | Create the file with your entries |
| "Python not found" | `brew install python3` |
| "Permission denied" | `chmod +x scripts/update.sh scripts/comprehensive_update.py` |

---

## Workflow Diagram

```
Create Entries JSON
        ↓
  Run update.sh
        ↓
  [script does all this automatically]
  ├─ git fetch origin/main
  ├─ validate repo
  ├─ load entries
  ├─ merge into data.json
  ├─ update state.json
  ├─ git commit
  ├─ git push
  └─ verify on GitHub
        ↓
   ✅ Entries Live
```

---

## What Gets Updated

| File | What Changes |
|------|--------------|
| `data/data.json` | New entries added to arrays |
| `data/state.json` | Last run timestamp, entry counts |
| GitHub repo | Commit with updated files |
| Public tracker | Entries visible (auto-synced) |

---

## Exit Codes

```
0 = Success ✓
1 = Failure ✗
```

Check logs for details: `update_log_*.txt`

---

## Time Requirements

- **Command line:** 30 seconds
- **Interactive:** 1-2 minutes
- **Dry-run:** 30 seconds
- **First setup:** 2 minutes

---

## Critical Files

```
✓ NEW_ENTRIES_APRIL_2026.json     ← You create this
✓ scripts/comprehensive_update.py  ← Automation engine
✓ scripts/update.sh                ← Shell wrapper
✓ data/data.json                   ← Tracker database
✓ data/state.json                  ← Metadata
```

---

## Common Commands

```bash
# Check what changed
git status --short

# See recent updates
git log --oneline -5

# Fetch latest
git fetch origin

# Preview (no commit)
./scripts/update.sh --dry-run

# Run with confirmation
./scripts/update.sh

# Run fully automated
./scripts/update.sh --auto

# View logs
cat update_log_*.txt | tail -50
```

---

## Success Checklist

After running `./scripts/update.sh --auto`:

- [ ] Command completed (exit code 0)
- [ ] Output shows entry counts increased
- [ ] Commit message shows "Added X new entries"
- [ ] Log shows "Successfully pushed to GitHub"
- [ ] Check GitHub: https://github.com/culturekeeperscircle/TRACKER-APP
- [ ] New entries visible on public tracker site

---

## Next Update

Repeat for next entries (same process every time):

1. Update `NEW_ENTRIES_APRIL_2026.json` with new entries
2. Run: `./scripts/update.sh --auto`
3. Done in 30 seconds

That's it!

---

**For full documentation:** See `AUTOMATION_GUIDE.md` or `scripts/README.md`
