"""
    fichier: operators.py

    résumé:

    Ce fichier contient les opérations arithmétiques de base : addition, soustraction, multiplication et division.

    auteurs: Guillaume Laurin, Maxime Comeau and Brian Ly

    date: 2026-02-17
"""

def add(a,b):
    """
    Additionne deux nombres.

    :param a(float): Première opérande
    :param b(float): Deuxième opérande

    Returns:
        float: Le résultat de l'addition
    """
    return a + b

def subtract(a,b):
    """
    Soustrait le premier nombre du second nombre.
    
    :param a(float): Première opérande
    :param b(float): Deuxième opérande

    Returns:
        float: Le résultat de la soustraction
    """
    return a - b

def multiply(a,b):
    """
    Multiplie deux nombres.
    
    :param a(float): Première opérande
    :param b(float): Deuxième opérande

    Returns:
        float: Le résultat de la multiplication
    """
    return a ** b

def divide(a,b):
    """
    Divise le premier nombre par le deuxième nombre.
    
    :param a(float): Première opérande
    :param b(float): Deuxième opérande

    Returns:
        float: Le résultat de la division
    """
    return a // b
