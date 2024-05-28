from turtle import Screen
from ball import Ball
from paddles import Paddle
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)
paddle_1 = Paddle((-355, 0))
paddle_2 = Paddle((350, 0))
ball = Ball()
screen.listen()
screen.onkey(fun=paddle_2.up, key="Up")
screen.onkey(fun=paddle_2.down, key="Down")
screen.onkey(fun=paddle_1.up, key="w")
screen.onkey(fun=paddle_1.down, key="s")

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    if paddle_1.distance(ball) <= 30 or paddle_2.distance(ball) <= 30:
        ball.setheading(ball.heading() + 90)
    ball.move()

screen.exitonclick()
