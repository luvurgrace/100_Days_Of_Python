from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.shape("turtle")
        self.back_to_start()
        self.setheading(90)

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def back_to_start(self):
        self.goto(STARTING_POSITION)

    def finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
