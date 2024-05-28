#!/usr/bin/python3
"""Starts web application"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """Home Page"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """HBNB Page"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """C Lang Greeting"""
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


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """number template"""
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
