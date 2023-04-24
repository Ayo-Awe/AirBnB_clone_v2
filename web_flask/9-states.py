#!/usr/bin/python3
"""This module contains a simple flask
server application. The flask server
listens on PORT 5000, 0.0.0.0

This server serves data from the storage engine
and renders it using jinja
"""

from flask import Flask, escape, render_template
from models import storage
import models
app = Flask(__name__)


@app.teardown_appcontext
def teardown(c):
    """Teardown function is called after each
    request

    This function is called after every request
    and it closes the current storage session
    """
    storage.close()


@app.route("/states/<id>", strict_slashes=False)
def serve_single_state(id):
    """Route handler for states endpoint
    it responds with html template

    This endpoint serves data from the storage engine
    and renders it using jinja
    """

    state = storage.all(models.classes["State"]).get("State.{}".format(id))

    if state is not None:
        state.cities.sort(key=lambda x: x.name)

    return render_template("9-states.html", state=state)


@app.route("/states", strict_slashes=False)
def serve_states():
    """Route handler for states endpoint
    it responds with html template

    This endpoint serves data from the storage engine
    and renders it using jinja
    """
    states = list(storage.all(models.classes["State"]).values())
    states.sort(key=lambda x: x.name)

    return render_template("9-states.html", states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
