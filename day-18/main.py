import turtle
from turtle import Turtle, Screen
from random import choice, random, randint


def geometric_figure(object_turtle, num_site):
    for _ in range(num_site):
        angle = 360 / num_site
        object_turtle.forward(100)
        object_turtle.right(angle)


def draw_geometric_figures(object_turtle, start_figure, end_figure):
    for _ in range(start_figure, end_figure + 1):
        object_turtle.pencolor(choice(colors))
        geometric_figure(object_turtle, _)


def random_walk(object_turtle):
    directions = [0, 90, 180, 270]
    object_turtle.width(15)
    object_turtle.speed(10)
    for _ in range(200):
        object_turtle.pencolor(random_color())
        object_turtle.setheading(choice(directions))
        object_turtle.forward(randint(1, 100))


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color_tuple = (r, g, b)

    return color_tuple


# Tuple
# my_tuple = (1, 3, 8)
# my_tuple[2] -> 8
# You cannot change a value in a tuple -> it is immutable

tim = Turtle()
turtle.colormode(255)
tim.shape("turtle")
tim.color("coral")

random_walk(tim)


# Draw a square
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# draw_geometric_figures(tim, 3, 10)

screen = Screen()
screen.exitonclick()

# Giving a module an alias
# import turtle as t
# tim = t.Turtle()
