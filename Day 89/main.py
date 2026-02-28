from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), nullable=False)
    done = db.Column(db.Boolean, default=False)
    created = db.Column(db.DateTime, default=datetime.utcnow)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    todos = Todo.query.order_by(Todo.created.desc()).all()
    return render_template("index.html", todos=todos)


@app.route("/add", methods=["POST"])
def add():
    text = request.form.get("text")
    if text:
        todo = Todo(text=text)
        db.session.add(todo)
        db.session.commit()
    return redirect(url_for("home"))


@app.route("/toggle/<int:todo_id>")
def toggle(todo_id):
    todo = db.session.get(Todo, todo_id)
    if todo:
        todo.done = not todo.done
        db.session.commit()
    return redirect(url_for("home"))


@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = db.session.get(Todo, todo_id)
    if todo:
        db.session.delete(todo)
        db.session.commit()
    return redirect(url_for("home"))


@app.route("/clear")
def clear():
    Todo.query.filter_by(done=True).delete()
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)