from typing import Final
from pathlib import Path

"""
===========================================================================
constantes globales à l'application principale et aux scripts secondaires
"""
BASE_DIR: Final[Path] = Path(__file__).resolve().parent

DOSSIER_DATA: Final[Path] = BASE_DIR / "data"
DOSSIER_COMMENTAIRE: Final[Path] = DOSSIER_DATA / "commentaire"

FICHIER_COMMENTAIRE_PLONGEMENT: Final[Path] = DOSSIER_DATA / "commentaire_plongement.csv"
FICHIER_RESEAU_NEURONE: Final[Path] = DOSSIER_DATA / "commentaire_pmc.pickle"

MIN_MAX_MOT_INITIAL: Final[tuple[int, int]] = (100, 300)
NB_MAX_COMMENTAIRE_PAR_FILM_INITIAL: Final[int] = 5

PERPLEXITE_TSNE_INITIAL: Final[float] = 5
DISTANCE_TSNE_INITIAL: Final[str] = 'cosine'
