import tkinter
import random
from tkinter import messagebox
import json

FONT = "Arial"
EMAIL = "anandachanta19@gmail.com"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    password_letters = [random.choice(letters) for _ in range(nr_letters - 1)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols - 1)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers - 1)]
    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)

    password_input.clipboard_clear()
    password_input.delete(0, "end")
    password_generated = "".join(password_list)
    password_input.insert(0, password_generated)
    password_input.clipboard_append(password_generated)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def clear():
    website_input.delete(0, "end")
    password_input.delete(0, "end")


def search_website():
    website_name = website_input.get().title()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Note!", message=f"There is no data. Start saving passwords!")
    else:
        if website_name.title() in data:
            messagebox.showinfo(title=f"{website_name}",
                                message=f"Email/Username: {data[website_name]["email"]}"
                                        f"\nPassword: {data[website_name]["password"]}")
        else:
            messagebox.showinfo(title="Note!", message=f"You haven't saved any password for {website_name}")


def save():
    website_info = website_input.get().title()
    email_info = email_input.get()
    password_info = password_input.get()
    new_data = {
        website_info: {
            "email": email_info,
            "password": password_info
        }
    }

    if len(website_info) == 0 or len(email_info) == 0 or len(password_info) == 0:
        messagebox.showinfo(title="Oops!", message="Please make sure you haven't left any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=f"{website_info}", message=f"These are "
                                                                        f"the details entered:\nEmail/Username: "
                                                                        f"{email_info}\n"
                                                                        f"Password: {password_info}"
                                                                        f"\nDo you want to proceed?")
        if is_ok:
            try:
                with open("data.json", "r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            except json.decoder.JSONDecodeError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
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
website_input = tkinter.Entry(width=33)
website_input.grid(row=1, column=1)
website_input.focus()
email_input = tkinter.Entry(width=51)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, EMAIL)
password_input = tkinter.Entry(width=33)
password_input.grid(row=3, column=1)

# Buttons
generate = tkinter.Button(text="Generate", borderwidth=1, width=14, command=generate_password)
generate.grid(row=3, column=2)
add = tkinter.Button(text="Add", width=43, borderwidth=1, command=save)
add.grid(row=4, column=1, columnspan=2)
search = tkinter.Button(text="Search", borderwidth=1, width=14, command=search_website)
search.grid(row=1, column=2)
window.mainloop()
