import tkinter

MILE = 1.609


def calculate():
    result["text"] = f"{round(float(user_input.get()) * MILE, 2)}"


window = tkinter.Tk()
window.title("Mile to KM Converter")
window.config(padx=20, pady=20)
# window.minsize(width=400, height=400)

miles = tkinter.Label(text="Miles", font=("Courier", 13, "bold"))
miles.grid(row=0, column=2)
is_equal = tkinter.Label(text="is equal to", font=("Courier", 13, "bold"))
is_equal.grid(row=1, column=0)
result = tkinter.Label(text="", font=("Courier", 13, "bold"))
result.grid(row=1, column=1)
km = tkinter.Label(text="Km", font=("Courier", 13, "bold"))
km.grid(row=1, column=2)
button = tkinter.Button(text="Calculate", command=calculate)
button.grid(row=2, column=1)
user_input = tkinter.Entry(width=7)
user_input.grid(row=0, column=1)

window.mainloop()
