#!/usr/bin/python3
"""
    starts a flask web app
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """
        Displays "Hello HBNB!"
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
        Displays "HBNB"
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_with_params(text):
    """
        Displays is_cool
    """
    text_no_underscore = text.replace('_', ' ')
    return "C {}".format(text_no_underscore)


@app.route('/python', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_with_text_params(text):
    """

    """
    text_no_underscore = text.replace('_', ' ')
    return "python{}".format(text_no_underscore)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
