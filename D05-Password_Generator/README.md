# 🔐 Password Generator – Day 5 (Python Loops)

## 📌 Project Overview

This project is a **random password generator** built using Python as part of **Day 5** of the *100 Days of Python* course.

The program generates a **strong, randomized password** based on user-defined criteria:

* Number of letters
* Number of symbols
* Number of numbers

It demonstrates the practical use of **loops, lists, the `random` module, and string manipulation**.

---

## 🎯 Project Objective

To understand and apply:

* `for` loops
* Python lists
* The `range()` function
* Random selection and shuffling
* Building strings dynamically

This project simulates how real-world password generators work.

---

## 🧠 Concepts Learned & Applied

### 1. **Python Lists**

Lists were used to store groups of characters:

* Letters (uppercase + lowercase)
* Numbers
* Symbols

```python
letters = ['a', 'b', ..., 'Z']
numbers = ['0', '1', ..., '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
```

📌 Lists allow indexed access and easy random selection.

---

### 2. **The `random` Module**

Imported Python’s built-in `random` module to introduce unpredictability.

Used functions:

* `random.choice()` → selects a random item from a list
* `random.shuffle()` → rearranges list elements randomly

```python
random.choice(letters)
random.shuffle(password_list)
```

📌 This ensures the password is **not predictable**.

---

### 3. **User Input & Type Conversion**

Collected user preferences using `input()` and converted them to integers using `int()`.

```python
nr_letters = int(input("How many letters would you like?\n"))
```

📌 This is important because `range()` requires integers.

---

### 4. **`for` Loops with `range()`**

Used `for` loops to repeat actions a specific number of times.

```python
for char in range(0, nr_letters):
    password_list.append(random.choice(letters))
```

📌 Learned how `range(start, end)` controls loop execution.

---

### 5. **Building a Password Step-by-Step**

Instead of generating a string directly:

1. Characters were added to a list
2. The list was shuffled
3. Characters were joined into a final string

```python
password = ""
for char in password_list:
    password += char
```

📌 This approach gives better control and randomness.

---

### 6. **Why Shuffling Is Important**

Without shuffling:

* Letters come first
* Symbols second
* Numbers last

This creates patterns.

By using:

```python
random.shuffle(password_list)
```

📌 The password becomes **secure and unpredictable**.

---

## 🔄 Program Flow (Logic Breakdown)

1. Display welcome message
2. Ask user for password requirements
3. Randomly select letters, symbols, and numbers
4. Store selections in a list
5. Shuffle the list
6. Convert list into a string
7. Display the final password

---

## 🛠️ Skills Strengthened

* Loop logic and repetition
* Working with lists
* Randomness and security basics
* Converting data types
* Breaking problems into steps
* Writing cleaner, modular logic

---

