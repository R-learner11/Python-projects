from tkinter import *
from quiz_brain import QuizBrain
from functools import partial
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        # create our ui here
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # adding all the basic ui for the quiz
        self.score_label = Label(text="score : 0", bg=THEME_COLOR, fg="white", font=('Arial', 18, 'bold'))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(height=250, width=300)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Hello hello mike testing",
            font=('Arial', 20, 'italic'),
            fill=THEME_COLOR)

        true = PhotoImage(file='./images/true.png')
        self.true_button = Button(image=true, highlightthickness=0, bg=THEME_COLOR, command=partial(self.check_answer,
                                                                                                    "true"))
        self.true_button.grid(row=2, column=0)

        false = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false, highlightthickness=0, bg=THEME_COLOR, command=partial(self.check_answer,
                                                                                                      "false"))
        self.false_button.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white', selectforeground=THEME_COLOR)
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz.")
            self.false_button.config(state="disabled")
            self.true_button.config(state="disabled")

    def check_answer(self, user_answer):
        answer = self.quiz.check_answer(user_answer)
        if answer:
            self.canvas.config(bg='Green', selectforeground='white')
        else:
            self.canvas.config(bg='red', selectforeground='white')
        self.window.after(1000, self.get_next_question)



