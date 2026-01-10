from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.penup()
        self.color("White")
        self.setposition(0, 250)
        self.hideturtle()
        self.score_update()

    def score_update(self):
        self.clear()
        self.write(arg=f"Total Score: {self.score} High score: {self.high_score}", align = ALIGNMENT, font = FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.score_update()

    def increase_score(self):
        self.score += 1
        self.score_update()



    # def game_over(self):
    #     self.teleport(0,0)
    #     self.write(arg="GAME OVER", align = ALIGNMENT, font = FONT)

