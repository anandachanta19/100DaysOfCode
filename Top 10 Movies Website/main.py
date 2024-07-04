from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


# CREATE DB
class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///my-top-10-movies.db"
db.__init__(app)


# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True, nullable=False)
    year: Mapped[int] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    rating: Mapped[float] = mapped_column(nullable=False)
    ranking: Mapped[int] = mapped_column(unique=True, nullable=False)
    review: Mapped[str] = mapped_column(nullable=False)
    image_url: Mapped[str] = mapped_column(nullable=False)


with app.app_context():
    db.create_all()


# Edit Form
class EditForm(FlaskForm):
    rating = StringField(label="Your Rating Out Of 10", validators=[DataRequired()])
    review = StringField(label="Your Review", validators=[DataRequired()])
    submit = SubmitField(label="Submit")


class AddForm(FlaskForm):
    movie = StringField(label="Movie Title", validators=[DataRequired()])
    submit = SubmitField(label="Submit")

@app.route("/")
def home():
    movies = db.session.execute(db.select(Movie)).scalars()
    return render_template("index.html", movies=movies)


@app.route("/edit/<movie_id>", methods=["GET", "POST"])
def edit(movie_id):
    form = EditForm()
    movie_to_be_update = db.get_or_404(Movie, movie_id)
    if form.validate_on_submit():
        movie_to_be_update.rating = form.rating.data
        movie_to_be_update.review = form.review.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", movie=movie_to_be_update, form=form)


@app.route("/delete/<movie_id>")
def delete(movie_id):
    movie_to_be_delete = db.get_or_404(Movie, movie_id)
    db.session.delete(movie_to_be_delete)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddForm()
    if form.validate_on_submit():
        response = requests.get(url=)
        return redirect(url_for("home"))
    return render_template("add.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
