#!/usr/bin/python3
"""Starts web application"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def greeting_c(text):
    return "C " + text.replace("_", " ")


@app.route("/python", strict_slashes=False)
def default_python_greeting():
    return "Python is cool"


@app.route("/python/<text>", strict_slashes=False)
def greeting_python(text):
    return "Python " + text.replace("_", " ")


if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
