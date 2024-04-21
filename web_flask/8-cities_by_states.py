#!/usr/bin/python3
"""flask webframe for lists of states in AiBnB"""
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/cities_by_states')
def cities_by_states_list():
    """list all states saved in a instance of dbstorage"""
    states_dict = storage.all("State")
    return render_template('8-states_list.html', states=states_dict)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
