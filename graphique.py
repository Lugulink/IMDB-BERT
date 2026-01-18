import textwrap
import numpy as np
import pandas as pd
from sklearn.manifold import TSNE,MDS
import plotly.express as px
import plotly.graph_objects as go
from sklearn.decomposition import PCA


from constante_app import LABEL_COMMENTAIRE_UTILISATEUR

def generer_graphique_projection_TSNE(commentaire_plongement: pd.DataFrame, perplexite: float, distance: str) -> go.Figure:

    if commentaire_plongement.shape[0] < 10:
        return {}

    perplexite = min(perplexite, commentaire_plongement.shape[0] - 1)

    tsne = TSNE(n_components=2, perplexity=perplexite, metric=distance, learning_rate='auto', init='random')

    coord = tsne.fit_transform(commentaire_plongement.loc[:, 'V_000':])

    coord_titre = pd.DataFrame(coord, columns=['x', 'y'], index=commentaire_plongement.index)
    coord_titre['titre'] = commentaire_plongement.titre.values

    coord_titre['review'] = commentaire_plongement.review.apply(lambda chaine: '<br>'.join(textwrap.wrap(textwrap.shorten(chaine, width=300), width=50)))

    # coord_titre['utilisateur'] = coord_titre.titre.apply(lambda chaine: 'u' if chaine == LABEL_ENTREE_UTILISATEUR else 'c')

    figure = px.scatter(data_frame=coord_titre, x='x', y='y', color='titre', labels={'x': '', 'y': ''},
                        hover_name='titre', hover_data={'titre': False, 'x': False, 'y': False, 'review': True})
    figure.update_layout(height=700,autosize=False)
    return figure

def generer_graphique_projection_ACP(commentaire_plongement: pd.DataFrame) -> go.Figure:

    if commentaire_plongement.shape[0] < 10:
        return {}


    pca = PCA(n_components=2)

    coord = pca.fit_transform(commentaire_plongement.loc[:, 'V_000':])

    coord_titre = pd.DataFrame(coord, columns=['x', 'y'], index=commentaire_plongement.index)
    coord_titre['titre'] = commentaire_plongement.titre.values

    coord_titre['review'] = commentaire_plongement.review.apply(lambda chaine: '<br>'.join(textwrap.wrap(textwrap.shorten(chaine, width=300), width=50)))

    # coord_titre['utilisateur'] = coord_titre.titre.apply(lambda chaine: 'u' if chaine == LABEL_ENTREE_UTILISATEUR else 'c')

    figure = px.scatter(data_frame=coord_titre, x='x', y='y', color='titre', labels={'x': '', 'y': ''},
                        hover_name='titre', hover_data={'titre': False, 'x': False, 'y': False, 'review': True})
    figure.update_layout(height=700,autosize=False)

    return figure

def generer_graphique_projection_MDS(commentaire_plongement: pd.DataFrame) -> go.Figure:

    if commentaire_plongement.shape[0] < 10:
        return {}


    mds = MDS(n_components=2)

    coord = mds.fit_transform(commentaire_plongement.loc[:, 'V_000':])

    coord_titre = pd.DataFrame(coord, columns=['x', 'y'], index=commentaire_plongement.index)
    coord_titre['titre'] = commentaire_plongement.titre.values

    coord_titre['review'] = commentaire_plongement.review.apply(lambda chaine: '<br>'.join(textwrap.wrap(textwrap.shorten(chaine, width=300), width=50)))

    # coord_titre['utilisateur'] = coord_titre.titre.apply(lambda chaine: 'u' if chaine == LABEL_ENTREE_UTILISATEUR else 'c')

    figure = px.scatter(data_frame=coord_titre, x='x', y='y', color='titre', labels={'x': '', 'y': ''},
                        hover_name='titre', hover_data={'titre': False, 'x': False, 'y': False, 'review': True})
    figure.update_layout(height=700,autosize=False)
    return figure


def generer_graphique_prediction_film(probabilite: pd.Series) -> go.Figure:
    fig = go.Figure(
        data=[
            go.Bar(
                x=probabilite.index,
                y=probabilite.values
            )
        ]
    )

    fig.update_layout(
        height=350,
        autosize=False,
        margin=dict(l=40, r=20, t=40, b=40),
        yaxis_title="Probabilité",
        xaxis_title="Film"
    )

    return fig


def generer_graphique_chronologie(df_filtre_chrono):
    # Agréger les données pour obtenir le nombre de commentaires par année pour chaque film
    nombre_commentaires_par_film = df_filtre_chrono.groupby(['date', 'titre']).size().reset_index(name='nombre_commentaires')

    # Créer une liste de traces pour chaque film
    traces = []
    for film in nombre_commentaires_par_film['titre'].unique():
        data_film = nombre_commentaires_par_film[nombre_commentaires_par_film['titre'] == film]
        trace_film = go.Scatter(
            x=data_film['date'],
            y=data_film['nombre_commentaires'],
            mode='lines',
            name=film
        )
        traces.append(trace_film)

    layout = go.Layout(
        title='Évolution temporelle du nombre de commentaires par film',
        xaxis=dict(title='Année'),
        yaxis=dict(title='Nombre de commentaires')
    )

    # Créer la figure contenant les traces et la mise en page
    return go.Figure(data=traces, layout=layout)
