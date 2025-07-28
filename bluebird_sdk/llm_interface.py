from openai import OpenAI

def extract_symbolic_data(entry: str) -> dict:
    prompt = f"Extract trigger, emotion profile (dict), meaning seed, and archetypal refs from: {entry}"
    response = OpenAI().chat.create(model="gpt-4", messages=[{"role": "user", "content": prompt}])
    return response.json()
