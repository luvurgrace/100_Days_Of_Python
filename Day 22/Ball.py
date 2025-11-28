from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.goto(0,0)
        self.x_dir = 5
        self.y_dir = 5
        self.move_speed = 0.05

    def reset_position(self):
        self.hit_lr_wall()
        self.hit_ud_wall()
        self.goto(0,0)
        self.move_speed = 0.05

    def move(self):
        self.penup()
        new_y = self.ycor() + self.y_dir
        new_x = self.xcor() + self.x_dir
        self.goto(new_x, new_y)

    def hit_lr_wall(self):
        self.x_dir *= -1

    def hit_ud_wall(self):
        self.y_dir *= -1

