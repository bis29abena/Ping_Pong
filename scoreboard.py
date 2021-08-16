from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score_l = 0
        self.score_r = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-100, 260)
        self.write(self.score_l, align="center", font=("Arial", 20, "normal"))
        self.goto(100, 260)
        self.write(self.score_r, align="center", font=("Arial", 20, "normal"))

    def l_score(self):
        self.score_l += 1
        self.update()

    def r_score(self):
        self.score_r += 1
        self.update()