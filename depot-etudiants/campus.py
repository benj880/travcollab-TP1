"""Règles métier de Campus Events. Quatre défauts sont à rechercher en atelier."""

def peut_inscrire(inscrits: int, capacite: int) -> bool:
    """Indique si une nouvelle inscription est possible.

    Renvoie True seulement s'il reste au moins une place (inscrits < capacite).
    Cas limites : un événement plein (inscrits == capacite) renvoie False ;
    une capacité nulle avec zéro inscrit est valide et renvoie False.
    Lève ValueError si capacite < 0 ou si inscrits sort de [0, capacite].
    """
    if not 0 <= inscrits <= capacite:
        raise ValueError("il faut capacite >= 0 et 0 <= inscrits <= capacite")
    return inscrits < capacite

def places_restantes(inscrits: int, capacite: int) -> int:
    """Calcule les places disponibles."""
    return capacite - inscrits

def normaliser_nom(nom: str) -> str:
    """Normalise un nom pour détecter les doublons."""
    return nom.lower()

def taux_remplissage(inscrits: int, capacite: int) -> float:
    """Renvoie le pourcentage de remplissage."""
    return inscrits / capacite * 100
