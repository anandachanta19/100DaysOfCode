from turtle import Turtle

FONT = ("Courier", 18, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 1
        self.create_scoreboard()

    def create_scoreboard(self):
        self.pu()
        self.setpos(x=-230, y=270)
        self.ht()
        self.color("black")
        self.write(arg=f"Level: {self.score}", move=False, align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", move=False, align="center", font=FONT)

    def update_score(self):
        self.score += 1
        self.undo()
        self.write(arg=f"Level: {self.score}", move=False, align="center", font=FONT)