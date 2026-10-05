# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

  The game looked like a regular guess a number game. When I clicked submit a guess, it kept telling me to go lower even when I guessed 1 when the values were between 1 and 100. The same happened when I put 1 and 100 and I guessed 100. It told me to go higher. There are more bugs listed below. In addition, I also noticed the game stops at 1 attempt left which is not exactly a bug but something I noticed.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

  Every time I guessed a number, it would tell me to go lower even if it is lower than the secret number.
  I tried the game on easy mode (1-20) and it still told me to select a number from 1-100.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Guess a number between 1 and 100. Input was 20 and guess was 25    |    Go higher      |  Go lower       | 25 was the guess and it's higher than 20
| Guess a number between 1 and 100. Input was 70 and guess was 75    |    Go higher      |  Go lower       | 75 was the guess and it's higher than 70
| Guess a number between 1 and 100. Input was 90 and guess was 83    |    Go lower       |  Go higher      | 83 was the guess and it's lower than 90

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

  Besides Claude, I used Copilot on VS Code.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

  I asked Copilot to move the check_guess function from app.py into logic_utils.py and fix the bug where the high/low hint text was inverted (a guess higher than the secret should say "Go lower," not "Go higher," and vice versa). Copilot correctly refactored the function and swapped the hint strings. I verified this was correct by writing a pytest test confirming that check_guess(60, 50) returns the "Too High" outcome with the "Go lower" message, and by manually playing the game with guesses both above and below the secret to confirm the hints now displayed correctly in both directions.
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

  When Copilot refactored the game's logic functions (including get_range_for_difficulty) out of app.py and into logic_utils.py, it initially left the function body as a placeholder that raised NotImplementedError instead of carrying over the real implementation. This crashed the app immediately with a traceback when I tried to run it. I rejected this version and asked Copilot to fill in the actual difficulty-range logic instead of leaving a stub. I verified the fix by rerunning the app with streamlit run app.py and confirming it loaded without errors, and that each difficulty setting produced the correct guessing range.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

  I considered a bug fixed when it passed two checks: an automated pytest test targeting the specific behavior, and manual playtesting in the live Streamlit app to confirm the fix held up under real use, not just in an isolated test case.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

   I ran a pytest test checking that check_guess(60, 50) returns the "Too High" outcome paired with the "Go lower" hint message. Before my fix, this would have failed because the hint text was inverted (it returned "Go higher" instead). After refactoring check_guess into logic_utils.py and correcting the hint strings, the test passed, confirming the fix worked at the function level — not just by chance in the UI. I also manually played multiple rounds in the app itself, guessing both above and below the secret number across several attempts, to confirm the hints were correct in live gameplay and that the attempts counter and secret comparison no longer broke on even-numbered attempts.
- Did AI help you design or understand any tests? How?

  Yes — I asked Copilot to generate the pytest test case in test/test_game_logic.py targeting the hint-text bug, since I wanted a test that directly verified the fixed behavior (check_guess(60, 50) returning "Too High" with "Go lower"). Having the AI generate the test also helped me confirm I understood the expected input/output shape of check_guess correctly, since I used that same understanding to manually verify the fix in the live game afterward.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Streamlit doesn't work like a normal app that updates one piece of the screen at a time. Instead, every time you click a button (like "Submit Guess"), Streamlit re-runs your entire Python script from top to bottom, like refreshing the whole page. Normally that would mean all your variables reset back to their starting values every single click, which would make it impossible to keep track of things like the secret number, your score, or how many attempts you've used. That's where session_state comes in as it's like a special storage box that survives across reruns, so even though the script restarts each time, anything you save into st.session_state (like st.session_state.attempts or st.session_state.score) sticks around. I actually saw this cause a real bug in my project because the attempts counter was initialized incorrectly before the rerun logic kicked in, the game was miscounting how many guesses I had left. The history of your guesses save in the history box.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

    Writing a pytest test immediately after fixing a bug, instead of just trusting that it looked right in the live app. Testing check_guess(60, 50) directly at the function level caught exactly what I expected and gave me real confidence the fix worked, rather than relying only on clicking through the UI. I want to be 100% sure the app works as it is supposed to.
- What is one thing you would do differently next time you work with AI on a coding task?

  I'd review the AI's refactored code more carefully before running it, rather than running the app first and discovering problems (like the NotImplementedError stub) through a crash. Reading the diff line-by-line before testing would have caught that issue sooner. I caught this error since Coplilot fixed the wrong code and it gave it problems temporarily before I debugged it.
- In one or two sentences, describe how this project changed the way you think about AI generated code.

  It reinforced that AI-generated code can look complete and confident while still containing real bugs or unfinished pieces (like leftover placeholder functions), so I need to actually test and verify every change rather than assuming it works just because it was generated by AI.

  
