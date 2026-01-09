# 🟦 Day 09 – Secret Auction  

## 📌 Project Overview

This project simulates a **secret auction system** where multiple users can place bids anonymously. Once all bids are entered, the program determines the **highest bidder** and announces the winner.

It focuses on using **Python dictionaries**, **loops**, **conditionals**, and **built-in functions** to manage and process auction data efficiently.

---

## 🧠 Concepts Learned (Notes)

### 1️⃣ Dictionaries in Python

A dictionary stores data in **key–value pairs**.

```python
bidders = {}
```

* **Key** → Bidder name
* **Value** → Bid amount

Example:

```python
bidders["Alex"] = 500
```

This allows us to associate each bidder with their bid.

---

### 2️⃣ Importing External Modules

```python
import art
print(art.logo)
```

* `import art` brings in external Python code
* Used here to display a **logo/banner** for better UI
* Encourages modular programming

---

### 3️⃣ While Loop for Continuous Input

```python
while flag:
```

* Keeps the program running until the condition changes
* Useful when the number of users is unknown

---

### 4️⃣ Taking User Input

```python
name = input("What is your name? ")
bid = input("What is your bid price? $")
```

* `input()` allows dynamic data entry
* Stores bidder details during runtime
  
---

### 5️⃣ Adding Data to Dictionary

```python
bidders[name] = bid
```

* Uses the bidder’s name as the key
* Stores their bid as the value
* Automatically updates the dictionary

---

### 6️⃣ Conditional Logic

```python
if cont == "n":
    break
```

* Checks whether more bidders exist
* `break` exits the loop when bidding is finished

---

### 7️⃣ Clearing the Screen (Simulated)

```python
print("\n" * 20)
```

* Creates blank lines to hide previous bids
* Simulates a **secret auction**
* Ensures privacy between bidders

---

### 8️⃣ Finding the Highest Bidder

```python
highest_bidder = max(bidders, key=bidders.get)
```

* `max()` finds the highest key based on its value
* `key=bidders.get` tells Python to compare bids, not names

---

### 9️⃣ Displaying the Winner

```python
print(f"The highest bidder is {highest_bidder} with a bid of ${bidders[highest_bidder]}.")
```

* Uses **f-strings** for clean output
* Retrieves both name and bid amount

---

## 🧪 Full Code

```python
import art
print(art.logo)

flag = True
bidders = {}

while flag:
    name = input("What is your name? ")
    bid = input("What is your bid price? $")
    bidders[name] = bid

    cont = input("Are there other bidders? y/n ").lower()
    print("\n" * 20)

    if cont == "n":
        break

highest_bidder = max(bidders, key=bidders.get)
print(f"The highest bidder is {highest_bidder} with a bid of ${bidders[highest_bidder]}. They win the auction!")
```

---

## ✅ Skills Practiced

* Python dictionaries
* Loops (`while`)
* Conditional statements
* User input handling
* Built-in functions (`max`)
* Clean output formatting
* Logical problem-solving

---



Just say the word.
