from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=500)
userBet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the color: ")

y = [-80, -40, 0, 40, 80, 120]
colors = ["violet", "blue", "green", "yellow", "orange", "red"]
turtles = []
distances = [0, 0, 0, 0, 0, 0]
for i in range(6):
    t1 = Turtle()
    t1.pu()
    t1.shape("turtle")
    t1.color(colors[i])
    t1.goto(-250.0, y[i])
    turtles.append(t1)

color = ""
maxDistance = 0
while maxDistance < 500:
    for i in range(6):
        distance = random.randint(0, 20)
        distances[i] += distance
        turtles[i].forward(distance)
        maxDistance = max(distances[i], maxDistance)
        if maxDistance >= 500:
            color = turtles[i].fillcolor()
            break

if color == userBet:
    print(f"Nice Bet! {userBet.capitalize()} turtle wins.")
else:
    print(f"You loose. {color.capitalize()} turtle wins the race.")
screen.exitonclick()
