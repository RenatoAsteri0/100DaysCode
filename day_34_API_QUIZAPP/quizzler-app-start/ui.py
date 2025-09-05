from tkinter import Tk, Label, Canvas, Button, PhotoImage

THEME_COLOR = "#375362"
BRANCO = "#FFFFFF"
FONT_LANGUAGE = ('Arial', 20, 'italic')

class QuizInterface():

    def __init__(self):
        self.windows = Tk()
        self.windows.title("Quiz")
        self.windows.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label()
        self.score_label.config(text='Score: 0', bg=THEME_COLOR, fg=BRANCO)
        self.score_label.grid(column=1,row=0)

        self.canvas = Canvas()
        self.canvas.config(width=300, height=250)
        self.canvas.create_text(150,125, anchor='center',text='teste', font=FONT_LANGUAGE)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.acertou = Button()
        self.img_acertou = PhotoImage(file="images/true.png")
        self.acertou.config(image=self.img_acertou, highlightthickness=0)
        self.acertou.grid(row=2, column=0)

        self.errou = Button()
        self.img_errou = PhotoImage(file="images/false.png")
        self.errou.config(image=self.img_errou, highlightthickness=0)
        self.errou.grid(row=2, column=1)
        self.windows.mainloop()