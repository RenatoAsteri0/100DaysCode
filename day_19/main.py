from turtle import Turtle, Screen


# Configurar a tela
tela = Screen()
tela.setup(width=500, height=400)
user_escolha = tela.textinput(title='faça a sua aposta', prompt='Qual tartaruga vai vencer a corrida? escolha uma cor')

# Dados das tartarugas
data = [
    {"cor": "red", "posicao": -50},
    {"cor": "orange", "posicao": -100},
    {"cor": "yellow", "posicao": 0},
    {"cor": "green", "posicao": 50},
    {"cor": "blue", "posicao": 100},
    {"cor": "purple", "posicao": 150}
]

tartarugas = []

# Criar e posicionar cada tartaruga
for info in data:
    tartaruga = Turtle(shape="turtle")
    tartaruga.color(info['cor'])
    tartaruga.penup()
    tartaruga.goto(x=-250, y=info["posicao"])
    tartarugas.append(tartaruga)

# Espera clique para fechar a tela
tela.exitonclick()
