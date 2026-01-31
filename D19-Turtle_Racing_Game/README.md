# 🐢 Turtle Race Game – Day 19 (Python Turtle Graphics)

## 📌 Project Overview

This project is a **graphical Turtle Race game** built using Python’s **`turtle` graphics module** as part of **Day 19** of the *100 Days of Python* course.

The program creates multiple turtle objects that race across the screen, while the user places a bet on which turtle will win. The winner is determined by random movement, making each race unpredictable and fun.

This project focuses on **object-oriented programming, GUI basics, and event-driven logic**.

---

## 🎯 How the Game Works

1. A window opens with a race track
2. The user is prompted to bet on a turtle color
3. Six turtles line up at the starting position
4. Each turtle moves forward by a random distance
5. The first turtle to cross the finish line wins
6. The result of the user’s bet is displayed in the console

---

## 🧠 Concepts Learned & Applied

---

## 1️⃣ Turtle Graphics & Screen Setup

The program uses Python’s built-in `turtle` module to create a graphical window.

```python
from turtle import Screen, Turtle
```

The screen is configured using:

```python
screen.setup(500, 400)
```

This establishes a coordinate system where:

* `(0, 0)` is the center
* X-axis controls horizontal movement
* Y-axis controls vertical positioning

---

## 2️⃣ User Interaction via `textinput()`

The user places a bet using a pop-up input dialog:

```python
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
```

This introduces **event-driven input**, where the program waits for user interaction before continuing.

---

## 3️⃣ Creating Multiple Objects (OOP)

Multiple turtle objects are created dynamically using a loop:

```python
turtles.append(Turtle(shape="turtle"))
```

Each turtle:

* Is an instance of the `Turtle` class
* Has its own color, position, and movement
* Is stored in a list for easy iteration

This reinforces **object-oriented programming concepts**.

---

## 4️⃣ Positioning Objects Using Coordinates

Turtles are positioned along the Y-axis at different starting points:

```python
turtle.goto(x=-230, y=pos)
```

This ensures:

* All turtles start from the same X position
* Each turtle has its own racing lane

---

## 5️⃣ Random Movement & Simulation

Each turtle moves forward by a random distance on each loop iteration:

```python
rand_distance = random.randint(0, 10)
turtle.forward(rand_distance)
```

This randomness simulates an unpredictable race outcome.

---

## 6️⃣ Game Loop & Race Control

The race runs inside a `while` loop:

```python
while is_race_on:
```

The loop:

* Moves turtles forward
* Continuously checks if any turtle has crossed the finish line
* Stops the race once a winner is found

---

## 7️⃣ Determining the Winner

A turtle wins when its X-coordinate exceeds the finish line:

```python
if turtle.xcor() > 230:
```

The winning turtle’s color is retrieved and compared with the user’s bet:

```python
winning_color = turtle.pencolor()
```

The result is printed to the console.

---

## 🔄 Program Flow Summary

1. Set up screen and window size
2. Ask user to place a bet
3. Create and position turtle objects
4. Start race if bet is placed
5. Move turtles randomly
6. Detect winner
7. Display result
8. Wait for user to close window

---

## 🛠 Skills Strengthened

* Turtle graphics and GUI basics
* Object-oriented programming with multiple instances
* Working with coordinate systems
* Event-driven input handling
* Game loops and simulation logic
* Using randomness in programs

---

## 🚀 Possible Improvements

* Display the result on the screen instead of the console
* Add a visual finish line
* Add more turtles or customizable racers
* Track wins and losses
* Allow replay without restarting the program
* Add animations or sound effects

---

## ✅ Conclusion

This project demonstrates how Python can be used to create **simple graphical games** using object-oriented design and random behavior.

Day 19 builds confidence with **GUI programming**, setting the foundation for more interactive applications in later lessons.

---

* Help you **refactor this using functions**
* Or prepare you for **Day 20–21 (Snake Game project)**
