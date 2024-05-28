from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.create_ball()
        self.move()

    def create_ball(self):
        self.pu()
        self.color("white")
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.setheading(random.randint(10, 45))

    def move(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)
        if self.ycor() >= 295 or self.ycor() <= -295:
            self.setheading(self.heading() + 90)
        if self.xcor() >= 395 or self.xcor() <= -395:
            self.setheading(self.heading() + 90)