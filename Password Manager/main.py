import tkinter
FONT = "Arial"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

# Window Creation
window = tkinter.Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

# Logo
canvas = tkinter.Canvas(width=200, height=200)
photo = tkinter.PhotoImage(file="logo.png")
logo = canvas.create_image(100, 100, image=photo)
canvas.grid(row=0, column=1)

# Field Names
website = tkinter.Label(text="Website:", font=(FONT, 10, "normal"))
website.grid(row=1, column=0)
email = tkinter.Label(text="Email/Username:", font=(FONT, 10, "normal"))
email.grid(row=2, column=0)
password = tkinter.Label(text="Password:", font=(FONT, 10, "normal"))
password.grid(row=3, column=0)

# Field Inputs
website_input = tkinter.Entry(width=50)
website_input.grid(row=1, column=1, columnspan=2)
email_input = tkinter.Entry(width=50)
email_input.grid(row=2, column=1, columnspan=2)
password_input = tkinter.Entry(width=32)
password_input.grid(row=3, column=1)


# Buttons
generate = tkinter.Button(text="Generate", borderwidth=1, relief="groove", width=14)
generate.grid(row=3, column=2)
add = tkinter.Button(text="Add", width=43, borderwidth=1, relief="groove")
add.grid(row=4, column=1, columnspan=2)

window.mainloop()

