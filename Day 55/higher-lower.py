from flask import Flask
from random import randint

app = Flask(__name__)

random_number = randint(0,9)


@app.route("/")
def hello_world():
    return ("<h1>Guess a number between 0 and 9</h1>"
            "<img src='https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExNXpvNmhpb2xxYjFpd2JtZWE2M3VvcGtvMXRudWo1NnE5NWtidWpuYiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/wZD7RX1fHKsU7FckHH/giphy.gif' alt='christmas gif'>")


@app.route("/<int:guess>")
def hello_user(guess):
    if random_number == guess:
        return f"<h1>You are right. The guessed number is {random_number}!</h1><img src='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExNzNkZGFlaThsYmptZHJkYnZ0dG5vdGpzenhtYTV2YmZzNXAyMXRiYSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/aTTIFKiFPIiD951CzP/giphy.gif' alt='Lando Norris'>"
    elif guess > random_number:
        return f"<h1>Too high, try again!</h1><img src='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExMXRtbXQ5dHBjeGpkcDg4ZWU0eHV3M3ZmZ211aXJ6ZnJrbDE4MG84biZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/jFItARFcDC46PpVDWC/giphy.gif' alt='baby'>"
    else:
        return f"<h1>Too low, try again!</h1><img src='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExeHM4NGNxYTlvNmdyN3N6djV2d21pcWtsMnpjNTRwdWxkMWV5MXVoYSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/5aeKTXAsQpD83c4xpW/giphy.gif' alt='grinch'>"


if __name__ == "__main__":
    app.run(debug=True)