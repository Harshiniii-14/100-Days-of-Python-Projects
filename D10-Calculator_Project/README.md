# 🧮 Calculator Project – Day 10 

## 📌 Project Overview

This project is a **command-line calculator application** built using Python as part of **Day 10** of the *100 Days of Python* course.

The calculator supports continuous calculations using basic arithmetic operations and demonstrates the use of:

* **Functions**
* **Dictionaries with functions as values**
* **While loops**
* **Recursion**
* **User input handling**

---

## 🎯 Features

* Perform addition, subtraction, multiplication, and division
* Continue calculations using the previous result
* Restart the calculator at any time
* Clean user interface using ASCII art
* Modular and reusable code structure

---

## 🧠 Concepts Learned & Applied

---

## 1️⃣ Functions with Return Values

Each arithmetic operation is implemented as a **separate function** that returns a result:

```python
def add(n1, n2):
    return n1 + n2
```

Other operations follow the same pattern:

* Addition
* Subtraction
* Multiplication
* Division

📌 Returning values allows results to be reused in further calculations.

---

## 2️⃣ Dictionaries with Functions as Values

A dictionary is used to map operation symbols to their corresponding functions:

```python
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
```

This allows:

* Dynamic function calling
* Cleaner and more scalable code
* Easy addition of new operations

Example usage:

```python
answer = operations[operation_symbol](num1, num2)
```

---

## 3️⃣ While Loop for Continuous Calculation

The calculator runs inside a `while` loop to allow repeated calculations:

```python
while should_accumulate:
```

The loop continues until the user chooses to stop.

---

## 4️⃣ Function Calls Inside Functions

The main program logic is wrapped inside a function:

```python
def calculator():
```

This:

* Keeps global scope clean
* Allows restarting the calculator
* Improves readability and structure

---

## 5️⃣ Recursion (Restarting the Program)

When the user chooses to start a new calculation, the `calculator()` function **calls itself**:

```python
calculator()
```

This is an example of **recursion**, where a function calls itself to restart the program flow.

📌 This avoids duplicating code and resets the calculator cleanly.

---

## 6️⃣ User Input & Type Conversion

User inputs are converted to floating-point numbers to allow decimal calculations:

```python
num1 = float(input("What is the first number?: "))
```

This ensures:

* Accurate mathematical operations
* Support for non-integer values

---

## 7️⃣ Displaying Available Operations

The available operators are dynamically displayed by looping through the dictionary keys:

```python
for symbol in operations:
    print(symbol)
```

This ensures the UI stays updated if new operations are added.

---

## 8️⃣ ASCII Art for Better UI

The calculator uses ASCII art imported from an external module:

```python
import art
print(art.logo)
```

This improves user experience and demonstrates modular design.

---

## 🔄 Program Flow

1. Display calculator logo
2. Ask for the first number
3. Show available operations
4. Ask for operation choice
5. Ask for next number
6. Perform calculation
7. Display result
8. Ask user to continue or restart
9. Repeat until user exits

---

## 🛠 Skills Strengthened

* Writing reusable functions
* Returning values from functions
* Using dictionaries effectively
* Calling functions dynamically
* Managing program flow with loops
* Understanding and applying recursion
* Structuring medium-sized Python programs

---

## ✅ Conclusion

This project demonstrates how **functions, dictionaries, and loops** can be combined to create a flexible and reusable program.
It marks an important step toward writing **structured, maintainable Python applications** rather than one-off scripts.

---


**Are you moving to Day 11 next, or are you revising Day 10 once before continuing?**
