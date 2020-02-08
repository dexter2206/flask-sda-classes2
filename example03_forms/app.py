from flask import Flask, render_template, flash, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    name = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_login = BooleanField("Remember Me")
    submit = SubmitField("Sign in")


app = Flask(__name__)
app.config['SECRET_KEY'] = "my-secret-key"


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f"Login user: {form.name.data}, remember_login: {form.remember_login.data}")
        return redirect("/")
    return render_template("login.html", title="Log in", form=form)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()