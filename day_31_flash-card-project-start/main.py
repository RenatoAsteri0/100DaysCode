from tkinter import Canvas, Tk, PhotoImage, Button
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_LANGUAGE = ('Arial', 40, 'italic')
FONT_TRADUCAO = ('Arial', 60, 'bold')

def generate_word():
    indice_aleatorio = random.choice(range(len(data_dict)))
    word_random = data_dict[indice_aleatorio]['French']
    canvas.itemconfig(traducao_text, text=word_random)


data = pd.read_csv('data/french_words.csv')
data_dict = data.to_dict('records')

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
traducao_text = canvas.create_text(400,263, text='teste',font=FONT_TRADUCAO)
canvas.grid(row=0, column=0,columnspan=2)

#botao falhou
erro = Button()
img_erro_button = PhotoImage(file="images/wrong.png")
erro.config(image=img_erro_button, command=generate_word)
erro.grid(row=1, column=0)

#botao acertou
acertou = Button()
img_acertou_button = PhotoImage(file="images/right.png")
acertou.config(image=img_acertou_button, command=generate_word)
acertou.grid(row=1, column=1)

window.mainloop()