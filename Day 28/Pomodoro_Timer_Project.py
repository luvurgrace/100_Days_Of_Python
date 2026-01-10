from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
reps = 0
checks_done = []
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
    global checks_done, reps
    window.after_cancel(timer) # cancel after
    timer_label.config(text = "Timer", fg = GREEN, bg = YELLOW, font = (FONT_NAME, 35, "bold"))
    canvas.itemconfig(timer_text, text="00:00")
    check_mark.config(text="")
    checks_done = []
    reps = 0





# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_min = LONG_BREAK_MIN*60
    if reps % 8 == 0:
        count_down(long_break_min)
        timer_label.config(text = "Break", fg = RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg = PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = math.floor(count/60) # the largest integer that is <= count (4.8. -> 4)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"


    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 15)
    else:
        start_timer()
        if reps % 2 == 0:
            checks_done.append("✔")
            checks = ''.join(checks_done)
            check_mark.config(text=checks)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(pady=50, padx=100, bg =YELLOW)


canvas = Canvas(width = 200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file ="tomato.png") # relative or absolute file path
canvas.create_image(100,112, image = tomato_img)
timer_text = canvas.create_text(100, 130, text ="00:00", fill = "white", font = (FONT_NAME, 25, "bold"))
canvas.grid(column=2, row=2)

timer_label = Label(text = "Timer", fg = GREEN, bg = YELLOW, font = (FONT_NAME, 35, "bold"))
timer_label.grid(column=2, row= 1)

reset_button = Button(text ="Reset", highlightthickness=0, command=timer_reset)
reset_button.grid(column=3, row=3)

start_button = Button(text = "Start", highlightthickness=0, command=start_timer)
start_button.grid(column=1, row =3 )

check_mark = Label(fg = GREEN, bg= YELLOW, font = "bold")
check_mark.grid(column=2, row = 4)


window.mainloop()
