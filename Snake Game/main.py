from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = Scoreboard()
screen.listen()
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
screen.onkey(snake.up, "Up")
is_gameon = True
while is_gameon:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detection of food collision
    if snake.head.distance(food) < 15:
        score_board.update_score()
        snake.grow()
        food.position()

screen.exitonclick()
