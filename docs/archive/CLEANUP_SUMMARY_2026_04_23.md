# Tracker Folder Cleanup Summary — 2026-04-23

Complete audit and reorganization of the tracker's folder structure, instructional files, and data archive. Performed during the same session as:

- SPLC duplicate-entry merge
- 6 state-level entry deletions + Chicago municipal mute
- Generation-cap audit and permanent raise (15 → 50)
- NAGPRA policy lock (federal-actor individual + monthly aggregate)
- GitHub Actions workflow-timeout raise (60 → 90 min)
- API-key migration to `.env` via `python-dotenv`

---

## Why

Prior folder had **eight overlapping instructional files** (CLAUDE, SKILL, SYSTEM_SUMMARY, AUTOMATION_GUIDE, INDEX, QUICKSTART, README, VS_CODE_BUTTON_GUIDE) totaling 2,224 lines with significant duplication. Stale entry counts (666 entries, 5 categories) were inconsistent with current state (~755 entries, 6 categories). Root directory was cluttered with update logs, old backups, and one-off working documents.

---

## Folder Structure — Before / After

### Before (root level, 2026-04-23 morning)

```
.DS_Store
2026 03 28 - [NOTES] - Federal Language Suppression Timeline.docx
2026 04 23 - [AUDIT] - 50 Relevant Items Triage.md
2026 04 23 - [METHODOLOGY] - ...
2026 04 23 - [STRATEGY] - ...
AUTOMATION_GUIDE.md         (deprecated)
Aesthetics/
Archive/
CLAUDE.md                   (stale counts)
INDEX.md                    (deprecated)
International/
QUICKSTART.md               (out of date)
README.md                   (stale counts)
SKILL.md                    (stale counts)
SYSTEM_SUMMARY.md           (deprecated)
TCKC Threat Tracker.code-workspace
UPDATE_SUMMARY_2026_04_02.md
UPDATE_SUMMARY_2026_04_21.md
UPDATE_SUMMARY_2026_04_22.md
VS_CODE_BUTTON_GUIDE.md     (deprecated)
data/
index.html
pipeline/
requirements.txt
scripts/
tckc-litigation-tracker/
update_log_20260423_081815.txt
update_log_20260423_084626.txt
```

### After (root level)

```
Aesthetics/
Archive/
CLAUDE.md                   (updated, canonical AI operating instructions)
International/
README.md                   (updated, canonical public overview)
SKILL.md                    (updated, canonical agent skill file)
TCKC Threat Tracker.code-workspace
data/                       (cleaned; backups → data/archive/)
docs/                       (NEW; working docs + archive)
index.html
pipeline/
requirements.txt
scripts/
tckc-litigation-tracker/
```

---

## File Movements

### Working docs → `docs/`
- `2026 04 23 - [AUDIT] - 50 Relevant Items Triage.md`
- `2026 04 23 - [METHODOLOGY] - Pipeline Queries and Research Questions Full Disclosure.md`
- `2026 04 23 - [STRATEGY] - Historical Backfill and QA Plan Since Jan 19 2025.md`
- `QUICKSTART.md` (tightened, rewritten)

### New canonical consolidated file
- `docs/AUTOMATION.md` (consolidates AUTOMATION_GUIDE + SYSTEM_SUMMARY + VS_CODE_BUTTON_GUIDE)

### Deprecated instruction files → `docs/archive/`
- `AUTOMATION_GUIDE.md` (original, preserved for reference)
- `SYSTEM_SUMMARY.md`
- `VS_CODE_BUTTON_GUIDE.md`
- `INDEX.md`

### Update summaries → `docs/archive/`
- `UPDATE_SUMMARY_2026_04_02.md`
- `UPDATE_SUMMARY_2026_04_21.md`
- `UPDATE_SUMMARY_2026_04_22.md`

### Orphan docs → `docs/archive/`
- `2026 03 28 - [NOTES] - Federal Language Suppression Timeline.docx`

### Old data backups → `data/archive/`
- `data.json.bak-20260419-174725`
- `data.json.bak-20260419-175258`
- `state.json.bak-20260423-post-pull`
- `indigenous_audit_results.json`
- `word_count_analysis_results.txt`

