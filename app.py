"""
    file: app.py

    brief:

    This file defines a Flask web application that provides a simple calculator interface.
    The application allows users to input a simple arithmetic expression (e.g., "3 + 4") and 
    computes the result using basic operators: addition, subtraction, multiplication, and division.

    authors: Guillaume Laurin, Maxime Comeau and Brian Ly

    date: 2026-02-17
"""

from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide

app = Flask(__name__)

OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculate(expr: str):
    """
        Parses an expression and computes the result.

        :param expr(str): A string containing a simple arithmetic expression with two operands and one operator (e.g., "3 + 4").
        
        Returns: 
            float: The result of the computation
        
        Raises:
            ValueError: If the expression is invalid or contains non-numeric operands.
    """

    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    s = expr.replace(" ", "")

    op_pos = -1
    op_char = None

    # Find the operator in the expression
    for i, ch in enumerate(s):
        if ch in OPS:
            if op_pos != -1:
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    if op_pos <= 0 or op_pos >= len(s) - 1:
        # operator at start/end or not found
        raise ValueError("invalid expression format")

    # Split the expression into left and right parts
    left = s[:op_pos]
    right = s[op_pos+1:]

    try:
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("operands must be numbers")

    return OPS[op_char](a, b)

@app.route('/', methods=['GET', 'POST'])
def index():
    """ 
        Handles the main page of the calculator application. It processes user input from a form, 
        computes the result using the calculate function, and renders the result on the page.
    """

    result = ""

    # Process form submission
    if request.method == 'POST':
        expression = request.form.get('display', '')
        try:
            result = calculate(expression)
        except Exception as e:
            result = f"Error: {e}"
    # Render the index page with the result only if it's a POST request
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)