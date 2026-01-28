from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

app = Flask(__name__)


# create database
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books.db"

db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Book(db.Model):
    __tablename__ = 'books'  # Имя таблицы

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)  # тип данных и ограничения


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == 'POST':
        with app.app_context():
            new_book = Book(
                title=request.form["title"],
                author=request.form["author"],
                rating=float(request.form["rating"])
            )
            db.session.add(new_book)
            db.session.commit()
        print(new_book)
        return redirect(url_for("home"))

    return render_template("add.html")

@app.route("/edit/<int:book_id>", methods=["GET", "POST"])
def edit(book_id):
    book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    if request.method == 'POST':
        book_to_update.rating = float(request.form["rating"])
        db.session.commit()
        print(book_to_update)
        return redirect(url_for("home"))
    return render_template("edit.html", book=book_to_update)

@app.route("/delete")
def delete():
    book_id = request.args.get('book_ids')
    book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    db.session.delete(book_to_delete)
    db.session.commit()
    print(book_to_delete)
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True, port=5000)
