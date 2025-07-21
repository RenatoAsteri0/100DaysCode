# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

import tkinter as tk
from tkinter import Canvas, PhotoImage, Label, Entry, Button

FONT_NAME = "Courier"

#criar cenario
windows = tk.Tk()
windows.title('password generator')
windows.config(padx=20, pady=20)

#criar espaço para inserir o widget
canvas = Canvas()
canvas.config(width=200, height=200)
cadeado = PhotoImage(file='logo.png')
canvas.create_image(100,100, image=cadeado)
canvas.grid(row=0, column=1)

#campo 'Website'
web_site_label = Label()
web_site_label.config(font=(FONT_NAME, 10), text='Website:')
web_site_label.grid(row=1, column=0)
web_site_input = Entry()
web_site_input.config(width=35)
web_site_input.grid(row=1, column=1, columnspan=2)

#campo Email/Username
email_username_label = Label()
email_username_label.config(font=(FONT_NAME, 10), text='Email/Username:')
email_username_label.grid(row=2, column=0)
email_input = Entry()
email_input.config(width=35)
email_input.grid(row=2, column=1, columnspan=2)


#campo password
password_label = Label()
password_label.config(font=(FONT_NAME, 10), text='Password:')
password_label.grid(row=3, column=0)
password_input = Entry()
password_input.config(width=21)
password_input.grid(row=3, column=1)
generate_password = Button()
generate_password.config(text='Generate Password')
generate_password.grid(row=3, column=2)

#campo botao add
add_button = Button()
add_button.config(text='Add', width=36)
add_button.grid(row=4, column=1, columnspan=2)

teste = 0
windows.mainloop()
