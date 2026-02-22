## Module tests ##

## Raison d'être du module
Le module tests a pour objectif de regrouper tous les tests unitaires et fonctionnels pour l’application de calculatrice Flask.

Il est responsable de :
    - Vérifier que la fonction calculate retourne le bon résultat pour toutes les opérations arithmétiques
    - Tester les cas de nombres positifs et négatifs
    - Vérifier le fonctionnement de la route Flask / pour les requêtes GET et POST
    - Garantir que les changements dans le code ne cassent pas le comportement attendu

Ce module ne contient aucune logique de calcul ; il teste uniquement le code de l’application.

## Fichiers principaux et leurs responsabilités

### test_app.py
Fichier principal des tests unitaires pour app.py.

Responsabilités :
    - Tests unitaires pour la fonction calculate : addition, soustraction, multiplication, division
    - Tests de cas avec nombres négatifs
    - GET → vérifie que la page se charge correctement
    - POST valide → vérifie que le résultat affiché correspond au calcul
    - POST invalide → vérifie que le message d’erreur est renvoyé

## Dépendances et hypothèses

### Dépendances
Compatible avec les navigateurs modernes supportant :
    - Python 3.12
    - Flask
    - pytest

### Hypothèses
    - Les tests doivent être exécutés depuis la racine du projet où se trouve app.py
    - Les fichiers HTML et CSS sont présents mais ne sont pas testés ici
    - Le module tests dépend de app.py