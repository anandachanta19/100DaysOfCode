from turtle import Turtle
import random

COLORS = ['red', 'green', 'blue', 'yellow', 'violet', 'pink', 'orange', 'brown']
LANES = [-225, -200, -175, -150, -125, -100, -75, -50, -25, 0, 25, 50, 75, 100, 125, 150, 175, 200, 225]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 3


class CarManager:

    def __init__(self):
        self.movement = STARTING_MOVE_DISTANCE
        self.all_cars = []

    def create_car(self):
        probability_number = random.randint(1, 8)
        if probability_number == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.pu()
            new_car.color(random.choice(COLORS))
            new_car.setpos(x=300, y=random.choice(LANES))
            new_car.setheading(180)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.movement)

    def increase_speed(self):
        self.movement += MOVE_INCREMENT