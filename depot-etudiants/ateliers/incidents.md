# Dossier incidents pour le TP3

Les signalements ne sont pas encore des diagnostics. Retrouvez la fonction concernée et produisez un contre-exemple exécutable. README.md définit le contrat qui fait foi.

## A — L'événement complet

Le responsable annonce que les dernières inscriptions dépassent le nombre de places. Les essais précédents portaient uniquement sur un événement à moitié rempli. Établissez à partir de quelle situation la décision devient incorrecte.

## B — Les places impossibles

Un import produit un nombre de places disponibles négatif ou supérieur à la capacité. Le responsable ne veut pas masquer une donnée invalide en ramenant arbitrairement le résultat à zéro. Déterminez quelles entrées doivent être refusées.

## C — Le nom qui semble identique

Deux noms visuellement identiques restent différents après normalisation quand on copie-colle depuis un formulaire. Un nom constitué seulement d'espaces est également accepté. Trouvez une règle qui préserve les espaces intérieurs.

## D — L'événement sans capacité

Un événement encore vide peut avoir une capacité égale à zéro. Le calcul de remplissage interrompt alors le traitement. Le contrat prévoit un résultat numérique de 0.0 pour ce cas ; les autres entrées invalides doivent rester refusées.

## Enquête attendue

Pour chaque incident : observation, hypothèse, entrée, résultat attendu, résultat réel, test rouge avant correction, test vert après correction, limite restante. Ne recopiez pas un correctif trouvé avant d'avoir démontré le défaut.
