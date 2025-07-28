from bluebird_sdk.weaver import Weaver
from bluebird_sdk.mirror_prompt import generate_mirror_prompt

# Initialize the symbolic mind
weaver = Weaver("symbolic_neurons.json")

# Sample journal input
entry = "I feel the weight of judgment again, like Saturn’s silence pressing on my chest."

# Parse and update
neuron = weaver.parse_entry(entry)
weaver.update_lattice(neuron)
weaver.save_lattice()

# Reflect
print("🧠 Neuron Added:", neuron["trigger"])
print("🔮 Archetypes:", neuron["archetypal_refs"])
print("🪞 Mirror Prompt:", generate_mirror_prompt(neuron["trigger"]))

