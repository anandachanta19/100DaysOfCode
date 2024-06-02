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

guessed_states = []
while len(guessed_states) < 50:
    answer = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?")
    answer = answer.title()

    if answer == "Exit":
        missing_states = [state for state in states if state not in guessed_states]
        missing_data = pandas.DataFrame(missing_states)
        missing_data.to_csv("States to learn.csv")
        break

    if answer in states:
        guessed_states.append(answer)
        index = states.index(answer)
        write_state(x_cor[index], y_cor[index], states[index])
    else:
        break
screen.exitonclick()
