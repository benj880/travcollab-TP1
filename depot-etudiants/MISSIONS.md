# Contrats détaillés des quatre missions

Pour démarrer le TP3, commencez par ateliers/incidents.md. Ce document explicite les critères métier et peut être consulté pour vérifier vos hypothèses ; il ne contient pas les corrections.

Créer une issue GitHub par mission. Répartition A, B, C, D ; pas de partage d'identifiants.

## A — Refuser une inscription lorsque l'événement est plein

Fonction peut_inscrire. Exemples attendus : (3,4) -> True ; (4,4) -> False ; (0,0) -> False.
Entrées (-1,4), (5,4), (0,-1) -> ValueError.
Ajouter les tests avant la correction. Documenter les cas limites dans la docstring.

## B — Fiabiliser le calcul des places

Fonction places_restantes. (1,4) -> 3 ; (4,4) -> 0 ; (0,0) -> 0.
Entrées (-1,4), (5,4), (0,-1) -> ValueError. Ne pas masquer une erreur avec max(0, ...).

## C — Normaliser les noms

Fonction normaliser_nom. " ALICE " -> "alice" ; "Anne Marie" -> "anne marie".
"", "   " -> ValueError. Ne pas modifier les espaces intérieurs.

## D — Gérer un événement de capacité nulle

Fonction taux_remplissage. (2,4) -> 50.0 ; (4,4) -> 100.0 ; (0,0) -> 0.0.
Entrées (-1,4), (5,4), (0,-1) -> ValueError. Documenter le choix pour 0/0.

## Définition de terminé

Une PR par mission ; test de régression ; cas normal, limite et invalide ; docstring ; revue d'un pair ; CI verte.
Ne pas ajouter de framework, d'interface web ni de base de données : la collaboration est l'objectif.