# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

The game was working fine but the problem was it
**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
| ----- | ----------------- | --------------- | ---------------------- |
|       |                   |                 |                        |
|       |                   |                 |                        |
|       |                   |                 |                        |

---

Installing requirements initially failed because the disk was full, so I used the workspace virtual environment instead. The Streamlit server later returned HTTP 200 at `http://localhost:8501`, but I did not complete a browser play-through. The cases below are based on the code paths and test results; visible gameplay still needs manual confirmation.

**Bug Reproduction Logs**
| Input Used / Trigger | Expected Behavior | Actual Behavior | Console Error / Output | Suspected Code Location |
|----------------------|-------------------|-----------------|------------------------|-------------------------|
| On a valid guess greater than the secret shown in Developer Debug Info | The game reports "Too High" and advises the player to go lower | `check_guess` returns "Too High" but displays "Go HIGHER!", sending the player in the wrong direction | none; the app displays a misleading hint | `app.py`, `check_guess` |
| On a fresh Normal game, if the debug secret is 20-99, submit `100` as the first guess | Report "Too High" and advise going lower | The first submission uses a string secret because attempts becomes 2; comparing `"100"` with a secret such as `"42"` lexically reports "Too Low" | none; the app displays the wrong outcome and hint | `app.py`, submit handler's `attempts % 2` secret conversion; `check_guess` |
| Start a fresh Normal game and count the allowed guesses | Show 8 attempts and allow 8 guesses | The app initially shows 7 attempts left; attempts starts at 1 and increments before processing the first guess, so the limit is reached after 7 submitted guesses | none; incorrect attempt count / early game over | `app.py`, initial `st.session_state.attempts` value and submit handler |
| Win or lose, then click "New Game" | Reset the game to playing state and allow another guess | The secret and attempt count change, but `status` remains `won` or `lost`; the terminal-state check stops the app again | none; "You already won" or "Game over" remains visible | `app.py`, New Game button branch; `st.session_state.status` initialization and terminal-state check |

---

## 2. How did you use AI as a teammate?

I used Claude and GitHub Copilot while investigating the game logic and writing tests. Copilot suggested moving the comparison and hint behavior into testable helpers in `logic_utils.py`; this fit the existing module and separated game rules from Streamlit rendering. The existing test already checked that `60` against `50` returns `"Too High"`, so I changed the regression approach to test the actual UI hint text as well; I added coverage for both directions because both messages had been reversed. The five passing pytest tests verify the outcomes and the displayed guidance, although they do not replace a manual browser play-through.

## 3. Debugging and testing your fixes

- I ran `PYTHONPATH=. ./.venv/bin/pytest`; all 5 tests passed, including the starter win/high/low tests and new checks that a too-high guess says `"Go LOWER!"` and a too-low guess says `"Go HIGHER!"`.
- `git diff --check` passed, and Pylance reported no errors in `logic_utils.py`. Pylance still reported Streamlit session-history typing warnings in `app.py`.
- I checked that the Streamlit server responded with HTTP 200 on port 8501. I did not complete an interactive browser test, so the end-to-end gameplay remains unverified.
- The testable hint helper let pytest verify the text shown to the player without depending on Streamlit's UI runtime.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
