import json
from collections import Counter

import anthropic
from dotenv import load_dotenv

load_dotenv()

MODEL = "claude-haiku-4-5-20251001"
PROMPT = (
    "Return ONLY JSON with keys name, role, level (1-10), secret "
    "for one tavern NPC in a fantasy LARP. No other text."
)
SAMPLES = 20

client = anthropic.Anthropic()


def remove_code_fences(text: str) -> str:
    # TODO: add counter for how many times we need to strip the backticks
    """Filters out any lines that contain a triple-backtick markdown fence.  This hides the format failure"""
    lines = text.splitlines()
    # Keep lines that do not start with the ``` code fence
    filtered_lines = [line for line in lines if not line.strip().startswith("```")]
    return "\n".join(filtered_lines).strip()


def sample_names(temperature):
    """Call the model SAMPLES times at this temperature; return the NPC names."""
    names = []
    for _ in range(SAMPLES):
        response = client.messages.create(model=MODEL,max_tokens=300,messages=[{"role": "user", "content": PROMPT}],extra_body={"temperature": temperature})
        response_text = response.content[0].text
        response_no_fence = remove_code_fences(response_text)
        try:
            response_json = json.loads(response_no_fence)
            name_value = response_json["name"]
            names.append(name_value)
        except (json.JSONDecodeError, KeyError) as e:
            names.append("<invalid>")
            print(f"Name parsed as 'invalid'.  ERROR: {e}")
    return names


def report(temperature, names):
    counts = Counter(names)
    print(f"\ntemperature={temperature}: {len(counts)} distinct names in {len(names)} samples")
    top_5_names = counts.most_common(5)
    for name, count in top_5_names:
        print(f"{name}: {count}")


if __name__ == "__main__":
    for t in (0.0, 1.0):
        report(t, sample_names(t))
