import tkinter

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Arial"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
# window.minsize(width=600, height=600)
window.config(padx=100, pady=100, bg=YELLOW)

canvas = tkinter.Canvas(width=220, height=223, bg=YELLOW, highlightthickness=0)
photo = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(112, 111, image=photo)
canvas.create_text(112, 130, text="00:00", fill=YELLOW, font=(FONT_NAME, 40, "bold"))
canvas.pack()
window.mainloop()
