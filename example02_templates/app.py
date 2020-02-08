from flask import Flask, render_template


app = Flask(__name__)


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email


@app.route("/hello")
def hello():
    return render_template("hello.html", title="My Awesome Page", username="Konrad")


@app.route("/user")
def user():
    return render_template("user.html", user=User("kjalowiecki", "dexter2206@gmail.com"))


@app.route("/items")
def items():
    return render_template(
        "items.html",
        items=[{"name": "Mobile Phone", "price": "$100"}, {"name": "Charger", "price": "$20"}],
    )


@app.route("/logged_in")
def logged_in():
    return render_template(
        "loggedin.html",
        logged_in=True
    )


@app.route("/not_logged_in")
def not_logged_in():
    return render_template(
        "loggedin.html",
        logged_in=False
    )


@app.route("/inheritance")
def inheritance():
    return render_template("child.html")


if __name__ == "__main__":
    app.run()
