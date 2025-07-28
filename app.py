
import streamlit as st
from bluebird_sdk.weaver import Weaver

st.set_page_config(page_title="Bluebird Symbolic Memory", layout="wide")

st.title("🧠 Bluebird Symbolic Memory Lattice")

# Initialize the Weaver
weaver = Weaver("symbolic_neurons.json")

# User journal entry input
st.header("📜 Enter a Journal Entry")
entry = st.text_area("Reflect below. Your words shape the lattice.")

if st.button("Reflect and Update Lattice"):
    neuron = weaver.parse_entry(entry)
    weaver.update_lattice(neuron)
    weaver.save_lattice()
    st.success(f"Symbolic Neuron '{neuron['trigger']}' updated in the Lattice.")

# Display current state of the symbolic lattice
st.header("🌐 Symbolic Lattice Overview")
lattice_dict = weaver.lattice.to_dict()

if lattice_dict:
    for trigger, data in lattice_dict.items():
        with st.expander(f"🔹 {trigger}"):
            st.json(data)
else:
    st.info("No symbolic neurons yet. Add a journal entry to begin.")
