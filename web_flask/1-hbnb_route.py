#!/usr/bin/python3
"""This module contains a simple flask
server application. The flask server
listens on PORT 5000 of 0.0.0.0. Enjoy!!!
"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def serve_root():
    """Route handler for web server root
    it responds with 'Hello HBNB!'
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Route handler for web hbnb endpoint
    it responds with 'HBNB!'
    """
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
