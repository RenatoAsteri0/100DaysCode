from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.setheading(90)
        self.player_goto_start()

    def subir(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)
    def descer(self):
        new_y = self.ycor() - 10
        self.goto(self.xcor(), new_y)

    def player_goto_start(self):
        self.goto(0,-300)

    def is_player_finished(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
