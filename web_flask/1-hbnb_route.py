#!/usr/bin/python3
"""A script that starts a flask web application"""

from flask import Flask

app = Flask(__name__)
strict_slashes=False


@app.route("/")
def hello():
    """return the root page"""
    return "Hello HBNB!"

@app.route("/hbnb")
def index():
    """returns the index page"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
