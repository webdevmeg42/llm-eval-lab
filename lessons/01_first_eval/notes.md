# Lesson 1 notes

## Schema test results

Pass count: 0 / 10

### Failures (error analysis)

| Run | Label | Raw output (trimmed) | Why it failed |
| --- | --- | --- | --- |
| 0 | markdown code fence | ` ```json{...}``` ` | payload starts with backticks, which is invalid json, model adding fence because claude chat is trained to render json in markdown format.  JSON content inside schema is schema-valid |
| 1–9 | markdown code fence | same pattern | same as run 0 |

## Variance experiment
NOTE: Script strips fences before parsing, so it doesn't show that 20/20 responses broke the 'ONLY JSON' rule.
| Run | Temperature | Distinct names (of 20) | Most common name |
| --- | --- | --- | --- |
| 1 | 0.0 | 1 | Marta Ironfoot |
| 1 | 1.0 | 2 | Marta Ironfoot |
| 2 | 0.0 | 1 | Marta Ironfoot |
| 2 | 1.0 | 8 | Marta Ironfoot |

What surprised me: Even when there was some variation, every first name came back as Marta.  I also found it interesting that I got different answers when I re-ran the test -- my variance experiment has variance.

## Questions

**1. Why is a single passing run nearly worthless as evidence?** 
Evidence of variance should be seen with multpile runs; multiple runs gives more evidence to produce better statistics from.  A single run that has passed doesn't fix a flakey test.  Multiple runs are needed to come up with a reliable, estimated pass rate.

**2. If my fix for a failure is "add 'no markdown' to the prompt," how would I prove the fix worked instead of getting lucky?**
Before the parsing fix, the strict check failed every run in the test.  Removing the parser - the test fails when the backticks are present because they're not valid JSON.  Enough samples would need to be run, I suggest at least two.  Going from a 0/10 run to a 20/20 run would be evidence for reliablilty.  
