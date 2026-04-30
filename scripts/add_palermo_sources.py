#!/usr/bin/env python3
"""Append a SOURCES section to the Palermo Atlantic entry's description."""
import json
import shutil
from pathlib import Path
from datetime import datetime

DATA_PATH = Path(__file__).parent.parent / "data" / "data.json"
BACKUP_PATH = DATA_PATH.with_suffix(
    f".json.bak-{datetime.now().strftime('%Y%m%d-%H%M%S')}-pre-palermo-sources"
)
TARGET_ID = "kennedy-center-palermo-atlantic-2026-003"

SOURCES_BLOCK = (
    "<br><br><b>SOURCES.</b><br>"
    "Primary source: Josef Palermo, \"What I Saw Inside the Kennedy Center,\" The Atlantic, April 16, 2026. "
    "<a href=\"https://www.theatlantic.com/culture/2026/04/inside-kennedy-center-shutdown-drama/686801/\">https://www.theatlantic.com/culture/2026/04/inside-kennedy-center-shutdown-drama/686801/</a><br>"
    "Secondary coverage and summaries: "
    "Broadway World, \"Former Kennedy Center Arts Curator Details Cronyism, Incompetence, and Bizarre Moves Amidst Trump Takeover,\" April 17, 2026. "
    "<a href=\"https://www.broadwayworld.com/article/Former-Kennedy-Center-Arts-Curator-Details-Cronyism-Incompetence-and-Bizarre-Moves-Amidst-Trump-Takeover-20260417\">https://www.broadwayworld.com/article/Former-Kennedy-Center-Arts-Curator-Details-Cronyism-Incompetence-and-Bizarre-Moves-Amidst-Trump-Takeover-20260417</a>; "
    "The Atlantic on Threads, introduction of the Palermo piece. "
    "<a href=\"https://www.threads.com/@theatlantic/post/DXXudhqFHok/josef-palermo-spent-months-working-at-the-kennedy-center-because-he-wanted-to\">https://www.threads.com/@theatlantic/post/DXXudhqFHok/josef-palermo-spent-months-working-at-the-kennedy-center-because-he-wanted-to</a>; "
    "PBS NewsHour, \"Ex-Kennedy Center staffer alleges chaos and cronyism under Trump leadership.\" "
    "<a href=\"https://www.pbs.org/newshour/show/ex-kennedy-center-staffer-alleges-chaos-and-cronyism-under-trump-leadership\">https://www.pbs.org/newshour/show/ex-kennedy-center-staffer-alleges-chaos-and-cronyism-under-trump-leadership</a>; "
    "The Violin Channel, \"Whistleblower Josef Palermo Gives Account of Cronyism and Incompetence Inside the Kennedy Center.\" "
    "<a href=\"https://theviolinchannel.com/whistleblower-josef-palermo-gives-account-of-cronyism-and-incompetence-inside-the-kennedy-center/\">https://theviolinchannel.com/whistleblower-josef-palermo-gives-account-of-cronyism-and-incompetence-inside-the-kennedy-center/</a>; "
    "Atlanta Black Star (aggregator coverage that surfaced the piece for this tracker entry).<br>"
    "Related tracker entries: kennedy-center-financial-decline-2026-002 (CBS News follow-up interview, 2026-04-21); "
    "v2025-009 (February 2025 Kennedy Center board purge); "
    "aa-2026-kennedy-closure (2-year closure order, February 2026); "
    "v2025-001 (Kennedy Center renaming); "
    "v2025-kennedy-002 (artist boycott response); "
    "beatty-v-trump-2025 (renaming litigation, Case 1:25-cv-03891 (D.D.C.))."
)


def main():
    if not DATA_PATH.exists():
        raise SystemExit(f"data.json not found at {DATA_PATH}")

    shutil.copy2(DATA_PATH, BACKUP_PATH)
    print(f"Backup written: {BACKUP_PATH.name}")

    with DATA_PATH.open() as f:
        data = json.load(f)

    target = None
    for e in data.get("other_domestic", []):
        if (e.get("id") or e.get("i")) == TARGET_ID:
            target = e
            break

    if target is None:
        raise SystemExit(f"Target entry {TARGET_ID} not found.")

    if "<b>SOURCES.</b>" in target.get("D", ""):
        raise SystemExit("Sources block already present. Aborting.")

    em_dash = "—"
    if em_dash in SOURCES_BLOCK:
        raise SystemExit("ABORT: em-dash detected in sources block.")

    target["D"] = target["D"] + SOURCES_BLOCK

    if "meta" in data and isinstance(data["meta"], dict):
        data["meta"]["lastUpdated"] = datetime.now().strftime("%Y-%m-%d")

    tmp = DATA_PATH.with_suffix(".json.tmp")
    with tmp.open("w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    tmp.replace(DATA_PATH)

    print(f"Appended SOURCES section to {TARGET_ID}.")


if __name__ == "__main__":
    main()
