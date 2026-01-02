# 💰 Tip Calculator – Python Mini Project

## 📌 Project Overview

The **Tip Calculator** is a beginner-friendly Python program that calculates how much each person should pay when splitting a bill, including a chosen tip percentage.
This project was built to practice **Python fundamentals**, **user input handling**, **type conversion**, **mathematical operations**, and **formatted output**.

---

## 🎯 What This Project Does

* Takes the **total bill amount** from the user
* Takes the **tip percentage** the user wants to give
* Takes the **number of people** splitting the bill
* Calculates:

  * The tip amount
  * The final bill including tip
  * The amount each person should pay
* Displays the result using **formatted strings**

---

## 🧠 Concepts & Topics Covered

### 1️⃣ User Input (`input()`)

* Used `input()` to collect values from the user.
* Learned that **input values are always strings** by default.

```python
billAmount = input("What was the total bill? $")
```

---

### 2️⃣ Python Primitive Data Types

* **String (`str`)** → User input values
* **Float (`float`)** → Bill amount, tip percentage, and calculations

Understanding when and why to use each data type was a key learning outcome.

---

### 3️⃣ Type Conversion (Type Casting)

Since mathematical operations cannot be performed directly on strings, type conversion was required.

```python
float(billAmount)
float(tipPercent)
float(numberPeople)
```

✔️ This helped avoid **TypeError** and enabled accurate calculations.

---

### 4️⃣ Mathematical Operations in Python

The project uses basic arithmetic operators:

* Multiplication (`*`)
* Division (`/`)
* Addition (`+`)

**Tip Calculation Logic:**

```python
tipAmount = (float(billAmount) * float(tipPercent)) / 100
```

**Final Bill Calculation:**

```python
billAmount = float(billAmount) + tipAmount
```

**Per Person Split:**

```python
eachPersonAmount = billAmount / float(numberPeople)
```

---

### 5️⃣ Variables & Naming

* Used meaningful variable names like:

  * `billAmount`
  * `tipPercent`
  * `numberPeople`
  * `eachPersonAmount`
* Improved readability and understanding of the program flow.

---

### 6️⃣ f-Strings (Formatted String Literals)

Used **f-strings** to print dynamic values cleanly and clearly.

```python
print(f"Each person should pay: ${eachPersonAmount}")
```

✔️ Learned how f-strings make output more readable and professional.

---

### 7️⃣ Program Flow & Logic

* Step-by-step execution from input → calculation → output
* Helped understand how data flows through a Python program
* Reinforced logical thinking and sequencing

---

## 🧪 Example Output

```
Welcome to the tip calculator!
What was the total bill? $100
How much tip % would you like to give? 10, 12, or 15? 10
How many people to split the bill? 4
Each person should pay: $27.5
```

---

## 🚀 What I Learned

* How Python handles user input
* Importance of type conversion
* Performing real-world mathematical calculations in code
* Writing cleaner output using f-strings
* Building confidence with beginner-level Python projects

---

