import unittest
from campus import peut_inscrire, places_restantes, normaliser_nom, taux_remplissage

class TestCampus(unittest.TestCase):
    def test_inscription_nominale(self):
        self.assertTrue(peut_inscrire(2, 4))

    def test_places_nominales(self):
        self.assertEqual(places_restantes(2, 4), 2)

    def test_nom_nominal(self):
        self.assertEqual(normaliser_nom("ALICE"), "alice")

    def test_taux_nominal(self):
        self.assertEqual(taux_remplissage(2, 4), 50.0)

if __name__ == '__main__':
    unittest.main()
