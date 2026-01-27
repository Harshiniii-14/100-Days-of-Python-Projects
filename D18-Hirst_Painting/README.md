# 🎨 Hirst Painting Dot Art (Turtle Graphics)

## 📌 Project Overview

This project recreates a **Damien Hirst–style dot painting** using Python’s **Turtle Graphics**.
Colors are extracted from an image using the **colorgram** library and then randomly used to draw a grid of colorful dots on the screen.

The final output is a **10 × 10 grid (100 dots)**, each dot having a random color sampled from the original image.

<img width="526" height="512" alt="image" src="https://github.com/user-attachments/assets/418795dc-55c6-4793-90a2-3740c0d21f4a" />


---

## 🧠 Concepts Covered

* Python modules & imports
* Working with external libraries (`colorgram`)
* RGB color handling
* Turtle graphics basics
* Loops and conditionals
* Randomization
* Coordinate and movement logic

---

## 📦 Libraries Used

* **turtle** → For drawing graphics
* **colorgram** → For extracting colors from an image
* **random** → To randomly choose colors

---

## 🖼️ How Color Extraction Works

```python
colours = col.extract('HirstPainting.jpg', 25)
```

* Extracts **25 colors** from the image.
* Each extracted color contains RGB values.

```python
colour_list = []
for i in range(0, 25):
    r = colours[i].rgb.r
    g = colours[i].rgb.g
    b = colours[i].rgb.b
    colour_list.append((r, g, b))
```

* RGB values are converted into tuples.
* Stored in a list so Turtle can use them.

---

## 🐢 Turtle Setup

```python
tim = turtle_module.Turtle()
turtle_module.colormode(255)
```

* Creates a turtle object named `tim`.
* Enables RGB color mode (0–255).

```python
tim.penup()
tim.hideturtle()
tim.speed("fastest")
```

* `penup()` → prevents drawing lines
* `hideturtle()` → hides the cursor
* `speed("fastest")` → faster drawing

---

## 📍 Positioning the Turtle

```python
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
```

* Moves the turtle to the **bottom-left starting position**.
* Ensures dots are drawn neatly from left to right.

---

## 🔴 Drawing the Dot Grid

```python
num_of_dots = 100
```

* Total dots to be drawn (10 × 10 grid).

```python
for dot_count in range(1, num_of_dots + 1):
    tim.dot(20, random.choice(colour_list))
    tim.forward(50)
```

* Draws a dot of size `20`.
* Picks a random color from the extracted color list.
* Moves forward to place the next dot.

---

## ↩️ Row Handling Logic

```python
if dot_count % 10 == 0:
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)
```

* Every 10 dots:

  * Moves up to the next row
  * Goes back to the starting position of that row
* `% 10` ensures a perfect grid structure.

---

## 🖥️ Screen Control

```python
screen = turtle_module.Screen()
screen.exitonclick()
```

* Keeps the window open until clicked.

---

## ✅ Final Output

* A **100-dot painting**
* Each dot:

  * Same size
  * Different random color
* Inspired by **Hirst’s dot art**

---

## 📌 Key Takeaway

This project combines **art + programming**, showing how Python can be used creatively with logic, loops, and color manipulation.

---

