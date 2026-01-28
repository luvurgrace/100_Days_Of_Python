import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float


# db = sqlite3.connect("books-collection.db")  # if the database does not exist then it will be created
#
# cursor = db.cursor()  # cursor will control the database
#
# # cursor.execute(
# #    "CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
#



# create Flask app
app = Flask(__name__)

# CREATE DATABASE
class Base(DeclarativeBase):
    pass

# Указываем Flask-приложению, где будет храниться база данных.
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"

# создаем объект базы данных
db = SQLAlchemy(model_class=Base)
# Initialise the app with the extension
db.init_app(app)

# CREATE TABLE
class Book(db.Model):
    __tablename__ = 'books'  # Имя таблицы

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False) # тип данных и ограничения

with app.app_context():
    db.create_all()

# 1) Create a new record
with app.app_context():
    new_book = [
        Book(id=2, title="Harry Managua", author="Footballer", rating=9)
    ]
    db.session.add_all(new_book)
    db.session.commit()
