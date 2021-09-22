from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '%', '$', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)
    if len(input_pass.get()) > 0:
        input_pass.delete(0, END)
    input_pass.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_details():
    website = input_website.get()
    email = input_user.get()
    password = input_pass.get()

    new_data = {
        website: {
            "Email": email,
            "Password": password
        }
    }

    if len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Invalid Details",
                            message="Please don't leave any fields empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            input_website.delete(0, END)
            input_pass.delete(0, END)


def search_details():
    website = input_website.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found")
    else:
        if any(data.keys()) == website:
            email = data.website["Email"]
            password = data.website["Password"]
            messagebox.showinfo(title=website, message=f"Email: {email} \n Password: {password}")
        else:
            messagebox.showinfo(title=website, message=f"Oops! No data found for {website}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
websiteL1 = Label(text="Website:")
websiteL1.grid(row=1, column=0)

userL2 = Label(text="Email/Username:")
userL2.grid(row=2, column=0)

passwordL3 = Label(text="Password:")
passwordL3.grid(row=3, column=0)

# Inputs/Entries
input_website = Entry(width=21)
input_website.grid(row=1, column=1, sticky="ew")
input_website.focus()

input_user = Entry(width=36)
input_user.grid(row=2, column=1, columnspan=2, sticky="ew")
input_user.insert(0, "suvigya2001@gmail.com")

input_pass = Entry(width=21)
input_pass.grid(row=3, column=1, sticky="ew")

# Buttons
addBtn = Button(text="Add", width=36, command=save_details)
addBtn.grid(row=4, column=1, columnspan=2)

generate_pass_btn = Button(text="Generate Password", command=gen_password, width=16)
generate_pass_btn.grid(row=3, column=2)

search_btn = Button(text="Search", command=search_details, width=16)
search_btn.grid(row=1, column=2)

window.mainloop()
