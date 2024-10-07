import turtle
from turtle import Turtle, Screen, colormode
import random

tim = Turtle()
tim.shape("turtle")
tim.color("Red", "Cyan3")
colormode(255)
tim.speed("fastest")
tim.pensize(2)
# for sides in range(4):
#     tim.forward(100)
#     tim.right(90)


def random_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    color = (r, b, g)
    print(color)
    return color

# for steps in range(25):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
color = ["red", "blue", "green", "cyan", "purple", "darkolivegreen", "lime", "orange", "indigo", "gold", "lightgray",
         "pink", "aquamarine"]
direction = [0, 90, 180, 270]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


def random_move(moves):
    tim.forward(30)
    tim.setheading(random.choice(direction))


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.pencolor(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(3)

# random_move(_)


#  for shape_side_n in range(3, 11):
#     tim.color(random.choice(color))
#     draw_shape(shape_side_n)



## change speeed
## Change color
## change direction randomly



screen = Screen()
screen.exitonclick()
