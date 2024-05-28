from turtle import Turtle

FONT = ("roboto", 50, "normal")


class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.create_scoreboard(position)

    def create_scoreboard(self, pos):
        self.pu()
        self.setpos(pos[0], pos[1])
        self.ht()
        self.color("white")
        self.write(arg=f"{self.score}", move=False, align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER.", move=False, align="center", font=FONT)

    def update_score(self):
        self.score += 1
        self.undo()
        self.write(arg=f"{self.score}", move=False, align="center", font=FONT)
