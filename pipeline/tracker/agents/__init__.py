"""Beat-agent registry. Add a new agent by importing it here."""
from .base import BeatAgent, BeatRunResult
from .doi import DOIBeatAgent
from .immigration import ImmigrationBeatAgent

REGISTRY: dict[str, type[BeatAgent]] = {
    "doi":         DOIBeatAgent,
    "immigration": ImmigrationBeatAgent,
    # future: civil-rights, cultural-institutions, environment, courts,
    #         language-access, voting-rights, religious-liberty, ...
}

__all__ = ["BeatAgent", "BeatRunResult", "REGISTRY"]
