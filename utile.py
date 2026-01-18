import numpy as np
import pandas as pd
from pathlib import Path
from typing import Union, List

def sauvegarder_dataframe_csv(nomfichier: Union[str, Path], df: pd.DataFrame, entete: Union[str, tuple[str]], caractere: str='#') -> None:
    """
    Cette fonction permet de sauvegarder des commentaires (entête) au dessus des données CSV

    :param nomfichier:
    :param df:
    :param entete: la ou les lignes d'entête
    :param caractere: caractère débutant la ou les lignes d'entête
    """
    with open(nomfichier, 'w', encoding="utf-8") as fichier:
        if isinstance(entete, (tuple, list)):
            for chaine in entete:
                fichier.write(caractere + " " + chaine + "\n")
        else:
            fichier.write(caractere + " " + entete + "\n")

        df.to_csv(fichier, index=False)

