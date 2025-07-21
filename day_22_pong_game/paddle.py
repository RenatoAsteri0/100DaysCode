from turtle import Turtle

class Paddle(Turtle):
    
    
    def __init__(self, start_positions):
        super().__init__()
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.shape('square')
        self.color('white')
        self.penup()
        self.goto(start_positions)


    def subir(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
    
    def descer(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

