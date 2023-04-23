#!/usr/bin/python3
"""This module contains a simple flask
server application. The flask server
listens on PORT 5000, 0.0.0.0
"""
from flask import Flask, escape, render_template
from models import storage, classes
app = Flask(__name__)


@app.teardown_appcontext
def teardown(c):
    """Teardown function is called after each
    request
    """
    storage.close()


@app.route("/states_list", strict_slashes=False)
def serve_states():
    """Route handler for states endpoint
    it responds with html template
    """
    states = storage.all(classes["State"])
    return render_template("7-states_list.html", states=list(states.values()))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
