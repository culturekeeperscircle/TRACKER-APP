"""
Insert-only sync from data.json into Supabase, intended for the daily
pipeline run. Existing rows are left untouched so manual Studio edits are
preserved.

Logic:
  1. Read data.json from disk.
  2. Convert every entry (including cross-refs) to a Postgres row.
  3. POST in batches with `Prefer: resolution=ignore-duplicates`.
     PostgREST silently skips rows whose primary key already exists.
  4. Refresh the singleton tracker_meta row.

Workflow position:
    git pull
    python -m pipeline.supabase.export        # bring data.json in line with Supabase
    python -m pipeline                         # ingest pipeline runs, appends new entries
    python -m pipeline.supabase.sync           # push only NEW entries to Supabase
    python -m pipeline.supabase.export         # regenerate data.json (canonical)
    git add ... && git commit && git push
"""
from .load import main as load_main


def main():
    """Thin wrapper around load.py's main with --insert-only."""
    import sys
    if "--insert-only" not in sys.argv:
        sys.argv.append("--insert-only")
    load_main()


if __name__ == "__main__":
    main()
