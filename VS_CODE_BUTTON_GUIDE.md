# TCKC Tracker - VS Code Quick Button Guide

## Using the VS Code Task Button (Easiest Method)

### Step 1: Open Command Palette
Press: **`Cmd + Shift + P`** (on Mac) or **`Ctrl + Shift + P`** (on Windows/Linux)

### Step 2: Search for "Tasks"
Type: `tasks: run task`

You'll see suggestions appear. Click or press Enter on "Tasks: Run Task"

### Step 3: Select Your Task

You'll see a list of TCKC tasks:

```
> TCKC: Comprehensive Update (Interactive)
> TCKC: Comprehensive Update (Auto)              ← Most common
> TCKC: Update Preview (Dry-Run)
> TCKC: Check Git Status
> TCKC: Fetch from GitHub
> TCKC: View Recent Commits
```

#### Select based on your needs:

**For most cases:** `TCKC: Comprehensive Update (Auto)`
- Runs automatically without prompts
- Best when you've already reviewed entries
- Completes in ~30 seconds

**For safety:** `TCKC: Comprehensive Update (Interactive)`
- Asks for confirmation before major steps
- Good for first-time or critical updates
- Takes 1-2 minutes

**For testing:** `TCKC: Update Preview (Dry-Run)`
- Shows what would happen without committing
- Safe to test before full run
- No changes to git

### Step 4: Watch the Output

A terminal panel appears showing real-time progress:

```
✓ Fetching latest from GitHub...
✓ Validating repository state...
✓ Found 9 entries in NEW_ENTRIES file
✓ Integrated 9 entries into tracker
✓ Updated state.json
✓ Committing changes...
✓ Pushing to GitHub...
✓ Verification complete
=== Update Complete ===
```

### Step 5: Verify Success

You'll see one of:
- ✅ **"Update completed successfully!"** - Entries are live on GitHub
- ❌ **"Update failed"** - Check logs for errors (see troubleshooting below)

---

## Common Workflows

### Workflow 1: Quick Update (30 seconds)
1. `Cmd+Shift+P` → `tasks: run task`
2. Select: `TCKC: Comprehensive Update (Auto)`
3. Wait for "✓ Update completed"
4. Done! ✅

### Workflow 2: Safe Update (1-2 minutes)
1. `Cmd+Shift+P` → `tasks: run task`
2. Select: `TCKC: Comprehensive Update (Interactive)`
3. Review prompt, confirm with `y`
4. Watch progress
5. Done! ✅

### Workflow 3: Test Before Publish
1. `Cmd+Shift+P` → `tasks: run task`
2. Select: `TCKC: Update Preview (Dry-Run)`
3. Review what would happen
4. If OK: Run `TCKC: Comprehensive Update (Auto)`
5. Done! ✅

### Workflow 4: Check Status
Before updating, check status:
1. `Cmd+Shift+P` → `tasks: run task`
2. Select: `TCKC: Check Git Status`
3. See any uncommitted changes
4. Then run update

---

## Keyboard Shortcuts (Optional Setup)

To make it even faster, add keyboard shortcuts:

1. Open VS Code Preferences
2. Search: "Keyboard Shortcuts"
3. Click "Open Keyboard Shortcuts (JSON)"
4. Add this to your keybindings:

```json
{
  "key": "shift+cmd+u",
  "command": "workbench.action.tasks.runTask",
  "args": "TCKC: Comprehensive Update (Auto)"
}
```

Then you can just press **`Shift+Cmd+U`** to update! (or any shortcut you prefer)

---

## Terminal Output Explained

### Successful Run
```
[2026-04-02 14:32:15] INFO: === TCKC Threat Tracker Comprehensive Update ===
[2026-04-02 14:32:15] INFO: Mode: AUTO | Dry-run: False
[2026-04-02 14:32:15] INFO: Fetching latest from GitHub...
[2026-04-02 14:32:17] INFO: Fetched successfully
[2026-04-02 14:32:18] INFO: Found 9 entries in NEW_ENTRIES file
[2026-04-02 14:32:19] INFO: Added 2 entries to executive_actions
[2026-04-02 14:32:19] INFO: Added 2 entries to legislation
[2026-04-02 14:32:19] INFO: Added 2 entries to litigation
[2026-04-02 14:32:19] INFO: Added 2 entries to agency_actions
[2026-04-02 14:32:19] INFO: Added 1 entries to international
[2026-04-02 14:32:20] INFO: Integrated 9 total entries
[2026-04-02 14:32:21] INFO: Committing changes...
[2026-04-02 14:32:22] INFO: Committed: [main 0e5fa0d] Comprehensive update: April 2, 2026...
[2026-04-02 14:32:23] INFO: Pushing to GitHub...
[2026-04-02 14:32:26] INFO: Successfully pushed to GitHub
[2026-04-02 14:32:26] INFO: Verifying publication...
[2026-04-02 14:32:27] INFO: Remote HEAD: 7dbe606 Add comprehensive update summary document
[2026-04-02 14:32:27] INFO: === Update Complete ===

✓ Update completed successfully!
```

