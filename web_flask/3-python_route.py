#!/usr/bin/python3
"""This module contains a simple flask
server application
"""
from flask import Flask, escape
app = Flask(__name__)


@app.get("/", strict_slashes=False)
def root():
    """Route handler for root of
    web server
    """
    return "Hello HBNB!"


@app.get("/hbnb", strict_slashes=False)
def hbnb():
    """Route handler for /hbnb endpoint
    """
    return "HBNB"


@app.get("/c/<text>", strict_slashes=False)
def c_handler(text):
    """Route handler for /c endpoint
    """
    return "C {}".format(escape(text.replace("_", " ")))


@app.get("/python", strict_slashes=False)
@app.get("/python/<text>", strict_slashes=False)
def python_handler(text="is_cool"):
    """Route handler for /python endpoint
    """
    return "Python {}".format(escape(text.replace("_", " ")))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
