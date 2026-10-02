"""Vérifications publiques du contrat : python tools/verifier.py A|B|C|D|all.

Ce vérificateur ne corrige aucun code et ne remplace ni vos tests ni une revue.
Ses échecs sur la version initiale sont attendus. Il ne valide pas les preuves GitHub.
"""
from pathlib import Path
import argparse
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from campus import peut_inscrire, places_restantes, normaliser_nom, taux_remplissage

class Contrat(unittest.TestCase):
    def numeriques(self, fn, cas):
        for entree, attendu in cas:
            with self.subTest(entree=entree):
                resultat = fn(*entree)
                if isinstance(attendu, bool):
                    self.assertIs(resultat, attendu)
                else:
                    self.assertAlmostEqual(resultat, attendu)
        for entree in [(-1,4),(5,4),(0,-1)]:
            with self.subTest(invalide=entree):
                with self.assertRaises(ValueError): fn(*entree)

    def test_A(self):
        self.numeriques(peut_inscrire, [((3,4),True),((4,4),False),((0,0),False),((0,7),True)])

    def test_B(self):
        self.numeriques(places_restantes, [((1,4),3),((4,4),0),((0,0),0),((2,7),5)])

    def test_C(self):
        for entree,attendu in [(' ALICE ','alice'),('Anne Marie','anne marie'),('  Ali  Baba  ','ali  baba')]:
            with self.subTest(entree=entree): self.assertEqual(normaliser_nom(entree),attendu)
        for entree in ['', '   ']:
            with self.subTest(invalide=entree):
                with self.assertRaises(ValueError): normaliser_nom(entree)

    def test_D(self):
        self.numeriques(taux_remplissage, [((2,4),50.0),((4,4),100.0),((0,0),0.0),((1,3),100/3)])

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mission', choices=['A','B','C','D','all'], nargs='?', default='all')
    args=parser.parse_args()
    names=['A','B','C','D'] if args.mission=='all' else [args.mission]
    suite=unittest.TestSuite(Contrat('test_'+name) for name in names)
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    print('Ce contrôle public couvre des exemples du contrat, pas toutes les propriétés du logiciel.')
    return 0 if result.wasSuccessful() else 1

if __name__=='__main__':
    sys.exit(main())
