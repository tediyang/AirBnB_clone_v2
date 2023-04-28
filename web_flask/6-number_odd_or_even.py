#!/usr/bin/python3
""" Module - script that starts a flask app """
from flask import Flask
from flask import render_template
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


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """using variable to create url"""
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """using int variable"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """diplaying number template if only n is int"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_even(n):
    """diplaying number template if only n is int"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
