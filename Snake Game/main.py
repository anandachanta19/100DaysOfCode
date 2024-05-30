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
        snake.extend()
        food.position()

    # Detection of wall collision
    if snake.head.xcor() >= 295 or snake.head.ycor() >= 295 or snake.head.xcor() <= -295 or snake.head.ycor() <= -295:
        answer = screen.textinput(prompt="wanna play again? (yes/no):", title="Game Over")
        if answer == "yes":
            score_board.game_reset()
            snake.snake_reset()
        else:
            score_board.game_over()
            is_gameon = False

    # Detection of snake segment collision
    for segment in snake.segments[1::]:
        if snake.head.distance(segment) < 11:
            answer = screen.textinput(prompt="wanna play again? (yes/no):", title="Game Over")
            if answer == "yes":
                score_board.game_reset()
                snake.snake_reset()
            else:
                score_board.game_over()
                is_gameon = False

screen.exitonclick()
