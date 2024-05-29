from turtle import Turtle
import random

COLORS = ['red', 'green', 'blue', 'yellow', 'firebrick', 'ForestGreen', 'orange', 'brown']



class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.create_car()

    def create_car(self):
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.pu()
        self.color(random.choice(COLORS))


