from tkinter import *

THEME_COLOR = "#375362"


def true_choice():
    pass


def false_choice():
    pass


class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quiz_App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.label = Label(text="Score")
        self.label.config(fg="white", bg=THEME_COLOR, font=("Arial", 20, "italic"))
        self.label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.ques_text = self.canvas.create_text(150, 125, text="", fill="black", font=("Arial", 26, "bold"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.true_img = PhotoImage(file="images/true.png")
        self.true = Button(image=self.true_img, highlightthickness=0, command=true_choice)
        self.true.grid(row=2, column=0)

        self.false_img = PhotoImage(file="images/false.png")
        self.false = Button(image=self.false_img, highlightthickness=0, command=false_choice)
        self.false.grid(row=2, column=1)

        self.window.mainloop()
