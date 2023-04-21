#!/usr/bin/python3
"""This module contains a simple flask
server application
This script starts a flask application that listens
on PORT 5000
"""
from flask import Flask
app = Flask(__name__)


@app.get("/", strict_slashes=False)
def serve_root():
    """Route handler for web server root
    it responds with 'Hello HBNB!'
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
