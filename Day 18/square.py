from turtle import Turtle, Screen

cursor = Turtle()
screen = Screen()

for time in range(0,4):
    cursor.right(90)
    cursor.forward(100)

screen.exitonclick()
