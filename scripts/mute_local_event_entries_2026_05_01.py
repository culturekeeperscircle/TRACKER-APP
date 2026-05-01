#!/usr/bin/env python3
"""Mute two out-of-scope local-event entries surfaced 2026-05-01.

Per the federal-actions-only scope rule (CLAUDE.md, locked 2026-04-23),
local community events are out of scope unless executed by a federal
actor. Both entries below are San Francisco Bay Area community events
sourced from sf.funcheap.com. Project policy is to mute, never delete,
so the records remain recoverable.
"""
import json
import shutil
from pathlib import Path
from datetime import datetime

DATA_PATH = Path(__file__).parent.parent / "data" / "data.json"
BACKUP_PATH = DATA_PATH.with_suffix(
    f".json.bak-{datetime.now().strftime('%Y%m%d-%H%M%S')}-pre-mute-local-events"
)

MUTE_DATE = "2026-05-01"

TARGETS = [
    {
        "id": "aapi-heritage-block-party-sf-2026-001",
        "category": "other_domestic",
        "reason": (
            "Local community event (San Francisco AAPI Heritage Month "
            "block party). No federal actor, sourced from sf.funcheap.com. "
            "Out of scope per federal-only rule (CLAUDE.md, 2026-04-23)."
        ),
    },
    {
        "id": "birthright-citizenship-attack-2026-001",
        "category": "other_domestic",
        "reason": (
            "Local community forum in Berkeley discussing federal "
            "birthright-citizenship litigation. Sourced from "
            "sf.funcheap.com. The forum is a local event by community "
            "speakers, not a federal action by a federal actor. The "
            "underlying federal litigation and EO remain trackable as "
            "their own discrete entries. Out of scope per federal-only "
            "rule (CLAUDE.md, 2026-04-23)."
        ),
    },
]


def main():
    if not DATA_PATH.exists():
        raise SystemExit(f"data.json not found at {DATA_PATH}")

    em_dash = "—"
    for t in TARGETS:
        if em_dash in t["reason"]:
            raise SystemExit(f"ABORT: em-dash in mute reason for {t['id']}.")

    shutil.copy2(DATA_PATH, BACKUP_PATH)
    print(f"Backup written: {BACKUP_PATH.name}")

    with DATA_PATH.open() as f:
        data = json.load(f)

    muted_count = 0
    for t in TARGETS:
        cat = t["category"]
        target_id = t["id"]
        found = False
        for entry in data.get(cat, []):
            if (entry.get("i") or entry.get("id")) == target_id:
                if entry.get("muted"):
                    print(f"  SKIP: {target_id} already muted")
                else:
                    entry["muted"] = True
                    entry["_mutedReason"] = t["reason"]
                    entry["_mutedDate"] = MUTE_DATE
                    print(f"  MUTED: {target_id}")
                    muted_count += 1
                found = True
                break
        if not found:
            print(f"  NOT FOUND: {target_id} (in {cat})")

    if "meta" in data and isinstance(data["meta"], dict):
        data["meta"]["lastUpdated"] = datetime.now().strftime("%Y-%m-%d")

    tmp = DATA_PATH.with_suffix(".json.tmp")
    with tmp.open("w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    tmp.replace(DATA_PATH)

    print(f"\nMuted {muted_count} entries.")


if __name__ == "__main__":
    main()
