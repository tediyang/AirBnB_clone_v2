#!/usr/bin/python3
"""
    Your web application must be listening on 0.0.0.0, port 5000
    You must use storage for fetching data from the storage engine
    (FileStorage or DBStorage) => from models import storage and storage.all(...)
    After each request you must remove the current SQLAlchemy Session:
    Declare a method to handle @app.teardown_appcontext
    Call in this method storage.close()
    Routes:
    /9-states: display a HTML page: (inside the tag BODY)
"""
from flask import Flask
from flask import render_template
from models.state import State
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def teardown():
    """ Close the session """
    return storage.close()


@app.route('/states', strict_slashes=False)
def state_list():
    """ state list function """
    states = storage.all(State)
    return render_template("9-states.html", states=states, id=None)


@app.route('/states/<id>', strict_slashes=False)
def state_city_list(id):
    """ Get state and cities with the provided id. """
    states = storage.all(State)
    for state_obj in states.values():
        if state_obj.id == id:
            state = state_obj
            return render_template("9-states.html", states=state, id=id)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
