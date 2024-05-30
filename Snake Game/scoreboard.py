from turtle import Turtle

FONT = ("Courier", 18, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.file = open("highscore.txt", 'r')
        self.highscore = int(self.file.read())
        self.file.close()
        self.create_scoreboard()

    def create_scoreboard(self):
        self.pu()
        self.setpos(x=0, y=270)
        self.ht()
        self.color("white")
        self.write(arg=f"Score: {self.score} Highscore: {self.highscore}", move=False, align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", move=False, align="center", font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.setpos(x=0, y=270)
        self.write(arg=f"Score: {self.score} Highscore: {self.highscore}", move=False, align="center", font=FONT)

    def game_reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.file = open("highscore.txt", 'w')
            self.file.write(str(self.highscore))
            self.file.close()
        self.score = 0
        self.update_score()
