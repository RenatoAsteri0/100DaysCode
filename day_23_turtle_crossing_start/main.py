import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

#Chama o Placar
placar = Scoreboard()

#criar o jogador
jogador = Player()
screen.listen()
screen.onkey(jogador.subir, "Up")
screen.onkey(jogador.descer, "Down")

#Chama os carros
car = CarManager()
tempo_ultimo_carro = time.time()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.criar_carros()

    for carro in car.carros:
        if jogador.distance(carro) < 20:
            placar.game_over()
            game_is_on = False

    if jogador.is_player_finished():
        placar.avancou()
        jogador.player_goto_start()
        car.avancou()

    car.mover_carros()