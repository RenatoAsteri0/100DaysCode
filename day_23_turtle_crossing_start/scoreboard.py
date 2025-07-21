from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.pontos = 1
        self.penup()
        self.color('black')
        self.hideturtle()
        self.goto(-280, 280)
        self.write(f'Nivel: {self.pontos}', font=FONT)

    def avancou(self):
        self.pontos += 1
        self.clear()
        self.write(f'Nível: {self.pontos}', font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write('game over')