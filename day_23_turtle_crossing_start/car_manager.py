from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 50


class CarManager():

    def __init__(self):
        self.carros = []
        self.velocidade = STARTING_MOVE_DISTANCE
        self.diminuir_chances = 6

    def criar_carros(self):
        random_change = random.randint(1,self.diminuir_chances)
        if random_change == 1:
            novo_carro = Turtle()
            novo_carro.shapesize(stretch_wid=1, stretch_len=2)
            novo_carro.penup()
            novo_carro.shape('square')
            novo_carro.color(random.choice(COLORS))
            y_position = random.randint(-250, 250)
            novo_carro.goto(300, y_position)
            self.carros.append(novo_carro)

    def mover_carros(self):
        for carro in self.carros:
            carro.backward(self.velocidade)

    def avancou(self):
        self.velocidade += MOVE_INCREMENT
        self.diminuir_chances -= 1
