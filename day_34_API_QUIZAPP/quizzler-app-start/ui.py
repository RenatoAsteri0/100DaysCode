from tkinter import Tk, Label, Canvas, Button, PhotoImage
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
BRANCO = "#FFFFFF"
FONT_LANGUAGE = ('Arial', 20, 'italic')

class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.windows = Tk()
        self.windows.title("Quiz")
        self.windows.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label()
        self.score_label.config(text='Score: 0', bg=THEME_COLOR, fg=BRANCO)
        self.score_label.grid(column=1,row=0)

        self.canvas = Canvas()
        self.canvas.config(width=300, height=250)
        self.question_data = self.canvas.create_text(150,125,width=280, anchor='center',text='teste', font=FONT_LANGUAGE)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.acertou = Button()
        self.img_acertou = PhotoImage(file="images/true.png")
        self.acertou.config(image=self.img_acertou, highlightthickness=0, command=self.send_answer_true)
        self.acertou.grid(row=2, column=0)

        self.errou = Button()
        self.img_errou = PhotoImage(file="images/false.png")
        self.errou.config(image=self.img_errou, highlightthickness=0, command=self.send_answer_false)
        self.errou.grid(row=2, column=1)

        self.get_next_question()
        self.windows.mainloop()

    def get_next_question(self):
        self.canvas.config(bg=BRANCO)
        self.score_label.config(text=f'Score: {self.quiz.score}')
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_data, text=q_text)

    def send_answer_true(self):
        is_right = self.quiz.check_answer('True')
        self.give_feedback(is_right)

    def send_answer_false(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.windows.after(1000, self.get_next_question)
