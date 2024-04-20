#!/usr/bin/python3
""" dynamic content configuration on
server listening on 0.0.0.0, port 5000"""

from flask import Flask, render_template
from markupsafe import escape


app = Flask(__name__)
app.__strict_slashes__ = False
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """return "Hello HBNB!" """
    return 'Hello HBNB!'


@app.route('/hbnb')
def HBNB():
    """return HBNB!" """
    return 'HBNB'


@app.route('/c/<text>')
def c_text(text):
    """ display “C ” followed by the value of the text variable"""
    return 'C {}'.format(escape(text).replace('_', ' '))


@app.route("/python")
@app.route('/python/<text>')
def python_text(text='is cool'):
    """ display “Python ” followed by the value of the text variable"""
    return 'Python {}'.format(escape(text).replace('_', ' '))


@app.route('/number/<int:n>')
def number(n):
    """ display “n is a number” only if n is an integer"""
    return '{} is a number'.format(escape(n))


@app.route('/number_template/<int:n>')
def number_page(n):
    """ display a html page only if n is an integer"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_type(n):
    """ display a html page to indicate n and its type
    only if n is an integer"""
    if n % 2 == 0:
        type = 'even'
    else:
        type = 'odd'
    return render_template('6-number.html', n=n, type=type)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
