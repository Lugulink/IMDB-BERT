import pandas as pd

from constante import *
from modele_langage import ModeleLangage
from commentaire import charger_commentaire, filtrer_commentaire,creer_liste_film
from constante import DOSSIER_COMMENTAIRE, FICHIER_COMMENTAIRE_PLONGEMENT
from utile import sauvegarder_dataframe_csv


df_commentaire = charger_commentaire(DOSSIER_COMMENTAIRE)
liste_film=creer_liste_film(df_commentaire)
df_commentaire = filtrer_commentaire(df_commentaire,liste_film, nb_max_commentaire_par_film=500, min_max_mot=MIN_MAX_MOT_INITIAL)

print(df_commentaire['titre'].value_counts())
print()

modele_langage = ModeleLangage()

plongement = modele_langage(df_commentaire['review'], barre_progression=True)

df_commentaire.reset_index(drop=True, inplace=True)
plongement.reset_index(drop=True, inplace=True)

df_commentaire_plongement = pd.concat([df_commentaire, plongement], axis=1)

entete = "modèle de langage : " + modele_langage.nom
sauvegarder_dataframe_csv(FICHIER_COMMENTAIRE_PLONGEMENT, df_commentaire_plongement, entete=entete)

print("Fin de l'encodage et la sauvegarde")
