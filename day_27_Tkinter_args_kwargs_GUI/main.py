import tkinter
from tkinter import Button, Entry
'''
window = tkinter.Tk()

window.title("my first GUI Program")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)

my_label['text'] = 'New text'

def press_buton():
    print('has clicked')
    texto = entry.get()
    my_label.config(text=texto)

def salvar():
    with open('file-button.txt', 'w') as file:
        file.write("hey! i've got it")
    print('arquivo salvo')

button = Button(text='Click me', command=press_buton)
button.grid(column=5, row=5)
button1 = Button(text='Salvar', command=salvar)
button1.grid(column=40, row=0)

entry = Entry(width=10)
entry.grid(column=10, row=2)

window.mainloop()'''

janela = tkinter.Tk()
janela.title('Mile to Km Converter')
janela.minsize(width=30, height=50)

def convert():
    miles = input.get()
    kms = float(miles) * float(1.6)
    rounded_kms = round(kms,2)
    label_result.config(text=rounded_kms)

label_mile = tkinter.Label(text="Miles", font=("Arial", 12))
label_mile.grid(column=2, row=0)

label_is_equal = tkinter.Label(text='is equal to',font=("Arial", 12))
label_is_equal.grid(column=0, row=1)

label_result = tkinter.Label(text='0',font=("Arial", 12))
label_result.grid(column=1, row=1)

label_km = tkinter.Label(text='Km',font=("Arial", 12))
label_km.grid(column=2, row=1)

input = Entry(width=4)
input.grid(column=1, row=0)

button = Button(text='Calculate', command=convert)
button.grid(column=1, row=2)

janela.mainloop()
