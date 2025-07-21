from turtle import Turtle

class Ball(Turtle):

    def __init__(self, direcao_x, direcao_y):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_mover = direcao_x
        self.y_mover = direcao_y


    def mover(self):
        new_x = self.xcor() + self.x_mover
        new_y = self.ycor() + self.y_mover
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_mover *= -1

    def bounce_x(self):
        self.x_mover *= -1


    def apagar(self):
        self.clear()