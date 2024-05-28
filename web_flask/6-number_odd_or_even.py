#!/usr/bin/python3
"""Starts web application"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """home"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """hbnb"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """c"""
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


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    """odd or even"""
    val = "even" if n % 2 == 0 else "odd"
    return render_template("6-number_odd_or_even.html", val=val, n=n)


if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
