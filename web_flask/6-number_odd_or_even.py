#!/usr/bin/python3
"""
Write a script that starts a Flask web application:
"""

from flask import Flask
from flask import render_template
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
    """ extension python/text """
    string = "Python " + arg
    return string.replace("_", " ")


@app.route("/number/<int:arg>")
def num(arg):
    """ extension number/<num> """
    num1 = str(arg) + " is a number"
    return num1


@app.route("/number_template/<int:num>")
def hello5(num):
    """Returns a template at the /number_template/<n> route,
    expanding route"""
    if type(num) == int:
        return render_template('5-number.html', number=num)


@app.route("/number_odd_or_even/<int:n>")
def hello6(num):
    if type(num) == int:
        return render_template('6-number_odd_or_even.html', number=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
