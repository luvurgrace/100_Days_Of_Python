import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing Capstone")

timmy_the_player = Player()
manager = CarManager()
scoreboard = Scoreboard()
manager.hideturtle()

screen.listen()
screen.onkey(timmy_the_player.go_up, "Up") # we do not call the method at once,
# but pass a reference to this method as an event handler, so there are no parenthesis



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if random.randint(1,6) == 1:
        manager.spawn_new_car()
    manager.car_moves()


    for car in manager.cars:
        if car.distance(timmy_the_player) < 21:
            game_is_on = False
            scoreboard.game_over()

    if timmy_the_player.finish_line():
        timmy_the_player.back_to_start()
        manager.level_up()
        scoreboard.level_up()





screen.exitonclick()
