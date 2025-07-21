import turtle
import random
from turtle import Turtle, Screen

# Lista de cores RGB extraídas da imagem
cores_imagem = [
    (213, 154, 96), (51, 107, 132), (202, 142, 31), (180, 77, 30), (115, 155, 171),
    (124, 79, 99), (122, 175, 156), (230, 236, 239), (226, 198, 131), (241, 247, 243),
    (192, 87, 108), (10, 50, 64), (55, 38, 18), (44, 168, 126), (47, 127, 123),
    (200, 121, 143), (168, 21, 29), (228, 92, 77), (244, 162, 160), (38, 32, 35),
    (2, 26, 25), (78, 148, 171), (169, 23, 18), (101, 126, 159), (17, 79, 91),
    (236, 165, 169), (178, 204, 185), (49, 62, 84), (184, 190, 202), (166, 203, 207),
    (79, 68, 42), (11, 113, 110)
]

# Configurações iniciais
turtle.colormode(255)
timmy = Turtle()
timmy.speed("fastest")
timmy.hideturtle()
timmy.penup()

# Parâmetros da grade
num_colunas = 10
num_linhas = 10
tamanho_ponto = 20
espaco = 50

# Posição inicial
start_x = -250
start_y = -250

# Desenha a grade de pontos
for linha in range(num_linhas):
    for coluna in range(num_colunas):
        x = start_x + coluna * espaco
        y = start_y + linha * espaco
        timmy.teleport(x, y)
        timmy.dot(tamanho_ponto, random.choice(cores_imagem))

# Finaliza
screen = Screen()
screen.exitonclick()
