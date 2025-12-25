from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1 style='text-align: center'>Hello, World!</h1><p>This is a paragraph</p>"

def make_bold(func):
    def wrapper(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"
    return wrapper

@app.route("/username/<name>")
@make_bold
def hello_user(name):
    # show the user profile for that user
    return f"Hello, {name}!"

if __name__ == "__main__":
    app.run(debug=True)




# Decorator Task 2
class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def decorator_func(function):
        def wrapper(*args, **kwargs):
            if args[0].is_logged_in:
                function(args[0])
        return wrapper

@decorator_func
def create_post(user):
    print(f"This is {user.name}'s new blog post.")

new_user = User("Nikita")
new_user.is_logged_in = True
create_post(new_user)




# Decorator Task 3
# TODO: Create the logging_decorator() function 👇
def logging_decorator(function):
    def wrapper(*args):
        print(f"You called {function.__name__}{args}")
        print(f"It returned: {function(*args)}")
        return function(*args)

    return wrapper


# TODO: Use the decorator 👇
@logging_decorator
def a_function(*args):
    return sum(args)


a_function(1, 2, 3)