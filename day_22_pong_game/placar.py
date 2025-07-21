from turtle import Turtle
FONTE = ('Arial', 24, 'normal')

class Placar(Turtle):
    def __init__(self, start_positions):
        super().__init__()
        self.pontos = 0
        self.penup()
        self.color('white')
        self.hideturtle()
        self.goto(start_positions)
        self.clear()
        self.write(self.pontos, False, 'center', FONTE)

    def atualizar_placar(self):
        self.pontos += 1
        self.clear()
        self.write(self.pontos, False, 'center', FONTE)

