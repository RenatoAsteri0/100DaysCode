from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.ler_hight_score()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.ler_hight_score()}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.ler_hight_score():
            self.escrever_high_score_file(self.score)
            self.score = 0
            self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def ler_hight_score(self):
        with open("data.txt", "r") as file:
            valor_atual = int(file.read())
            return valor_atual

    def escrever_high_score_file(self, score):
        with open("data.txt", "w") as file:
            file.write(str(score))
