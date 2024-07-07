from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory, abort
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'
login_manager = LoginManager()


# CREATE DATABASE


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
login_manager.init_app(app)
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CREATE TABLE IN DB


class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))


with app.app_context():
    db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        user = db.session.execute(db.select(User).where(User.email == request.form.get("email"))).scalar()
        if user:
            return redirect(url_for("login", is_email_exist=True))
        else:
            # Hashing and salting a Password
            hashed_password = generate_password_hash(
                password=request.form.get("password"),
                method='pbkdf2:sha256',
                salt_length=8
            )
            new_user = User(
                email=request.form.get("email"),
                password=hashed_password,
                name=request.form.get("name")
            )
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for("login", method="GET"))
    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():

    if request.method == "POST":
        user = db.session.execute(db.select(User).where(User.email == request.form.get("email"))).scalar()
        if check_password_hash(user.password, request.form.get("password")):
            login_user(user)
            return redirect(url_for("secrets"))
        else:
            print("Iam entered here")
            return redirect(url_for("login", is_not_password=True, method="GET"))
    return render_template(
        "login.html",
        is_email_exist=request.args.get("is_email_exist"),
        is_not_password=request.args.get("is_not_password"))


@app.route('/secrets')
@login_required
def secrets():
    name = current_user.name
    return render_template("secrets.html", name=name, logged_in=True)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
def download():
    return send_from_directory(
        'static', 'files/cheat_sheet.pdf', as_attachment=True
    )


if __name__ == "__main__":
    app.run(debug=True)
