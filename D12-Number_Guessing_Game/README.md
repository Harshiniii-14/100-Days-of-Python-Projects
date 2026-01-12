# 🔢 Number Guessing Game – Day 12 

## 📌 Project Overview

This project is a **command-line number guessing game** built in Python as part of **Day 12** of the *100 Days of Python* course.

The player must guess a randomly generated number between **1 and 100** within a limited number of attempts, based on the chosen difficulty level.

This project primarily focuses on understanding and applying:

* **Global scope**
* **Local scope**
* **Function behavior and return values**
* **Game logic and state management**

---

## 🎯 Game Rules

* The computer randomly selects a number between **1 and 100**
* The player chooses a difficulty:

  * **Easy** → 10 attempts
  * **Hard** → 5 attempts
* After each guess:

  * The game gives feedback (too high / too low / correct)
  * Attempts decrease if the guess is wrong
* The game ends when:

  * The player guesses correctly
  * Attempts reach zero

---

## 🧠 Concepts Learned & Applied

---

## 1️⃣ Global Scope

### What Is Global Scope?

Variables created **outside of functions** are in the **global scope** and can be accessed anywhere in the program.

In this project, global variables include:

```python
answer = random.randint(1, 100)
difficulty = input("Choose a difficulty: ")
lives = 10 or 5
```

These variables:

* Control overall game state
* Persist throughout the program
* Are shared across multiple parts of the code

📌 Example:

```python
answer = random.randint(1,100)
```

The `answer` variable exists globally and is passed into functions when needed.

---

## 2️⃣ Local Scope

### What Is Local Scope?

Variables created **inside a function** exist only within that function.

In this project, the function:

```python
def check_answer(guess, answer):
```

has **local variables**:

* `guess`
* `answer` (parameter)
* internal return values

These variables:

* Cannot be accessed outside the function
* Are destroyed once the function finishes executing

---

## 3️⃣ Using Parameters Instead of Globals

Rather than directly using global variables inside the function, values are **passed as parameters**:

```python
guessed = check_answer(guess, answer)
```

This:

* Prevents unwanted side effects
* Makes the function reusable
* Improves clarity and testing

📌 This is **good practice** and exactly what Day 12 teaches.

---

## 4️⃣ Function Return Values to Control Flow

The `check_answer()` function returns values to control the game logic:

```python
return 0  # correct guess
return 1  # incorrect guess
```

The main loop then reacts to this return value:

```python
if guessed == 0:
    break
else:
    lives -= 1
```

This demonstrates:

* Separation of logic
* Clean communication between functions and global flow

---

## 5️⃣ Difficulty Selection & State Control

The number of lives is set based on difficulty:

```python
if difficulty == "easy":
    lives = 10
elif difficulty == "hard":
    lives = 5
```

`lives` is a **global variable**, but it is modified **inside the loop**, showing how global state changes over time.

---

## 6️⃣ While Loop for Game Continuation

The game runs as long as the player has remaining lives:

```python
while lives > 0:
```

This loop:

* Handles repeated guessing
* Ends automatically when lives reach zero
* Stops early when the correct guess is made

---

## 🖼 ASCII Art & User Experience

The game imports ASCII art for visual polish:

```python
import art
print(art.logo)
```

This reinforces:

* Modular programming
* Separation of logic and presentation

---

## 🔄 Program Flow Summary

1. Display game logo
2. Generate random number (global)
3. Ask for difficulty
4. Set number of lives
5. Start guessing loop
6. Check each guess using a function
7. Adjust lives or end game
8. Exit when win or lose condition is met

---

## 🛠 Skills Strengthened

* Understanding global vs local scope
* Writing clean, reusable functions
* Passing data through parameters
* Using return values for control flow
* Managing game state correctly
* Avoiding unnecessary global variable usage

---

## ✅ Conclusion

This project demonstrates a clear understanding of **scope in Python**, showing how:

* Global variables manage game state
* Local variables keep functions isolated and safe
* Functions interact with the main program through parameters and return values

Mastering scope here is critical — mistakes with scope cause bugs in **every real-world program**.

---
