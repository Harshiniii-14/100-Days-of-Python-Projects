# 🐢 Turtle Graphics (5 Challenges)

## 📌 Imports & Setup

```python
import turtle as t
import random
```

* `turtle` → Python module used for **graphics and drawing**.
* Imported as `t` to make the code shorter and cleaner.
* `random` → Used to generate **random colors and directions**.

```python
timmy = t.Turtle()
timmy.shape("turtle")
timmy.color("red")
```

* Creates a turtle object named **timmy**.
* Changes the turtle’s appearance to a turtle shape.
* Sets its default color to red.

---

## 🟦 Turtle Challenge 1 – Draw a Square

### 🎯 Goal:

Draw a **square** using turtle movements.

### 💡 Key Concepts:

* `forward(distance)` → Moves the turtle forward.
* `right(angle)` → Turns the turtle clockwise.
* A square has **4 sides**.
* Each internal turn = **90°**.

```python
for _ in range(4):
    timmy.forward(100)
    timmy.right(90)
```

### ✅ What we learn:

* **For loops** reduce repetitive code.
* Functions can be replaced by loops when logic is repetitive.
* Optimized, cleaner code is preferred.

---

## 🟦 Turtle Challenge 2 – Draw a Dotted Line

### 🎯 Goal:

Draw a **dotted arrow/line**.

### 💡 Key Concepts:

* `penup()` → Turtle moves **without drawing**.
* `pendown()` → Turtle resumes drawing.

```python
for _ in range(10):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()
```

### ✅ What we learn:

* Control when the turtle draws.
* Alternating pen up/down creates dotted effects.
* Movement logic + drawing state = patterns.

---

## 🟦 Turtle Challenge 3 – Draw Multiple Shapes (3 to 10 sides)

### 🎯 Goal:

Draw shapes from **triangle to decagon**.

### 💡 Mathematical Concept:

* A full circle = **360°**
* Turning angle = `360 / number_of_sides`

### 🔁 Optimized Approach:

Instead of writing separate functions for each shape, use **one generalized function**:

```python
def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)
```

```python
for shape_side_n in range(3, 11):
    timmy.color(random.choice(colours))
    draw_shape(shape_side_n)
```

<img width="444" height="368" alt="image" src="https://github.com/user-attachments/assets/fe9d595b-59f3-4ea5-9536-28bb730f4f21" />


### ✅ What we learn:

* **Normalization** using formulas.
* Writing **reusable functions**.
* Using `range(3, 11)` to loop shapes.
* Random color selection for better visuals.

---

## 🎨 Color Concepts (RGB Mode)

```python
t.colormode(255)
```

* Enables **RGB color mode**.
* Each color channel ranges from `0–255`.

```python
def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b
```

### ✅ What we learn:

* Functions can **return tuples**.
* RGB gives more color variety than named colors.
* Randomization adds visual interest.

---

## 🟦 Turtle Challenge 4 – Random Walk

### 🎯 Goal:

Make the turtle walk randomly in different directions.

### 💡 Concepts Used:

* `setheading(angle)` → Sets turtle direction.
* Possible angles: `0, 90, 180, 270`
* `pensize()` → Thickness of the line.
* `speed("fastest")` → Faster drawing.

```python
angles = [0, 90, 180, 270]

for _ in range(500):
    timmy.setheading(random.choice(angles))
    timmy.color(random_colour())
    timmy.forward(20)
```

<img width="562" height="460" alt="image" src="https://github.com/user-attachments/assets/7e219e8a-ef37-4907-8f36-ac43b60fdb8e" />


### ✅ What we learn:

* Lists store predefined directions.
* `random.choice()` picks random values.
* Random walk simulates **unpredictable movement**.
* Combining loops + randomness creates complex patterns.

---

## 🟦 Turtle Challenge 5 – Draw a Spirograph

### 🎯 Goal:

Create a **spirograph pattern** using circles.

### 💡 Logic:

* Draw multiple circles.
* Slightly rotate the turtle after each circle.
* Smaller gap → smoother spirograph.

```python
def spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.speed("fastest")
        timmy.color(random_colour())
        timmy.circle(100)
        timmy.right(size_of_gap)
```

```python
spirograph(10)
```

<img width="486" height="451" alt="image" src="https://github.com/user-attachments/assets/85aba9ec-f8f8-4bfa-831a-d4a9a5ac0d66" />


### ✅ What we learn:

* `circle(radius)` draws a circle.
* `360 / gap` decides number of rotations.
* Combining geometry + loops creates advanced art.
* Parameterized functions give flexibility.

---

## 🖥️ Screen Control

```python
screen = t.Screen()
screen.exitonclick()
```

* Keeps the turtle window open.
* Program exits only when the user clicks.

---

## 🧠 Overall Concepts Learned

* Object-oriented programming (`Turtle` object)
* Loops & functions
* Code optimization
* Geometry in programming
* Randomization
* RGB color system
* Visual pattern generation

---
