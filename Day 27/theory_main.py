import tkinter
FONT = ("Arial", 24, "italic")

window = tkinter.Tk() # creates window
window.title("My First GUI Program") # window's title
window.minsize(width=500,height=300) # set minimum screen size
window.config(padx = 20, pady = 20) # make padding (add more space around the program)

# Label
my_label = tkinter.Label(text = "I Am a Label", font = FONT) # create label
my_label["text"] = "Hello"
my_label.config(text = "Hello") # the same
my_label.grid(column = 0, row = 0) # pack () places "my_label" into the screen (side - bottom, left, right, top)
my_label.config(padx=50, pady=50) # add more space around my_label

# Button
def button_clicked():
    print("I got clicked. ")
    new_text = input.get()
    my_label.config(text = input.get(), font = FONT)

button = tkinter.Button(text = "Click me", command = button_clicked)
button.grid(column = 1, row = 1) # creating a button

button2 = tkinter.Button(text = "New button", command = button_clicked)
button2.grid(column = 2, row = 0) # creating a button

# Entry
input = tkinter.Entry(width=10) # entry line
input.grid(column = 3, row = 2)











window.mainloop() # keep window open
