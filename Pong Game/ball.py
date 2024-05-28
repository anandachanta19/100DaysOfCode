from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.create_ball()
        self.x_move = 10
        self.y_move = 10
        self.move()

    def create_ball(self):
        self.pu()
        self.color("red")
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.setheading(random.randint(10, 45))

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move = -1 * self.y_move

    def bounce_x(self):
        self.x_move = -1 * self.x_move