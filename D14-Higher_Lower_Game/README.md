# 🔼🔽 Higher Lower Game – Day 14 

## 📌 Project Overview

This project is a **command-line Higher Lower game** built in Python as part of **Day 14** of the *100 Days of Python* course.

The game challenges the player to compare two public figures and guess **who has more followers**. The game continues as long as the player keeps guessing correctly, with the score increasing after each correct answer.

This project focuses on **game logic, loops, randomness, and data handling**.

---

## 🎯 How the Game Works

1. The game displays a logo
2. Two random options (A and B) are selected from a dataset
3. Each option shows:

   * Name
   * Description
   * Country
4. The player chooses who they think has more followers
5. If the guess is correct:

   * Score increases
   * Game continues
6. If the guess is wrong:

   * Game ends
   * Final score is displayed

---

## 🧠 Concepts Learned & Applied

---

## 1️⃣ Working with External Data

The game imports structured data from an external file:

```python
import game_data
data = game_data.data
```

Each entry in the dataset is a dictionary containing:

* `name`
* `follower_count`
* `description`
* `country`

This reinforces working with **lists of dictionaries**, a very common real-world data structure.

---

## 2️⃣ Random Selection

Random indices are used to pick two different options:

```python
a = random.randint(0, length - 1)
b = random.randint(0, length - 1)
```

A `while` loop ensures option **A and B are never the same**:

```python
while b == a:
    b = random.randint(0, length - 1)
```

---

## 3️⃣ Game Loop with State Tracking

The main game runs inside a `while` loop:

```python
while not gameover:
```

This loop:

* Keeps the game running
* Tracks score
* Ends only when the player makes an incorrect guess

---

## 4️⃣ Score Management

The score is stored in a variable that persists across rounds:

```python
score = 0
```

Correct guesses increment the score:

```python
score += 1
```

The current score is displayed after each correct answer, reinforcing **state management**.

---

## 5️⃣ Conditional Logic

The game checks whether the player’s choice matches the correct comparison:

```python
if chosen == "a" and data[a]["follower_count"] > data[b]["follower_count"]:
```

This uses:

* Logical operators
* Conditional statements
* Numeric comparisons

---

## 6️⃣ Input Handling

Player input is normalized using `.lower()`:

```python
chosen = input("Who has more followers? Type 'A' or 'B': ").lower()
```

This prevents errors caused by uppercase or lowercase input differences.

---

## 7️⃣ Visual Feedback with ASCII Art

The game uses ASCII art to improve user experience:

```python
import art
print(art.logo)
print(art.vs)
```

This keeps visual elements separate from logic, demonstrating **modular design**.

---

## 🔄 Program Flow Summary

1. Display game logo
2. Randomly select option A
3. Randomly select option B (ensuring it’s different)
4. Display both options
5. Ask player for input
6. Compare follower counts
7. Update score or end game
8. Repeat until incorrect guess

---

## 🛠 Skills Strengthened

* Loop-based game logic
* Random number generation
* Data handling with dictionaries
* Conditional comparisons
* State tracking across iterations
* Modular imports
* Writing interactive CLI programs

---

## 🚀 Possible Improvements

* Carry forward the winning option to the next round
* Add input validation for invalid choices
* Hide follower counts completely from code output
* Add difficulty levels
* Store high scores

---

## ✅ Conclusion

This project demonstrates how multiple Python concepts can be combined to build a **complete interactive game**.
It reinforces logical thinking, clean control flow, and working with real-world data structures.

Day 14 marks a step forward into **logic-driven programs**, not just syntax-based exercises.

---
* Help you **refactor this code** to the official Day 14 “carry-forward” version
* Or write a **short Day 14 reflection** for your GitHub profile
