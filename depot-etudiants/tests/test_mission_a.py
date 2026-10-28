import unittest
from campus import peut_inscrire

class TestMissionA(unittest.TestCase):
    # Nominal : il reste des places
    def test_place_disponible(self):
        self.assertIs(peut_inscrire(3, 4), True)

    def test_evenement_vide(self):
        self.assertIs(peut_inscrire(0, 7), True)

    # Frontière : régression de l'incident A, l'événement est plein
    def test_evenement_plein_refuse(self):
        self.assertIs(peut_inscrire(4, 4), False)

    def test_capacite_nulle_refuse(self):
        self.assertIs(peut_inscrire(0, 0), False)

    # Cas original : un seul siège, déjà pris
    def test_derniere_place_prise(self):
        self.assertIs(peut_inscrire(1, 1), False)

    # Invalide : hors du domaine 0 <= inscrits <= capacite
    def test_inscrits_negatifs(self):
        with self.assertRaises(ValueError):
            peut_inscrire(-1, 4)

    def test_inscrits_superieurs_capacite(self):
        with self.assertRaises(ValueError):
            peut_inscrire(5, 4)

    def test_capacite_negative(self):
        with self.assertRaises(ValueError):
            peut_inscrire(0, -1)

if __name__ == '__main__':
    unittest.main()
