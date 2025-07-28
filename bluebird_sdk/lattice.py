
from typing import Dict, Any, List
import json

class SymbolicLattice:
    def __init__(self):
        self.neurons = {}

    def has_neuron(self, trigger: str) -> bool:
        return trigger in self.neurons

    def add_neuron(self, trigger: str, data: Dict[str, Any]):
        self.neurons[trigger] = data

    def update_neuron(self, trigger: str, data: Dict[str, Any]):
        for key, value in data.items():
            if key == "resonance_weight":
                self.neurons[trigger][key] = max(0.0, min(1.0,
                    self.neurons[trigger].get(key, 0.5) + value * 0.5))
            elif key == "timestamp":
                self.neurons[trigger][key] = value
            elif isinstance(value, list):
                current = set(self.neurons[trigger].get(key, []))
                current.update(value)
                self.neurons[trigger][key] = list(current)
            elif isinstance(value, dict):
                self.neurons[trigger][key] = {**self.neurons[trigger].get(key, {}), **value}
            else:
                self.neurons[trigger][key] = value

    def decay_resonance(self, rate: float = 0.05):
        for neuron in self.neurons.values():
            if "resonance_weight" in neuron:
                neuron["resonance_weight"] = max(0.0, neuron["resonance_weight"] - rate)

    def to_dict(self) -> Dict[str, Any]:
        return self.neurons

    def save_to_file(self, filepath: str):
        with open(filepath, 'w') as f:
            json.dump(self.neurons, f, indent=2)
