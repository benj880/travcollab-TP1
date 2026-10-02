"""Diagnostic local sans installation, connexion ni modification du dépôt."""
from pathlib import Path
import importlib.util
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]

def main():
    errors = []
    print('Diagnostic Campus Events — aucune donnée envoyée')
    print('Python :', sys.version.split()[0])
    if sys.version_info < (3, 11):
        errors.append('Python 3.11 ou supérieur est nécessaire.')
    print('Dossier courant à la racine du projet :', Path.cwd().resolve() == ROOT)
    if Path.cwd().resolve() != ROOT:
        print('CONSEIL : ouvrez le terminal dans le dossier contenant campus.py.')
    for name in ['campus.py', 'tests/test_campus.py', 'tools/build_docs.py', '.github/workflows/qualite.yml']:
        present = (ROOT / name).is_file()
        print(('OK ' if present else 'ABSENT ')+name)
        if not present: errors.append('Fichier manquant : '+name)
    git = shutil.which('git')
    print('Git disponible :', bool(git))
    if git:
        result = subprocess.run([git, 'rev-parse', '--show-toplevel'], cwd=ROOT, capture_output=True, text=True)
        own_repo = result.returncode == 0 and Path(result.stdout.strip()).resolve() == ROOT
        print('Dépôt Git propre à ce projet :', own_repo)
        if not own_repo: print('INFO : cette copie peut provenir du ZIP ; utilisez le clone préparé pour votre groupe.')
    else:
        print('INFO : les expériences Python restent possibles ; Git est nécessaire aux TP de collaboration.')
    print('Connexion, authentification et droits GitHub : à vérifier par ouverture du dépôt ; non testés ici.')
    print('Contrôle des règles métier : volontairement exclu de ce diagnostic.')
    for error in errors: print('À CORRIGER :',error)
    return 1 if errors else 0

if __name__ == '__main__':
    sys.exit(main())