### Files kept in `data/` (recent and canonical)
- `data.json` (source of truth)
- `state.json` (pipeline state)
- `state_level_archive_20260422.json` (recoverable state-level exports)
- `data.json.bak-20260422-pre-mute` (most recent rollback point; retained for 30 days)

### Deleted
- `.DS_Store` (untracked + gitignored)
- `update_log_20260423_081815.txt` (gitignored pattern)
- `update_log_20260423_084626.txt` (gitignored pattern)
- `Aesthetics/TRACKER APP.code-workspace` (stale old-name workspace file)

### Rewritten
- `CLAUDE.md` — Canonical AI operating instructions. Updated counts (~755 entries, 6 categories), scope rules locked, NAGPRA policy encoded, mute metadata specified, file layout reflects new structure.
- `SKILL.md` — Canonical agent skill file. Updated description with new triggers (NAGPRA Roundup, state-level mute, MAX_ENTRIES_PER_RUN, BGHPN storymap, Cultural Heritage Partners, NPCA NCRC). Current state snapshot updated.
- `README.md` — Canonical public overview. Updated counts, added Documentation Map, updated architecture diagram, reflects new `docs/` structure.
- `docs/AUTOMATION.md` — Fresh consolidated workflow guide. Covers both automated pipeline and manual JSON + comprehensive_update paths, VS Code tasks, env setup, state/dedup, caps/timeouts, scripts, troubleshooting.
- `docs/QUICKSTART.md` — One-page cheat sheet. Commands, schema, scope, troubleshooting.

---

## Net Counts

| Metric | Before | After |
|---|---|---|
| Instruction files in root | 8 | 3 (CLAUDE, SKILL, README) |
| Total root directory entries | 30 (including 4 hidden) | 14 (including 5 hidden) |
| Data folder files | 9 | 4 (plus `archive/` with 5) |
| Instructional-content duplication | High | Eliminated |
| Stale entry counts in docs | "666 / 5 categories" | Updated to "~755 / 6 categories" |

---

## Canonical File Map (Post-Cleanup)

| File | Purpose | Size |
|---|---|---|
| `CLAUDE.md` | AI operating rules (scope, style, NAGPRA, mute policy) | ~11 KB |
| `SKILL.md` | Agent skill trigger file (frontmatter + overview) | ~7 KB |
| `README.md` | Public-facing overview with documentation map | ~6 KB |
| `docs/AUTOMATION.md` | Complete update-workflow guide | ~8 KB |
| `docs/QUICKSTART.md` | One-page cheat sheet | ~4 KB |
| `docs/2026 04 23 - [METHODOLOGY] - ...md` | Full query + research-question transparency | ~22 KB |
| `docs/2026 04 23 - [STRATEGY] - ...md` | Historical-backfill plan (Jan 19 2025 →) | ~15 KB |
| `docs/2026 04 23 - [AUDIT] - ...md` | 50-item triage report from the 2026-04-23 pipeline pass | ~8 KB |

Archive files in `docs/archive/` and `data/archive/` are preserved for historical reference and are not expected to be consulted during normal operation.

---

## Recovery Instructions

If any of the deprecated instruction files need to be restored for reference (e.g., VS Code-button-specific troubleshooting), copies exist in `docs/archive/`. To restore to root:

```bash
cp "docs/archive/AUTOMATION_GUIDE.md" .
# etc.
```

If old data backups need to be restored (e.g., `data.json.bak-20260419-*`):

```bash
cp "data/archive/data.json.bak-20260419-175258" data/data.json
```

Note: the most recent rollback point (`data/data.json.bak-20260422-pre-mute`) is still in the main `data/` folder, not archived. It can be restored directly if needed.

---

## Follow-Ups

None required. The cleanup is complete and reversible. Future maintenance should:

1. Keep the three canonical files (CLAUDE.md, SKILL.md, README.md) current.
2. New working docs go in `docs/`; dated subfolders or archive as appropriate.
3. Periodic update summaries go in `docs/archive/`.
4. Data backups older than ~30 days move to `data/archive/`.
5. `update_log_*.txt` files are gitignored; they can be deleted at will.

---

*Cleanup performed 2026-04-23. File at `docs/archive/CLEANUP_SUMMARY_2026_04_23.md`.*
