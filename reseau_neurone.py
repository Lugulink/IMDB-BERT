import datetime
from sklearn.neural_network import MLPClassifier
import pandas as pd
import pickle

from constante import *

df_commentaire_plongement = pd.read_csv(FICHIER_COMMENTAIRE_PLONGEMENT, comment='#')  # le fichier peut contenir une entête

nb_film = df_commentaire_plongement.titre.nunique()

reseau_neurone = MLPClassifier(hidden_layer_sizes=(3*nb_film, 2*nb_film),
                               random_state=1,
                               early_stopping=True,
                               verbose=True)

matrice_x = df_commentaire_plongement.loc[:, 'V_000':].to_numpy()
vecteur_y = df_commentaire_plongement.titre.to_numpy()

reseau_neurone.fit(matrice_x, vecteur_y)

prediction = reseau_neurone.predict_proba(matrice_x)

dico = {
    'commentaire': "early_stopping",
    'date': datetime.date.today().strftime('%d-%m-%Y'),
    'reseau_neurone': reseau_neurone
}

with open(FICHIER_RESEAU_NEURONE, "wb") as fichier:  # write binary
    pickle.dump(dico, fichier)


print("fin de l'apprentissage")
