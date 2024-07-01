from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/guess/<name>")
def guess(name):
    user_name = str(name).title()
    params = {
        "name": user_name
    }
    age_response = requests.get(url="https://api.agify.io", params=params)
    age = age_response.json()["age"]
    gender_response = requests.get(url="https://api.genderize.io", params=params)
    gender = gender_response.json()["gender"]
    return render_template("index.html", name=user_name, age=age, gender=gender)


if __name__ == "__main__":
    app.run(debug=True)
