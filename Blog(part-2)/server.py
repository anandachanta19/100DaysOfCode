from flask import Flask, render_template, request
from post import Post
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()
FROM = os.getenv("MY_EMAIL")
PASSWORD = os.getenv("MY_APP_PASSWORD")
TO = os.getenv("TO_EMAIL")

app = Flask(__name__)
posts = Post()
blogs = posts.blogs


@app.route("/")
def home():
    return render_template("index.html", blogs=blogs)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        message = (f"Name: {data['name']}\n"
                   f"Email: {data['email']}\n"
                   f"Phone Number: {data['phone']}\n"
                   f"Message: {data['message']}")
        print(message)
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=FROM, password=PASSWORD)
            connection.sendmail(from_addr=FROM,
                                to_addrs=TO,
                                msg=f"Subject:New Visitor to Blogs\n\n"
                                    f"{message}")
        return render_template("contact.html", msg_sent=True)
    else:
        return render_template("contact.html", msg_sent=False)


@app.route('/post/<blog_id>')
def get_post(blog_id):
    for blog in blogs:
        if blog["id"] == int(blog_id):
            return render_template("post.html", blog=blog)
    return render_template("post.html", blog=None)


if __name__ == "__main__":
    app.run(debug=True)
