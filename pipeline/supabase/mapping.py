"""
Bidirectional mapping between data.json entry shape and the Postgres schema.

Source of truth for what each JSON key means. Used by both the loader (to
transform JSON -> rows) and the exporter (to transform rows -> JSON). Keep
this single-file so additions stay in sync.
"""
import re
from datetime import datetime

CATEGORIES = [
    "executive_actions",
    "agency_actions",
    "legislation",
    "litigation",
    "other_domestic",
    "international",
]

SEVERITY_VALUES = {"SEVERE", "HARMFUL", "PROTECTIVE", "WATCH"}

# Keys that map to dedicated columns. Anything outside this set lands in `extras`.
MAPPED_JSON_KEYS = {
    "i", "id",                         # primary key (id_field_name remembers which one)
    "t", "T", "n", "s", "d", "a",      # type, title, name, summary, date, administration
    "A", "S", "L", "D",                # agencies, status, severity, description
    "I", "c", "U",                     # community impacts, communities, source URL
    "_source",                          # source tag
    "_isRef", "_primaryRef",           # cross-ref flags
    "_relatedActions", "_derivedFrom", # graph edges
    "keyQuotes", "agencyMandates", "impactByCommunity",
    "_crossRef",
    "muted", "_mutedReason", "_mutedDate",
    "_isAggregate",
}


def normalize_date(s):
    if not s or not isinstance(s, str):
        return None
    s = s.strip()
    if re.match(r"^\d{4}-\d{2}-\d{2}$", s):
        try:
            datetime.strptime(s, "%Y-%m-%d")
            return s
        except ValueError:
            return None
    if re.match(r"^\d{4}-\d{2}$", s):
        return s + "-01"
    if re.match(r"^\d{4}$", s):
        return s + "-01-01"
    return None


def normalize_severity(s):
    if not s:
        return None
    up = s.strip().upper()
    return up if up in SEVERITY_VALUES else None


def entry_to_row(entry, category):
    """Convert a data.json entry dict to a Postgres-shaped row dict."""
    if "id" in entry and "i" not in entry:
        eid = entry["id"]
        id_field = "id"
    else:
        eid = entry.get("i")
        id_field = "i"
    if not eid:
        return None

    agencies = entry.get("A") or []
    if not isinstance(agencies, list):
        agencies = [str(agencies)]
    agencies = [str(a) for a in agencies if a is not None]

    communities = entry.get("c") or []
    if not isinstance(communities, list):
        communities = [str(communities)]

    related = entry.get("_relatedActions") or []
    derived = entry.get("_derivedFrom") or []

    extras = {k: v for k, v in entry.items() if k not in MAPPED_JSON_KEYS}

    return {
        "id": eid,
        "id_field_name": id_field,
        "category": category,
        "entry_type": entry.get("t"),
        "official_name": entry.get("n"),
        "title_html": entry.get("T"),
        "summary": entry.get("s"),
        "action_date": normalize_date(entry.get("d")),
        "administration": entry.get("a"),
        "agencies": agencies,
        "status_text": entry.get("S"),
        "severity": normalize_severity(entry.get("L")),
        "description_html": entry.get("D"),
        "community_impacts": entry.get("I"),
        "communities": [str(c) for c in communities],
        "source_url": entry.get("U"),
        "source_tag": entry.get("_source"),
        "is_cross_ref": bool(entry.get("_isRef")),
        "primary_ref_id": entry.get("_primaryRef"),
        "related_action_ids": list(related) if isinstance(related, list) else [],
        "derived_from_ids": list(derived) if isinstance(derived, list) else [],
        "key_quotes": entry.get("keyQuotes"),
        "agency_mandates": entry.get("agencyMandates"),
        "impact_by_community": entry.get("impactByCommunity"),
        "cross_ref_payload": entry.get("_crossRef"),
        "is_muted": bool(entry.get("muted", False)),
        "mute_reason": entry.get("_mutedReason"),
        "mute_date": normalize_date(entry.get("_mutedDate")),
        "is_aggregate": bool(entry.get("_isAggregate", False)),
        "extras": extras if extras else None,
        "crossrefs_into": [],  # filled separately when reading data.json (legacy denorm)
    }


def row_to_entry(row):
    """Convert a Postgres row (dict) back to a data.json entry dict."""
    out = {}
    id_key = row.get("id_field_name") or "i"
    out[id_key] = row["id"]

    if row.get("entry_type") is not None:        out["t"] = row["entry_type"]
    if row.get("title_html") is not None:        out["T"] = row["title_html"]
    if row.get("official_name") is not None:     out["n"] = row["official_name"]
    if row.get("summary") is not None:           out["s"] = row["summary"]
    if row.get("action_date") is not None:       out["d"] = str(row["action_date"])
    if row.get("administration") is not None:    out["a"] = row["administration"]
    if row.get("agencies"):                       out["A"] = list(row["agencies"])
    if row.get("status_text") is not None:       out["S"] = row["status_text"]
    if row.get("severity") is not None:          out["L"] = row["severity"]
    if row.get("description_html") is not None:  out["D"] = row["description_html"]
    if row.get("community_impacts") is not None: out["I"] = row["community_impacts"]
    if row.get("communities"):                    out["c"] = list(row["communities"])
    if row.get("source_url") is not None:        out["U"] = row["source_url"]
    if row.get("source_tag") is not None:        out["_source"] = row["source_tag"]
    if row.get("is_cross_ref"):                   out["_isRef"] = True
    if row.get("primary_ref_id") is not None:    out["_primaryRef"] = row["primary_ref_id"]
    if row.get("related_action_ids"):             out["_relatedActions"] = list(row["related_action_ids"])
    if row.get("derived_from_ids"):               out["_derivedFrom"] = list(row["derived_from_ids"])
    if row.get("key_quotes") is not None:        out["keyQuotes"] = row["key_quotes"]
    if row.get("agency_mandates") is not None:   out["agencyMandates"] = row["agency_mandates"]
    if row.get("impact_by_community") is not None: out["impactByCommunity"] = row["impact_by_community"]
    if row.get("cross_ref_payload") is not None: out["_crossRef"] = row["cross_ref_payload"]
    if row.get("is_muted"):                       out["muted"] = True
    if row.get("mute_reason") is not None:       out["_mutedReason"] = row["mute_reason"]
    if row.get("mute_date") is not None:         out["_mutedDate"] = str(row["mute_date"])
    if row.get("is_aggregate"):                   out["_isAggregate"] = True

    extras = row.get("extras") or {}
    for k, v in extras.items():
        out[k] = v
    return out
