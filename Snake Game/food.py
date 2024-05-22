from turtle import Turtle
import random
X = (-280, 280)
Y = (-280, 280)


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.food = None
        self.create_food()
        self.position()

    def create_food(self):
        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.pu()

    def position(self):
        self.setpos(x=random.randint(X[0], X[1]), y=random.randint(Y[0], Y[1]))
