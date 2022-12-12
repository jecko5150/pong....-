from turtle import Turtle

STARTING_POSITIONS = [(350, 0), (-350, 0)]

UP = 90
DOWN = 270


class Paddle:
    def __init__(self):
        self.segments = []
        self.position_paddles()
        self.right = self.segments[0]
        self.left = self.segments[1]

    def position_paddles(self):
        for position in STARTING_POSITIONS:
            self.make_paddle(position)

    def make_paddle(self, position):
        new_paddle = Turtle('square')
        new_paddle.color("white")
        new_paddle.penup()
        new_paddle.resizemode('user')
        new_paddle.setheading(90)
        new_paddle.shapesize(stretch_wid=2, stretch_len=10)
        new_paddle.goto(position)
        self.segments.append(new_paddle)
