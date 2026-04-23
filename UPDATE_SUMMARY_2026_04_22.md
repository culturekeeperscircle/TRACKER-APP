# TCKC Tracker Update Summary — 2026-04-22

## Scope of Change

Federal-only hygiene pass. Six state-level entries removed from the tracker. One municipal entry flagged `muted`. Frontend updated to filter muted entries from public view.

## Deleted (6 entries)

Archived to `data/state_level_archive_20260422.json` for potential reclassification into the BGHPN Storymap state-policy layer (see `Culture Keepers Circle/BGHPN Storymap Partnership/`).

| Category | ID | Title |
|---|---|---|
| legislation | `s-tennessee-immigrant-school-ban-2026` | Tennessee HB/SB Undocumented Student Exclusion Bill |
| other_domestic | `arizona-maricopa-election-2026-001` | Arizona 2026 Midterm Election Administration — Maricopa County |
| other_domestic | `indiana-fairness-act-2026` | Indiana FAIRNESS Act (SEA 76) |
| other_domestic | `ohio-drag-ban-hb249-2026` | Ohio HB 249 — Drag Performance Ban |
| other_domestic | `idaho-trans-bathroom-criminal-2026` | Idaho HB 752 — Criminal Transgender Bathroom Ban |
| other_domestic | `kansas-trans-license-invalidation-2026` | Kansas SB 244 — Transgender License Invalidation |

## Muted (1 entry)

| Category | ID | Reason |
|---|---|---|
| other_domestic | `chicago-reparations-tipped-wages-2026-001` | Municipal-level (Chicago mayoral advocacy), not federal |

Muted entries carry `"muted": true`, `"_mutedReason": "..."`, and `"_mutedDate": "2026-04-22"`.

## Frontend Changes (index.html)

Added `isVisibleItem(item)` helper that returns `false` for entries with `muted === true`. Wired into:

1. `getAllItems()` — the all-category aggregator.
2. The category-specific branch in `filterCards()`.

Auditors can override the mute by appending `?show_muted=1` to the URL.

## Deliberately Kept (not muted, not deleted)

These are federal cases with state parties, where the forum and the action are federal:

- `lit-2026-disability-504` — *Texas v. Kennedy* (N.D. Tex., federal court)
- `lit-2026-scotus-trans-athletes` — *West Virginia v. B.P.J.; Little v. Hecox* (SCOTUS)
- `noaa-washington-climate-lawsuit` — Washington AG case against federal NOAA
- `intl-ref-lit-daca-texas` — *Texas v. US (DACA)*, federal court
- `intl-ref-lit-refugee-snap` — *Oregon v. USDA*, federal court

## Counts

| Category | Before | After |
|---|---:|---:|
| executive_actions | 99 | 99 |
| agency_actions | 255 | 255 |
| legislation | 195 | 194 |
| litigation | 126 | 126 |
| other_domestic | 24 | 19 |
| international | 60 | 60 |
| **TOTAL** | **759** | **753** |

## Backup

Pre-change snapshot: `data/data.json.bak-20260422-pre-mute` (58 MB, identical to pre-operation state).

## Audit Status

Ran `python3 scripts/audit_toolkit.py --full`. Reported 171 pre-existing word-count issues across 154 entries (the open "dropdown analyses" work already tracked in memory). No new issues introduced by this operation.

## Rollback Instructions

If this change needs to be reversed:

```bash
cd "Culture Keepers Circle/TCKC Threat Tracker"
cp data/data.json.bak-20260422-pre-mute data/data.json
git checkout index.html  # if tracked in git, otherwise restore manually
```

The six deleted entries remain intact in `data/state_level_archive_20260422.json` for reference even after rollback.

## Related Work

The deleted state-level entries are exactly the type of data the BGHPN Storymap five-state layer (FL, AL, MD, NY, MS — due May 28) will need. Tennessee, Ohio, Indiana, Idaho, Kansas, and Arizona are outside the Phase 1 scope, but the archive file provides a template and sample data for Phase 2 expansion. See `Culture Keepers Circle/BGHPN Storymap Partnership/2026 04 22 - [PLAN] - Five-State Policy Layer Delivery Plan (Due May 28).md`.

---

*Operation executed 2026-04-22 by A. Prince Albert III with Claude assistance.*
