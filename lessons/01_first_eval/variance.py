"""Lesson 1 variance experiment: how much does temperature change the output?

Finish the TODOs, then run:  python lessons/01_first_eval/variance.py
"""
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


def sample_names(temperature):
    """Call the model SAMPLES times at this temperature; return the NPC names."""
    names = []
    for _ in range(SAMPLES):
        # TODO 1: call client.messages.create(...) with MODEL, PROMPT, max_tokens,
        #         and this temperature. (test_npc_schema.py has a working call.)
        # TODO 2: parse the JSON text and append the "name" field to `names`.
        #         If parsing fails, append "<invalid>" instead of crashing.
        pass
    return names


def report(temperature, names):
    counts = Counter(names)
    print(f"\ntemperature={temperature}: {len(counts)} distinct names in {len(names)} samples")
    # TODO 3: print the 5 most common names with their counts.
    #         Hint: Counter has a method for exactly this.


if __name__ == "__main__":
    for t in (0.0, 1.0):
        report(t, sample_names(t))
