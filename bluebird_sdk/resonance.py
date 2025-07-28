from typing import Dict
from datetime import datetime, timedelta

class ResonanceEngine:
    def __init__(self, decay_rate: float = 0.01, amplify_scale: float = 0.1):
        """
        Initialize the Resonance Engine.
        :param decay_rate: Daily decay rate of resonance weight.
        :param amplify_scale: How much emotional intensity boosts resonance.
        """
        self.decay_rate = decay_rate
        self.amplify_scale = amplify_scale

    def amplify(self, current_weight: float, emotional_intensity: float) -> float:
        """
        Amplify resonance based on emotional intensity.
        """
        amplified = current_weight + emotional_intensity * self.amplify_scale
        return min(1.0, max(0.0, amplified))

    def decay(self, current_weight: float, days_passed: int) -> float:
        """
        Apply time-based decay to resonance.
        """
        decayed = current_weight - (self.decay_rate * days_passed)
        return max(0.0, decayed)

    def score_emotional_profile(self, profile: Dict[str, float]) -> float:
        """
        Aggregate emotional profile into a single intensity score.
        """
        if not profile:
            return 0.0
        return sum(profile.values()) / len(profile)

    def update_resonance(self, current_weight: float, profile: Dict[str, float], last_update: str) -> float:
        """
        Compute new resonance based on time passed and emotional profile.
        """
        intensity = self.score_emotional_profile(profile)
        days = self._days_since(last_update)
        decayed = self.decay(current_weight, days)
        return self.amplify(decayed, intensity)

    def _days_since(self, timestamp: str) -> int:
        """
        Helper to calculate days since last update.
        """
        try:
            past = datetime.fromisoformat(timestamp)
            delta = datetime.utcnow() - past
            return max(0, delta.days)
        except Exception:
            return 0

