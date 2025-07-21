from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_pomodoro():
    window.after_cancel(timer)
    global reps
    timer_label.config(font=(FONT_NAME, 45, 'bold'), text='Timer', fg=GREEN, bg=YELLOW)
    mark.config(fg=GREEN, bg=YELLOW)
    canvas.itemconfig(time_canvas, text='00:00')

    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        decrease_time(long_break_sec)
        timer_label.config(font=(FONT_NAME, 45, 'bold'), text='Long Break', fg=RED, bg=YELLOW)
    elif reps % 2 == 0:
        decrease_time(short_break_sec)
        timer_label.config(font=(FONT_NAME, 45, 'bold'), text='Short Break', fg=PINK, bg=YELLOW)
    else:
        decrease_time(work_sec)
        timer_label.config(font=(FONT_NAME, 45, 'bold'), text='Work', fg=GREEN, bg=YELLOW)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def decrease_time(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(time_canvas, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(1000, decrease_time, count - 1)
    else:
        start_timer()
        checkmark = ''
        for _ in range(math.floor(reps/2)):
            checkmark += '✔'
        mark.config(text=checkmark)
        # ---------------------------- UI SETUP ------------------------------- #


'''Window configuration'''
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

'''Create a great widget canvas to input all resources'''
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100,110, image=tomato_img)
time_canvas = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)

'''Create Label Timer'''
timer_label = Label(font=(FONT_NAME, 45, 'bold'), text='Timer', fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

'''Create the buttons'''
start = Button(text='Start', highlightthickness=0, command=start_timer)
start.grid(row=2, column=0)

reset = Button(text='Reset', highlightthickness=0,command=reset_pomodoro)
reset.grid(row=2, column=2)


'''Create the check mark'''
mark = Label(fg=GREEN, bg=YELLOW)
mark.grid(row=3, column=1)

window.mainloop()