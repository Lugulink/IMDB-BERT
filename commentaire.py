from pathlib import Path
import pandas as pd
from typing import Union, List


#------------------------------------------------------------------------------
def charger_commentaire(dossier: Union[Path, str]) -> pd.DataFrame:
    """

    :param dossier:
    :return:
    """

    if isinstance(dossier, str):
        dossier = Path(dossier)

    liste_nom_fichier = dossier.glob('*.csv')

    liste_df = []

    for nom_fichier in liste_nom_fichier:

        print(nom_fichier)

        df = pd.read_csv(nom_fichier, sep=',', header=0, encoding='utf8')
        df = df[['date', 'rating', 'review']]
        df['date'] = pd.to_datetime(df['date'])

        df['titre'] = nom_fichier.stem

        df.review = df.review.str.replace("<br/>", "")

        liste_df.append(df)

    df = pd.concat(liste_df)

    df = df.sort_values(by='titre')

    df.index = range(0, len(df))

    return df[['titre', 'date', 'rating', 'review']]


#------------------------------------------------------------------------------
def filtrer_commentaire(df_commentaire: pd.DataFrame, liste_film,
                        nb_max_commentaire_par_film: int = None, min_max_mot: tuple[int, int] = (100, 300)) -> pd.DataFrame:
    """

    :param df_commentaire: peut contenir les plongements
    :param nb_max_commentaire_par_film:
    :param min_max_mot:
    :return:
    """
    if len(liste_film)  < 2:
        df_commentaire = None
        return df_commentaire
    else:
        df_commentaire = df_commentaire[df_commentaire['titre'].isin(liste_film)]

    ok_longueur = df_commentaire.review.str.count(" ").between(*min_max_mot)

    print(min_max_mot, sum(ok_longueur))

    df_commentaire = df_commentaire[ok_longueur]

    if nb_max_commentaire_par_film is not None:
        df_commentaire = df_commentaire.groupby('titre').head(nb_max_commentaire_par_film)

    return df_commentaire

def creer_liste_film(df_commentaire: pd.DataFrame ) -> list :
    liste_films = list(set(df_commentaire['titre'].tolist()))
    return liste_films