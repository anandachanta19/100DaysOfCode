from flask import Flask, render_template
from post import Post

app = Flask(__name__)
posts = Post()
blogs = posts.blogs


@app.route('/')
def home():
    return render_template("index.html", blogs=blogs)


@app.route('/post/<blog_id>')
def get_post(blog_id):
    for blog in blogs:
        if blog["id"] == int(blog_id):
            return render_template("post.html", blog=blog)
    return render_template("post.html", blog=None)


if __name__ == "__main__":
    app.run(debug=True)
