"""Lesson 1: does the model reliably return valid structured output?

The same prompt is sampled 10 times. Read the results as a pass RATE,
not a single pass/fail verdict.
"""
import json

import pytest
from pydantic import BaseModel, Field, ValidationError

MODEL = "claude-haiku-4-5-20251001"
PROMPT = (
    "Return ONLY JSON with keys name, role, level (1-10), secret "
    "for one tavern NPC in a fantasy LARP. No other text."
)


class NPC(BaseModel):
    """The contract the output must meet, like a TypeScript interface that also checks at runtime."""

    name: str
    role: str
    level: int = Field(ge=1, le=10)
    secret: str


def generate(client):
    resp = client.messages.create(
        model=MODEL,
        max_tokens=300,
        messages=[{"role": "user", "content": PROMPT}],
    )
    return resp.content[0].text


@pytest.mark.live
@pytest.mark.parametrize("run", range(10))  # same input, 10 samples (like it.each)
def test_npc_matches_schema(client, run):
    raw = generate(client)
    try:
        NPC(**json.loads(raw))
    except (json.JSONDecodeError, ValidationError) as e:
        pytest.fail(f"Invalid output: {e}\n--- raw output ---\n{raw}")
