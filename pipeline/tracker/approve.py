"""
Quarantine reviewer CLI.

Usage:
    # List queue
    python -m pipeline.tracker.approve list
    python -m pipeline.tracker.approve list --beat land-tribal --risk low

    # Approve / reject one
    python -m pipeline.tracker.approve approve 42 --by prince --note "spot-checked"
    python -m pipeline.tracker.approve reject  43 --by prince --note "wrong agency"

    # Bulk auto-approve low-risk edits from a trusted agent (after the first month)
    python -m pipeline.tracker.approve bulk-approve --agent doi-beat-v1 --risk low --by auto-approver
"""
from __future__ import annotations

import argparse
import sys

from .sdk import client


def cmd_list(args):
    t = client()
    rows = t.list_pending(beat=args.beat, agent_id=args.agent, risk_class=args.risk, limit=args.limit)
    if not rows:
        print("queue empty")
        return
    print(f"{'id':>5}  {'risk':6}  {'beat':14}  {'agent':20}  {'fields':40}  rationale")
    print("-" * 120)
    for r in rows:
        fields = ",".join(r.get("field_set") or [])[:38]
        rationale = (r.get("rationale") or "")[:60]
        print(f"{r['id']:>5}  {r['risk_class']:6}  {(r.get('beat') or '-'):14}  "
              f"{r['agent_id']:20}  {fields:40}  {rationale}")


def cmd_approve(args):
    t = client()
    res = t.approve(args.id, resolved_by=args.by, note=args.note)
    print(res)


def cmd_reject(args):
    if not args.note:
        sys.stderr.write("--note required when rejecting\n")
        sys.exit(2)
    t = client()
    res = t.reject(args.id, resolved_by=args.by, note=args.note)
    print(res)


def cmd_bulk_approve(args):
    t = client()
    rows = t.list_pending(beat=args.beat, agent_id=args.agent, risk_class=args.risk, limit=args.limit)
    print(f"approving {len(rows)} edits as {args.by}")
    for r in rows:
        try:
            t.approve(r["id"], resolved_by=args.by, note="bulk-approved")
        except Exception as e:
            sys.stderr.write(f"failed on {r['id']}: {e}\n")
    print("done")


def main():
    p = argparse.ArgumentParser(description="TCKC quarantine reviewer")
    sub = p.add_subparsers(dest="cmd", required=True)

    pl = sub.add_parser("list")
    pl.add_argument("--beat")
    pl.add_argument("--agent")
    pl.add_argument("--risk", choices=["low", "medium", "high"])
    pl.add_argument("--limit", type=int, default=50)
    pl.set_defaults(func=cmd_list)

    pa = sub.add_parser("approve")
    pa.add_argument("id", type=int)
    pa.add_argument("--by", required=True)
    pa.add_argument("--note")
    pa.set_defaults(func=cmd_approve)

    pr = sub.add_parser("reject")
    pr.add_argument("id", type=int)
    pr.add_argument("--by", required=True)
    pr.add_argument("--note")
    pr.set_defaults(func=cmd_reject)

    pb = sub.add_parser("bulk-approve")
    pb.add_argument("--beat")
    pb.add_argument("--agent")
    pb.add_argument("--risk", choices=["low", "medium", "high"], default="low")
    pb.add_argument("--limit", type=int, default=200)
    pb.add_argument("--by", required=True)
    pb.set_defaults(func=cmd_bulk_approve)

    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
