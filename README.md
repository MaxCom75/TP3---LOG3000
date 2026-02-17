TP3--LOG3000

Équipe 18

Objectif:
Vous avez rejoint une petite équipe de développement dans une startup qui construit une
application web qui consiste en une calculatrice simple. L’équipe a déjà rédigé un peu de code,
mais elle n’a pas encore de bonnes pratiques de gestion de versions. Votre gestionnaire a demandé
à votre équipe de configurer le projet sur GitHub afin de mieux collaborer.
Au cours des prochaines semaines, différents développeurs corrigeront des bogues et ajouteront
des fonctionnalités. Pour s’y préparer, vous devez :
    • Créer et configurer un dépôt GitHub.
    • Documenter le dépôt et la base de code.
    • Réaliser des tests et des corrections de bogues au moyen d’un pipeline entièrement
      documenté.
Enfin, sachez que la base de code actuelle est désordonnée, mal documentée et contient des bogues
cachés. Sans surprise, votre patron n’a pas vraiment d’idée de ce qui se passe « sous le capot ». On
vous donnera seulement une description approximative de ce que chaque composant est censé
faire. C’est à vous de prendre le relais, d’apporter de la structure au projet et de rendre l’application
fiable.

Prérequis d'installation:
Avant de commencer, assurez-vous d’avoir :
    • Un compte GitHub.
    • Git installé localement.
    • Python et pip installés.
    • Flask d'installés

Instruction d'installation:
Vous devez cloner ce dépôt Github:

    git clone git@github.com:greyli/flask-examples.git

Ou:

    git clone https://github.com/helloflask/flask-examples.git

Vous aller devoir créer un environnement virtuel et installer les dépendances:

    python3 -m venv venv  # sur Windows, utiliser "python -m venv venv" à la place
    . venv/bin/activate   # sur Windows, utiliser "venv\Scripts\activate" à la place
    pip install -r requirements.txt