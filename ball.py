from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("white")
        self.setpos(0, 0)
        self.x_move = random.randint(5, 10)
        self.y_move = random.randint(5, 10)
        self.move_speed = .1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= - 1

    def hit(self):
        self.x_move *= -1
        self.move_speed *= .8

    def start_game(self):
        self.home()
        start = [-1, 1]
        self.x_move *= random.choice(start)
        self.move_speed = .1
