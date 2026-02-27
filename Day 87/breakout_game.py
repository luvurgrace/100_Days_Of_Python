import turtle
import time

# Screen setup
screen = turtle.Screen()
screen.title("Breakout")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Game variables
score = 0
lives = 3
speed = 3
bricks_per_row = 10
total_rows = 5
rows_destroyed = 0

# Paddle
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, -230)
ball.dx = speed
ball.dy = speed

# Score display
score_display = turtle.Turtle()
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)


def update_score():
    score_display.clear()
    score_display.write(f"Score: {score}  Lives: {lives}  Speed: {speed}",
                        align="center", font=("Arial", 16, "normal"))


# Create bricks
bricks = []
colors = ["red", "orange", "yellow", "green", "blue"]

for row in range(total_rows):
    for col in range(bricks_per_row):
        brick = turtle.Turtle()
        brick.shape("square")
        brick.color(colors[row])
        brick.shapesize(stretch_wid=1, stretch_len=3)
        brick.penup()
        x = -350 + col * 75
        y = 200 - row * 30
        brick.goto(x, y)
        brick.row = row  # Remember which row
        bricks.append(brick)

# Track bricks per row
row_counts = {row: bricks_per_row for row in range(total_rows)}


def increase_speed():
    """Increase ball speed"""
    global speed
    speed += 0.5

    # Update ball direction with new speed
    ball.dx = speed if ball.dx > 0 else -speed
    ball.dy = speed if ball.dy > 0 else -speed

    update_score()

    # Show speed up message
    msg = turtle.Turtle()
    msg.color("yellow")
    msg.penup()
    msg.hideturtle()
    msg.write("SPEED UP!", align="center", font=("Arial", 20, "bold"))
    screen.update()
    time.sleep(0.5)
    msg.clear()


# Paddle movement
def paddle_left():
    x = paddle.xcor()
    if x > -350:
        paddle.setx(x - 30)


def paddle_right():
    x = paddle.xcor()
    if x < 350:
        paddle.setx(x + 30)


# Keyboard bindings
screen.listen()
screen.onkeypress(paddle_left, "Left")
screen.onkeypress(paddle_right, "Right")
screen.onkeypress(paddle_left, "a")
screen.onkeypress(paddle_right, "d")

# Game loop
update_score()
game_running = True

while game_running:
    screen.update()
    time.sleep(0.01)

    # Move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Wall collision (left/right)
    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.dx *= -1

    # Wall collision (top)
    if ball.ycor() > 290:
        ball.dy *= -1

    # Ball falls down
    if ball.ycor() < -290:
        lives -= 1
        update_score()

        if lives <= 0:
            score_display.clear()
            score_display.write(f"GAME OVER! Final Score: {score}",
                                align="center", font=("Arial", 30, "bold"))
            game_running = False
        else:
            ball.goto(0, -230)
            ball.dx = speed if ball.dx > 0 else -speed
            ball.dy = speed
            time.sleep(1)

    # Paddle collision
    if (ball.ycor() < -240 and ball.ycor() > -250 and
            ball.xcor() < paddle.xcor() + 50 and ball.xcor() > paddle.xcor() - 50):
        ball.dy *= -1
        ball.sety(-230)

    # Brick collision
    for brick in bricks[:]:
        if (abs(ball.xcor() - brick.xcor()) < 35 and
                abs(ball.ycor() - brick.ycor()) < 15):
            ball.dy *= -1

            # Track row destruction
            row = brick.row
            row_counts[row] -= 1

            # Check if row is fully destroyed
            if row_counts[row] == 0:
                rows_destroyed += 1
                increase_speed()

            brick.hideturtle()
            bricks.remove(brick)
            score += 10
            update_score()

    # Win condition
    if len(bricks) == 0:
        score_display.clear()
        score_display.write(f"YOU WIN! Score: {score}",
                            align="center", font=("Arial", 30, "bold"))
        game_running = False

screen.mainloop()