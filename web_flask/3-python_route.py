#!/usr/bin/python3
"""This module contains a simple flask
server application. The flask server
listens on PORT 5000 of 0.0.0.0
"""
from flask import Flask, escape
app = Flask(__name__)


@app.get("/", strict_slashes=False)
def serve_root():
    """Route handler for web server root
    it responds with 'Hello HBNB!'
    """
    return "Hello HBNB!"


@app.get("/hbnb", strict_slashes=False)
def hbnb():
    """Route handler for web hbnb endpoint
    it responds with 'HBNB!'
    """
    return "HBNB"


@app.get("/c/<text>", strict_slashes=False)
def c_handler(text):
    """Route handler for c endpoint. It responds
    with some text from the route parameters
    """
    return "C {}".format(escape(text.replace("_", " ")))


@app.get("/python", strict_slashes=False)
@app.get("/python/<text>", strict_slashes=False)
def python_handler(text="is_cool"):
    """Route handler for python endpoint,
    it responds with some python text concatinated
    with a route parameter is any
    """
    return "Python {}".format(escape(text.replace("_", " ")))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
