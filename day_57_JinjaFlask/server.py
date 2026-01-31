from flask import Flask, render_template
from datetime import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template(template_name_or_list='index.html', current_year=datetime.now().year, autor='renato')

@app.route('/guess/<name>')
def guess(name):
    get_gender = requests.get(url=f"https://api.genderize.io?name={name}")
    gender = get_gender.json()['gender']

    get_age = requests.get(url=f"https://api.agify.io?name={name}")
    age = get_age.json()['age']

    return render_template(template_name_or_list='guess.html', name=name, age=age, gender=gender)

@app.route('/blog')
def blog():
    response = requests.get(url='https://api.npoint.io/c790b4d5cab58020d391')
    all_blogs = response.json()
    return render_template(template_name_or_list='blog.html',blogs=all_blogs)


if __name__ == '__main__':
    app.run(debug=True)