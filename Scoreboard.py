import turtle
from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as data:
            self.high_score = int(data.read())
        self.penup()
        self.ht()
        self.color('white')
        self.setpos(160.00, 260.00)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score}', align='center', font=("courier", 12, 'normal'))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as f:
                f.write(f"{self.score}")
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f'GAME OVER\nScore: {self.score} High Score: {self.high_score}', align="center",
                   font=('courier', 18, 'normal')
                   )


class PlayerName(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.ht()
        self.color('white')
        self.setpos(-210, 260)
        name = turtle.textinput("", "Enter Player Name")
        self.write(f"Player: {name}", align="center", font=('courier', 12, 'normal'))
