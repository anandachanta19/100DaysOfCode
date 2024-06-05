import tkinter

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

# Window Creation
window = tkinter.Tk()
window.title("Password Manager")
window.config(pady=20, padx=20)

# Logo
canvas = tkinter.Canvas(width=200, height=200)
photo = tkinter.PhotoImage(file="logo.png")
logo = canvas.create_image(100, 100, image=photo)
canvas.pack()
window.mainloop()
