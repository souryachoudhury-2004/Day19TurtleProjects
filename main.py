from turtle import *
from random import *

cursor = Turtle()
screen = Screen()
colormode(255)
cursor.width(5)

def move_forward():
    cursor.forward(20)

def turn_right():
    cursor.right(30)
    cursor.color(randint(0, 255), randint(0, 255), randint(0,255))

def turn_left():
    cursor.left(30)
    cursor.color(randint(0, 255), randint(0, 255), randint(0, 255))

def move_backward():
    cursor.backward(20)

def pen_up():
    cursor.penup()

def pen_down():
    cursor.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="p", fun=pen_up)
screen.onkey(key="l", fun=pen_down)


exitonclick()
