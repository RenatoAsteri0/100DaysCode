from tkinter import Canvas, Tk, PhotoImage, Label, LabelFrame, Button

BACKGROUND_COLOR = "#B1DDC6"
FONT_LANGUAGE = ('Arial', 40, 'italic')
FONT_TRADUCAO = ('Arial', 60, 'bold')

#janela
window = Tk()
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

#canvas front
canvas = Canvas(height=526, width=800, highlightthickness=0)
img_card_front = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263,image=img_card_front)
canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)
#language
language_text = canvas.create_text(400,150, text='Franch',font=FONT_LANGUAGE)
#traducao
traducao_text = canvas.create_text(400,263, text='Trouve',font=FONT_TRADUCAO)
canvas.grid(row=0, column=0,columnspan=2)

#botao falhou
erro = Button()
img_erro_button = PhotoImage(file="images/wrong.png")
erro.config(image=img_erro_button)
erro.grid(row=1, column=0)

#botao acertou
acertou = Button()
img_acertou_button = PhotoImage(file="images/right.png")
acertou.config(image=img_acertou_button)
acertou.grid(row=1, column=1)

window.mainloop()