import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
turtle.colormode(255)
timmy.speed('fastest')

direction = [0, 90, 180, 270]
def different_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color
def draw_spirograph(gap):
    for _ in range(int(360 / gap)):
        timmy.color(different_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + gap)
draw_spirograph(0.5)

screen = Screen()
screen.exitonclick()