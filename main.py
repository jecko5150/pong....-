import time
from turtle import Screen

from Scoreboard import Scoreboard
from ball import Ball
from paddle import Paddle
import turtle

# Screen setup
screen = Screen()
screen.setup(800, 600)
screen.bgcolor('black')
screen.title('Pong!')
screen.tracer(0)

paddle = Paddle()
ball = Ball()

# Control the paddles 
screen.listen()
screen.onkeypress(fun=paddle.move_up, key="Up")
screen.onkeypress(fun=paddle.move_down, key="Down")
screen.onkeypress(fun=paddle.move_up_l, key="w")
screen.onkeypress(fun=paddle.move_down_l, key="x")

# Players.... 
player_1 = Scoreboard('Player 1', [240, 260])
player_2 = Scoreboard('Player 2', [-240, 260])

# The game
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #  Detect wall

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # Detect Paddle
    
    if ball.distance(paddle.right) < 50 and ball.xcor() > 320:
        ball.hit()
        ball.bounce()

    elif ball.distance(paddle.left) < 50 and ball.xcor() < -320:
        ball.hit()
        ball.bounce()

    # Keeping track of score 
    if ball.xcor() > 380:
        ball.start_game()
        player_2.increase_score()
    if ball.xcor() < -380:
        player_1.increase_score()
        ball.start_game()

screen.exitonclick()
