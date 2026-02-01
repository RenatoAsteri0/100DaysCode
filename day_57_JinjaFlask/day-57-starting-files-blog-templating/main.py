from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get(url='https://api.npoint.io/c790b4d5cab58020d391')
    blogs = response.json()
    return render_template("index.html", blogs=blogs)

@app.route('/posts/<idnum>')
def get_post(idnum):
    return render_template('posts.html')

if __name__ == "__main__":
    app.run(debug=True)
