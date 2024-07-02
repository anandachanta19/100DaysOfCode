from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/login', methods=['POST'])
def login():
    username = request.form["name"]
    print(username)
    return "Form Submitted!!"


if __name__ == "__main__":
    app.run(debug=True)
