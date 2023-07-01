from random import *
from turtle import *

# Setting up screen
screen = Screen()
screen.setup(width=600, height=500)

# Setting colour mode to RGB
colormode(255)

#drawing starting and finishing lines
lineDraw = Turtle()
lineDraw.color("black")
lineDraw.width(5)
lineDraw.penup()
lineDraw.goto(-200, 150)
lineDraw.pendown()
lineDraw.goto(-200, -150)
lineDraw.penup()
lineDraw.goto(200, -150)
lineDraw.pendown()
lineDraw.goto(200, 150)

#Taking bets
username1 = textinput(title="Enter your name!", prompt="Enter your name, first player!")
username2 = textinput(title="Enter your name!", prompt="Enter your name, second player!")

if username1 == "" or username2 == "":
    print("Please enter your name!")
    exit()

# Setting up turtles
turtle1 = Turtle()
turtle2 = Turtle()
turtle1.color(randint(0, 200), randint(0, 200), randint(0, 200))
turtle2.color(randint(0, 200), randint(0,200), randint(0,200))
turtle1.penup()
turtle2.penup()
turtle1.shape("arrow")
turtle2.shape("arrow")
turtle1.goto(-195, 100)
turtle2.goto(-195, -100)
turtle1.speed("slow")
turtle2.speed("slow")


# Racing the turtles
winner = ""
while True:
    turtle1.forward(randint(0, 10))
    turtle2.forward(randint(0,10))
    if turtle1.xcor() >= 190:
        winner = username1
        break
    if turtle2.xcor() >= 190:
         winner = username2
         break

# Declaring winner
lineDraw.speed("fastest")
lineDraw.penup()
lineDraw.goto(0, 200)
lineDraw.pendown()
lineDraw.write(f"{winner} wins!", font=("Times New Roman", 20, "bold"), align="center")



exitonclick()

