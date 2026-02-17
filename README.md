# TP3--LOG3000

Équipe 18

## But
Le but du projet est de développer une application web qui consiste en une calculatrice simple.

La documentation est utilisée pour structurer le projet. Elle résume les différents modules utilisés dans l'application, elle décrit les grosses lignes de la majorité des fichiers et décrit les comportements attendu de chaque fonction utilisée.

## Décomposition du projet
Le projet est construit avec la biblothèque Flask de python

- **Frontend**
    - Un fichier HTML qui fournit l'interface utilisateur
    - Un fichier CSS qui gère le style

- **Backend**
    - Un fichier Python qui exécute le serveur Flask et gère la logique
    - Un fichier Python qui contient les functions utilitaites d'opérations

- **Tests**
    - Quelques fichiers Python qui testent unitairement les différentes functions

## Installation 

### Dépôt Github
Vous devez cloner ce dépôt Github:

    git clone git@github.com:greyli/flask-examples.git

Ou:

    git clone https://github.com/helloflask/flask-examples.git

Vous aller devoir vous déplacer dans le répertoire fraichement cloné:

    cd TP3---LOG3000

### Environnement virtuel
Vous aller devoir créer un environnement virtuel

    python3 -m venv venv  # sur Windows, utiliser "python -m venv venv" à la place
    . venv/bin/activate   # sur Windows, utiliser "venv\Scripts\activate" à la place

### Installation des dépendances
    pip install -r requirements.txt

### Exécuter l'application
Vous aller devoir exécuter la commande suivant

    flask run

### Utilisation
une fois que l'application est exécuté

### Exécuter les tests
Vous aller devoir exécuter la commande suivante

    python -m pytest

## Contribution
Si vous souhaitez contribuer au projet:

Différents préfixe de branche:
1. feature : Ajoute nouvelle fonctionnalité
2. fix : Correction de fonctionnalité avec bug
3. documentation : Ajoute seulement de la documentation

### 1. Créer une branche :
    git checkout -b feature/ma-nouvelle-fonctionnalité

### 2. Effectuer vos modification et commiter :
    git add .
    git commit -m "Ajouter une nouvelle fonctionnalité"

### 3. Soumettre une Pull Request (PR) :
- Depuis votre branche vers `dev`
- Décrire clairement les changements et le but de la PR
- Une PR sans tests unitaires ne sera pas considérée et sera automatiquement rejetée

### 4. Gérer les issues :
- Créez une issue pour signaler un bug ou proposer une amélioration.
- Liez votre PR à l'issue correspondante
