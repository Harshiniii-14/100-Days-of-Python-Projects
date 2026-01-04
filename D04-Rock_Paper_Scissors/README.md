# 🪨📄✂️ Rock Paper Scissors Mini Project

## 📌 Project Overview

This project is a **command-line Rock Paper Scissors game** built using Python.
The user plays against the computer by choosing **Rock, Paper, or Scissors**, and the program determines the result based on game rules.

This project was created as part of **Day 4: Randomisation and Python Lists**, focusing on:

* Random number generation
* Lists and indexing
* Input validation
* Logical decision-making
* Cleaner and optimized code using mathematics

---

## 🎯 How the Game Works

* The user inputs a number:

  * `0` → Rock
  * `1` → Paper
  * `2` → Scissors
* The computer randomly chooses a number between `0` and `2`
* Both choices are displayed using ASCII art
* The program compares the choices and prints:

  * **You win**
  * **You lose**
  * **It's a draw**
  * **Invalid input**

---

## 🧠 Concepts Learned & Used

### 1️⃣ Python `random` Module

The `random` module is used to generate the computer’s choice.

```python
import random
computerNumber = random.randint(0, 2)
```

🔹 `randint(0,2)` generates a **random integer** between 0 and 2 (inclusive).

---

### 2️⃣ Multi-line Strings (ASCII Art)

Each game option is represented using **multi-line strings**:

```python
rock = ''' ... '''
paper = ''' ... '''
scissors = ''' ... '''
```

These make the game visually interactive in the terminal.

---

### 3️⃣ Python Lists

The ASCII art is stored inside a list:

```python
game_images = [rock, paper, scissors]
```

This allows:

* Easy access using indexes
* Clean mapping of numbers → choices
* Avoiding repetitive `if-else` statements

Example:

```python
print(game_images[userNumber])
```

---

### 4️⃣ List Indexing

Python lists use **zero-based indexing**:

* Index `0` → Rock
* Index `1` → Paper
* Index `2` → Scissors

This directly matches the user’s numeric input.

---

### 5️⃣ Input Handling & Validation

The user input is converted to an integer:

```python
userNumber = int(input("Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
```

Validation ensures the program doesn’t crash:

```python
if userNumber not in [0, 1, 2]:
    print("You typed an invalid number. You lose!")
```

This prevents **IndexError** and incorrect inputs.

---

### 6️⃣ Conditional Logic (`if–elif–else`)

The game outcome is determined using conditions:

* Invalid input
* Draw
* Win
* Loss

Instead of long and repetitive conditions, an **optimized mathematical approach** is used.

---

### 7️⃣ Modulo Arithmetic for Game Logic

The winning logic uses modulo (`%`) arithmetic:

```python
elif (userNumber - computerNumber) % 3 == 1:
    print("You win!")
```

#### Why this works:

Rock–Paper–Scissors follows a **circular pattern**:

```
Rock → Scissors → Paper → Rock
```

Modulo arithmetic handles this circular relationship cleanly and efficiently.

| Situation                    | Result     |
| ---------------------------- | ---------- |
| Same choice                  | Draw       |
| `(user - computer) % 3 == 1` | User wins  |
| Otherwise                    | User loses |

This replaces multiple complex conditions with **one clean line**.

---

## 🧼 Code Optimization

The project originally used many `if-elif` statements to check every case.
That approach was **redundant and harder to maintain**.

It was optimized by:

* Removing duplicate conditions
* Using list indexing
* Using modulo arithmetic
* Improving readability and scalability

---

## 🧪 Sample Output

```
What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.
1

Computer chose:

(scissors ASCII art)

You lose!
```

---

## 🚀 Skills Gained

* Writing cleaner Python code
* Understanding lists and indexing
* Using randomness in programs
* Preventing runtime errors
* Applying math to simplify logic
* Building beginner-friendly CLI games

---

## 📂 Project Files

* `main.py` – Contains the full game logic
* No external libraries required (uses built-in `random` module)

---

## ✅ Conclusion

This project strengthened my understanding of **randomisation, lists, indexing, and decision logic** in Python.
It also introduced me to **writing optimized and readable code**, which is essential for larger projects and real-world applications.

---

