## Module template ##

## Raison d’être du module
Le module template a pour objectif de définir l’interface utilisateur de l’application développée avec le framework Flask.

Il contient les fichiers responsables de la structure HTML et de l’interaction côté client. Ce module permet :
    - D’afficher l’interface graphique de la calculatrice.
    - De présenter le champ d’affichage des résultats.
    - De gérer l’entrée utilisateur via les boutons numériques et opérateurs.
    - D’envoyer les expressions mathématiques au serveur Flask pour traitement.

Il constitue la couche de présentation de l’application selon le modèle MVC.

## Fichiers principaux et leurs responsabilités

### index.html
Définir la structure et le comportement de l’interface de la calculatrice.

Responsabilités:
    - Structure HTML
    - Intégration avec Flask
    - Boutons de la calculatrice

## Dépendances et hypothèses

### Dépendances
Le module template dépend des éléments suivants :
    - Flask
    - Dossier static
    - Fichier style.css requis pour la mise en forme de l’interface
    - Navigateur web moderne compatible avec HTML5

### Hypothèses
    - Une route Flask existe pour recevoir le formulaire.
    - Le backend valide et sécurise les expressions envoyées par l’utilisateur.
    - Le CSS définit correctement les classes utilisées dans le HTML.