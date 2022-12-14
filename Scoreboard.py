from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, name, position):
        super().__init__()
        self.score = 0
        self.penup()
        self.ht()
        self.color('white')
        self.name = name
        self.position = position
        self.score = 0
        self.points()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f'{self.name} Score: {self.score}', align='center', font=("courier", 12, 'normal'))

    def points(self):
        self.goto(self.position)
        self.write(f'{self.name} Score: {self.score}', align='center', font=("courier", 12, 'normal'))
