from turtle import Turtle

class WhiteLine(Turtle):
    def __init__(self, degree, distance):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.setheading(degree)
        self.forward(distance)




