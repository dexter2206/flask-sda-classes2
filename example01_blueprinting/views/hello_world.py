"""Hello world example."""

from flask import Blueprint


hello = Blueprint("hello", __name__)


@hello.route("/")
def hello_world():
    return "Hello, World!"


@hello.route("/greetings/<who>")
def greetings(who):
    return f"Greetings, {who}"
