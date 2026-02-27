from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean

app = Flask(__name__)

class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


with app.app_context():
    db.create_all()


# Home
@app.route("/")
def home():
    cafes = db.session.execute(db.select(Cafe)).scalars().all()
    return render_template("index.html", cafes=cafes)


# Add
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_cafe = Cafe(
            name=request.form["name"],
            map_url=request.form["map_url"],
            img_url=request.form["img_url"],
            location=request.form["location"],
            seats=request.form["seats"],
            coffee_price=request.form["coffee_price"],
            has_wifi=request.form.get("has_wifi") == "on",
            has_sockets=request.form.get("has_sockets") == "on",
            has_toilet=request.form.get("has_toilet") == "on",
            can_take_calls=request.form.get("can_take_calls") == "on",
        )
        db.session.add(new_cafe)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html")


# Edit
@app.route("/edit/<int:cafe_id>", methods=["GET", "POST"])
def edit(cafe_id):
    cafe = db.session.get(Cafe, cafe_id)
    if request.method == "POST":
        cafe.name = request.form["name"]
        cafe.map_url = request.form["map_url"]
        cafe.img_url = request.form["img_url"]
        cafe.location = request.form["location"]
        cafe.seats = request.form["seats"]
        cafe.coffee_price = request.form["coffee_price"]
        cafe.has_wifi = request.form.get("has_wifi") == "on"
        cafe.has_sockets = request.form.get("has_sockets") == "on"
        cafe.has_toilet = request.form.get("has_toilet") == "on"
        cafe.can_take_calls = request.form.get("can_take_calls") == "on"
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", cafe=cafe)


# Delete
@app.route("/delete/<int:cafe_id>")
def delete(cafe_id):
    cafe = db.session.get(Cafe, cafe_id)
    if cafe:
        db.session.delete(cafe)
        db.session.commit()
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True)