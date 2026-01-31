from tkinter import *
from tkinter import messagebox
from random import choice, randint,shuffle
import pyperclip

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


    if len(email) == 0 or len(web) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you have not left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=web, message=f"These are the details entered: \n\nEmail: {email} "
                                                  f"\nPassword: {password}")
        if is_ok:
            with open("data.txt", mode="a") as data:
                data.write(f"{web} | {email} | {password}\n")
            email_entry.delete(0,END)
            website_entry.delete(0,END)
            pass_entry.delete(0,END)
            email_entry.insert(0,"username@example.ex")

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
website_entry = Entry(width=53)
website_entry.grid(column=1, row=1, columnspan=2)
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




window.mainloop()