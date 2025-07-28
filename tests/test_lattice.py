from bluebird_sdk.lattice import SymbolicLattice
import datetime

def test_add_and_update_neuron():
    lattice = SymbolicLattice()
    data = {
        "emotion_profile": {"confusion": 0.8},
        "meaning_seed": "searching",
        "archetypal_refs": ["Hermit"],
        "resonance_weight": 0.6,
        "timestamp": datetime.datetime.utcnow().isoformat()
    }
    lattice.add_neuron("fog", data)
    assert lattice.has_neuron("fog")
    updated = {"resonance_weight": 0.3, "archetypal_refs": ["Moon"]}
    lattice.update_neuron("fog", updated)
    assert "Moon" in lattice.neurons["fog"]["archetypal_refs"]

