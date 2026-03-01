from flask import Flask, render_template
import requests
from post import Post

posts = requests.get(url='https://api.npoint.io/c790b4d5cab58020d391').json()
post_object = []

for post in posts:
    post_obj = Post(id=post['id'], body=post['body'], title=post['title'], subtitle=post['subtitle'])
    post_object.append(post_obj)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", blogs=post_object)

@app.route('/posts/<int:idnum>')
def get_post(idnum):
    requested = None
    for blog_post in post_object:
        if blog_post.id == idnum:
            requested = blog_post
    return render_template('post.html', post=requested)

if __name__ == "__main__":
    app.run(debug=True)
