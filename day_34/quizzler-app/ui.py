from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # score label
        self.score_label = Label(
            text="Score: 0", fg="white", bg=THEME_COLOR, font=("Courier", 15, "normal")
        )
        self.score_label.grid(row=0, column=1)

        # canvas
        self.canvas = Canvas(height=250, width=300, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=290,
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"),
            text="Amazon acquired Twitch in August 2014 for $970 million dollars.",
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Buttons
        check_image = PhotoImage(file="./images/true.png")
        self.right_btn = Button(
            image=check_image, command=self.true_pressed, highlightthickness=0
        )
        self.right_btn.grid(row=2, column=0)

        cross_image = PhotoImage(file="./images/false.png")
        self.wrong_btn = Button(
            image=cross_image, command=self.false_pressed, highlightthickness=0
        )
        self.wrong_btn.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_text, text="You've reached the end of the game."
            )
            self.right_btn.config(state="disabled")
            self.wrong_btn.config(state="disabled")

    def true_pressed(self):
        # is_right = self.quiz.check_answer("True")
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
