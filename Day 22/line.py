from turtle import Turtle

class DottedLine(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0,300)
        self.pensize(width=5)
        self.color("white")
        self.setheading(270)
        self.hideturtle()

        while self.ycor() > -300:
            self.pendown()
            self.forward(30)
            self.penup()
            self.forward(25)