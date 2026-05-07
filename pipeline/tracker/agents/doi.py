"""
Pilot beat-agent: Department of the Interior cluster (DOI, BIA, BLM, NPS,
ACHP, FWS). The noisiest beat, with the highest signal density per Prince's
2026-04-30 audit. Subclasses BeatAgent; Phase 1 only exercises the
augment loop. Real research logic comes in a follow-up pass.

To make this a real agent (Phase 2):
1. Wire `discover()` to RSS/Federal Register/regs.gov feeds for these agencies.
2. Wire `reconcile()` to dedup against existing entry IDs.
3. Replace the placeholder `augment()` with a Claude call that reads the
   entry's description_html plus the source document text and proposes
   structured fills for legal_authorities, personnel, dollar_impacts, etc.
"""
from .base import BeatAgent


class DOIBeatAgent(BeatAgent):
    agent_id = "doi-beat-v1"
    beat = "land-tribal"
    agency_filters = ["DOI", "BIA", "BLM", "NPS", "ACHP", "FWS"]
