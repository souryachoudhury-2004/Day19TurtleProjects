import turtle
from turtle import *
from random import *

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a colour.")
user_bet = user_bet.lower()

colours = ["red", "orange", "blue", "green", "black", "grey"]
if user_bet not in colours:
    print("Invalid Colour! Please choose one of the following: Red, Orange, Blue, Green, Black, Grey.")
    exit()

all_turtles = []
for turtle_index in range(0, 6):
    cursor = Turtle(shape="turtle")
    cursor.penup()
    cursor.color(colours[turtle_index])
    cursor.goto(x=-230, y=150-(50*turtle_index))
    all_turtles.append(cursor)


if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        rand_dist = randint(0, 10)
        turtle.forward(rand_dist)
        if turtle.xcor() > 230:
            is_race_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print(f"You won! Winning colour is {user_bet}.")
            else:
                print(f"You lost! Winning colour is {winning_colour}")


exitonclick()







exitonclick()