"""
Tracker SDK. One stable surface for beat-agents and ad-hoc scripts.

All writes go through `pending_edits` so the quarantine workflow stays in
control. The reviewer (humans, or an auto-approver job for low-risk fields)
applies approved edits to `entries`.
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from datetime import date
from typing import Any, Iterable, Optional

import requests

from ..supabase.client import get_credentials

SEVERITY_RANK = {"WATCH": 0, "PROTECTIVE": 1, "HARMFUL": 2, "SEVERE": 3}

# Fields where agent edits are considered low risk and can be auto-approved
# after the first month of human review. Fields outside this set always stay
# in quarantine pending explicit approval.
LOW_RISK_FIELDS = {
    "legal_authorities",
    "affected_programs",
    "personnel",
    "dollar_impacts",
    "procedural_status",
    "cited_quotes",
    "source_documents",
    "explicit_related_ids",
    "deep_research_notes",
    "last_deep_researched_at",
    "research_depth",
}

HIGH_RISK_FIELDS = {
    "severity",
    "category",
    "title_html",
    "description_html",
    "is_muted",
    "muted",
}


def _classify_risk(field_set: Iterable[str]) -> str:
    fs = set(field_set)
    if fs & HIGH_RISK_FIELDS:
        return "high"
    if fs - LOW_RISK_FIELDS:
        return "medium"
    return "low"


@dataclass
class SearchHit:
    id: str
    category: str
    severity: Optional[str]
    action_date: Optional[str]
    official_name: Optional[str]
    summary: Optional[str]
    agencies: list[str]
    research_depth: str
    raw: dict = field(default_factory=dict)


@dataclass
class ProposalReceipt:
    pending_edit_id: int
    risk_class: str


class Tracker:
    """Thin wrapper around the Supabase REST API."""

    def __init__(self, creds: dict):
        self.creds = creds

    def _get(self, path: str, **params) -> Any:
        r = requests.get(f"{self.creds['base_url']}/{path}", headers=self.creds["headers"], params=params, timeout=60)
        r.raise_for_status()
        return r.json()

    def _post(self, path: str, body: Any, prefer: str = "return=representation") -> Any:
        headers = {**self.creds["headers"], "Prefer": prefer}
        r = requests.post(f"{self.creds['base_url']}/{path}", headers=headers, data=json.dumps(body), timeout=60)
        r.raise_for_status()
        return r.json() if r.text else None

    def _patch(self, path: str, body: Any, prefer: str = "return=representation") -> Any:
        headers = {**self.creds["headers"], "Prefer": prefer}
        r = requests.patch(f"{self.creds['base_url']}/{path}", headers=headers, data=json.dumps(body), timeout=60)
        r.raise_for_status()
        return r.json() if r.text else None

    # ---- Read ----

    def search(
        self,
        agency: Optional[str] = None,
        category: Optional[str] = None,
        since: Optional[str] = None,                  # YYYY-MM-DD
        until: Optional[str] = None,
        min_severity: Optional[str] = None,
        research_depth: Optional[str] = None,         # 'shallow' | 'deep' | 'expert'
        community: Optional[str] = None,
        text_match: Optional[str] = None,
        limit: int = 100,
    ) -> list[SearchHit]:
        params: dict[str, str] = {"select": "*", "limit": str(limit)}
        if agency:
            params["agencies"] = f"cs.{{{agency}}}"
        if category:
            params["category"] = f"eq.{category}"
        if since:
            params["action_date"] = f"gte.{since}"
        if until:
            existing = params.get("action_date", "")
            params["action_date"] = f"{existing},lte.{until}" if existing else f"lte.{until}"
        if research_depth:
            params["research_depth"] = f"eq.{research_depth}"
        if community:
            params["communities"] = f"cs.{{{community}}}"
        if text_match:
            # Postgres full-text. The `description_html` is the bulk of the searchable text.
            params["description_html"] = f"plfts.{text_match}"

        rows = self._get("entries", **params)

        # Severity post-filter: PostgREST cannot easily filter on the enum's ordinal,
        # so we filter client-side.
        if min_severity:
            threshold = SEVERITY_RANK.get(min_severity.upper(), 0)
            rows = [r for r in rows if SEVERITY_RANK.get((r.get("severity") or "WATCH").upper(), 0) >= threshold]

        return [
            SearchHit(
                id=r["id"],
                category=r["category"],
                severity=r.get("severity"),
                action_date=r.get("action_date"),
                official_name=r.get("official_name"),
                summary=r.get("summary"),
                agencies=r.get("agencies") or [],
                research_depth=r.get("research_depth") or "shallow",
                raw=r,
            )
            for r in rows
        ]

    def get(self, entry_id: str) -> Optional[dict]:
        rows = self._get("entries", select="*", id=f"eq.{entry_id}")
        return rows[0] if rows else None

    # ---- Write (proposals only) ----

    def propose_augment(
        self,
        entry_id: str,
        fields: dict,
        rationale: str,
        agent_id: str,
        beat: Optional[str] = None,
        risk: Optional[str] = None,    # auto-classified if not given
    ) -> ProposalReceipt:
        risk = risk or _classify_risk(fields.keys())
        body = [{
            "entry_id": entry_id,
            "is_new_entry": False,
            "proposed_data": fields,
            "field_set": list(fields.keys()),
            "agent_id": agent_id,
            "beat": beat,
            "rationale": rationale,
            "risk_class": risk,
        }]
        result = self._post("pending_edits", body)
        return ProposalReceipt(pending_edit_id=result[0]["id"], risk_class=risk)

    def propose_new_entry(
        self,
        data: dict,
        rationale: str,
        agent_id: str,
        beat: Optional[str] = None,
    ) -> ProposalReceipt:
        # New entries always start at high risk.
        body = [{
            "entry_id": None,
            "is_new_entry": True,
            "proposed_data": data,
            "field_set": list(data.keys()),
            "agent_id": agent_id,
            "beat": beat,
            "rationale": rationale,
            "risk_class": "high",
        }]
        result = self._post("pending_edits", body)
        return ProposalReceipt(pending_edit_id=result[0]["id"], risk_class="high")

    # ---- Reviewer surface (humans or auto-approver) ----

    def list_pending(
        self,
        beat: Optional[str] = None,
        agent_id: Optional[str] = None,
        risk_class: Optional[str] = None,
        limit: int = 200,
    ) -> list[dict]:
        params: dict[str, str] = {
            "select": "*",
            "status": "eq.pending",
            "limit": str(limit),
            "order": "created_at.asc",
        }
        if beat:
            params["beat"] = f"eq.{beat}"
        if agent_id:
            params["agent_id"] = f"eq.{agent_id}"
        if risk_class:
            params["risk_class"] = f"eq.{risk_class}"
        return self._get("pending_edits", **params)

    def approve(self, pending_edit_id: int, resolved_by: str, note: Optional[str] = None) -> dict:
        # Fetch the pending row.
        rows = self._get("pending_edits", select="*", id=f"eq.{pending_edit_id}")
        if not rows:
            raise ValueError(f"pending_edit {pending_edit_id} not found")
        row = rows[0]
        if row["status"] != "pending":
            raise ValueError(f"pending_edit {pending_edit_id} is {row['status']}, not pending")

        if row["is_new_entry"]:
            self._post("entries", [row["proposed_data"]], prefer="resolution=merge-duplicates,return=minimal")
        else:
            self._patch(f"entries?id=eq.{row['entry_id']}", row["proposed_data"], prefer="return=minimal")

        self._patch(
            f"pending_edits?id=eq.{pending_edit_id}",
            {
                "status": "approved",
                "resolved_at": "now()",
                "resolved_by": resolved_by,
                "resolved_note": note,
            },
        )
        return {"id": pending_edit_id, "status": "approved"}

    def reject(self, pending_edit_id: int, resolved_by: str, note: str) -> dict:
        self._patch(
            f"pending_edits?id=eq.{pending_edit_id}",
            {
                "status": "rejected",
                "resolved_at": "now()",
                "resolved_by": resolved_by,
                "resolved_note": note,
            },
        )
        return {"id": pending_edit_id, "status": "rejected"}

    # ---- Reporting ----

    def record_gap_report(
        self,
        agent_id: str,
        beat: str,
        window_start: str,
        window_end: str,
        augmented_count: int = 0,
        proposed_count: int = 0,
        gap_candidates: Optional[list] = None,
        needs_review: Optional[list] = None,
        notes: Optional[str] = None,
        cost_usd: Optional[float] = None,
    ) -> int:
        body = [{
            "agent_id": agent_id,
            "beat": beat,
            "window_start": window_start,
            "window_end": window_end,
            "augmented_count": augmented_count,
            "proposed_count": proposed_count,
            "gap_candidates": gap_candidates,
            "needs_review": needs_review,
            "notes": notes,
            "cost_usd": cost_usd,
        }]
        result = self._post("gap_reports", body)
        return result[0]["id"]


def client() -> Tracker:
    """Construct a Tracker from environment credentials (service role preferred)."""
    return Tracker(get_credentials())
