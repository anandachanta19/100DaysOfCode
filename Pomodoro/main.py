import tkinter
import time

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
reps = 0
pomo_timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global reps, pomo_timer
    window.after_cancel(pomo_timer)
    canvas.itemconfig(countdown, text="00 : 00")
    check.config(text="")
    timer.config(text="POMODORO", fg=YELLOW)
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        timer.config(text="LONG-BREAK", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        timer.config(text="SHORT-BREAK", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
    else:
        timer.config(text="WORK-TIME", fg=GREEN)
        count_down(WORK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global pomo_timer
    count_min = int(count / 60)
    count_sec = count % 60
    if len(str(count_sec)) == 1:
        count_sec = "0" + str(count_sec)
    if len(str(count_min)) == 1:
        count_min = "0" + str(count_min)
    canvas.itemconfig(countdown, text=f"{count_min} : {count_sec}")
    if count > 0:
        pomo_timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        status = ""
        work_sessions = int(reps / 2)
        for _ in range(work_sessions):
            status += CHECK
        check.config(text=status)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=DARK)

# State
timer = tkinter.Label(text="POMODORO", fg=YELLOW, bg=DARK, font=(FONT_NAME, 30, "bold"))
timer.grid(row=0, column=1)

# Start
start = tkinter.Button(text="START", command=start_timer, font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=DARK,
                       highlightthickness=0)
start.grid(row=2, column=0)

# Reset
reset = tkinter.Button(text="RESET", command=reset, font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=DARK,
                       highlightthickness=0)
reset.grid(row=2, column=3)

# Check
check = tkinter.Label(text="", font=(FONT_NAME, 15, "bold"), fg="green", bg=DARK)
check.grid(row=2, column=1)

# Image
canvas = tkinter.Canvas(width=220, height=223, bg=DARK, highlightthickness=0)
photo = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(112, 111, image=photo)
countdown = canvas.create_text(112, 130, text="00 : 00", fill=YELLOW, font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)

window.mainloop()
