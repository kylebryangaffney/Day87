# main.py

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from brick import Brick
import time

# Initialize screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Brick Game 9000")
screen.tracer(0)

# Initialize game objects
paddle = Paddle()
ball = Ball()
scoreboard = Scoreboard()

# Create bricks
brick_list = []

def create_bricks():
    for x in range(-350, 351, 100):
        for y in range(250, 150, -30):
            brick = Brick()
            brick.goto(x, y)
            brick_list.append(brick)

def reset_game():
    global is_running
    ball.reset_position()
    paddle.reset_position()
    scoreboard.reset()
    create_bricks()
    is_running = True

create_bricks()

# Key bindings
screen.listen()
screen.onkey(paddle.go_left, "Left")
screen.onkeypress(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")
screen.onkeypress(paddle.go_right, "Right")
screen.onkey(reset_game, "r")

# Game loop
is_running = True
while is_running:
    time.sleep(0.05)
    screen.update()
    ball.travel()

    # Ball collisions with walls
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.x_bounce()
    if ball.ycor() > 280:
        ball.y_bounce()
    
    # Ball collisions with bricks
    for brick in brick_list:
        if ball.distance(brick) < 35:
            ball.y_bounce()
            scoreboard.score_point()
            brick.goto(1000, 1000)  # Move the brick out of screen
            brick_list.remove(brick)
            break

    # Check if all bricks are broken
    if not brick_list:
        is_running = False
        scoreboard.game_over()
    
    # Ball collisions with paddle
    if ball.ycor() < -260 and paddle.distance(ball) < 50:
        ball.y_bounce()
    elif ball.ycor() < -280:
        ball.reset_position()
        scoreboard.lose_life()
    if scoreboard.lives <= 0:
        is_running = False
        scoreboard.game_over()

screen.exitonclick()
