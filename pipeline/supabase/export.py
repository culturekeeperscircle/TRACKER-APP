"""
Export the entire entries + tracker_meta state from Supabase into data.json.

Supabase is the source of truth. data.json is a generated artifact: queryable
with normal tools, citeable via Zenodo, and consumed by the static index.html.
This script runs in the GitHub Actions workflow before commit.

Usage:
    python -m pipeline.supabase.export                       # writes to data/data.json
    python -m pipeline.supabase.export --out /tmp/export.json
    python -m pipeline.supabase.export --pretty              # human-readable indent

Output shape (matches the legacy data.json):
    {
      "executive_actions": [...],
      "agency_actions":    [...],
      "legislation":       [...],
      "litigation":        [...],
      "other_domestic":    [...],
      "international":     [...],
      "meta": {...}
    }
"""
import argparse
import json
from pathlib import Path

import requests

from .client import get_credentials
from .mapping import CATEGORIES, row_to_entry

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_OUT = REPO_ROOT / "data" / "data.json"

PAGE_SIZE = 200  # PostgREST default cap is 1000; 200 keeps payloads small


def fetch_all_entries(creds):
    """Page through entries ordered by category and date so output is stable."""
    rows = []
    offset = 0
    while True:
        r = requests.get(
            f"{creds['base_url']}/entries",
            headers={**creds["headers"], "Range-Unit": "items", "Range": f"{offset}-{offset + PAGE_SIZE - 1}"},
            params={"select": "*", "order": "category.asc,action_date.desc.nullslast,id.asc"},
            timeout=60,
        )
        r.raise_for_status()
        page = r.json()
        rows.extend(page)
        if len(page) < PAGE_SIZE:
            break
        offset += PAGE_SIZE
    return rows


def fetch_meta(creds):
    r = requests.get(
        f"{creds['base_url']}/tracker_meta?select=*&id=eq.1",
        headers=creds["headers"],
        timeout=30,
    )
    r.raise_for_status()
    rows = r.json()
    return rows[0] if rows else {}


def assemble(rows, meta_row):
    """Bucket rows into categories and append the meta block in legacy shape."""
    out = {cat: [] for cat in CATEGORIES}
    for row in rows:
        cat = row.get("category")
        if cat in out:
            out[cat].append(row_to_entry(row))

    # Sort each category by action_date descending, ties broken by id, matching
    # the legacy data_manager.add_entries() convention.
    for cat in CATEGORIES:
        out[cat].sort(key=lambda e: (e.get("d", ""), e.get("i") or e.get("id", "")), reverse=True)

    total = sum(len(out[c]) for c in CATEGORIES)
    cross_ref_count = sum(1 for r in rows if r.get("is_cross_ref"))
    out["meta"] = {
        "total": total,
        "by_category": {c: len(out[c]) for c in CATEGORIES},
        "_crossRefCount": meta_row.get("cross_ref_count") or cross_ref_count,
        "_note": meta_row.get("note") or "",
        "lastUpdated": str(meta_row["last_updated"]) if meta_row.get("last_updated") else None,
    }
    return out


def main():
    parser = argparse.ArgumentParser(description="Export Supabase state to data.json")
    parser.add_argument("--out", default=str(DEFAULT_OUT), help="output path")
    parser.add_argument("--pretty", action="store_true", help="indent the output JSON")
    args = parser.parse_args()

    creds = get_credentials()
    print(f"export using {creds['key_kind']} from {creds['base_url']}", flush=True)

    rows = fetch_all_entries(creds)
    meta = fetch_meta(creds)
    print(f"fetched {len(rows)} rows, meta total={meta.get('total')}", flush=True)

    payload = assemble(rows, meta)

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    if args.pretty:
        out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    else:
        out_path.write_text(json.dumps(payload, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    size = out_path.stat().st_size
    print(f"wrote {out_path} ({size:,} bytes, {payload['meta']['total']} entries)", flush=True)


if __name__ == "__main__":
    main()
