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

- [ ] Describe the game's purpose.

   A number-guessing game built in Streamlit where the player tries to guess a secret number within a limited number of attempts, based on difficulty level (Easy, Normal, Hard), receiving "higher/lower" hints after each guess.
- [ ] Detail which bugs you found.

1. The high/low hint text was inverted like guessing too high returned "Go higher" instead of "Go lower," and vice versa.
2. The secret number was converted to a string on even-numbered attempts but left as an integer on odd attempts, causing a type mismatch that triggered incorrect string-based comparisons instead of numeric ones.
3. The attempts counter initialized at 1 instead of 0, causing the game to end one attempt earlier than it should have.

- [ ] Explain what fixes you applied.

1. Refactored `check_guess` into `logic_utils.py` and corrected the hint strings so "Too High" returns "Go lower" and "Too Low" returns "Go higher."
2. Removed the string conversion of the secret number so it's always compared as an integer.
3. Changed the initial `attempts` value from 1 to 0 so it matches the reset value used by "New Game," ensuring the first guess is correctly counted as attempt #1.
4. Added pytest tests in `tests/test_game_logic.py` to verify the corrected behavior; all 12 tests pass.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User selects "Normal" difficulty (range 1–100, 8 attempts)
2. User enters a guess of 25 against a secret of 20 — game correctly returns "Go lower"
3. User enters a guess of 15 — game correctly returns "Go higher"
4. User enters a guess of 20 — game returns a win message and the score updates
5. Attempts remaining count down accurately with each guess, and the game only ends after all 8 attempts are used without a correct guess

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```


PS C:\Users\issam\Downloads\ai110-module1show-gameglitchinvestigator-starter> python -m pytest
================================================= test session starts =================================================
platform win32 -- Python 3.14.6, pytest-9.1.1, pluggy-1.6.0
rootdir: C:\Users\issam\Downloads\ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.15.1
collected 12 items

tests\test_game_logic.py ............                                                                            [100%]

================================================= 12 passed in 0.03s ==================================================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
