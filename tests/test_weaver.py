from bluebird_sdk.weaver import Weaver

def test_parse_and_update():
    w = Weaver()
    test_input = "There’s fog again. I can’t see what I’m becoming."
    neuron = w.parse_entry(test_input)
    assert "trigger" in neuron
    assert isinstance(neuron["emotion_profile"], dict)
    assert "resonance_weight" in neuron

