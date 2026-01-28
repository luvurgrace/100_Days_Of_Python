from flask import Flask, render_template
from post import Post
import requests

app = Flask(__name__)

blog_url = "https://api.npoint.io/916cb885f8b90c7bd624"
blog_response = requests.get(blog_url)
all_posts = blog_response.json()
post_objects = []
for post in all_posts:
    post_object = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_object)
print(all_posts)

@app.route('/blog')
def home():
    return render_template("index.html", all_posts=post_objects)

@app.route('/post/<int:index>')
def get_post(index):
    print(index)
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post = requested_post)

if __name__ == "__main__":
    app.run(debug=True)
