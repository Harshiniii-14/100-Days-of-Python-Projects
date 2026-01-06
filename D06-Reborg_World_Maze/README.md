# 🤖 Day 6 – Python Functions & Loops (Reeborg / Karel)

## 📌 Overview

Day 6 of the *100 Days of Python* course focuses on **functions, indentation, loops, and control flow**, applied through hands-on robot challenges using **Reeborg’s World** (inspired by Karel the Robot).

The goal of this day is to learn how to:

* Write **reusable code**
* Control program flow using **loops and conditions**
* Solve problems with **unknown and changing constraints**
* Debug logical errors and avoid infinite loops


## 🧠 Concepts Covered


## 1️⃣ Introduction to Functions

### What Is a Function?

A **function** is a reusable block of code that performs a specific task.

Python already provides built-in functions such as:

* `print()`
* `len()`
* `int()`
* `range()`

Functions are identified by:

* A name
* Parentheses `()`

Example:

```python
print("Hello")
len("Hello")
```

---

## 2️⃣ Defining and Calling Custom Functions

### Defining a Function

Functions are defined using the `def` keyword.

```python
def my_function():
    print("Hello")
    print("Bye")
```

Key points:

* `def` starts a function definition
* The function name describes what it does
* Parentheses define inputs (if any)
* A colon `:` starts the function body
* **Indented code belongs to the function**

### Calling a Function

A function does nothing until it is **called**.

```python
my_function()
```

When called, Python:

1. Finds the function definition
2. Executes each indented line inside it
3. Returns to where it was called from

---

## 3️⃣ Why Functions Matter (Robot Analogy)

Functions prevent **repetition**.

Instead of rewriting the same robot instructions repeatedly, we:

* Group steps into a function
* Call the function whenever needed

This:

* Reduces typing
* Improves readability
* Makes debugging easier

---

## 4️⃣ Creating New Functions from Existing Ones

Reeborg provides:

* `move()`
* `turn_left()`

But **no `turn_right()`**.

So we define it ourselves:

```python
def turn_right():
    turn_left()
    turn_left()
    turn_left()
```

Turning left three times equals turning right once.

This makes code:

* Shorter
* Easier to understand
* More expressive

---

## 5️⃣ The Hurdles Challenge (Loops + Functions)

### Problem

The robot must jump over multiple hurdles to reach the goal.

Writing each step manually would be inefficient.

---

### Creating a `jump()` Function

We encapsulate the steps for jumping a hurdle:

```python
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
```

Now one function call = one hurdle jump.

---

### Repeating with a `for` Loop

Instead of calling `jump()` repeatedly:

```python
for step in range(6):
    jump()
```

This:

* Uses `range()` to control repetition
* Reduces code size
* Improves clarity

---

## 6️⃣ Indentation in Python

### Why Indentation Matters

Python uses **indentation to define code blocks**.

Indented code belongs to:

* Functions
* Loops
* Conditional blocks

Example:

```python
def example():
    print("Inside function")
print("Outside function")
```

Only the indented line runs when the function is called.

---

### Rules of Indentation

* Python officially uses **4 spaces per indent**
* Tabs and spaces **cannot be mixed**
* Most editors convert Tab → 4 spaces automatically

Indentation visually represents **program structure**.

---

## 7️⃣ While Loops

### What Is a While Loop?

A `while` loop runs **as long as a condition is true**.

```python
while not at_goal():
    jump()
```

This reads like English:

> “While not at the goal, keep jumping.”

---

### When to Use While vs For

| Loop Type    | Use Case                              |
| ------------ | ------------------------------------- |
| `for` loop   | Known number of iterations            |
| `while` loop | Unknown or condition-based repetition |

---

## 8️⃣ Avoiding Infinite Loops

A `while` loop becomes **infinite** if its condition never becomes false.

Example:

```python
while 5 > 3:
    move()
```

Debugging tip:

* Print or track the condition
* Ensure variables change
* Test incrementally

---

## 9️⃣ Hurdles with Random Placement (Hurdle 3)

### Problem

* Wall positions are random
* Number of hurdles is unknown

### Solution Strategy

```python
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
```

This allows the robot to:

* Move when possible
* Jump only when necessary
* Adapt dynamically

---

## 🔟 Variable Height Hurdles (Hurdle 4)

### New Challenge

* Walls have **random heights**
* Robot must climb until the wall ends

### Key Logic

```python
while wall_on_right():
    move()
```

This lets the robot:

* Move upward until the wall ends
* Descend safely
* Continue forward

Nested `while` loops are required for full control.

---

## 🧩 Final Project: Escaping the Maze

### Goal

Navigate a maze where:

* Starting position is random
* Facing direction is random

### Strategy: Right-Hand Rule

The robot follows the **right wall** until it reaches the exit.

Decision hierarchy:

1. If right is clear → turn right & move
2. Else if front is clear → move
3. Else → turn left

---

### Final Algorithm

```python
while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
```

This prevents infinite loops and works in all valid maze configurations.

---

## 🛠 Skills Strengthened

* Writing reusable functions
* Logical problem decomposition
* Loop control and conditions
* Debugging infinite loops
* Algorithmic thinking
* Clean, readable Python code

---
