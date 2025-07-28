import json
from datetime import datetime
from typing import Dict, Any
from .lattice import SymbolicLattice
from .llm_interface import extract_symbolic_data

class Weaver:
    def __init__(self, lattice_file: str = "symbolic_neurons.json"):
        self.lattice_file = lattice_file
        self.lattice = SymbolicLattice()
        self.load_lattice()

    def parse_entry(self, text: str) -> Dict[str, Any]:
        """
        Use an LLM to extract symbolic metadata from user input.
        """
        neuron = extract_symbolic_data(text)
        neuron["timestamp"] = datetime.utcnow().isoformat()
        if "resonance_weight" not in neuron:
            neuron["resonance_weight"] = 0.5
        return neuron

    def update_lattice(self, neuron_data: Dict[str, Any]):
        trigger = neuron_data["trigger"]
        if self.lattice.has_neuron(trigger):
            self.lattice.update_neuron(trigger, neuron_data)
        else:
            self.lattice.add_neuron(trigger, neuron_data)

    def save_lattice(self):
        self.lattice.save_to_file(self.lattice_file)

    def load_lattice(self):
        try:
            with open(self.lattice_file, 'r') as f:
                self.lattice.neurons = json.load(f)
        except FileNotFoundError:
            self.lattice.neurons = {}
