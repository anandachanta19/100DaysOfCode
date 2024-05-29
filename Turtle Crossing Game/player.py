from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.create_player()

    def create_player(self):
        self.shape("turtle")
        self.pu()
        self.setheading(90)
        self.setpos(x=0, y=-280)

    def move(self):
        self.forward(10)

    def new_level(self):
        self.setpos(x=0, y=-280)