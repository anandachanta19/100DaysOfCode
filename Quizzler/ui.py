import time
import tkinter
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
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
            width=280,
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
            borderwidth=0,
            command=lambda: self.get_next_question(True)
        )
        self.cross = tkinter.Button(
            image=self.cross_photo,
            highlightthickness=0,
            relief="flat",
            borderwidth=0,
            command=lambda: self.get_next_question(False)
        )
        self.tick.grid(row=2, column=0)
        self.cross.grid(row=2, column=1)
        self.get_next_question(False)
        self.window.mainloop()

    def get_next_question(self, answer):
        try:
            if self.quiz.check_answer(str(answer)):
                self.score += 1
                self.scoreboard.config(text=f"Score:{self.score}")
                self.give_feedback("green")
            else:
                self.give_feedback("red")
        except AttributeError:
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        except IndexError:
            print("Questions have been completed")

    def give_feedback(self, color):
        self.canvas.config(bg=color)
        self.window.after(1000, self.change_color)

    def change_color(self):
        self.canvas.config(bg="white")
        try:
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        except IndexError:
            self.canvas.itemconfig(self.question, text=f"No more questions. Your Final score is: {self.score}")
            self.tick.config(state="disabled")
            self.cross.config(state="disabled")
