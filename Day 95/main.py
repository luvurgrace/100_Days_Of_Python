"""
Space Invaders - Simple Version
Controls: Left/Right arrows, Space to shoot, Q to quit
"""

import turtle

# Setup
screen = turtle.Screen()
screen.title("Space Invaders")
screen.bgcolor("black")
screen.setup(800, 600)
screen.tracer(0)

score = 0
game_over = False

# Player
player = turtle.Turtle()
player.shape("triangle")
player.color("green")
player.penup()
player.goto(0, -250)
player.setheading(90)

# Bullet
bullet = turtle.Turtle()
bullet.shape("square")
bullet.color("yellow")
bullet.shapesize(0.5, 0.2)
bullet.penup()
bullet.hideturtle()
bullet_active = False

# Aliens
aliens = []
for row in range(3):
    for col in range(8):
        alien = turtle.Turtle()
        alien.shape("turtle")
        alien.color("red")
        alien.penup()
        alien.goto(-250 + col * 60, 200 - row * 50)
        aliens.append(alien)

alien_dir = 1

# Score display
score_text = turtle.Turtle()
score_text.color("white")
score_text.penup()
score_text.hideturtle()
score_text.goto(-380, 260)
score_text.write(f"Score: {score}", font=("Arial", 16, "normal"))


# Controls
def move_left():
    if player.xcor() > -380:
        player.setx(player.xcor() - 20)

def move_right():
    if player.xcor() < 380:
        player.setx(player.xcor() + 20)

def shoot():
    global bullet_active
    if not bullet_active:
        bullet_active = True
        bullet.goto(player.xcor(), player.ycor() + 10)
        bullet.showturtle()

screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.onkeypress(shoot, "space")


# Game loop
while not game_over:
    screen.update()

    # Move bullet
    if bullet_active:
        bullet.sety(bullet.ycor() + 15)
        if bullet.ycor() > 300:
            bullet_active = False
            bullet.hideturtle()

    # Move aliens
    move_down = False
    for alien in aliens:
        if alien.isvisible():
            if alien.xcor() > 360 or alien.xcor() < -360:
                move_down = True
                break

    if move_down:
        alien_dir *= -1
        for alien in aliens:
            if alien.isvisible():
                alien.sety(alien.ycor() - 30)

    for alien in aliens:
        if alien.isvisible():
            alien.setx(alien.xcor() + 2 * alien_dir)

            # Alien reaches player = game over
            if alien.ycor() < -220:
                game_over = True

            # Bullet hits alien
            if bullet_active and bullet.distance(alien) < 25:
                alien.hideturtle()
                bullet_active = False
                bullet.hideturtle()
                score += 10
                score_text.clear()
                score_text.write(f"Score: {score}", font=("Arial", 16, "normal"))

    # Win check
    if all(not a.isvisible() for a in aliens):
        score_text.goto(0, 0)
        score_text.write("YOU WIN!", align="center", font=("Arial", 36, "bold"))
        break

    import time
    time.sleep(0.02)

# Game over
if game_over:
    score_text.goto(0, 0)
    score_text.write("GAME OVER", align="center", font=("Arial", 36, "bold"))

screen.mainloop()