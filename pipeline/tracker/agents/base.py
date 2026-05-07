"""
BeatAgent contract.

A beat-agent owns a slice of the federal landscape and runs on a schedule.
Each run does four things:

1. Discover  : pull source feeds for the beat in the date window.
2. Reconcile : diff against existing tracker entries, identify gaps.
3. Augment   : for existing entries, fill granular legal/policy fields.
4. Report    : record a gap_report with cost + counts + review queue notes.

Every write goes through `tracker.propose_augment` or `propose_new_entry`,
landing in `pending_edits`. The reviewer (humans during the first month,
auto-approver afterward for low-risk fields) is the only path to `entries`.

Augmentation cap: 50 proposals per beat per week per Prince's directive.
Subclasses should respect MAX_AUGMENTATIONS_PER_RUN.
"""
from __future__ import annotations

import logging
from dataclasses import dataclass, field
from datetime import date, timedelta
from typing import Optional

from ..sdk import Tracker

logger = logging.getLogger("tckc.beat")

MAX_AUGMENTATIONS_PER_RUN = 50


@dataclass
class BeatRunResult:
    agent_id: str
    beat: str
    window_start: date
    window_end: date
    augmented_count: int = 0
    proposed_count: int = 0
    gap_candidates: list = field(default_factory=list)
    needs_review: list = field(default_factory=list)
    notes: str = ""
    cost_usd: float = 0.0


class BeatAgent:
    """Base class. Subclasses set `agent_id`, `beat`, `agency_filters`."""

    agent_id: str = "base-beat"
    beat: str = "unspecified"
    agency_filters: list[str] = []

    def __init__(self, tracker: Tracker, *, augmentation_cap: int = MAX_AUGMENTATIONS_PER_RUN):
        self.t = tracker
        self.cap = augmentation_cap

    # ---- Lifecycle methods. Subclasses override augment(); discover/reconcile are
    #      optional in Phase 1 (sources are stubbed) and become real in Phase 3.

    def discover(self, window_start: date, window_end: date) -> list[dict]:
        """Pull source-feed candidates for the beat. Stub in Phase 1."""
        logger.info(f"[{self.agent_id}] discover stub: 0 candidates")
        return []

    def reconcile(self, candidates: list[dict]) -> list[dict]:
        """Return candidates not yet in the tracker. Stub in Phase 1."""
        return []

    def augment(self, window_start: date, window_end: date, result: BeatRunResult) -> None:
        """
        Phase 1 default: pick existing shallow entries in the agent's agency
        scope and submit a placeholder augmentation proposal so the workflow
        is exercised end-to-end. Real per-beat research lives in subclasses.
        """
        hits = self.t.search(
            agency=self.agency_filters[0] if self.agency_filters else None,
            since=window_start.isoformat(),
            until=window_end.isoformat(),
            research_depth="shallow",
            limit=self.cap,
        )
        logger.info(f"[{self.agent_id}] augment scope: {len(hits)} shallow hits")
        for hit in hits[: self.cap]:
            receipt = self.t.propose_augment(
                entry_id=hit.id,
                fields={
                    "deep_research_notes": (
                        f"Auto-flagged for deep research by {self.agent_id} "
                        f"on {date.today().isoformat()}."
                    ),
                },
                rationale="Phase 1 scaffold: marking entry as a deep-research candidate.",
                agent_id=self.agent_id,
                beat=self.beat,
                risk="low",
            )
            result.proposed_count += 1
            logger.debug(f"[{self.agent_id}] proposed edit #{receipt.pending_edit_id} on {hit.id}")

    # ---- Orchestration ----

    def run(self, window_start: date, window_end: date) -> BeatRunResult:
        result = BeatRunResult(
            agent_id=self.agent_id,
            beat=self.beat,
            window_start=window_start,
            window_end=window_end,
        )
        candidates = self.discover(window_start, window_end)
        gaps = self.reconcile(candidates)
        result.gap_candidates = gaps
        self.augment(window_start, window_end, result)
        # Record the run.
        self.t.record_gap_report(
            agent_id=self.agent_id,
            beat=self.beat,
            window_start=window_start.isoformat(),
            window_end=window_end.isoformat(),
            augmented_count=result.augmented_count,
            proposed_count=result.proposed_count,
            gap_candidates=result.gap_candidates,
            needs_review=result.needs_review,
            notes=result.notes,
            cost_usd=result.cost_usd,
        )
        logger.info(
            f"[{self.agent_id}] done: proposed={result.proposed_count} "
            f"gaps={len(result.gap_candidates)} cost=${result.cost_usd:.2f}"
        )
        return result
