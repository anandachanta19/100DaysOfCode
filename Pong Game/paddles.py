from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, coordinates):
        super().__init__()
        self.positions = coordinates
        self.create_paddle()

    def create_paddle(self):
        self.pu()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setheading(90)
        self.color("white")
        self.speed("fastest")
        self.goto(self.positions)

    def up(self):
        if self.ycor() >= 225:
            self.forward(0)
        else:
            if self.heading() != 90:
                self.setheading(90)
            self.forward(30)

    def down(self):
        if self.ycor() <= -225:
            self.forward(0)
        else:
            if self.heading() != 270:
                self.setheading(270)
            self.forward(30)
