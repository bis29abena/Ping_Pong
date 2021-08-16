from turtle import Screen
from Paddles import Paddle
from Ball import Ball
from scoreboard import Score
from screen import WhiteLine
import time

# Setting Up the screen for the game
screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("Black")
screen.title("PONG GAME")
screen.tracer(0)
screen.listen()

# Creating the turtle, the size and position of the turtle
r_paddle = Paddle(position=(350, 0))
l_paddle = Paddle(position=(-350, 0))
ball = Ball()
score = Score()
white_line = WhiteLine(90, 300)
white_line_ = WhiteLine(270, 300)

# Left Paddle Movement Using Up and Down
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

# Right paddle movement using the W for Up and S for Down
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

is_game_on = True

while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision of the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect when r_paddle misses
    if ball.xcor() > 400:
        ball.restart()
        score.l_score()

    # Detect when l_padded miss
    if ball.xcor() < -400:
        ball.restart()
        score.r_score()

screen.exitonclick()
