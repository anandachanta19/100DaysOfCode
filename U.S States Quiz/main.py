from turtle import Screen, Turtle
import pandas

FONT = ("Arial", 8, "normal")


def write_state(x, y, st):
    new = Turtle()
    new.pu()
    new.ht()
    new.goto(x=x, y=y)
    new.write(arg=f"{st}", move=False, align="center", font=FONT)


screen = Screen()
turtle = Turtle()
screen.title("U.S States Quiz")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

data = pandas.read_csv("50_states.csv")
states = data["state"].tolist()
x_cor = data["x"].tolist()
y_cor = data["y"].tolist()

count = 0
while count < len(states):
    answer = screen.textinput(title=f"{count}/50 States Correct", prompt="What's another state's name?")
    answer = answer.title()
    if answer in states:
        index = states.index(answer)
        write_state(x_cor[index], y_cor[index], states[index])
        count += 1
    else:
        break
screen.exitonclick()
