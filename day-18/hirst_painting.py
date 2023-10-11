# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 15)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import turtle
from turtle import Screen
from random import choice


def getting_starting_position(object_turtle):
    object_turtle.hideturtle()
    object_turtle.setheading(225)
    object_turtle.penup()
    object_turtle.forward(300)
    object_turtle.setheading(0)


def get_to_new_line(object_turtle):
    object_turtle.penup()
    object_turtle.setx(-212.13203435596424)
    object_turtle.sety(object_turtle.ycor() + 50)
    object_turtle.pendown()


def draw_lines(object_turtle):
    getting_starting_position(object_turtle)
    for row in range(10):
        for _ in range(10):
            object_turtle.dot(20, choice(color_list))
            object_turtle.penup()
            object_turtle.forward(50)
            object_turtle.setheading(0)
            object_turtle.pendown()
        get_to_new_line(object_turtle)


color_list = [(102, 170, 217), (225, 245, 239), (246, 228, 200), (230, 150, 70), (239, 213, 80),
              (243, 218, 235), (97, 199, 144), (50, 84, 150), (212, 79, 143), (220, 131, 180), (207, 59, 30),
              (189, 38, 139), (21, 45, 147), (216, 170, 220)]

tim = turtle.Turtle()
screen = Screen()
turtle.colormode(255)
screen.screensize(1800, 1800)

draw_lines(tim)


screen.exitonclick()
