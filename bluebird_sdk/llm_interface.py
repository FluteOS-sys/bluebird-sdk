import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def extract_symbolic_data(entry: str) -> dict:
    prompt = (
        "Parse the following journal entry into symbolic memory components:\n\n"
        f"{entry}\n\n"
        "Return JSON with keys:\n"
        "- trigger (str)\n"
        "- emotion_profile (dict[str → float])\n"
        "- meaning_seed (str)\n"
        "- archetypal_refs (list[str])"
    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return eval(response.choices[0].message["content"])
    except Exception as e:
        print("LLM extract_symbolic_data error:", e)
        return {
            "trigger": "unknown",
            "emotion_profile": {},
            "meaning_seed": "unsure",
            "archetypal_refs": []
        }
