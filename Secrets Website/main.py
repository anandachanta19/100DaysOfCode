import os
from dotenv import load_dotenv
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField
from wtforms.validators import DataRequired

load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv("APP_SECRET_KEY")


class MyForm(FlaskForm):
    email = EmailField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = MyForm()
    if form.validate_on_submit():
        return "Success"
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
