from tkinter import *
import random
import pandas

FILE = "flashcard.png"
FILE_2 = "images/card_back.png"
BACKGROUND_COLOR = "#B1DDC6"

# File determining
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/spanish_words.csv")
    new_dict = original_data.to_dict(orient="records")
else:
    new_dict = data.to_dict(orient="records")

# Functions

def generate_word():
    global random_word, flip_timer
    window.after_cancel(flip_timer) # cancels timer to count
    canvas.itemconfig(canvas_image, image=old_card)
    random_word = random.choice(new_dict)
    canvas.itemconfig(card_title, text = "Spanish", fill = "black")
    canvas.itemconfig(card_word, text = random_word["Spanish"], fill = "black")
    flip_timer = window.after(3000, card_flip)

def card_flip():
    canvas.itemconfig(canvas_image, image = new_card)
    canvas.itemconfig(card_title, text="English", fill = "white")
    canvas.itemconfig(card_word, text=random_word["English"], fill = "white")

def remove_current_word():
    new_dict.remove(random_word)
    data = pandas.DataFrame(new_dict)
    data.to_csv("data/words_to_learn.csv", index = False)
    generate_word()


# Program Start
window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg = BACKGROUND_COLOR)

old_card = PhotoImage(file = FILE)
new_card = PhotoImage(file = FILE_2)

flip_timer = window.after(3000, card_flip)

# Canvas
canvas = Canvas(width=800, height=526)
canvas_image = canvas.create_image(400, 263, image=old_card)
canvas.config(bg = BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=1, row=1, columnspan=2)

# Buttons
yes_image = PhotoImage(file = "images/right.png")
yes_button = Button(image = yes_image, highlightthickness=0, command=remove_current_word)
yes_button.grid(column=2, row=2)

no_image = PhotoImage(file = "images/wrong.png")
no_button = Button(image = no_image, highlightthickness=0, command=generate_word)
no_button.grid(column=1, row=2)

# Text
card_title = canvas.create_text(400, 150, text = "Title", font  = ("Ariel",40,"italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))



generate_word()



window.mainloop()