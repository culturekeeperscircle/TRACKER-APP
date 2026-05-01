#!/usr/bin/env python3
"""Delete all non-federal (muted) entries 2026-05-01.

Prince explicitly authorized destructive deletion of every entry
flagged `muted: true` in this session, overriding the standing
CLAUDE.md mute-only rule. Reason: he is rebuilding sub-federal
tracking from scratch and wants a clean slate.

Two carve-outs apply.

1. The birthright-citizenship-attack-2026-001 entry is un-muted and
   retained because birthright citizenship is a federal matter under
   active Supreme Court litigation. The entry's current body describes
   a Berkeley public forum on the federal litigation; a separate
   future revision can refactor it to center the federal EO and the
   litigation itself.

2. Every other entry with `muted: true` is removed from data.json.

A timestamped backup is taken before any write so the records remain
recoverable on disk even though they leave the live database.
"""
import json
import shutil
from pathlib import Path
from datetime import datetime

DATA_PATH = Path(__file__).parent.parent / "data" / "data.json"
BACKUP_PATH = DATA_PATH.with_suffix(
    f".json.bak-{datetime.now().strftime('%Y%m%d-%H%M%S')}-pre-delete-nonfederal"
)

CATS = [
    "executive_actions",
    "agency_actions",
    "legislation",
    "litigation",
    "other_domestic",
    "international",
]

UNMUTE_IDS = {"birthright-citizenship-attack-2026-001"}


def main():
    if not DATA_PATH.exists():
        raise SystemExit(f"data.json not found at {DATA_PATH}")

    shutil.copy2(DATA_PATH, BACKUP_PATH)
    print(f"Backup written: {BACKUP_PATH.name}")

    with DATA_PATH.open() as f:
        data = json.load(f)

    unmuted = 0
    for c in CATS:
        for entry in data.get(c, []):
            eid = entry.get("i") or entry.get("id")
            if eid in UNMUTE_IDS and entry.get("muted"):
                entry.pop("muted", None)
                entry.pop("_mutedReason", None)
                entry.pop("_mutedDate", None)
                unmuted += 1
                print(f"  UNMUTED: {eid}")

    deleted_total = 0
    deleted_by_cat = {}
    deleted_ids = []
    for c in CATS:
        kept = []
        removed = 0
        for entry in data.get(c, []):
            if entry.get("muted"):
                deleted_ids.append(entry.get("i") or entry.get("id"))
                removed += 1
            else:
                kept.append(entry)
        if removed:
            deleted_by_cat[c] = removed
            deleted_total += removed
        data[c] = kept

    if "meta" in data and isinstance(data["meta"], dict):
        data["meta"]["lastUpdated"] = datetime.now().strftime("%Y-%m-%d")

    tmp = DATA_PATH.with_suffix(".json.tmp")
    with tmp.open("w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    tmp.replace(DATA_PATH)

    print(f"\nUn-muted: {unmuted}")
    print(f"Deleted: {deleted_total}")
    for c, n in deleted_by_cat.items():
        print(f"  {c}: -{n}")

    log_path = Path(__file__).parent.parent / "data" / "archive" / (
        f"deleted-nonfederal-ids-{datetime.now().strftime('%Y%m%d-%H%M%S')}.txt"
    )
    log_path.parent.mkdir(parents=True, exist_ok=True)
    log_path.write_text("\n".join(deleted_ids) + "\n")
    print(f"Deleted-id log: {log_path.relative_to(DATA_PATH.parent.parent)}")


if __name__ == "__main__":
    main()
