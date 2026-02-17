"""
    fichier: app.py

    résumé:

    Ce fichier définit une application web Flask qui fournit une interface de calculatrice simple.
    L'application permet aux utilisateurs de saisir une expression arithmétique simple 
    (par exemple, « 3 + 4 ») et calcule le résultat en utilisant les opérateurs de base : addition, 
    soustraction, multiplication et division.

    auteurs: Guillaume Laurin, Maxime Comeau and Brian Ly

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
        Analyse une expression et calcule le résultat.

        :param expr(str): Une chaîne de caractères contenant une expression arithmétique simple avec deux opérandes et un opérateur (par exemple, « 3 + 4 »).
        
        Returns: 
            float: Le résultat du calcul.
        
        Raises:
            ValueError: Si l'expression est invalide ou contient des opérandes non numériques.
    """

    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    s = expr.replace(" ", "")

    op_pos = -1
    op_char = None

    # Trouve l’opérateur dans l’expression
    for i, ch in enumerate(s):
        if ch in OPS:
            if op_pos != -1:
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    if op_pos <= 0 or op_pos >= len(s) - 1:
        # opérateur au début/à la fin ou non trouvé
        raise ValueError("invalid expression format")

    # Divise l’expression en parties gauche et droite
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
        Gère la page principale de l'application de calculatrice. Elle traite les saisies de 
        l'utilisateur à partir d'un formulaire, calcule le résultat en utilisant la fonction 
        calculate et affiche le résultat sur la page.
    """

    result = ""

    # Traite la soumission du formulaire
    if request.method == 'POST':
        expression = request.form.get('display', '')
        try:
            result = calculate(expression)
        except Exception as e:
            result = f"Error: {e}"
    # Affiche la page d’index avec le résultat uniquement s’il s’agit d’une requête POST
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)