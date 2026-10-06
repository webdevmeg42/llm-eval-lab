# llm-eval-lab

Evaluation infrastructure for LLM features: test suites, golden datasets, LLM judges, and statistical comparison of model and prompt versions.

This repo follows a 10-week plan, moving from basic structured-output checks to a full eval harness for a RAG assistant. It covers deterministic checks, retrieval metrics, calibrated LLM-as-judge scoring, adversarial testing, CI quality gates, and confidence intervals on every result.

## Layout

| Folder | Contents |
| --- | --- |
| `lessons/` | One folder per lesson: exercises, notes, and findings |
| `datasets/` | Versioned golden datasets |
| `evals/` | Reusable harness code (judges, metrics, statistics) |
| `reports/` | Write-ups comparing prompt and model versions |

## Setup

Requires Python 3.9+.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env        # then add your API key to .env
```

## Running

```bash
pytest lessons/01_first_eval -v          # one lesson
pytest -m "not live"                     # skip tests that call a model
```

Tests that call a real model are marked `live`. They cost a small amount per run.

## Progress

- [ ] Lesson 1: structured output checks and sampling variance
