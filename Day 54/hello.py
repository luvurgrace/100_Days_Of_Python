from flask import Flask
app = Flask(__name__)


@app.route("/") # triggers function under only if User opens URL (homepage/)
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye") # if User goes to /bye, then they see "Bye"
def say_bye():
    return "<p>Bye!</p>"

if __name__ == "__main__": # runs
    app.run() # no need to clarify the File name


# Decorator Task >>>
import time

current_time = time.time()
print(current_time)  # seconds since Jan 1st, 1970


# Write your code below 👇
def speed_calc_decorator():
    fast_function()
    changed_time = time.time()
    print(f"fast_function run speed: {changed_time - current_time}")
    slow_function()
    slow_time = time.time()
    print(f"slow_function run speed: {slow_time - changed_time}")


def fast_function():
    for i in range(1000000):
        i * i


def slow_function():
    for i in range(10000000):
        i * i


speed_calc_decorator()
