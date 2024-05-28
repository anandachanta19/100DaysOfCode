from turtle import Screen
from ball import Ball
from paddles import Paddle
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)
paddle_1 = Paddle((-355, 0))
paddle_2 = Paddle((350, 0))
ball = Ball()
p1_score = Scoreboard((-80, 200))
p2_score = Scoreboard((80, 200))
screen.listen()
screen.onkey(fun=paddle_2.up, key="Up")
screen.onkey(fun=paddle_2.down, key="Down")
screen.onkey(fun=paddle_1.up, key="w")
screen.onkey(fun=paddle_1.down, key="s")

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle_2) < 50 and ball.xcor() > 340:
        p2_score.update_score()
        ball.bounce_x()

    if ball.distance(paddle_1) < 50 and ball.xcor() < -345:
        p1_score.update_score()
        ball.bounce_x()

    if ball.xcor() >= 390 or ball.xcor() <= -395:
        p1_score.game_over()
        p2_score.game_over()
        is_game_on = False

screen.exitonclick()
