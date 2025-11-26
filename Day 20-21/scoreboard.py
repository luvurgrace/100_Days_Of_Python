from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("White")
        self.setposition(0, 250)
        self.write(arg = f"Total Score: {self.score}", align = ALIGNMENT, font = FONT)
        self.hideturtle()

    def score_count(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Total Score: {self.score}", align = ALIGNMENT, font = FONT)

    def game_over(self):
        self.teleport(0,0)
        self.write(arg="GAME OVER", align = ALIGNMENT, font = FONT)