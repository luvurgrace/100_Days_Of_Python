import requests
from flask import Flask, render_template
from random import randint
import datetime

app = Flask(__name__)




@app.route('/')
def home():
    random_number = randint(0,10)
    name = "Nikita Lutik"
    current_year = datetime.date.today().year
    return render_template("index.html", num=random_number, RAND=random_number, MY_NAME=name, YEAR=current_year)

@app.route('/guess/<name>') #name - variable
def guess(name):
    URL_GEN = f"https://api.genderize.io?name={name}"
    response_gen = requests.get(URL_GEN)
    URL_AGE = f"https://api.agify.io?name={name}"
    response_age = requests.get(URL_AGE)
    return render_template("guess.html", NAME=name, MY_GENDER=response_gen.json()["gender"], MY_AGE=response_age.json()["age"])

@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/916cb885f8b90c7bd624"
    blog_response = requests.get(blog_url)
    all_posts = blog_response.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)
