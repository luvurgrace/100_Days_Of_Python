from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


# CREATE DB
class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-movies.db"

db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()

new_movie = Movie(
    title="Interstellar",
    year=2014,
    description="A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival as Earth faces environmental collapse.",
    rating=8.6,
    ranking=7,
    review="A visually stunning and emotionally powerful journey through space and time.",
    img_url="https://image.tmdb.org/t/p/w500/gEU2QniE6E77NI6lCU6JMgEwQI9.jpg"
)

with app.app_context():
    db.session.add(new_movie)
    db.session.commit()


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()  # delete Debut mode, since Flask actually starts two processes -
    # one for the main application and one for the reloader that watches for file changes.
