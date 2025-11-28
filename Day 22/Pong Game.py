# TODO 1: create screen
# TODO 2: create a player
# TODO 3: create another player
# TODO 4: create a ball and make it move
# TODO 5: detect collision with wall and bounce
# TODO 6: detect collision with players
# TODO 7: detect when puddle misses
# TODO 8: keep score

import time
from turtle import Screen
from Puddle import Player
from Ball import Ball
from scoreboard import Scoreboard
from line import DottedLine



screen = Screen()
screen.tracer(0)
dotted_line = DottedLine()

scoreboard = Scoreboard()
r_puddle = Player(285)
l_puddle = Player(-285)
ball = Ball()

screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(800,600)


screen.listen()
screen.onkey(r_puddle.go_up, "Up")
screen.onkey(r_puddle.go_down, "Down")

screen.onkey(l_puddle.go_up, "w")
screen.onkey(l_puddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < - 280:
        ball.hit_ud_wall()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        r_puddle.reset_position(285)
        l_puddle.reset_position(-285)

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        r_puddle.reset_position(285)
        l_puddle.reset_position(-285)

    if ball.distance(r_puddle) < 25 and ball.xcor() > 265 or ball.distance(l_puddle) < 25 and ball.xcor() < -265:
        ball.hit_lr_wall()
        ball.move_speed *= 0.9




screen.exitonclick()
