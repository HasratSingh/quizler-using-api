from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quiz_App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
        self.score_label.config(fg="white", bg=THEME_COLOR, font=("Arial", 20, "italic"))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="",
            fill="black",
            font=("Arial", 18, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def give_feedback(self, is_correct):
        if is_correct:
            print("green")
            self.canvas.config(bg="green")
            self.canvas.itemconfigure(self.question_text, text="Correct")
        else:
            print("red")
            self.canvas.config(bg="red")
            self.canvas.itemconfigure(self.question_text, text="Wrong!")
        self.score_label.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
        self.window.after(1000, self.get_next_question)

    def true_pressed(self):
        is_correct = self.quiz.check_answer("True")
        self.give_feedback(is_correct)

    def false_pressed(self):
        is_correct = self.quiz.check_answer("False")
        self.give_feedback(is_correct)

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            ques = self.quiz.next_question()
            self.canvas.itemconfigure(self.question_text, text=ques)
        else:
            self.canvas.itemconfigure(self.question_text, text='No more questions')
            self.true_button.config(command="")
            self.false_button.config(command="")
