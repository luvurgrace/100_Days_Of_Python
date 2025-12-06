from tkinter import *
from quiz_brain import QuizBrain

FONT = ("Arial", 15, "italic")
SCORE_FONT = ("Arial", 15)
THEME_COLOR = "#375362"



class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg = THEME_COLOR)

        # Canvas
        self.canvas = Canvas(height=250, width=300, bg="white")
        self.canvas.grid(column=1, row=2, columnspan=2, padx= 20, pady=50)

        # Labels
        self.score = Label(text = f"Score: 0", bg=THEME_COLOR, fg = "white", font=SCORE_FONT)
        self.score.grid(column=2, row=1)

        # Buttons
        self.right_image = PhotoImage(file = "images/true.png")
        self.right_button = Button(image=self.right_image, highlightthickness=0, command = self.true_pressed)
        self.right_button.grid(column = 1, row=3)

        self.false_image = PhotoImage(file = "images/false.png")
        self.false_button = Button(image=self.false_image, highlightthickness=0, command = self.false_pressed)
        self.false_button.grid(column=2, row=3)

        # Text

        self.q_text = self.canvas.create_text(150,
                                              125,
                                              width=250,
                                              text = "Some Text",
                                              font=FONT,
                                              fill=THEME_COLOR)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.q_text,text = q_text)
        else:
            self.canvas.itemconfig(self.q_text, text = "You've reached the end of the quiz!")
            self.right_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)


    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.score.config(text= f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg="red")
        self.canvas.after(1000, self.get_next_question)


