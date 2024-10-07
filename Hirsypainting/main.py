import random
from turtle import Turtle, Screen, colormode

color_list = [(198, 13, 32), (248, 236, 25), (40, 76, 188), (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216), (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198), (65, 231, 239), (217, 88, 51), (6, 68, 42), (176, 176, 233), (239, 168, 161), (249, 8, 48), (5, 246, 222), (15, 76, 110), (243, 15, 14), (38, 43, 221)]

#### extract color from picture
# colors = colorgram.extract('hirst.jpg', 40)
# hcolors = []
# rgb_colors = []
# for color in colors:
#         r = color.rgb.r
#         g = color.rgb.g
#         b = color.rgb.b
#         new_color = (r, g, b)
#         rgb_colors.append(new_color)
# print(rgb_colors)

# 10 x 10 spots
# 20 size spaced out 50


t = Turtle()
t.hideturtle()
colormode(255)
t.pensize(20)
screen = Screen()
t.speed(20)
t.penup()
t.setx(-250)
t.sety(350)
print(t.pos())


def draw(space,x):
    for i in range(x):
        for _ in range(x):
            t.pencolor(random.choice(color_list))
            t.dot()
            t.forward(space)
        t.penup()
        t.backward(space*x)
        t.right(90)
        t.forward(50)
        t.left(90)
        print(t.pos())


t.penup()
draw(75, 10)


screen.exitonclick()
