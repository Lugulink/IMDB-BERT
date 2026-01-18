import pandas as pd
import pickle
from sklearn.neural_network import MLPClassifier

from constante import *
from modele_langage import ModeleLangage

"""
===========================================================================
constantes globales spécifiques à l'application principale
"""

# dataframe commentaire et plongement
DF_COMMENTAIRE_PLONGEMENT: Final[pd.DataFrame] = pd.read_csv(FICHIER_COMMENTAIRE_PLONGEMENT, comment='#')

# BERT
MODELE_LANGAGE: Final[ModeleLangage] = ModeleLangage()

# chargement du MLP pour la classification
with open(FICHIER_RESEAU_NEURONE, 'rb') as fichier:
    dico = pickle.load(fichier)

assert set(dico['reseau_neurone'].classes_) == set(DF_COMMENTAIRE_PLONGEMENT.titre), "le réseau de neurones ne traite pas cette liste de films"

RESEAU_NEURONE: Final[MLPClassifier] = dico['reseau_neurone']
del dico     # ne pas polluer l'espace global
del fichier

# label pour le commentaire de l'utilisateur
LABEL_COMMENTAIRE_UTILISATEUR: Final[str] = '*UTILISATEUR*'
