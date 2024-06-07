import tkinter
BACKGROUND_COLOR = "#B1DDC6"
FONT_1 = ("Ariel", 40, "italic")
FONT_2 = ("Ariel", 60, "bold")

# UI Setup
window = tkinter.Tk()
window.title("Flash Card")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front = tkinter.PhotoImage(file="images/card_front.png")
# back = tkinter.PhotoImage(file="images/card_back.png")
card_front = canvas.create_image(400, 263, image=front)
# card_back = canvas.create_image(400, 265, image=back)
canvas.grid(row=0, column=0, columnspan=3)

name = tkinter.Label(text="French", font=FONT_1, bg="white")
name.place(x=400, y=150, anchor="center")
word = tkinter.Label(text="trouve", font=FONT_2, bg="white")
word.place(x=400, y=263, anchor="center")


right = tkinter.PhotoImage(file="images/right.png")
wrong = tkinter.PhotoImage(file="images/wrong.png")
# Image Buttons
right_button = tkinter.Button(image=right, highlightthickness=0, relief="flat", borderwidth=0)
right_button.grid(row=1, column=2)
left_button = tkinter.Button(image=wrong, highlightthickness=0, relief="flat", borderwidth=0)
left_button.grid(row=1, column=0)
window.mainloop()
