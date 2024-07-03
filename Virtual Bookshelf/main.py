from flask import Flask
from flask import render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db.init_app(app)


class Books(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True, nullable=False)
    author: Mapped[str] = mapped_column(nullable=False)
    rating: Mapped[float] = mapped_column(nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    books = db.session.execute(db.select(Books).order_by(Books.rating)).scalars()
    return render_template('index.html', books=books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        book = Books(
            title=request.form["title"],
            author=request.form["author"],
            rating= request.form["rating"]
        )
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')


@app.route('/delete/<book_id>')
def delete(book_id):
    book_to_delete = db.get_or_404(Books, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/edit/<book_id>', methods=['GET', 'POST'])
def edit(book_id):
    if request.method == "POST":
        with app.app_context():
            book_to_update = db.get_or_404(Books, book_id)
            book_to_update.rating = request.form["rating"]
            db.session.commit()
            return redirect(url_for('home'))
    book = db.get_or_404(Books, book_id)
    return render_template("edit.html", book=book)


if __name__ == "__main__":
    app.run(debug=True)
