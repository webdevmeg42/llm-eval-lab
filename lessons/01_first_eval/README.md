# Lesson 1: Structured output checks and sampling variance

**Big idea:** an LLM returns a sample from a range of outputs, not one fixed answer. You can't make that variation go away, so you measure it.

## Files

| File | Status |
| --- | --- |
| `test_npc_schema.py` | Given. Run it, then study why it passes or fails. |
| `variance.py` | Yours to finish. The `TODO`s mark what to write. |
| `notes.md` | Your findings and answers. Bring these back to the lesson chat. |

## Exercise

1. Run the schema test 10 times:
   ```bash
   pytest lessons/01_first_eval/test_npc_schema.py -v
   ```
   Record the pass count. For every failure, save the raw output in `notes.md` and say *why* it failed. This is error analysis.
2. Finish `variance.py`, then run it:
   ```bash
   python lessons/01_first_eval/variance.py
   ```
   Compare how many distinct NPC names you get at temperature 0 vs 1.
3. Answer the two questions in `notes.md`.
