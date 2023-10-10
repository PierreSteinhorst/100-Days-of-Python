from turtle import Turtle, Screen
from random import choice

colors = ["chocolate", "lime green", "hot pink", "light green", "red", "blue", "yellow", "coral"]


def geometric_figure(object_turtle, num_site):
    for _ in range(num_site):
        angle = 360 / num_site
        object_turtle.forward(100)
        object_turtle.right(angle)


def draw_geometric_figures(object_turtle, start_figure, end_figure):
    for _ in range(start_figure, end_figure + 1):
        object_turtle.pencolor(choice(colors))
        geometric_figure(object_turtle, _)


tim = Turtle()
tim.shape("turtle")
tim.color("coral")

# Draw a square
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

draw_geometric_figures(tim, 3, 10)

screen = Screen()
screen.exitonclick()

# Giving a module an alias
# import turtle as t
# tim = t.Turtle()
