"""
Bulk-load (upsert) the entire data.json into Supabase.

This is the canonical full-sync loader: every entry, including cross-refs.
For incremental insert-only loading from the daily pipeline, see sync.py.

Usage:
    python -m pipeline.supabase.load                # full upsert from data/data.json
    python -m pipeline.supabase.load --insert-only  # skip rows that already exist

Environment:
    SUPABASE_PROJECT_REF       (default xsqdjhjcqbawghuaqqwj)
    SUPABASE_SERVICE_ROLE_KEY  (preferred)
    SUPABASE_ANON_KEY          (works only when temp policy is open)
"""
import argparse
import json
import os
import sys
import time
from collections import defaultdict
from pathlib import Path

import requests

from .client import get_credentials
from .mapping import CATEGORIES, entry_to_row

REPO_ROOT = Path(__file__).resolve().parents[2]
DATA_JSON = REPO_ROOT / "data" / "data.json"

BATCH_SIZE = 50


def build_rows(data):
    """Walk every category, including cross-refs, and produce row dicts."""
    rows = []
    crossrefs_into = defaultdict(set)

    for cat in CATEGORIES:
        for entry in data.get(cat, []):
            if not isinstance(entry, dict):
                continue
            row = entry_to_row(entry, cat)
            if row is None:
                continue
            rows.append(row)
            # Track which categories each primary entry is referenced into.
            if row["is_cross_ref"] and row.get("primary_ref_id"):
                crossrefs_into[row["primary_ref_id"]].add(cat)

    # Attach crossrefs_into to primaries that exist in our row set.
    by_id = {r["id"]: r for r in rows}
    for primary_id, cats in crossrefs_into.items():
        if primary_id in by_id:
            by_id[primary_id]["crossrefs_into"] = sorted(cats)

    return rows


def post(creds, table, rows, prefer):
    url = f"{creds['base_url']}/{table}"
    headers = {**creds["headers"], "Prefer": prefer}
    r = requests.post(url, headers=headers, data=json.dumps(rows), timeout=120)
    if r.status_code >= 300:
        sys.stderr.write(f"FAIL {r.status_code} {r.text[:600]}\n")
        if rows:
            sys.stderr.write(f"first row id: {rows[0].get('id')!r}\n")
        r.raise_for_status()
    return r


def load_entries(creds, rows, insert_only):
    if insert_only:
        prefer = "resolution=ignore-duplicates,return=minimal"
    else:
        prefer = "resolution=merge-duplicates,return=minimal"

    print(f"loading {len(rows)} entries (mode={'insert-only' if insert_only else 'upsert'})", flush=True)
    sent = 0
    for i in range(0, len(rows), BATCH_SIZE):
        batch = rows[i : i + BATCH_SIZE]
        post(creds, "entries?on_conflict=id", batch, prefer)
        sent += len(batch)
        if sent % 200 == 0 or sent == len(rows):
            print(f"  {sent}/{len(rows)}", flush=True)
        time.sleep(0.04)


def load_meta(creds, data):
    meta_in = data.get("meta", {}) or {}
    last = meta_in.get("lastUpdated")
    if last and not last[:10].count("-") == 2:
        last = None
    meta_row = {
        "id": 1,
        "total": meta_in.get("total"),
        "by_category": meta_in.get("by_category"),
        "cross_ref_count": meta_in.get("_crossRefCount"),
        "note": meta_in.get("_note"),
        "last_updated": last,
    }
    post(creds, "tracker_meta?on_conflict=id", [meta_row], "resolution=merge-duplicates,return=minimal")
    print("meta loaded", flush=True)


def verify(creds):
    r = requests.get(
        f"{creds['base_url']}/entries?select=id",
        headers={**creds["headers"], "Prefer": "count=exact", "Range-Unit": "items", "Range": "0-0"},
        timeout=30,
    )
    print(f"verify: status={r.status_code}, content-range={r.headers.get('Content-Range')}")


def main():
    parser = argparse.ArgumentParser(description="Full-sync loader for TCKC tracker")
    parser.add_argument("--insert-only", action="store_true", help="skip rows that already exist")
    parser.add_argument("--data-json", default=str(DATA_JSON), help="path to data.json")
    args = parser.parse_args()

    creds = get_credentials()
    print(f"using {creds['key_kind']} key against {creds['base_url']}", flush=True)

    with open(args.data_json, "r", encoding="utf-8") as f:
        data = json.load(f)

    rows = build_rows(data)
    print(f"prepared {len(rows)} rows from {args.data_json}", flush=True)
    load_entries(creds, rows, args.insert_only)
    load_meta(creds, data)
    verify(creds)


if __name__ == "__main__":
    main()
