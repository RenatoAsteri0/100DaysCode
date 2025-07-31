from codecs import backslashreplace_errors
from tkinter import Canvas, Tk, PhotoImage

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

canvas = Canvas()
img_card_front = PhotoImage(file="C:/Users/renat/Documents/pythonNote/100DaysCode/day_31_flash-card-project-start/images"
                                 "card_front.png")
canvas.config(height=526, width=800)
canvas.create_image(10, 10, image=img_card_front)
canvas.grid(row=0, column=0,columnspan=2)
window.mainloop()