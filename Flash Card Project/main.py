import tkinter
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_1 = ("Ariel", 40, "italic")
FONT_2 = ("Ariel", 60, "bold")

# Working with data
data = pandas.read_csv("data/french_words.csv")
words = data.to_dict(orient="records")
new_word ={}


def reveal():
    global new_word
    canvas.itemconfig(card_front, image=back)
    canvas.itemconfig(name, fill="white", text="English")
    canvas.itemconfig(word, fill="white", text=new_word["English"])


def generate_flashcard():
    global new_word, flip_timer
    window.after_cancel(flip_timer)
    new_word = random.choice(words)
    canvas.itemconfig(card_front, image=front)
    canvas.itemconfig(name, text="French", fill="black")
    canvas.itemconfig(word, text=new_word["French"], fill="black")
    window.after(3000, func=reveal)


# UI Setup
window = tkinter.Tk()
window.title("Flash Card")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=reveal)

canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front = tkinter.PhotoImage(file="images/card_front.png")
back = tkinter.PhotoImage(file="images/card_back.png")
card_front = canvas.create_image(400, 263, image=front)
name = canvas.create_text(400, 150, text="Title", font=FONT_1)
word = canvas.create_text(400, 263, text="word", font=FONT_2)
canvas.grid(row=0, column=0, columnspan=3)

right = tkinter.PhotoImage(file="images/right.png")
wrong = tkinter.PhotoImage(file="images/wrong.png")
# Image Buttons
right_button = tkinter.Button(image=right, highlightthickness=0, relief="flat", borderwidth=0,
                              command=generate_flashcard)
right_button.grid(row=1, column=2)
left_button = tkinter.Button(image=wrong, highlightthickness=0, relief="flat", borderwidth=0,
                             command=generate_flashcard)
left_button.grid(row=1, column=0)
window.mainloop()
