#!/usr/bin/python3
""" Display the states data stored in the database """
from flask import Flask
from flask import render_template
from 
app = Flask(__name__)


@app.teardown_appcontext
def teardown():
    return storage.close()


@app.route('/states_list', strict_slashes=False)
def state_list():
    
    


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
