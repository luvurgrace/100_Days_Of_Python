from turtle import Turtle, Screen

cursor = Turtle()
screen = Screen()


for time in range(15):
    cursor.forward(10)
    cursor.penup()
    cursor.forward(10)
    cursor.pendown()

screen.exitonclick()