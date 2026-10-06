# Learning plan context

Megan is an SDET (4+ years: JavaScript, Cypress, Playwright, Selenium, some Go) moving into AI evaluation roles: AI Evaluation Engineer, AI Quality Engineer, Evaluation Infrastructure Engineer, Model Evaluation Engineer, LLM QA Engineer. She is applying but not getting interviews, and this repo is the portfolio proof for that move.

## Where she stands

- **Transferable:** regression suites, baselines, CI quality gates, `cy.intercept()` mocking, k6/ghz/chaos testing, PostgreSQL in production, test case design.
- **Already done:** validated LLM-generated reports for hallucinations and format conformance. That is eval experience.
- **Gaps:** Python; evaluating open-ended output; eval platforms (LangSmith, Langfuse); eval frameworks (RAGAS, DeepEval, promptfoo); statistics for eval (significance tests, confidence intervals); RAG and agent evaluation.

## 10-week plan (8–10 hrs/week)

| Weeks | Topic | Outcome |
| --- | --- | --- |
| 1–2 | Python for testers (pytest, fixtures, parametrize, pydantic, pandas); model API basics (temperature, max_tokens, system prompt, structured output, tokens and cost); sampling variance | pytest file that calls a model and asserts on structured output |
| 3 | Eval method ladder: code checks first, then reference-based (exact match, F1, embedding similarity; why BLEU/ROUGE are weak), then LLM-as-judge (binary, rubric, pairwise, G-Eval); promptfoo | promptfoo suite with all three kinds of assertion |
| 4 | RAG eval: retrieval vs generation; recall@k, precision@k, MRR, nDCG; RAGAS faithfulness, answer relevancy, context precision/recall | RAGAS run she can explain row by row |
| 5 | Trustworthy judges: hand-label 50 outputs, Cohen's kappa vs judge; position/verbosity/self-preference bias and fixes; DeepEval with a custom GEval metric | "Judge agrees with me at kappa X" write-up |
| 6 | Langfuse (self-hosted) and LangSmith: tracing, datasets, experiments; offline vs online evals. **Start applying.** | Capstone traces in Langfuse with scores |
| 7 | Statistics: run-to-run variance, bootstrap confidence intervals, McNemar / Wilcoxon / paired t-test, sample size and power, multiple comparisons | Two-prompt comparison report with intervals and a ship/no-ship verdict |
| 8 | Agents (outcome + trajectory eval, mocked tools); red teaming (prompt injection, jailbreaks, PII leakage); Inspect | Adversarial test set in the capstone |
| 9–10 | Capstone README, walkthrough video or blog post, mock interviews | Portfolio link at the top of her resume |

## Capstone

A rules and lore Q&A assistant over her LARP content (Hellion's Vale), built in her separate Node app Plotrunner. This repo tests it through its API. Planned components: golden dataset of 60–100 tagged questions; deterministic checks; retrieval metrics; RAGAS/DeepEval generation metrics; a binary judge calibrated with Cohen's kappa; adversarial set (injection in lore text, made-up rules, extracting GM-only secrets); GitHub Actions gate that fails on drops beyond the confidence interval; Langfuse tracing; a results report with bootstrap intervals.

## Interview prep themes

Testing deterministic vs non-deterministic systems; building evals from zero (error analysis first); code checks vs judges vs humans; golden dataset upkeep; hallucination detection; offline vs online evals; RAG debugging; judge reliability and bias; "82% to 85% on 200 cases: ship it?"; flaky-tolerant CI gates; eval platform system design.

## Current status

Update this section as lessons finish.

- **Lesson 1 (in progress):** `lessons/01_first_eval/`. Run the schema test 10× and do error analysis on failures; finish `variance.py` (temperature 0 vs 1, distinct names in 20 samples); answer the questions in `notes.md`.
- **Next, Lesson 2:** turn Lesson 1 failures into a first golden dataset; more pytest (fixtures, parametrize over cases, not just runs).
