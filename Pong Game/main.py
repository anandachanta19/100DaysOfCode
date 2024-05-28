from turtle import Screen
from paddles import Paddle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=900, height=700)
screen.title("Pong Game")
screen.tracer(0)
paddle_1 = Paddle()
paddle_1.setpos(x=-440, y=0)
paddle_2 = Paddle()
paddle_2.setpos(x=435, y=0)
screen.listen()
screen.onkey(fun=paddle_2.up, key="Up")
screen.onkey(fun=paddle_2.down, key="Down")
screen.onkey(fun=paddle_1.up, key="w")
screen.onkey(fun=paddle_1.down, key="s")

is_game_on = True
while is_game_on:
    screen.update()

screen.exitonclick()
