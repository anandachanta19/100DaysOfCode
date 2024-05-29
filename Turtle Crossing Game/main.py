import time
from turtle import Screen
from carManager import CarManager
from player import Player
from scoreBoard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)
car_manager = CarManager()
player = Player()
score_board = Scoreboard()
screen.listen()
screen.onkey(fun=player.move, key="w")

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    for car in car_manager.all_cars:
        if player.distance(car) < 22:
            score_board.game_over()
            is_game_on = False
    if player.ycor() >= 300:
        score_board.update_score()
        player.new_level()
        car_manager.increase_speed()


screen.exitonclick()
