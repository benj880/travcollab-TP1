"""Génère un rapport technique HTML autonome à partir des sources et des tests."""
from pathlib import Path
import ast, html, os, subprocess, sys

ROOT = Path(__file__).resolve().parents[1]

def render_md(text):
    # Sous-ensemble volontairement simple : titres, paragraphes et blocs de code.
    parts, code, inside = [], [], False
    for line in text.splitlines():
        if line.startswith('```'):
            if inside:
                parts.append('<pre><code>' + html.escape('\n'.join(code)) + '</code></pre>')
                code = []
            inside = not inside
        elif inside:
            code.append(line)
        elif line.startswith('#'):
            level = min(len(line) - len(line.lstrip('#')) + 1, 6)
            parts.append(f'<h{level}>' + html.escape(line.lstrip('# ').strip()) + f'</h{level}>')
        elif line.strip():
            parts.append('<p>' + html.escape(line) + '</p>')
    if code:
        parts.append('<pre>' + html.escape('\n'.join(code)) + '</pre>')
    return '\n'.join(parts)

def main():
    out = ROOT / 'build'
    out.mkdir(exist_ok=True)
    target = out / 'documentation.html'
    # Supprimer seulement l'ancien résultat connu : éviter de livrer un rapport périmé après échec.
    if target.exists():
        target.unlink()
    result = subprocess.run([sys.executable, '-m', 'unittest', 'discover', '-s', 'tests', '-v'],
                            cwd=ROOT, capture_output=True, text=True, encoding='utf-8', errors='replace')
    log = result.stdout + result.stderr
    print(log)
    if result.returncode:
        print('Génération interrompue : corriger les tests.', file=sys.stderr)
        return result.returncode
    revision = os.environ.get('GITHUB_SHA', '')
    if not revision:
        try:
            git_root = subprocess.check_output(['git','rev-parse','--show-toplevel'], cwd=ROOT, stderr=subprocess.DEVNULL, text=True).strip()
            if Path(git_root).resolve() != ROOT.resolve():
                raise OSError('Le projet doit avoir son propre dépôt Git')
            revision = subprocess.check_output(['git','rev-parse','HEAD'], cwd=ROOT, stderr=subprocess.DEVNULL, text=True).strip()
            if subprocess.check_output(['git','status','--porcelain'], cwd=ROOT, text=True).strip():
                revision += ' + modifications locales'
        except (OSError, subprocess.CalledProcessError):
            revision = 'hors dépôt Git — copie locale'
    sections = []
    for path in sorted((ROOT/'docs').glob('*.md')):
        sections.append('<section><small>Source : docs/' + html.escape(path.name) + '</small>' + render_md(path.read_text(encoding='utf-8')) + '</section>')
    tree = ast.parse((ROOT/'campus.py').read_text(encoding='utf-8'))
    api = []
    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            signature = node.name + '(' + ast.unparse(node.args) + ')'
            if node.returns:
                signature += ' -> ' + ast.unparse(node.returns)
            api.append('<h3>' + html.escape(signature) + '</h3><p>' + html.escape(ast.get_docstring(node) or 'Documentation absente') + '</p>')
    page = '<!doctype html><html lang="fr"><meta charset="utf-8"><title>Campus Events — Documentation technique</title><style>body{font:18px/1.65 system-ui;max-width:1000px;margin:50px auto;padding:0 24px;color:#151515}h1,h2{color:#007569}section{margin:40px 0}pre{background:#edf8f4;padding:20px;white-space:pre-wrap}small{color:#55635d}@media print{body{font-size:11pt;margin:0}section{break-inside:avoid}}</style><h1>Campus Events</h1><p>Documentation technique générée à partir des sources du dépôt.</p><p>Révision des sources : <code>' + html.escape(revision) + '</code></p><p>Sur une pull request, la révision GitHub peut être celle du commit de fusion de test. Consulter le run associé pour identifier les branches.</p>'
    page += ''.join(sections) + '<section><h2>Référence API extraite du code</h2>' + ''.join(api) + '</section><section><h2>Résultat réel des tests</h2><pre>' + html.escape(log) + '</pre></section></html>'
    target.write_text(page, encoding='utf-8')
    print('Rapport créé :', target)
    return 0

if __name__ == '__main__':
    sys.exit(main())
