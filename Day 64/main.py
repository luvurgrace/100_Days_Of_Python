from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
MOVIE_DB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"
MOVIE_DB_API_KEY = os.getenv("MOVIE_DB_API_KEY")
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


class MovieForm(FlaskForm):
    movie_rating = StringField('Movie rating out of 10', validators=[DataRequired()])
    movie_review = StringField('Review', validators=[DataRequired()])
    submit = SubmitField('Submit')


class AddMovieForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')


with app.app_context():
    db.create_all()


# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
#
# with app.app_context():
#     db.session.add(new_movie)
#     db.session.commit()


@app.route("/")
def home():
    movies = db.session.execute(db.select(Movie)).scalars().all()
    return render_template("index.html", movies=movies)


@app.route("/edit", methods=["GET", "POST"])
def rate_movie():
    form = MovieForm()  # create a form
    movie_id = request.args.get("id")  # return film's id
    movie = db.get_or_404(Movie, movie_id)  # search for film in database
    if form.validate_on_submit():  # if form is submitted
        movie.rating = float(form.movie_rating.data)  # rating update
        movie.review = form.movie_review.data  # review update
        db.session.commit()  # confirm changes
        return redirect(url_for('home'))
    return render_template("edit.html", movie=movie, form=form)


@app.route("/delete")
def delete_movie():
    movie_id = request.args.get("id")
    movie_to_delete = db.get_or_404(Movie, movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    print(movie_to_delete)
    return redirect(url_for('home'))


@app.route("/add", methods=["GET", "POST"])
def add_movie():
    add_form = AddMovieForm()
    if add_form.validate_on_submit():
        movie_title = add_form.title.data
        response = requests.get(MOVIE_DB_SEARCH_URL, params={
            "api_key": MOVIE_DB_API_KEY, "query": movie_title}
                                )
        data = response.json()["results"]
        return render_template("select.html", options=data)
    return render_template("add.html", form=add_form)


@app.route("/find")
def find_movie():
    movie_api_id = request.args.get("id")
    if movie_api_id:
        movie_api_url = f"{MOVIE_DB_INFO_URL}/{movie_api_id}"
        response = requests.get(movie_api_url, params={"api_key": MOVIE_DB_API_KEY, "language": "en-US"})
        data = response.json()

        # print(f"poster_path: {data.get('poster_path')}")
        # print(f"Full URL: {MOVIE_DB_IMAGE_URL}{data.get('poster_path')}")

        new_movie = Movie(
            title=data["title"],
            year=data["release_date"].split("-")[0],
            img_url=f"{MOVIE_DB_IMAGE_URL}{data['poster_path']}",
            description=data["overview"]
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("rate_movie", id=new_movie.id))


if __name__ == '__main__':
    app.run()  # delete Debut mode, since Flask actually starts two processes -
    # one for the main application and one for the reloader that watches for file changes.
