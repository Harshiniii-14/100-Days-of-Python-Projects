import colorgram as col
import turtle as turtle_module
import random

# Create a list of colors from our image
colours = col.extract('HirstPainting.jpg', 25)
colour_list = []
for i in range(0, 25):
    r = colours[i].rgb.r
    g = colours[i].rgb.g
    b = colours[i].rgb.b
    colour = (r, g, b)
    colour_list.append(colour)

tim = turtle_module.Turtle()
turtle_module.colormode(255)

tim.penup()
tim.hideturtle()
tim.speed("fastest")
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
num_of_dots = 100

for dot_count in range(1, num_of_dots + 1):
    tim.dot(20, random.choice(colour_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)



screen = turtle_module.Screen()
screen.exitonclick()

