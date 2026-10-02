# Ressources pour chercher et vérifier

## Préparation autonome

Prérequis : Python 3.11 ou supérieur, Git, un éditeur, un navigateur et un compte GitHub individuel. Aucun paquet Python externe. L'établissement fournit les cinq dépôts et les droits avant la séance. La connexion Git doit fonctionner ; un jeton ne doit jamais apparaître dans l'URL ou un document de preuve.

1. Extraire le kit complet. Ouvrir cours-interactif.html dans un navigateur.
2. Ouvrir le dépôt attribué par le formateur, copier son URL HTTPS depuis Code.
3. Cloner dans un dossier de travail, puis ouvrir le terminal dans ce dossier.
4. Exécuter le diagnostic ci-dessous. Sous Windows, utiliser py si python n'est pas reconnu ; sous macOS/Linux, python3 selon l'installation.

```sh
git clone URL_DU_DEPOT
cd NOM_DU_DEPOT
python tools/diagnostic.py
python -m unittest discover -s tests -v
```

Le résultat initial attendu est quatre tests réussis. Les défauts métier restent présents. Le diagnostic vérifie les fichiers et Python ; il ne prouve ni les droits GitHub ni la conformité métier.

## Outils du kit

| Besoin | Ressource | Résultat ou limite |
| --- | --- | --- |
| Vérifier le poste | python tools/diagnostic.py | Diagnostic local, aucune connexion |
| Tester votre code | python -m unittest discover -s tests -v | Tests du groupe, incomplets au départ |
| Vérifier votre mission | python tools/verifier.py A | Remplacer A par B, C ou D ; échec initial attendu |
| Vérifier les quatre contrats | python tools/verifier.py all | Exemples publics ; ne remplace pas vos propres tests |
| Produire la documentation | python tools/build_docs.py | build/documentation.html si les tests du groupe passent |
| Garder les preuves | ateliers/preuves/tp01.md à tp08.md | Huit trames à compléter dans le dépôt |
| Explorer des cas | ateliers/cas-exploration.json | Entrées à examiner ; prédire avant exécution |
| Rendre une revue ou un audit | ateliers/grille-revue.md et grille-audit.md | Modèles à copier ou compléter |

Le vérificateur public est volontairement distinct de la suite de tests du groupe : il permet un contrôle par mission sans rendre tout le dépôt initial inutilisable. La CI exécute les tests présents dans tests/ via build_docs.py ; elle ne lance pas automatiquement verifier.py. À la livraison, vous devez lancer les deux et conserver leurs résultats.

## Aide locale et recherche documentaire

```sh
git help COMMAND
git COMMAND -h
python -m unittest -h
python tools/verifier.py -h
```

Remplacez COMMAND par la commande étudiée. Dans votre journal, notez la question recherchée, la page ou l'aide consultée, l'information retenue et l'expérience qui la confirme. Une citation de documentation sans expérience n'est pas une preuve de fonctionnement.

Références officielles :

- Git, commandes et concepts : https://git-scm.com/docs
- GitHub flow : https://docs.github.com/en/get-started/using-github/github-flow
- Revue de PR : https://docs.github.com/en/pull-requests/how-tos/review-pull-requests/reviewing-proposed-changes-in-a-pull-request
- unittest : https://docs.python.org/3/library/unittest.html
- Python et Actions : https://docs.github.com/en/actions/tutorials/build-and-test-code/python
- Artefacts : https://docs.github.com/en/actions/tutorials/store-and-share-data

Les captures et animations de ressources-notions.html sont également disponibles hors connexion. Les références en ligne sont un complément ; le kit suffit pour les expériences locales.

## Mémo à consulter quand vous avez une question

| Intention | Commande ou emplacement | Attention |
| --- | --- | --- |
| Comprendre l'état courant | git status | À lire avant de changer de branche |
| Voir les modifications | git diff ; git diff --staged | Non indexé puis indexé |
| Voir le parcours | git log --oneline --graph --all | Aide à expliquer les branches |
| Créer une branche | git switch -c NOM | Partir du main synchronisé |
| Sélectionner un fichier | git add CHEMIN | Vérifier le diff sélectionné |
| Enregistrer | git commit -m "Message précis" | Reste local |
| Publier la première fois | git push -u origin NOM | Vérifier la bonne branche |
| Récupérer l'état distant | git fetch origin | N'intègre pas automatiquement dans votre branche |
| Mettre main à jour | git switch main ; git pull --ff-only | Un refus demande un diagnostic |
| Intégrer main dans votre branche | git merge origin/main | Après fetch ; conflits possibles |
| Abandonner une fusion conflictuelle non committée | git merge --abort | Lire l'état et garder les preuves avant |
| Consulter une PR | Conversation, Commits, Checks, Files changed | Lire base et compare |
| Identifier une révision | git rev-parse HEAD | Une PR CI peut utiliser une fusion de test |

Les points-virgules du tableau séparent deux commandes à exécuter l'une après l'autre. Ne lancez pas reset --hard, force push ou une suppression de dépôt pour faire disparaître un blocage.

## Dépannage par hypothèse

| Symptôme | Vérification | Suite raisonnable |
| --- | --- | --- |
| Python introuvable | python --version ou py --version | Signaler un prérequis de poste, utiliser un poste prêt |
| campus introuvable | Dossier courant contenant campus.py ? | Revenir à la racine du clone |
| Zéro test | Noms test_*.py et dossier tests ? | Relancer avec -s tests |
| PR vide | Branche source, commit puis push ? | Corriger le contexte de comparaison |
| Push refusé | Droits, réseau, historique distant ? | Lire le message ; fetch et inspection ; demander aide si conflit |
| Impossible d'approuver | Êtes-vous l'auteur ? Avez-vous accès ? | Demander une revue à un autre membre autorisé |
| Pas de run | Événement prévu ? Workflow présent ? Politique Actions ? | Vérifier le fichier et demander au formateur pour les droits |
| Pas d'artefact | Bon run, réussite, rétention ? | Lire le job avant de rechercher un fichier |

## Mode de secours sans réseau

Utiliser le dossier depot-etudiants comme copie locale. Les tests, les branches après git init et les conflits locaux restent possibles ; la revue se joue sur un diff et sa grille. Indiquer explicitement « simulation locale ». GitHub PR et Actions devront être rejoués quand l'accès revient ; une simulation n'est pas une PR publiée.

Si Git manque mais Python fonctionne, démarrer la cartographie et les expériences métier sur ce poste, puis rejoindre un poste Git prêt en tournant le clavier. Si Python manque aussi, utiliser un poste préparé : aucune installation payante ou environnement cloud n'est nécessaire au parcours.
