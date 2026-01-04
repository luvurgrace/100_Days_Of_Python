from flask import Flask, render_template, request
import requests
import smtplib
from dotenv import load_dotenv
import os
from datetime import datetime

app = Flask(__name__)

load_dotenv()
response = requests.get("https://api.npoint.io/555e3b14f9a5332f8785")
response.raise_for_status()
posts = response.json()  # list of dictionaries
today = datetime.now()
formatted_date = today.strftime("%B %d, %Y")

my_gmail = "alesspy7@gmail.com"
my_pass = os.environ.get("pass")
my_yahoo = "lutik.nikita228@gmail.com"


@app.route('/')
def home():
    return render_template("index.html", posts=posts, POST_DATE=formatted_date)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        print(f"{name}\n{email}\n{phone}\n{message}")
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_gmail, password=my_pass)
            connection.sendmail(from_addr=my_gmail,
                                to_addrs=my_yahoo,
                                msg=f"Subject: User data\n\nName: {name}\nEmail: {email}\nPhone number: {phone}\nMessage: {message}")
        return render_template("contact.html", m_sent=True)
    return render_template("contact.html", m_sent=False)


@app.route('/post/<int:index>')
def get_post(index):
    post = posts[index - 1]
    return render_template("post.html", post=post, POST_DATE=formatted_date)


if __name__ == "__main__":
    app.run(debug=True, port=5002)

print("Hello")