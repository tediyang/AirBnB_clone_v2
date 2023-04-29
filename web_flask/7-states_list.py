#!/usr/bin/python3
""" Display the States data stored in the database """

from flask import Flask
from flask import render_template
from models.state import State
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def teardown():
    """ Close the session """
    return storage.close()


@app.route('/states_list', strict_slashes=False)
def state_list():
    """ state list function """
    states = storage.all(State)
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
