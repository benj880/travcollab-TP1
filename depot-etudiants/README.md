# Campus Events

Projet pédagogique Python pour travailler avec GitHub en Bachelor 2.
Ce dépôt initial contient volontairement quatre défauts et seulement quatre tests nominaux.

## Démarrage

Python 3.11 ou plus récent ; aucune bibliothèque externe.
Depuis la racine du dépôt :

```sh
python -m unittest discover -s tests -v
python tools/build_docs.py
```

Sous Windows, utiliser `py` si `python` n'est pas reconnu. Sous macOS/Linux, utiliser `python3` si nécessaire.
Ouvrir ensuite `build/documentation.html` dans un navigateur.

## Règles métier à respecter

Les arguments numériques sont des entiers ; le contrôle des types est hors périmètre.
Pour les trois fonctions numériques : capacité >= 0 et 0 <= inscrits <= capacité.
Toute valeur hors de ce domaine doit lever ValueError.
Une capacité nulle avec zéro inscrit est valide : pas d'inscription possible, zéro place, taux de 0.0.
Un événement plein refuse une inscription supplémentaire.
Un nom normalisé est passé en minuscules et débarrassé des espaces en début et fin ; les espaces intérieurs sont conservés.
Un nom vide après nettoyage doit lever ValueError. L'entrée est toujours une chaîne.

## Organisation

Une issue par besoin, une branche par changement, une pull request relue par un autre membre.
Ne pas pousser directement sur main après l'initialisation. Lire CONTRIBUTING.md et MISSIONS.md.
Compléter les documents de docs/ et les preuves de contribution dans docs/contributions.md.

## Livraison

Tests réussis ; quatre défauts corrigés ; documentation expliquée et relue ; rapport HTML généré.
Le dossier build/ est un résultat de génération, pas une source à modifier ou à committer.


## Parcours autonome des huit TP

Commencer par ateliers/TP01.md puis suivre les huit fiches TP01 à TP08. Les horaires et restitutions sont indiqués dans chaque fiche. Lire ateliers/RESSOURCES.md pour les commandes et le dépannage.

```sh
python tools/diagnostic.py
python tools/verifier.py A
python tools/verifier.py all
```

Le vérificateur échoue volontairement sur le code initial. Il couvre des exemples publics du contrat et ne remplace pas vos tests ni vos revues. Compléter une trace par atelier dans ateliers/preuves/tp01.md à tp08.md.

Chaque TP se termine par une démonstration à un pair et un verdict argumenté consigné. Le dossier ateliers/ contient les incidents, cas d'exploration, grilles de revue, audit, contrôle documentaire et scénario d'échec CI. Aucun fichier de solution métier n'est nécessaire pour commencer.