### What Each Line Means
- `Fetching...` = Getting latest from GitHub
- `Found 9 entries` = NEW_ENTRIES file loaded
- `Added X entries to [category]` = Integration in progress
- `Committing...` = Git commit being created
- `Pushing to GitHub...` = Upload in progress
- `Successfully pushed` = ✅ Entries are now live!

---

## Troubleshooting from VS Code

### Error: "Repository has uncommitted changes"
**Meaning:** You have unsaved git changes
**Solution:**
1. Open VS Code terminal: `` Cmd+` ``
2. Run: `git status` (to see what changed)
3. Run: `git stash` (to temporarily save)
4. Go back to task: `Cmd+Shift+P` → run task again
5. After success: `git stash pop` (to restore changes)

### Error: "Push failed: non-fast-forward"
**Meaning:** Remote has changes you don't have locally
**Solution:** (Script should auto-fix this)
- If it fails, wait 30 seconds and try again
- Or manually: `git pull --rebase origin main`

### Error: "NEW_ENTRIES file not found"
**Meaning:** Missing the input file
**Solution:**
1. Create: `NEW_ENTRIES_APRIL_2026.json`
2. Add your entries to it
3. Try task again

### No Output Appearing
**Solution:**
1. Check if terminal panel is open (bottom of VS Code)
2. If not, click "Terminal" panel or press `` Cmd+` ``
3. Scroll down to see latest output

---

## File Locations in VS Code

### Explorer View
```
TRACKER APP/
├── scripts/
│   ├── comprehensive_update.py       ← Automation engine
│   ├── update.sh                     ← Shell script
│   └── README.md                     ← Detailed guide
│
├── AUTOMATION_GUIDE.md               ← Full documentation
├── QUICKSTART.md                     ← Quick reference
├── NEW_ENTRIES_APRIL_2026.json       ← Your entries (create this)
├── data/
│   ├── data.json                     ← Updated by script
│   └── state.json                    ← Updated by script
└── .vscode/
    └── tasks.json                    ← Task definitions
```

---

## What Gets Updated

| File | Change | When |
|------|--------|------|
| `NEW_ENTRIES_APRIL_2026.json` | Nothing (input file) | You edit before running |
| `data/data.json` | New entries added | During integration step |
| `data/state.json` | Timestamps updated | During integration step |
| GitHub | Commit pushed | During push step |
| Public website | Auto-updated | Within 1 minute |

---

## Success Checklist

After running `TCKC: Comprehensive Update (Auto)`:

- [ ] Terminal shows: "Update completed successfully!"
- [ ] Output shows: "Added X new entries"
- [ ] Terminal shows: "Successfully pushed to GitHub"
- [ ] Visit GitHub: https://github.com/culturekeeperscircle/TRACKER-APP
- [ ] Confirm new commit appears
- [ ] Check public tracker site for live entries

---

## Next Updates

The process is exactly the same every time:

1. **Prepare entries** → Edit `NEW_ENTRIES_APRIL_2026.json` (or create new file)
2. **Run task** → `Cmd+Shift+P` → "TCKC: Comprehensive Update (Auto)"
3. **Verify** → Check GitHub in 30 seconds

That's it! No more manual git commands needed.

---

## Tips & Tricks

### Quick Access
- Pin the task by right-clicking in task list
- Use keyboard shortcut (see above)
- It appears in "recent tasks" after first run

### Monitoring
- Keep terminal open to see progress
- Logs saved in: `update_log_*.txt` (if you need to review later)

### Debugging
- Try `TCKC: Update Preview (Dry-Run)` first to test
- Check `TCKC: Check Git Status` to see pending changes
- View `TCKC: View Recent Commits` to confirm push worked

### Automation
- Can be integrated with GitHub Actions for scheduled runs
- Can be triggered from external APIs
- Can send notifications on completion

---

**That's everything! You're all set to use the automated system.** 🚀
