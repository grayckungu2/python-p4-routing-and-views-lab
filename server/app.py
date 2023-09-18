#!/usr/bin/env python3


# Importing necessary modules
from flask import Flask

# Creating a Flask app
app = Flask(__name__)

# Route for the home page
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# Route for printing a string
@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return parameter

# use Route for counting numbers
@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = '\n'.join(str(num) for num in range(parameter))
    return numbers

# This Route is used for performing math operations
@app.route('/math/<int:num1><operation><int:num2>')
def math(num1, operation, num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    return str(result)

# Running the Flask app
if __name__ == '__main__':
    app.run(port=5555)


