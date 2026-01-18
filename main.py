from sentence_transformers import SentenceTransformer, util
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
import seaborn as sns

from commentaire import *

from constante import *


# C:\Users\username\.cache\torch\sentence_transformers\sentence-transformers_all-MiniLM-L6-v2
df_commentaire = charger_commentaire(DOSSIER_COMMENTAIRE)
liste_film=creer_liste_film(df_commentaire)
df_filtre_commentaire = filtrer_commentaire(df_commentaire,liste_film, min_max_mot=MIN_MAX_MOT_INITIAL, nb_max_commentaire_par_film=20)


model = SentenceTransformer('all-MiniLM-L6-v2')

sentences = df_filtre_commentaire.review.tolist()

#Encode all sentences
embeddings = model.encode(sentences)

#Compute cosine similarity between all pairs
similarite = util.cos_sim(embeddings, embeddings)
similarite = similarite.numpy()

effectif = df_filtre_commentaire['titre'].value_counts().values

index = np.cumsum(effectif)

index = [0] + index[:-1].tolist()

similarite_diag = similarite.copy()
np.fill_diagonal(similarite_diag, 0)



# dissimilarite = 1 - np.abs(np.minimum(similarite, 1.0))
# coord = TSNE(n_components=2, metric="precomputed", learning_rate='auto', init='random', perplexity=3).fit_transform(dissimilarite)

# dissimilarite = 1 - np.minimum(similarite, 1.0)
# coord = TSNE(n_components=2, metric="precomputed", learning_rate='auto', init='random', perplexity=3).fit_transform(dissimilarite)

coord = TSNE(n_components=2, metric="cosine", learning_rate='auto', init='random', perplexity=3).fit_transform(embeddings)

df_coord = pd.DataFrame({
    "axe0": coord[:, 0],
    "axe1": coord[:, 1],
    "titre": df_filtre_commentaire['titre']})

graphique = sns.lmplot(x="axe0", y="axe1", hue="titre", data=df_coord, fit_reg=False)
graphique.set(xlabel="Axe 0", ylabel="Axe 1")
graphique.fig.suptitle("TSNE: commentaires IMDB")



'''
#Add all pairs to a list with their cosine similarity score
all_sentence_combinations = []
for i in range(len(cos_sim)-1):
    for j in range(i+1, len(cos_sim)):
        all_sentence_combinations.append([cos_sim[i][j], i, j])

#Sort list by the highest cosine similarity score
all_sentence_combinations = sorted(all_sentence_combinations, key=lambda x: x[0], reverse=True)

print("Top-5 most similar pairs:")
for score, i, j in all_sentence_combinations:
    print("{} \t {} \t {:.4f}".format(sentences[i], sentences[j], cos_sim[i][j]))
'''