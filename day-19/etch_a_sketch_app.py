from turtle import Turtle, Screen


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def turn_left():
    tim.left(5)


def tun_right():
    tim.right(5)


def clear_screen():
    tim.penup()
    tim.clear()
    tim.home()
    tim.pendown()


tim = Turtle()
screen = Screen()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=tun_right)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()