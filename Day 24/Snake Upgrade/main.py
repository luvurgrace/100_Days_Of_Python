# TODO 1: Create a snake body (3 squares on a screen)
# TODO 2: How to make the snake (choose direction)
# TODO 3: Control the snake
# TODO 4: Detect collision with food (once the snake eat food, it disappears, a new one is created
# TODO 5: Create a scoreboard (that updates)
# TODO 6: Detect collision with wall
# TODO 7: Detect collision with tail (Game over is written)

import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("My Snake Game") # How "application" named
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with Food
    if snake.head.distance(food) < 15: # if the snake's head is within 15 px of the food or even closer
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with Wall

    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        scoreboard.reset()
        snake.reset()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()

screen.exitonclick()

