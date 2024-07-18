#!/usr/bin/python3
"""
Flask web app
"""


from flask import Flask, render_template
from models import *

app = Flask(__name__)



@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
    Lists cities linked to states for each state
    """
    return render_template(
                           '8-cities_by_states.html',
                           states=storage.all("State").values()
                           )

@app.teardown_appcontext
def teardown_db(exception):
    """
    closes the storage
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
