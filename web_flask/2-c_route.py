#!/usr/bin/python3
""" Module - script that starts a flask app """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnh():
    """Handles the root url"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hnbn():
    """url to display hbnb"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """using variable to create url"""
    return "C {}".format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
