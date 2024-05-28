#!/usr/bin/python3
"""Flask framework
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """Home Page For HBNB"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """HBNB Page, displays HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def greeting_c(text):
    """Greeting Route for C"""
    return "C " + text.replace("_", " ")


@app.route("/python/", defaults={"text": "is_cool"})
@app.route("/python/<text>", strict_slashes=False)
def greeting_python(text):
    """Greeting Python"""
    return "Python " + text.replace("_", " ")


@app.route("/number/<int:n>", strict_slashes=False)
def display_number(n):
    """Number route"""
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
