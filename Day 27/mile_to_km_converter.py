from tkinter import *

FONT = ("Arial", 10, "normal")
FONT_NUM = ("Arial", 10, "bold")

def miles_to_km():
    """converts miles to kilometers"""
    to_convert = float(entry.get())*1.609
    calc_num.config(text = round(to_convert)) # rounds to whole number

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=75)
window.config(pady=20, padx=20)

# Labels ("number", "Miles", "Km", "is equal to")
calc_num = Label(text=0, font=FONT_NUM)
calc_num.grid(column=2, row=2)

miles = Label(text = "Miles", font=FONT)
miles.grid(column=3, row= 1)

Km = Label(text="Km", font=FONT)
Km.grid(column=3, row = 2)

eq_to = Label(text = "is equal to", font=FONT)
eq_to.grid(column=1, row=2)


# Botton "Calculate"
button = Button(text = "Calculate", command = miles_to_km)
button.grid(column = 2, row = 3)

entry = Entry(width=10)
entry.grid(column=2, row=1)



window.mainloop()