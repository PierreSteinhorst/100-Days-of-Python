import random
from turtle import Turtle, Screen
from random import randint


is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []


def create_turtles():
    y_pos = -125
    for turtle_index in range(0, 6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.penup()
        new_turtle.color(colors[turtle_index])
        new_turtle.goto(x=-230, y=y_pos)
        y_pos += 50
        all_turtles.append(new_turtle)


create_turtles()

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"You were  right. The color was {winning_color}.")
            else:
                print(f"You lost. The color was {winning_color}.")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
