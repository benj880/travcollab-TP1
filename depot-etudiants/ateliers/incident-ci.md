# Incident contrôlé de la chaîne automatique

Dans une branche d'essai dédiée, créer tests/test_incident_ci.py. Ne pas réaliser cette expérience sur main.

```python
import unittest

class IncidentCI(unittest.TestCase):
    def test_incident_controle(self):
        self.assertEqual(1, 2)
```

Avant de lancer : prédire le résultat des tests, de la génération et de l'upload. Exécuter en local puis pousser et ouvrir une PR d'essai. Lire le run correspondant.

Pour réparer cette panne artificielle, retirer ce fichier d'essai dans l'éditeur, enregistrer sa suppression dans un nouveau commit et pousser sur la même branche. Constater le résultat du nouveau run, puis fermer la PR d'essai sans la fusionner.

Si Actions est indisponible, réaliser le même aller-retour avec python tools/build_docs.py. Après un premier succès, provoquer l'échec et vérifier que build/documentation.html est absent ; réparer puis régénérer. Inscrire « preuve locale, Actions non vérifié » dans le journal. Ne pas modifier les protections ou désactiver les tests pour contourner l'incident.
