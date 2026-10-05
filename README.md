# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- The game is a Streamlit number-guessing game. The player selects a difficulty, guesses the secret number, and receives higher/lower feedback while earning or losing points.
- I found that the hint text pointed in the wrong direction and that alternating between numeric and string secret values could cause incorrect comparisons. I also found that the displayed guess range did not follow the selected difficulty, the attempt count starts one too high, and New Game does not reset a finished status.
- I moved the range selection, input parsing, guess comparison, hint text, and score calculation into `logic_utils.py`. I corrected the hint direction, kept guess comparisons numeric, and made the displayed and newly generated ranges follow the selected difficulty. The attempt-count and finished-status reset issues remain unfixed.

## Demo Walkthrough

The following is a sample walkthrough derived from the game logic, not a browser-recorded play-through. Assume Normal difficulty and a secret number of 60.

1. The player starts a Normal game and enters `40`.
2. The game returns `Too Low` and displays `Go HIGHER!`; the score changes from 0 to -5.
3. The player enters `70`; the game returns `Too High` and displays `Go LOWER!`; the score changes to -10.
4. The player enters `60`; the game returns `Win`, displays `Correct!`, and ends the round.
5. With the current scoring formula and attempt counter, the final score for this sequence is 40.

The attempt counter currently starts at 1, so its displayed attempts-left value is off by one. Starting a new game after a win or loss also does not reset the game status yet.

## 🧪 Test Results

```
$ PYTHONPATH=. ./.venv/bin/pytest
tests/test_game_logic.py .....                                           [100%]

============================== 5 passed in 0.01s ==============================
```

These tests cover winning, too-high and too-low outcomes, and the corresponding high/low hint directions. Advanced edge-case testing was not completed.

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
