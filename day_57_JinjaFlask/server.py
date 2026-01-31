from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template(template_name_or_list='index.html', current_year=datetime.now().year, autor='renato')

@app.route('/guess/<name>')
def guess(name):
    name = 'renato'
    return render_template(template_name_or_list='guess.html'), name

if __name__ == '__main__':
    app.run(debug=True)