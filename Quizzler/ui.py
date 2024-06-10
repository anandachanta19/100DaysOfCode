import tkinter

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self):
        self.score = 0
        # Window Creation
        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        # ScoreBoard Creation
        self.scoreboard = tkinter.Label(
            text=f"Score:{self.score}",
            bg=THEME_COLOR,
            fg="white",
            font=("Arial", 15, "normal")
        )
        self.scoreboard.grid(row=0, column=1)
        # Question Display
        self.canvas = tkinter.Canvas(width=300, height=250)
        self.question = self.canvas.create_text(
            150,
            125,
            text="Question goes here",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.tick_photo = tkinter.PhotoImage(file="images/true.png")
        self.cross_photo = tkinter.PhotoImage(file="images/false.png")
        self.tick = tkinter.Button(
            image=self.tick_photo,
            highlightthickness=0,
            relief="flat",
            borderwidth=0
        )
        self.cross = tkinter.Button(
            image=self.cross_photo,
            highlightthickness=0,
            relief="flat",
            borderwidth=0
        )
        self.tick.grid(row=2, column=0)
        self.cross.grid(row=2, column=1)
        self.window.mainloop()
