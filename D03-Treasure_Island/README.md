# 🏴‍☠️ Treasure Island – Python Control Flow Project 

## 📌 Project Overview

This is a **text-based adventure game** built using Python as part of **Day 3** of the *100 Days of Python* course.
The game guides the player through a series of choices using **control flow and logical decision-making**, ultimately leading to either victory or game over.

The objective is to **find the treasure** by making the correct decisions at each stage.

---

## 🧠 Concepts Covered & Learned

### 1. **Printing Multi-line Strings**

* Used triple quotes (`''' '''`) to print **ASCII art** at the start of the game.
* Learned how raw strings (`r''' '''`) prevent escape characters from being interpreted.

```python
print(r''' ... ''')
```

📌 This helps in displaying banners, game art, or formatted text cleanly.

---

### 2. **The `print()` Function**

* Used to:

  * Display instructions
  * Show story narration
  * Inform the player about outcomes (win/lose)

Example:

```python
print("Welcome to Treasure Island.")
```

---

### 3. **Taking User Input with `input()`**

* Learned how to collect user decisions during runtime.
* Inputs are stored in variables for later comparison.

Example:

```python
firstDecision = input("Will you go 'right' or 'left': ")
```

📌 Important note:
All inputs are treated as **strings**, so comparisons must also be strings.

---

### 4. **Variables**

* Used variables to store user choices:

  * `firstDecision`
  * `secondDecision`
  * `thirdDecision`

This improves readability and allows decision-based logic.

---

### 5. **Conditional Statements (`if`, `elif`, `else`)**

* Learned how to control the program flow using conditions.
* Each decision leads to a different branch in the story.

Example:

```python
if firstDecision == "left":
    ...
else:
    ...
```

📌 This is the core logic behind the entire game.

---

### 6. **Nested `if` Statements**

* Implemented **if statements inside other if statements**.
* Allows multi-level decision making (like a real game).

Example:

```python
if firstDecision == "left":
    if secondDecision == "wait":
        if thirdDecision == "yellow":
            print("You win!")
```

📌 This teaches how complex logic is built step-by-step.

---

### 7. **Logical Flow & Game Design**

* Designed a **decision tree** where:

  * Correct choices move the player forward
  * Wrong choices end the game
* Learned how **order of conditions matters**.

---


## 🎮 Game Logic Summary

1. Player starts at a crossroad
2. Chooses between **left** or **right**
3. Encounters a lake → **swim** or **wait**
4. Reaches a house with three doors → **red**, **blue**, or **yellow**
5. Only one path leads to victory

---

## 🛠️ Skills Strengthened

* Problem-solving
* Logical thinking
* Writing readable conditional code
* Structuring beginner-level Python programs
* Understanding how games and decision systems work internally

---

## 🚀 Possible Improvements (Future Enhancements)

* Make input case-insensitive using `.lower()`
* Add replay functionality
* Use functions to reduce repetition
* Add scoring or inventory system

