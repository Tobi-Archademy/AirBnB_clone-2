#!/usr/bin/python3
"""
Write a script that starts a Flask web application:
"""

from flask import Flask
app = Flask(__name__)
strict_slashes = False


@app.route("/")
def hello():
    """ root routing """
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """ extension hbnb """
    return "HBNB"


@app.route("/c/<arg>")
def cisfun(arg):
    """ using dynamic url """
    string = "C " + arg
    return string.replace("_", " ")


@app.route("/python/")
@app.route("/python")
def hello1():
    """ extension /python """
    return "Python is cool"


@app.route("/python/<arg>")
def hello2(arg):
    """ python extension /text """
    string = "Python " + arg
    return string.replace("_", " ")


@app.route("/number/<int:arg>")
def num(arg):
    """ python extention /int """
    num1 = str(arg) + " is a number"
    return num1


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
