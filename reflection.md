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
| Guess a number between 1 and 100. Input was 70 and guess was 75   |    Go higher      |  Go lower       | 75 was the guess and it's higher than 70
| Guess a number between 1 and 100. Input was 90 and guess was 83    |    Go lower       |  Go higher      | 83 was the guess and it's lower than 90

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
