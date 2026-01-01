from flask import Flask, render_template
import requests
from datetime import datetime

app = Flask(__name__)

response = requests.get("https://api.npoint.io/555e3b14f9a5332f8785")
response.raise_for_status()
posts = response.json()  # list of dictionaries
today = datetime.now()
formatted_date = today.strftime("%B %d, %Y")


@app.route('/')
def home():
    return render_template("index.html", posts=posts, POST_DATE=formatted_date)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/post/<int:index>')
def get_post(index):
    post = posts[index - 1]
    return render_template("post.html", post=post, POST_DATE=formatted_date)


if __name__ == "__main__":
    app.run(debug=True)
