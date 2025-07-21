from turtle import Screen
import time
from paddle import Paddle
from placar import Placar
from ball import Ball

#posições jogadores
STARTING_POSITION_JOGADOR1 = (-350, 0)
STARTING_POSITION_JOGADOR2 = (350, 0)

#posições placares
STARTING_POSITION_PLACAR1 = (-330,200)
STARTING_POSITION_PLACAR2 = (330,200)

#1
screen = Screen()
screen.bgcolor('black')
screen.title('pong')
screen.setup(width=800, height=600)
screen.tracer(0)

jogador1 = Paddle(STARTING_POSITION_JOGADOR1)
jogador2 = Paddle(STARTING_POSITION_JOGADOR2)
placar1 = Placar(STARTING_POSITION_PLACAR1)
placar2 = Placar(STARTING_POSITION_PLACAR2)
ball = Ball(10,10)

screen.listen()
screen.onkey(jogador1.subir, "w")
screen.onkey(jogador1.descer, "s")
screen.onkey(jogador2.subir, "Up")
screen.onkey(jogador2.descer, "Down")
screen.onkey(placar1.atualizar_placar, "a")
screen.onkey(placar2.atualizar_placar, "l")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.mover()

    #detectar colisao com a parede
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detectar colisao com o jogador2 e com jogador1
    if ball.distance(jogador2) < 50 and ball.xcor() > 320 or ball.distance(jogador1) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #detectar se a bola saiu do campo jogador2
    if ball.xcor() > 390:
        placar1.atualizar_placar()
        ball = Ball(10,10)

    #detectar se a bola saiu do campo jogador1
    if ball.xcor() < -390:
        placar2.atualizar_placar()
        ball = Ball(-10,10)




screen.exitonclick()