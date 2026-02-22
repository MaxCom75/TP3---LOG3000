"""
    fichier: test_app.py

    résumé:

    Ce fichier contient des tests pour la fonction calculate (logique de calcul) et la route 
    principale '/' de l'application Flask.

    auteurs: Guillaume Laurin, Maxime Comeau and Brian Ly

    date: 2026-02-21
"""

import pytest
from app import calculate, app

def test_addition_positive_positive():
    """
    Vérifie que la fonction calculate effectue correctement une addition de deux nombre positifs.
    """
    assert calculate("123+2500") == 2623

def test_addition_negative_positive():
    """Vérifie que la fonction calculate effectue correctement une addition de un nombre négatif à un nombre positif."""
    assert calculate("-123+2500") == 2377

def test_addition_negative_negative():
    """Vérifie que la fonction calculate effectue correctement une addition de deux nombres négatifs."""
    assert calculate("-123+-2500") == -2623

def test_subtraction_positive_result():
    """
    Vérifie que la fonction calculate effectue correctement une soustraction donnant un résultat positif.
    """
    assert calculate("2500-123") == 2377

def test_subtraction_negative_result():
    """
    Vérifie que la fonction calculate effectue correctement une soustraction donnant un résultat négatif.
    """
    assert calculate("123-2500") == -2377

def test_subtraction_negative_positive():
    """
    Vérifie que la fonction calculate effectue correctement une soustraction de un nombre négatif à un nombre positif.
    """
    assert calculate("-123-2500") == -2623

def test_subtraction_positive_negative():
    """
    Vérifie que la fonction calculate effectue correctement une soustraction de un nombre positif à un nombre négatif.
    """
    assert calculate("123--2500") == 2623

def test_multiplication_positive_positive():
    """
    Vérifie que la fonction calculate effectue correctement une multiplication de deux nombres positifs.
    """
    assert calculate("10*10") == 100

def test_multiplication_negative_positive():
    """
    Vérifie que la fonction calculate effectue correctement une multiplication de un nombre négatif à un nombre positif.
    """
    assert calculate("-10*10") == -100

def test_multiplication_negative_negative():
    """
    Vérifie que la fonction calculate effectue correctement une multiplication de deux nombres négatifs.
    """
    assert calculate("-10*-10") == 100

def test_division_whole_number_result_positive_positive():
    """
    Vérifie que la fonction calculate effectue correctement une division donnant un nombre entier.
    """
    assert calculate("8/2") == 4

def test_division_whole_number_result_negative_positive():
    """
    Vérifie que la fonction calculate effectue correctement une division donnant un nombre entier de un nombre négatif par un nombre positif.
    """
    assert calculate("-8/2") == -4

def test_division_whole_number_result_positive_negative():
    """
    Vérifie que la fonction calculate effectue correctement une division donnant un nombre entier de un nombre positif par un nombre négatif.
    """
    assert calculate("8/-2") == -4

def test_division_whole_number_result_negative_negative():
    """
    Vérifie que la fonction calculate effectue correctement une division donnant un nombre entier de deux nombres négatifs.
    """
    assert calculate("-8/-2") == 4

def test_division_decimal_result_positive_positive():
    """
    Vérifie que la fonction calculate effectue correctement une division donnant un nombre à virgule de deux nombres positifs.
    """
    assert calculate("10/4") == 2.5

def test_division_decimal_result_negative_positive():
    """
    Vérifie que la fonction calculate effectue correctement une division donnant un nombre à virgule de un nombre négatif par un nombre positif.
    """
    assert calculate("-10/4") == -2.5

def test_division_decimal_result_positive_negative():
    """
    Vérifie que la fonction calculate effectue correctement une division donnant un nombre à virgule de un nombre positif par un nombre négatif.
    """
    assert calculate("10/-4") == -2.5

def test_division_decimal_result_negative_negative():
    """
    Vérifie que la fonction calculate effectue correctement une division donnant un nombre à virgule de deux nombres négatifs.
    """
    assert calculate("-10/-4") == 2.5

@pytest.fixture
def client():
    """Crée un client de test Flask."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_index_get(client):
    """Vérifie que la page GET / se charge correctement."""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Flask Calculator" in response.data

def test_index_post_valid_expression(client):
    """Vérifie qu'un POST avec une expression valide retourne le bon résultat."""
    response = client.post("/", data={"display": "123+1"})
    assert response.status_code == 200
    assert b"124" in response.data

def test_index_post_invalid_expression(client):
    """Vérifie qu'un POST avec une expression invalide retourne un message d'erreur."""
    response = client.post("/", data={"display": "123++1"})
    assert response.status_code == 200
    assert b"Error" in response.data