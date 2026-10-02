# Contribuer

1. Créer une issue avec besoin, cas observé, résultat attendu et critères d'acceptation.
2. Synchroniser main et créer une branche courte : fix/numero-sujet ou docs/numero-sujet.
3. Écrire un test de régression qui échoue, puis corriger et relancer tous les tests.
4. Examiner git diff puis git diff --staged avant le commit.
5. Pousser la branche, ouvrir une PR vers main, lier l'issue et demander une revue.
6. Relire une autre PR : reproduire un cas, commenter une ligne et rendre une décision argumentée.
7. Après correction, refaire les tests et relire le nouveau diff avant approbation.
8. Fusionner après revue et contrôle réussi ; synchroniser main localement.

## Convention de revue

Format : constat, impact, proposition, test attendu. Signaler si le commentaire est bloquant ou facultatif.
L'auteur ne valide pas sa propre PR. Une coche verte ne prouve pas l'exhaustivité des tests.
Résoudre une conversation ne remplace pas la correction du code.
En cas de désaccord, revenir aux critères de l'issue et faire trancher un troisième membre.
