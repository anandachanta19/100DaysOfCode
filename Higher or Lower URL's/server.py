import random

from flask import Flask

NUMBERS_GIF = ("https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNnF3azI2amd6NjE5amZ2MDVlMGR2Zm9sbDc5bGF5ND"
               "FuOHd3enhnaSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/IsfrRWvbUdRny/giphy.gif")

HIGH_GIF = ("https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExZ3QydDI2dnAzc2dpZnl3MGIzeXpyMXkzbnhham9iMzd3cnp3"
            "bzZpeCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/TKk37hADNFG5iVxE4Y/giphy.gif")

LOW_GIF = ("https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExZmpmY2w2NXZvMW0wemhpbDB5MXV3Z3E5NnF1OXlnZnBnZzJ3Y"
           "Wc3ayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/nzsWN8iSDwSlhCDokc/giphy.gif")

CORRECT_GIF = ("https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExMzBiaWpnMzU0eWJ6enBsbWNxdndyZm9yMHR2cTg3Y2UxYm93bnhoNi"
               "ZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Y6FUCFt5N7Y8gRSInL/giphy.gif")

OTHER_GIF = ("https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExd2l2ZGN2bjZ1Ym1oeTFnN3B5NHZ1eG4zdWh1aXhwNn"
             "JtbGVoN3RrOSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Wck09E7lHDabjhHbzJ/giphy.gif")

random_number = random.randint(0, 9)
app = Flask(__name__)


# Home page
@app.route("/")
def guess_number():
    return f'<h1>Guess a number between 0 and 9</h1>' \
           f'<img src="{NUMBERS_GIF}"/>'


@app.route("/<user_number>")
def check_number(user_number):
    try:
        user_number = int(user_number)
    except ValueError:
        return f'<h1>I have asked you to guess a number</h1>' \
               f'<img src="{OTHER_GIF}"/>'
    else:
        if user_number == random_number:
            return f'<h1>Alright!!!!</h1>' \
                   f'<img src="{CORRECT_GIF}"/>'
        elif user_number < random_number:
            return f'<h1>Too Low! Try again.</h1>' \
                   f'<img src="{LOW_GIF}"/>'
        elif user_number > random_number:
            return f'<h1>Too High! Jump of from there.</h1>' \
                   f'<img src="{HIGH_GIF}"/>'


if __name__ == "__main__":
    app.run(debug=True)
