from turtle import Turtle, Screen

cursor = Turtle()
screen = Screen()

colors = ["pink","red","yellow","blue","green","black","orange","brown","purple","grey"]

for side in range (3,11):
    num = side - 3
    cursor.color(colors[num])
    for time in range(side):
        cursor.right(360/side)
        cursor.forward(100)


screen.exitonclick()