# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

I could not complete a first browser play-through because installing the requirements initially failed when the disk was full. Later, the Streamlit server returned HTTP 200 from the workspace virtual environment, but I still did not finish an interactive game. Code review showed that the high/low hint text was backwards and that some guesses compared a string secret with a number, which could produce the wrong result. I also found an off-by-one attempt count and that starting a new game did not reset the finished-game status; the log below records these code-path findings, not manually confirmed gameplay.

**Bug Reproduction Logs**
The following cases were identified from the code; I did not verify them by playing through the browser.
| Input Used / Trigger | Expected Behavior | Actual Behavior | Console Error / Output | Suspected Code Location |
|----------------------|-------------------|-----------------|------------------------|-------------------------|
| On a valid guess greater than the secret shown in Developer Debug Info | The game reports "Too High" and advises the player to go lower | `check_guess` returns "Too High" but displays "Go HIGHER!", sending the player in the wrong direction | none; the app displays a misleading hint | `app.py`, `check_guess` |
| On a fresh Normal game, if the debug secret is 20-99, submit `100` as the first guess | Report "Too High" and advise going lower | The first submission uses a string secret because attempts becomes 2; comparing `"100"` with a secret such as `"42"` lexically reports "Too Low" | none; the app displays the wrong outcome and hint | `app.py`, submit handler's `attempts % 2` secret conversion; `check_guess` |
| Start a fresh Normal game and count the allowed guesses | Show 8 attempts and allow 8 guesses | The app initially shows 7 attempts left; attempts starts at 1 and increments before processing the first guess, so the limit is reached after 7 submitted guesses | none; incorrect attempt count / early game over | `app.py`, initial `st.session_state.attempts` value and submit handler |
| Win or lose, then click "New Game" | Reset the game to playing state and allow another guess | The secret and attempt count change, but `status` remains `won` or `lost`; the terminal-state check stops the app again | none; "You already won" or "Game over" remains visible | `app.py`, New Game button branch; `st.session_state.status` initialization and terminal-state check |

---

## 2. How did you use AI as a teammate?

I used Claude and GitHub Copilot while investigating the game logic and writing tests. Copilot's suggestion to move the comparison into `logic_utils.py` was correct because it keeps the game rule separate from Streamlit UI code; the existing tests could then call it directly, and all three starter tests passed. Copilot also suggested a focused regression test for the misleading hint, and I broadened that suggestion to cover both high and low guesses because both directions were reversed. I added `get_hint_message` so the tests could check the actual player-facing text, and all five tests passed. I reviewed the changes in both files and kept the helper small rather than adding UI-level test machinery.

## 3. Debugging and testing your fixes

- I ran `PYTHONPATH=. ./.venv/bin/pytest`; all 5 tests passed, including the starter win/high/low tests and new checks that a too-high guess says `"Go LOWER!"` and a too-low guess says `"Go HIGHER!"`.
- `git diff --check` passed, and Pylance reported no errors in `logic_utils.py`. Pylance still reported Streamlit session-history typing warnings in `app.py`.
- I checked that the Streamlit server responded with HTTP 200 on port 8501. I did not complete an interactive browser test, so the end-to-end gameplay remains unverified.
- The testable hint helper let pytest verify the text shown to the player without depending on Streamlit's UI runtime.

---

## 4. What did you learn about Streamlit and state?

Streamlit reruns a Python script from the top when a user interacts with a widget, so ordinary variables are recalculated each time. Values stored in `st.session_state` persist between those reruns for the current user's session, which is why the game's secret and progress belong there. Every action that starts or resets a game must update all related state, including the status, or an old value can affect the next run.

---

## 5. Looking ahead: your developer habits

I want to reuse the habit of checking existing tests first, writing a small regression test for the user-visible bug, and rerunning the suite after each focused change. Next time, I would inspect the full app in a browser earlier and give the AI one bug at a time with the relevant files attached. This project reminded me that AI-generated code can be useful, but its assumptions still need to be checked against the actual code, tests, and behavior.
