import turtle, random
from turtle import Turtle, Screen
from random import randint,choice

cursor = Turtle()
turtle.colormode(255) # change colormode to 255
screen = Screen()

def random_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    return (r,g,b)


cursor.speed(100)
cursor.pensize(2)

for i in range(int(360/5)):
    cursor.setheading(i*5)
    cursor.color(random_color())
    cursor.circle(100)





screen.exitonclick()