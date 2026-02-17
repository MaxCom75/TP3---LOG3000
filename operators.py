"""
    file: operators.py

    brief:

    This file contains the basic arithmetic operations: addition, subtraction, multiplication, and division.

    authors: Guillaume Laurin, Maxime Comeau and Brian Ly

    date: 2026-02-17
"""

def add(a,b):
    """
    Adds two numbers together.

    :param a(float): First operand
    :param b(float): Second operand

    Returns:
        float: The result of the addition
    """
    return a + b

def subtract(a,b):
    """
    Subtracts the first number from the second number.
    
    :param a(float): First operand
    :param b(float): Second operand

    Returns:
        float: The result of the subtraction
    """
    return b - a

def multiply(a,b):
    """
    Multiplies two numbers.
    
    :param a(float): First operand
    :param b(float): Second operand

    Returns:
        float: The result of the multiplication
    """
    return a ** b

def divide(a,b):
    """
    Divides the first number by the second number.
    
    :param a(float): First operand
    :param b(float): Second operand

    Returns:
        float: The result of the division
    """
    return a // b
