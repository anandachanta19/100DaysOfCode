import os
import smtplib
from datetime import date
from functools import wraps

from dotenv import load_dotenv
from flask import Flask, abort, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_gravatar import Gravatar
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from werkzeug.security import generate_password_hash, check_password_hash

from forms import CreatePostForm, RegisterForm, LoginForm, CommentForm

load_dotenv()
FROM = os.getenv("MY_EMAIL")
PASSWORD = os.getenv("MY_APP_PASSWORD")
TO = os.getenv("TO_EMAIL")

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap5(app)
gravatar = Gravatar(app,
                    size=100,
                    rating='g',
                    default='retro',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None)

# TODO: Configure Flask-Login
login_manager = LoginManager(app)


@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


def admin_only(function):
    @wraps(function)
    @login_required
    def decorated_function(*args, **kwargs):
        if current_user.id != 1:
            return abort(403)
        return function(*args, **kwargs)

    return decorated_function


# CONFIGURE TABLES

class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(250), nullable=False)
    name: Mapped[str] = mapped_column(String(250), nullable=False)
    posts = relationship("BlogPost", back_populates="author")
    comments = relationship("Comment", back_populates="cmt_author")

    def add_details(self, email, password, name):
        self.email = email
        self.password = password
        self.name = name


class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author = relationship("User", back_populates="posts")
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)
    author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("user.id"))
    comments = relationship("Comment", back_populates="cmt_post")


class Comment(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("user.id"))
    cmt_author = relationship("User", back_populates="comments")
    post_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("blog_posts.id"))
    cmt_post = relationship("BlogPost", back_populates="comments")
    text: Mapped[str] = mapped_column(Text, nullable=False)


with app.app_context():
    db.create_all()


@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = db.session.execute(db.select(User).where(User.email == form.email.data)).scalar()
        if user:
            # Email already exists
            return redirect(
                url_for(
                    "login",
                    is_already_exist=True
                )
            )
        if form.password.data == form.confirm_password.data:
            # Adding new user to the Database
            # Hash the password
            hashed_password = generate_password_hash(
                password=form.password.data,
                method="pbkdf2:sha256",
                salt_length=8
            )
            new_user = User()
            new_user.add_details(
                email=form.email.data,
                password=hashed_password,
                name=form.name.data
            )
            db.session.add(new_user)
            db.session.commit()
            # After Successful Registration redirect to log in
            return redirect(url_for("login", registered_now=True))
        else:
            # The Password and Confirm Password are not the same
            return redirect(url_for("register", is_no_match=True))
    return render_template(
        "register.html",
        form=form,
        is_no_match=request.args.get("is_no_match"),
        has_to_register=request.args.get("has_to_register")
    )


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.execute(db.select(User).where(User.email == form.email.data)).scalar()
        # Let us check if user exist or not
        if user:
            if check_password_hash(pwhash=user.password, password=form.password.data):
                login_user(user)
                return redirect(url_for("get_all_posts"))
            else:
                return redirect(url_for("login", password_incorrect=True))
        else:
            return redirect(url_for("register", has_to_register=True))
    return render_template(
        "login.html",
        form=form,
        is_already_exist=request.args.get("is_already_exist"),
        registered_now=request.args.get("registered_now"),
        password_incorrect=request.args.get("password_incorrect")
    )


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


@app.route('/')
def get_all_posts():
    result = db.session.execute(db.select(BlogPost))
    posts = result.scalars().all()
    return render_template("index.html", all_posts=posts, current_user=current_user)


@app.route("/post/<int:post_id>", methods=["GET", "POST"])
def show_post(post_id):
    form = CommentForm()
    requested_post = db.get_or_404(BlogPost, post_id)
    if form.validate_on_submit():
        if not current_user.is_authenticated:
            flash("You need to login or register to comment.")
            return redirect(url_for("login"))
        new_comment = Comment(
            cmt_author=current_user,
            cmt_post=requested_post,
            text=form.comment.data
        )
        db.session.add(new_comment)
        db.session.commit()
    return render_template("post.html", form=form, post=requested_post, current_user=current_user)


@app.route("/new-post", methods=["GET", "POST"])
@admin_only
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user,
            date=date.today().strftime("%B %d, %Y"),
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form, curremt_user=current_user)


@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@admin_only
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = current_user
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template("make-post.html", form=edit_form, is_edit=True, current_user=current_user)


@app.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


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


if __name__ == "__main__":
    app.run(debug=True, port=5002)
