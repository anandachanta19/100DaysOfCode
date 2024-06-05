import tkinter
from tkinter import messagebox

FONT = "Arial"
EMAIL = "anandachanta19@gmail.com"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def clear():
    website_input.delete(0, "end")
    password_input.delete(0, "end")


def save():
    if len(website_input.get()) == 0 or len(email_input.get()) == 0 or len(password_input.get()) == 0:
        messagebox.showinfo(title="Oops!", message="Please make sure you haven't left any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=f"{website_input.get()}", message=f"These are "
                                                                               f"the details entered:\nEmail/Username: "
                                                                               f"{email_input.get()}\n"
                                                                               f"Password: {password_input.get()}"
                                                                              f"\nDo you want to proceed?")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"\n{website_input.get()} | {email_input.get()} | {password_input.get()}")
            clear()
            website_input.focus()


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
website_input = tkinter.Entry(width=51)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()
email_input = tkinter.Entry(width=51)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, EMAIL)
password_input = tkinter.Entry(width=33)
password_input.grid(row=3, column=1)

# Buttons
generate = tkinter.Button(text="Generate", borderwidth=1, width=14)
generate.grid(row=3, column=2)
add = tkinter.Button(text="Add", width=43, borderwidth=1, command=save)
add.grid(row=4, column=1, columnspan=2)

window.mainloop()
