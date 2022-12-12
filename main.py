from turtle import Screen
from right import Paddle
import turtle

screen = Screen()
screen.setup(800, 600)
screen.bgcolor('black')
screen.title('Pong!')
paddles = Paddle()

screen.listen()




screen.exitonclick()
