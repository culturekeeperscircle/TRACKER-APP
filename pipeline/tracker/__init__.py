"""TCKC tracker SDK for beat-agents and ad-hoc edits.

Public surface:
    from pipeline.tracker import client
    t = client()
    hits = t.search(agency="DOI", since="2025-01-20", min_severity="HARMFUL")
    t.propose_augment(entry_id="eo-14154", fields={...}, rationale="...", risk="low")
    t.propose_new_entry(data={...}, rationale="...")
    t.record_gap_report(agent_id="doi-beat", beat="land-tribal", window=(start, end), ...)
"""
from .sdk import Tracker, client

__all__ = ["Tracker", "client"]
