"""Shared pytest setup. Loads .env so ANTHROPIC_API_KEY is available to every test."""
import os

import pytest
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture(scope="session")
def client():
    """One Anthropic client shared across the whole test run.

    Works like a Cypress `before()` hook: created once and passed to any test
    that takes `client` as an argument.
    """
    if not os.getenv("ANTHROPIC_API_KEY"):
        pytest.skip("ANTHROPIC_API_KEY not set (see .env.example)")
    import anthropic

    return anthropic.Anthropic()
