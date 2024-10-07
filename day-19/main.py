from turtle import Turtle, Screen
from random import randint
from tkinter import messagebox


screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="make your bet", prompt="Which turtle will win the race? ")
color = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

for _ in range(0, 6):
    xAxis = -125 + (_ * 50)
    new_turtle_ = Turtle(shape="turtle")
    new_turtle_.up()
    new_turtle_.color(color[0 + _])
    new_turtle_.goto(x=-230, y= xAxis)
    all_turtles.append(new_turtle_)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        random_distance = randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() > 230:
            is_race_on = False
            if turtle.fillcolor() == user_bet:
                messagebox.showinfo(f"{turtle.fillcolor()} wins!", "you win the bet!")
            else:
                messagebox.showinfo(f"{turtle.fillcolor()} wins!", "Your turtle lost. You loose the bet!")


#
# def move_forwards():
#     tim.forward(10)
#
# def move_backwards():
#     tim.backward(10)
#
#
# def turn_clockwise():
#     tim.right(10)
#
#
# def turn_counterClockWise():
#     tim.left(10)
#
#
# def clear():
#     screen.resetscreen()
#
#
# screen.listen()
# screen.onkey(move_forwards, "w")
# screen.onkey(turn_clockwise, "d")
# screen.onkey(turn_counterClockWise, "a")
# screen.onkey(move_backwards, "s")
# screen.onkey(clear, "c")
screen.exitonclick()