# ☕ Coffee Machine – Day 15

## 📌 Project Overview

This project is a **command-line Coffee Machine simulation** built in Python as part of **Day 15** of the *100 Days of Python* course.

The program simulates the internal logic of a real coffee machine by:

* Managing resources (water, milk, coffee)
* Processing user input and coin payments
* Checking if resources are sufficient
* Making drinks and tracking profit

This project focuses heavily on **functions, dictionaries, loops, and program state management**.

---

## 🎯 Features

* Offers three drinks: **espresso, latte, cappuccino**
* Tracks available resources
* Handles coin-based payment system
* Calculates and returns change
* Keeps track of total profit
* Allows admin commands (`report`, `off`)

---

## 🧠 Concepts Learned & Applied

---

## 1️⃣ Dictionaries for Structured Data

The menu and resources are stored using nested dictionaries:

```python
MENU = {
    "espresso": {
        "ingredients": {...},
        "cost": 1.5
    }
}
```

This structure allows:

* Easy access to drink ingredients and cost
* Scalable design (easy to add more drinks)
* Clear separation of data and logic

---

## 2️⃣ Global State Management

Two important global variables are used:

```python
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0
```

These variables represent the **current state of the machine** and are updated as drinks are made.

---

## 3️⃣ Functions for Modular Design

Each major task is handled by a separate function, improving readability and maintainability.

### 🔹 `is_resource_sufficient()`

Checks whether enough ingredients are available to make the selected drink.

```python
def is_resource_sufficient(order_ingredients):
```

* Loops through required ingredients
* Compares them with available resources
* Returns `True` or `False`

---

### 🔹 `process_coins()`

Handles user coin input and calculates total money inserted.

```python
def process_coins():
```

* Accepts quarters, dimes, nickels, and pennies
* Converts coin count into dollar value
* Returns total amount paid

---

### 🔹 `is_transaction_successful()`

Validates the payment and updates profit.

```python
def is_transaction_successful(money_received, drink_cost):
```

* Checks if payment is sufficient
* Calculates and returns change
* Updates global `profit`
* Refunds money if insufficient

📌 Demonstrates controlled use of the `global` keyword.

---

### 🔹 `make_coffee()`

Deducts ingredients and serves the drink.

```python
def make_coffee(drink_name, order_ingredients):
```

* Subtracts ingredient quantities from resources
* Confirms drink preparation to the user

---

## 4️⃣ While Loop for Continuous Operation

The coffee machine runs continuously using a `while` loop:

```python
while is_on:
```

The loop:

* Takes user input repeatedly
* Responds to commands
* Stops only when `"off"` is entered

---

## 5️⃣ User Commands

The machine supports special commands:

### 🧾 `report`

Displays current resource levels and profit.

### 🔌 `off`

Turns off the coffee machine and exits the loop.

---

## 🔄 Program Flow Summary

1. Prompt user for drink choice
2. Check if machine is turned off or report is requested
3. Verify sufficient resources
4. Process coin payment
5. Validate transaction
6. Make coffee and update resources
7. Repeat until machine is turned off

---

## 🛠 Skills Strengthened

* Writing reusable functions
* Working with nested dictionaries
* Managing shared program state
* Using loops for continuous programs
* Handling user input cleanly
* Applying real-world logic to code
* Understanding when and how to use global variables

---

## 🚀 Possible Improvements

* Add input validation for invalid drink names
* Handle missing milk for espresso more explicitly
* Add refill functionality
* Convert the program to OOP (classes)
* Add unit tests for functions

---

## ✅ Conclusion

This project simulates a **real-world system** using core Python concepts.
It demonstrates how functions, data structures, and loops work together to create a complete, interactive program.

Day 15 is a major milestone because it shows how to manage **logic + state + user interaction** in a clean and scalable way.

---

