from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField
from wtforms.fields.simple import SubmitField
from flask_bootstrap import Bootstrap
from wtforms.validators import DataRequired, Email, Length
import email_validator

class LoginForm(FlaskForm):
    login = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label="Log In")



app = Flask(__name__)
app.secret_key = "para-pa-pa-pa-pa"
Bootstrap(app)  # ← инициализация Bootstrap

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    log_form = LoginForm()
    if log_form.validate_on_submit(): # if request.method == "POST" - True/False
        print(log_form.login.data)
        if log_form.login.data == "admin@email.com" and log_form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=log_form)


if __name__ == '__main__':
    app.run(debug=True, port=5003)