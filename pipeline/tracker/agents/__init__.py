"""Beat-agent registry. Add a new agent by importing it here."""
from .base import BeatAgent, BeatRunResult
from .doi import DOIBeatAgent

REGISTRY: dict[str, type[BeatAgent]] = {
    "doi": DOIBeatAgent,
    # future: dhs, doj, smithsonian, ed, hhs, epa, dos, dod, omb, courts, ...
}

__all__ = ["BeatAgent", "BeatRunResult", "REGISTRY"]
