import random

# TODO 0: Getting color list through Cologram
# import colorgram
# colors = colorgram.extract('hirst_painting.jpg', 42)
#
# col_list = []
#
# for col in colors:
#     r = col.rgb.r
#     g = col.rgb.g
#     b = col.rgb.b
#     new_color = (r,g,b)
#     col_list.append(new_color)
#
# print(col_list)

import turtle
from turtle import Turtle, Screen
color_list = [(27, 108, 163), (192, 39, 81), (234, 160, 54), (233, 214, 87), (221, 137, 175), (142, 108, 58), (106, 194, 217), (21, 57, 131), (203, 166, 32), (211, 73, 92), (237, 89, 54), (119, 191, 141), (142, 208, 226), (138, 29, 72), (106, 108, 197), (7, 184, 172), (6, 160, 86), (97, 51, 36), (21, 159, 208), (230, 167, 185), (86, 46, 34), (31, 88, 93), (34, 45, 83), (235, 170, 160), (172, 186, 222), (149, 214, 192), (244, 213, 8), (96, 28, 55), (40, 82, 82)]

# TODO 1: 10x10 image
# TODO 2: dot 20 in size
# TODO 3: spaced apart by 50
# TODO 4: 100 dots

turtle.colormode(255) # определяем, в каком диапазоне будут задаваться значения цветов (1.0 или 255)
cursor = Turtle()
screen = Screen()
cursor.shape("turtle")
cursor.speed("fastest")
cursor.hideturtle()

def random_color(list):
    return random.choice(list)
cursor.penup()
cursor.setheading(225)
cursor.forward(300)
cursor.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    cursor.dot(20, random_color(color_list))
    cursor.forward(50)

    if dot_count % 10 == 0:
        cursor.setheading(90)
        cursor.forward(50)
        cursor.setheading(180)
        cursor.forward(500)
        cursor.setheading(0)

screen.exitonclick()

