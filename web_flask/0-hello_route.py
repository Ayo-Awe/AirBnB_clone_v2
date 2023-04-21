#!/usr/bin/python3
"""This module contains a simple flask
server application
"""
from flask import Flask
app = Flask(__name__)


@app.get("/", strict_slashes=False)
def root():
    """Route handler for web server root
    it responsds with 'Hello HBNB'
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
