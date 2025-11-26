# TODO 1: What is random walk?
# TODO 2: Thick of a cursor
# TODO 3: Make cursor move faster
# TODO 4: Each time it walks, it uses a different color
import turtle, random
from turtle import Turtle, Screen
from random import random, randint,choice

cursor = Turtle()
turtle.colormode(255) # change colormode to 255
screen = Screen()

def random_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    return (r,g,b)

directions = [0, 90, 180, 270]


cursor.pensize(10)
cursor.speed(100)
for i in range(1000):
    cursor.color(random_color())
    steps = 30
    angle = choice(directions)
    cursor.setheading(angle)
    cursor.fd(steps)




screen.exitonclick()