from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.create_paddle()

    def create_paddle(self):
        self.pu()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setheading(90)
        self.color("white")
        self.speed("fastest")

    def up(self):
        if self.heading() != 90:
            self.setheading(90)
        self.forward(30)

    def down(self):
        if self.heading() != 270:
            self.setheading(270)
        self.forward(30)
