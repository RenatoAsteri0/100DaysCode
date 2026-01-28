from flask import Flask
from random import randint

right_number = randint(0, 10)

def make_bold(func):
    def wrapper():
        return f'<b>'+ func() +'</b>'
    return wrapper

app = Flask(__name__)

@app.route("/")
@make_bold
def hello_world():
    return ("<h1>Guess a number between 0 and 9!<h1>"
            "<img src='https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExZjA4bXZ1M21xODE1NTF0djN2MTl0MmFseDF2amc0ZG5sa2"
            "d1MmM3ZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3oz8xLlw6GHVfokaNW/giphy.gif'>")

@app.route('/<int:guess>')
def guess_page(guess):
    if guess == right_number:
        return ("<h1 style='color: green';>You found me<h1>")
    elif guess < right_number:
        return ("<h1 style='color: red';>To low, try again!<h1>")
    else:
        return ("<h1 style='color: blue';>To high, try again!<h1>")


if __name__ == "__main__":
    #Run the app in debug mode to auto-reload
    app.run()