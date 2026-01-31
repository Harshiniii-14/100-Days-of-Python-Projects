from turtle import Screen, Turtle
import random

screen = Screen()
screen.setup(500, 400)

is_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# tim = Turtle()
# tim.shape("turtle")
# tim.color("red")
# tim.penup()
# tim.goto(-230,-100)
#The screen is a coordinate system, where the center is at 0,0
# Since the height is 400 here, top coordinate is 200, bottom is -200... similarly left -250 and right 250


turtles = []
pos=-120
# We are using objects, classes and instances in this challenge
for i in range(len(colors)):
    turtles.append(Turtle(shape="turtle"))
    turtles[i].color(colors[i])
    turtles[i].penup()
    turtles[i].goto(x=-230, y=pos)
    pos = pos + 50

if user_bet: #Ensures the race doesn't start before the user makes a bet
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! The {winning_color} turtle is the winner!")
            else:
                print(f"You lost! The {winning_color} turtle is the winner!")

        rand_distance =  random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()