# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

Add a useful Guess History feature to the Streamlit guessing game. Show each valid guess, its Too High/Too Low/Win result, and how far it was from the secret in the sidebar; keep the history for the current Streamlit session.

**What did the agent do?**

Modified `app.py` to initialize a separate `guess_history` session-state list, append structured records for valid guesses, and display a sidebar table with Guess, Outcome, and Distance columns. Modified `README.md` to describe the new feature. The existing debug `history` remains unchanged, so invalid entries can still be inspected separately. The full pytest suite passed with 10 tests. In the running app, I submitted `50` when the displayed secret was `62`; the app showed `Go HIGHER!` and the sidebar recorded `50 | Too Low | 12`.

**What did you have to verify or fix manually?**

I checked that the distance is the absolute difference between the integer guess and secret, and that the table renders after a submitted guess so it includes the newest entry without clearing the feedback. I kept the feature session-only rather than adding file persistence, and kept invalid text out of the guess table because it has no numeric distance. The browser check confirmed the displayed outcome and distance matched the secret and guess.

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case               | Prompt Used                                                                                                                                                                                                                                                                           | AI-Suggested Test                                                                       | Did It Pass?              | Your Reasoning                                                                                                           |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| Empty input             | "Suggest pytest cases for `parse_guess` and `check_guess` covering empty, non-numeric, decimal, negative, and extremely large guesses. Expect empty and malformed values to return validation errors, decimals not to be silently changed, and integer edge cases to compare safely." | Assert `parse_guess("")` returns the prompt-to-enter error.                             | Yes                       | Empty text is a common input and should not crash or create a guess.                                                     |
| Non-numeric text        | Same prompt as above.                                                                                                                                                                                                                                                                 | Assert `parse_guess("abc")` returns the invalid-number error.                           | Yes                       | Confirms arbitrary text is handled as validation feedback rather than an exception.                                      |
| Decimal input           | Same prompt as above.                                                                                                                                                                                                                                                                 | Assert `parse_guess("12.7")` rejects the input instead of returning 12.                 | Yes, after fixing parsing | The old parser silently truncated fractions, changing the value the player entered.                                      |
| Negative integer        | Same prompt as above.                                                                                                                                                                                                                                                                 | Parse `-4` and verify comparison against secret `10` returns `Too Low`.                 | Yes                       | Confirms signed integer parsing and comparison behave consistently even outside the intended range.                      |
| Extremely large integer | Same prompt as above.                                                                                                                                                                                                                                                                 | Parse a 100-digit integer and verify comparison against secret `10` returns `Too High`. | Yes                       | Confirms Python integer parsing and the comparison handle values much larger than any difficulty range without overflow. |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
<!-- Paste the prompt you gave the AI -->
```

**Linting output before:**

```
<!-- Paste relevant linter warnings/errors -->
```

**Changes applied:**

<!-- Describe what you changed based on the AI's suggestions -->

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

|                          | Model A | Model B |
| ------------------------ | ------- | ------- |
| **Model name**           |         |         |
| **Response summary**     |         |         |
| **More Pythonic?**       |         |         |
| **Clearer explanation?** |         |         |

**Which did you prefer and why?**

<!-- Your conclusion -->
