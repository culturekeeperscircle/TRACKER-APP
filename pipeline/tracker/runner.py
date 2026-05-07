"""
Beat-agent runner.

Usage:
    python -m pipeline.tracker.runner --beat doi
    python -m pipeline.tracker.runner --beat doi --since 2026-04-30 --until 2026-05-07
    python -m pipeline.tracker.runner --beat ALL    # every registered beat in turn

Designed for Render's cron jobs. One beat per run.
"""
from __future__ import annotations

import argparse
import logging
import sys
from datetime import date, timedelta

from .agents import REGISTRY
from .sdk import client

logger = logging.getLogger("tckc.runner")


def parse_args():
    p = argparse.ArgumentParser(description="TCKC beat-agent runner")
    p.add_argument("--beat", required=True, help="beat name from agents.REGISTRY, or ALL")
    p.add_argument("--since", help="window start date (YYYY-MM-DD); default 7 days ago")
    p.add_argument("--until", help="window end date (YYYY-MM-DD); default today")
    p.add_argument("--cap", type=int, default=50, help="max augmentations per beat per run")
    p.add_argument("--dry-run", action="store_true", help="construct agents but do not run")
    return p.parse_args()


def main():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")
    args = parse_args()

    today = date.today()
    window_end = date.fromisoformat(args.until) if args.until else today
    window_start = date.fromisoformat(args.since) if args.since else (window_end - timedelta(days=7))

    if args.beat == "ALL":
        beats = list(REGISTRY.keys())
    elif args.beat in REGISTRY:
        beats = [args.beat]
    else:
        sys.stderr.write(f"unknown beat {args.beat!r}; available: {sorted(REGISTRY)}\n")
        sys.exit(2)

    tracker = client()
    for name in beats:
        agent_cls = REGISTRY[name]
        agent = agent_cls(tracker, augmentation_cap=args.cap)
        if args.dry_run:
            logger.info(f"[dry-run] would run {agent.agent_id} for {window_start}..{window_end}")
            continue
        agent.run(window_start, window_end)


if __name__ == "__main__":
    main()
