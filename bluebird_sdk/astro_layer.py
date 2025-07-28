# Astro Layer - basic symbolic hooks for planetary archetypes

from typing import List

PLANET_ARCHETYPES = {
    "Saturn": ["Shadow", "Judgment", "Discipline"],
    "Moon": ["Emotion", "Cycle", "Uncertainty"],
    "Mercury": ["Mind", "Communication", "Duality"],
    "Venus": ["Love", "Attraction", "Harmony"],
    "Mars": ["Drive", "Anger", "Courage"]
}

class AstroLayer:
    def __init__(self, active_transits: List[str]):
        self.transits = active_transits

    def modulate_archetypes(self, active_archetypes: List[str]) -> List[str]:
        modulated = list(active_archetypes)
        for planet in self.transits:
            if planet in PLANET_ARCHETYPES:
                modulated.extend(PLANET_ARCHETYPES[planet])
        return list(set(modulated))

