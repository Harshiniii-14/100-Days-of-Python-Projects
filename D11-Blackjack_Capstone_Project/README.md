---

# 🃏 Blackjack Capstone Game 

A simple **command-line Blackjack game** built using Python.
This project simulates the classic Blackjack card game where a user plays against the computer (dealer), following standard house rules.

---

## 📌 Project Overview

The goal of Blackjack is to get a card total **as close to 21 as possible without exceeding it**.

* You (the player) compete against the computer (dealer).
* Both draw cards randomly from an unlimited deck.
* The computer follows strict dealer rules.
* The winner is decided based on final scores.

---

## 🎯 Game Rules (House Rules)

* The deck is **unlimited** in size.
* There are **no jokers**.
* Number cards (2–10) count as their face value.
* **Jack, Queen, King = 10**
* **Ace = 11 or 1** (automatically adjusted to avoid bust).
* Cards are **not removed** after drawing.
* The computer is the **dealer**.

Deck used in the game:

```python
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
```

---

## 🧠 Project Logic Breakdown

### 1️⃣ Starting the Game

* The user is asked if they want to play Blackjack.
* If the user types `y`, the game starts.
* If the user types `n`, the program exits.

---

### 2️⃣ Dealing Initial Cards

* Both the **player and computer receive two cards**.
* The player sees:

  * Their full hand
  * Their current score
* The player only sees **the first card of the computer** (just like real Blackjack).

---

### 3️⃣ Score Calculation Logic

A function calculates the score for both players:

* If the total is **21 with exactly two cards**, it is treated as **Blackjack**.
* If the total exceeds 21 and an **Ace (11)** is present:

  * Ace is converted from **11 → 1**
* This prevents unnecessary busts.

---

### 4️⃣ Player Turn

* The player chooses:

  * `y` → Draw another card
  * `n` → Pass and end their turn
* The player can keep drawing until:

  * They choose to stop
  * OR their score exceeds 21 (bust)

---

### 5️⃣ Computer (Dealer) Turn

* The computer draws cards **only after the player finishes**.
* Dealer rules:

  * Must draw cards until the score is **17 or higher**
  * Stops automatically at 17+

---

### 6️⃣ Comparing Results

Final scores are compared using clear conditions:

* Blackjack beats all other hands
* Busting (score > 21) results in an automatic loss
* Higher score wins if both are under 21
* Equal scores result in a draw

---

## 🏆 Win Conditions

| Condition                     | Result       |
| ----------------------------- | ------------ |
| Player has Blackjack          | Player wins  |
| Computer has Blackjack        | Player loses |
| Player score > 21             | Player loses |
| Computer score > 21           | Player wins  |
| Player score > Computer score | Player wins  |
| Computer score > Player score | Player loses |
| Equal scores                  | Draw         |

---

## 🧩 Functions Used

### `deal_card()`

* Returns a random card from the deck.

### `calculate_score(hand)`

* Calculates the total score.
* Handles Ace conversion (11 → 1).
* Detects Blackjack.

### `compare(user_score, computer_score)`

* Determines the final result.
* Returns a message declaring win, loss, or draw.

---

## 🔁 Game Loop Structure

1. Ask if the user wants to play.
2. Deal initial cards.
3. Player takes their turn.
4. Computer takes its turn.
5. Scores are compared.
6. Result is displayed.
7. User can choose to play again.

---

## 📚 Concepts Learned

* Functions and modular programming
* Loops and conditional logic
* Lists and random selection
* Game state control
* Real-world rule simulation
* Clean code structure

---

## 🚀 How to Run

1. Make sure Python is installed.
2. Clone this repository.
3. Ensure `art.py` (for logo) is in the same directory.
4. Run the game:

```bash
python blackjack.py
```

---



