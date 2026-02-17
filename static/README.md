## Module static ##

## Raison d'être du module
Le module static a pour objectif de regrouper toutes les ressources statiques nécessaires à l’interface utilisateur de l’application.

Il est responsable de :
    - La mise en forme visuelle de l’application (styles CSS)
    - L’apparence et l’ergonomie de la calculatrice
    - L’expérience utilisateur (UX) côté client
    - La séparation claire entre la logique et la présentation

Ce module ne contient aucune logique de calcul. Il gère uniquement la couche visuelle.

## Fichiers principaux et leurs responsabilités

### style.css
Fichier principal de stylisation de l’application.

Responsabilités :
    - Définition du style global de la page (body)
    - Mise en forme du conteneur principal .calculator
    - Stylisation du titre (h1)
    - Mise en forme de l’écran d’affichage (#display)
    - Organisation des boutons via une grille CSS (.buttons)
    - Stylisation des boutons (.btn)
    - Mise en évidence des opérateurs (.operator)

## Dépendances et hypothèses

### Dépendances
Compatible avec les navigateurs modernes supportant :
    - Flexbox
    - CSS Grid
    - Transitions CSS

Nécessite un fichier HTML structuré avec les mêmes classes que défini dans les fichiers css.

### Hypothèses
Le module est intégré dans une architecture séparant :
    - Frontend (statique)
    - Backend (logique de calcul)