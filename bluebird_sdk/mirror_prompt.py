# Mirror Prompt Generator

import random

PROMPTS = [
    "What part of you is hidden in this moment?",
    "What is the fog trying to teach you?",
    "Who are you becoming, despite the fear?",
    "Where does this pattern echo in your past?",
    "What archetype walks beside you right now?"
]

def generate_mirror_prompt(trigger: str = "") -> str:
    if trigger:
        return f"What is '{trigger}' asking you to see?"
    return random.choice(PROMPTS)

