---

# 🎯 Hangman Game – Day 7 

## 📌 Project Overview

This project is a **command-line Hangman game** built using Python as part of **Day 7** of the *100 Days of Python* course.

The game randomly selects a word, tracks user guesses, manages remaining lives, and visually displays progress using ASCII art.
The player wins by guessing all letters correctly before running out of lives.

---

## 🎮 How the Game Works

1. A random word is selected from a predefined word list
2. The player guesses one letter at a time
3. Correct guesses reveal letters in the word
4. Incorrect guesses reduce available lives
5. The game ends when:

   * All letters are guessed (**Win**)
   * Lives reach zero (**Lose**)

---

## 🧠 Concepts Learned & Applied

---

## 1️⃣ Python Modules & Imports

The project uses **custom modules** to keep the code clean and organized.

```python
import random
import hangman_words
import hangman_art
```

* `hangman_words` → stores the word list
* `hangman_art` → stores ASCII art for stages and the logo
* `random` → selects a random word

📌 This demonstrates **modular programming** and separation of concerns.

---

## 2️⃣ Random Word Selection

A word is randomly chosen from the word list:

```python
chosen_word = random.choice(word_list)
```

This ensures:

* Replayability
* Unpredictable gameplay

---

## 3️⃣ Variables & Game State

Key variables used to manage the game:

```python
lives = 6
game_over = False
correct_letters = []
guessed = []
```

* `lives` → tracks remaining attempts
* `game_over` → controls the main loop
* `correct_letters` → stores correct guesses
* `guessed` → tracks all attempted letters

---

## 4️⃣ Creating the Placeholder Word

Before guessing begins, the word is hidden using underscores:

```python
placeholder = ""
for position in range(word_length):
    placeholder += "_"
```

This visually represents progress as the game runs.

---

## 5️⃣ While Loop (Main Game Loop)

The game continues until `game_over` becomes `True`:

```python
while not game_over:
```

This loop:

* Displays lives
* Takes input
* Updates the word
* Checks win/lose conditions

---

## 6️⃣ Input Handling & Validation

User input is converted to lowercase:

```python
guess = input("Guess a letter: ").lower()
```

Duplicate guesses are handled safely:

```python
if guess in guessed:
    print(f"You've already guessed {guess}")
    continue
```

📌 Prevents wasting lives on repeated guesses.

---

## 7️⃣ Updating the Displayed Word

Each guess rebuilds the display string:

```python
for letter in chosen_word:
    if letter == guess:
        display += letter
        correct_letters.append(guess)
    elif letter in correct_letters:
        display += letter
    else:
        display += "_"
```

This logic:

* Reveals correct letters
* Keeps previously guessed letters visible
* Maintains hidden letters as `_`

---

## 8️⃣ Life Management & Losing Condition

If the guess is incorrect:

```python
if guess not in chosen_word:
    lives -= 1
```

When lives reach zero:

```python
if lives == 0:
    game_over = True
    print(f"IT WAS <{chosen_word}>! YOU LOSE")
```

The corresponding hangman stage is displayed using ASCII art.

---

## 9️⃣ Winning Condition

The player wins when there are no underscores left:

```python
if "_" not in display:
    game_over = True
    print("YOU WIN")
```

This ensures the game ends **immediately upon success**.

---

## 🖼 ASCII Art & Visual Feedback

The game uses ASCII art to:

* Display the Hangman logo
* Show progression as lives decrease

```python
print(stages[lives])
/filtering
```

This improves user experience even in a terminal environment.

---

## 🛠 Skills Strengthened

* Game loops with `while`
* State management
* Lists and string manipulation
* Modular code structure
* Input validation
* Logical condition checks
* Debugging control flow

---

## ✅ Conclusion

This project combines **loops, conditionals, lists, modules, and user input** into a complete, playable game.
It represents a major step from simple scripts to **structured programs with real logic and flow**.

---
