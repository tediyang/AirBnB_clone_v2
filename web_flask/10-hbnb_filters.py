#!/usr/bin/python3
""" Your web application must be listening on 0.0.0.0, port 5000
    You must use storage for fetching data from the storage engine
    (FileStorage or DBStorage) => from models import storage and storage.all(...)
    After each request you must remove the current SQLAlchemy Session:
    Declare a method to handle @app.teardown_appcontext
    Call in this method storage.close()
    Routes:
    /hbnb_filters: display a HTML page: (inside the tag BODY)
"""
from flask import Flask
from flask import render_template
from models.state import State
from models.amenity import Amenity
from models import storage
app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def state_filter_list():
    """ state list function """
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template("7-states_list.html", states=states, amenities=amenities)


@app.teardown_appcontext
def teardown():
    """ Close the session """
    return storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)