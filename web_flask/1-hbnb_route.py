#!/usr/bin/python3
"""This module contains a simple flask
server application
"""
from flask import Flask
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
