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
move_speed = 0.1
count = 0

is_game_on = True
while is_game_on:
    if count == 5:
        count = 0
        move_speed = 0.1
    time.sleep(move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle_2) < 60 and ball.xcor() > 320:
        ball.bounce_x()

    if ball.distance(paddle_1) < 60 and ball.xcor() < -325:
        ball.bounce_x()

    if ball.xcor() >= 390 and move_speed > 0:
        p1_score.update_score()
        count += 1
        move_speed *= 0.9
        ball.reset_position()

    if ball.xcor() <= -395 and move_speed > 0:
        p2_score.update_score()
        move_speed *= 0.9
        count += 1
        ball.reset_position()

screen.exitonclick()
