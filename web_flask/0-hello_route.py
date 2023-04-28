#!/usr/bin/python3
""" Flask Hello world """
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    """ print hello hbnb """
    return "Hello HBNB!"


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000)
