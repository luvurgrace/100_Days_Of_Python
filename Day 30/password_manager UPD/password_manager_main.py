from tkinter import *
from tkinter import messagebox
from random import choice, randint,shuffle
import pyperclip
import json

FONT = ("Times New Roman", 14, "italic")
LOGO_PATH = "logo.png"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project Day 5 (shortened)

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_nums = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_nums
    shuffle(password_list)

    password = "".join(password_list)

    pass_entry.delete(0,END)
    pass_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    """saves passwords that user adds"""
    email = email_entry.get()
    web = website_entry.get()
    password = pass_entry.get()

    new_data = { # creating new dictionary
        web:{
            "email": email,
            "password": password
        }
    }

    if len(email) == 0 or len(web) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you have not left any fields empty.")
    else:
        try:
            with open("data.json", mode="r") as f:
                data = json.load(f) # json reading mode
        except FileNotFoundError:
            with open("data.json", mode="w") as f:
                json.dump(new_data, f, indent=4)  # json write mode
        else:
            data.update(new_data)  # what to update then ".", then (update with what) = update "data" with 'new data'
            with open("data.json", mode="w") as f:
                json.dump(data, f, indent=4)  # saving updated data
        finally:
            email_entry.delete(0,END)
            website_entry.delete(0,END)
            pass_entry.delete(0,END)
            email_entry.insert(0,"username@example.ex")

# ------------------------- SEARCH WEBSITE ---------------------------- #
def search_for_website():
    web_for_search = website_entry.get()
    try:
        with open("data.json", mode="r") as f:
            data = json.load(f)
            email = data[web_for_search]["email"]
            password = data[web_for_search]["password"]
    except KeyError:
        if web_for_search != "":
            messagebox.showinfo(title="Oops", message=f"There is no {web_for_search} account data yet")
        else:
            messagebox.showinfo(title="Oops", message="Enter the field 'Website' for search.")
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="There is no any account data yet")
    else:
        messagebox.showinfo(title=web_for_search, message=f"Email: {email}\nPassword: {password}")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

logo = PhotoImage(file = LOGO_PATH)

# Canva
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)


# Labels
website_label = Label(text = "Website:")
website_label.grid(column=0,row=1)

email_label = Label(text = "Email/Username:")
email_label.grid(column=0,row=2)

pass_label = Label(text = "Password:")
pass_label.grid(column=0,row=3)


# Entries
website_entry = Entry(width=34)
website_entry.grid(column=1, row=1)
website_entry.focus() # focus on that particular entry for user

email_entry = Entry(width=53)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "username@example.ex") # END if you want to type after "text", 0 - at the beginning

pass_entry = Entry(width=35)
pass_entry.grid(column=1, row=3)

# Buttons

add_button = Button(text="Add", width=45, command=save)
add_button.grid(column = 1, row = 4, columnspan=2)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column = 2, row = 3)

search_button = Button(text = "Search", command=search_for_website, width = 15)
search_button.grid(column=2,row =1)




window.mainloop()