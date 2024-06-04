import tkinter

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#94B0A2"
YELLOW = "#f7f5dd"
DARK = "#2F4858"
FONT_NAME = "Impact"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK = "✔"


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    pass


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start():
    pass


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=DARK)

# State
timer = tkinter.Label(text="TIMER", fg=YELLOW, bg=DARK, font=(FONT_NAME, 30, "bold"))
timer.grid(row=0, column=1)

# Start
start = tkinter.Button(text="START", command=start, font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=DARK,
                       highlightthickness=0)
start.grid(row=2, column=0)

# Reset
reset = tkinter.Button(text="RESET", command=reset, font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=DARK,
                       highlightthickness=0)
reset.grid(row=2, column=3)

# Check
check = tkinter.Label(text=CHECK, font=(FONT_NAME, 15, "bold"), fg="green", bg=DARK)
check.grid(row=2, column=1)

# Image
canvas = tkinter.Canvas(width=220, height=223, bg=DARK, highlightthickness=0)
photo = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(112, 111, image=photo)
canvas.create_text(112, 130, text="00 : 00", fill=YELLOW, font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)

window.mainloop()
