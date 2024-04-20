#!/usr/bin/python3
""" dynamic content configuration on
server listening on 0.0.0.0, port 5000"""

from flask import Flask

app = Flask(__name__)
app.__strict_slashes__ = False


@app.route('/')
def hello():
    """return "Hello HBNB!" """
    return 'Hello HBNB!'


@app.route('/hbnb')
def HBNB():
    """return HBNB!" """
    return 'HBNB'


if __name__ == "__main__":
    app.run(host='0.0.0.0')
