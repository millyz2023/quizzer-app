from tkinter import *
THEME_COLOR = "#375362"
from quiz_brain import QuizBrain

class QuizInterface:

    def __init__(self, quiz_brain_object: QuizBrain):
        self.question = quiz_brain_object
        # we have access to our quiz brain object in here which is saved under self.question
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.scoreboard = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.scoreboard.grid(row=0, column=1, sticky="E")

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=280,
                                                     text="Some Question Text: {xxx}",
                                font=("Arial", 20, "italic"), fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=30)

        right_image = PhotoImage(file="images/true.png")
        self.right_button = Button(image=right_image, anchor="center", command=self.true_pressed)
        self.right_button.grid(row=2, column=1, padx=20, sticky="E")
        wrong_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=wrong_image, anchor="center", command=self.false_pressed)
        self.wrong_button.grid(row=2, column=0, padx=20, sticky="W")

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(self.canvas, bg="white")
        if self.question.still_has_questions():
            q_text = self.question.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")
    def true_pressed(self):
        self.give_feedback(self.question.check_answer("true"))
        self.update_scoreboard()

    def false_pressed(self):
        self.give_feedback(self.question.check_answer("false"))
        self.update_scoreboard()

    def give_feedback(self, is_correct):
        if is_correct:
            self.canvas.config(self.canvas, bg="green")
        else:
            self.canvas.config(self.canvas, bg="red")
        self.window.after(1000, self.get_next_question)

    def update_scoreboard(self):
        self.scoreboard.config(self.scoreboard, text=f"Score: {self.question.score}")

