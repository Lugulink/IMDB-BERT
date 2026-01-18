from io import StringIO
from dash import Dash, Input, Output, State
import dash_bootstrap_components as dbc
import plotly.graph_objects as go

from constante_app import *
from commentaire import filtrer_commentaire

from datetime import *
from graphique import *
from tab_donnees import *
from tab_projection import *
from tab_prediction_film import *
from tab_temporalite import *

"""
===========================================================================
application
"""
application = Dash(
    __name__,
    external_stylesheets=[dbc.themes.SPACELAB]
)


"""
===========================================================================
pied de page
"""
pied_de_page = html.Div(
    dcc.Markdown(
        """
         Cette application a pour but d'analyser des commentaires de films (IMDB) grâce au modèle de langage BERT. 
        """
    ),
    className='p-2 mt-5 bg-primary text-white small'  # padding margin-top
)


"""
===========================================================================
menu Onglets
"""
tabs = dbc.Tabs(
    [
        dbc.Tab([card_donnees], tab_id='Tab_donnees', label='Données'),
        dbc.Tab([card_projection], tab_id='Tab_projection', label='Projection', className='pb-4'),  # padding bottom
        dbc.Tab([card_prediction_film], tab_id='Tab_prediction_film', label='Prédiction film'),
        dbc.Tab([card_chronologie], tab_id='Tab_chronologie', label='Chronologie')
    ],
    id='Tabs', active_tab='Tab_projection', className='mt-2'   # margin-top
)


"""
===========================================================================
Mise en page principale (layout)
"""
application.layout = dbc.Container(
    [
        dbc.Row(
            dbc.Col(
                html.H2(
                    "Commentaires IMDB",
                    className='text-center bg-primary text-white p-2',
                ),
            )
        ),
        dbc.Row(
            [
                dbc.Col(tabs, width=12, lg=5, className='mt-4 border'), 

                dbc.Col(
                    [
                        html.H4("Projection T-SNE"),
                        dcc.Graph(id='Graph_projection',style={"height": "700px"}, figure={}),

                        html.H4("Prédiction du film"),
                        dcc.Graph(id='Graph_prediction_film',style={"height": "700px"}, figure={})
                    ],
                    width=12,
                    lg=7,
                    className='pt-4',
                )
            ],
            className='ms-1',
        ),
        dbc.Row(dbc.Col(pied_de_page)),
        dcc.Store(id='Store_donnees_partage', storage_type='session', data={})
    ],
    fluid=True,
)


"""
===========================================================================
callback
"""
@application.callback(
    Output('Store_donnees_partage', 'data'),
    Input('Button_predire_film', 'n_clicks'),
    State('Textarea_commentaire', 'value'),
)
def stocker_commentaire_utilisateur(n_click:int, commentaire: str) -> dict:

    if commentaire is None or len(commentaire) == 0:
        return {}

    commentaire = commentaire.strip()

    plongement = MODELE_LANGAGE(commentaire)

    return {'commentaire': commentaire, 'plongement': plongement.to_json(orient='split')}  # il faut que l'on puisse générer un Json


@application.callback(
    Output('Graph_projection', 'figure'),
    Input('Slider_nombre_commentaire', 'value'),
    Input('RangeSlider_nombre_mot', 'value'),
    Input('Slider_perplexite', 'value'),
    Input('Dropdown_distance', 'value'),
    Input('Store_donnees_partage', 'data'),
    Input('dropdown_liste_film','value'),
    Input('dropdown_projection','value')
)
def mettre_a_jour_figure_projection(nb_max_commentaire_par_film: int, min_max_mot: tuple[int, int],
                                    perplexite: int, distance: str,
                                    donnees_partage: dict, liste_film,choix_projection) -> go.Figure:

    df_filtre = filtrer_commentaire(DF_COMMENTAIRE_PLONGEMENT,liste_film,
                                    nb_max_commentaire_par_film=nb_max_commentaire_par_film,
                                    min_max_mot=min_max_mot)

    if len(donnees_partage) != 0:
        df_plongement = pd.read_json(StringIO(donnees_partage['plongement']), orient='split')
        df_une_ligne = pd.DataFrame({'titre': [LABEL_COMMENTAIRE_UTILISATEUR], 'rating': [-1], 'review': [donnees_partage['commentaire']]})
        df_une_ligne = pd.concat([df_une_ligne, df_plongement], axis=1)
        df_filtre = pd.concat([df_filtre, df_une_ligne])

    if choix_projection == 'tsne':
        figure = generer_graphique_projection_TSNE(df_filtre, perplexite=perplexite, distance=distance)
    elif choix_projection == 'acp':
        figure = generer_graphique_projection_ACP(df_filtre)
    elif choix_projection =='mds':
        figure = generer_graphique_projection_MDS(df_filtre)
    return figure


@application.callback(
    Output('Graph_prediction_film', 'figure'),
    Input('Store_donnees_partage', 'data'),
    Input('dropdown_liste_film','value')
)
def mettre_a_jour_figure_prediction(donnees_partage: dict,liste_film) -> go.Figure:   # {'commentaire': commentaire, 'plongement': plongement} ou {}

    if len(donnees_partage) != 0:
        plongement = pd.read_json(StringIO(donnees_partage['plongement']), orient='split')
        plongement = plongement.to_numpy()
        probabilite = RESEAU_NEURONE.predict_proba(plongement).squeeze()

    else:

        nb_titre = RESEAU_NEURONE.n_outputs_
        probabilite = [1/nb_titre for i in range(nb_titre)]

    modalite = RESEAU_NEURONE.classes_.tolist()
    probabilite_film_select = [probabilite[modalite.index(film)] for film in liste_film]
    probabilite_film_select = np.array(probabilite_film_select)
    probabilite_film_select = probabilite_film_select / np.sum(probabilite_film_select)

    figure = generer_graphique_prediction_film(pd.Series(probabilite_film_select, index=liste_film))

    return figure

@application.callback(
    Output('graphique_evolution_temporelle', 'figure'),
    Input('RangeSlider_plage_chrono', 'value')
)
def mettre_a_jour_figure_chronologie(plage_chrono):
    from main import df_commentaire  # Importez df_commentaire à l'intérieur de la fonction pour le mettre à jour à chaque appel
    
    # Convertir les bornes en format datetime
    plage_chrono_dates = [datetime(year=plage_chrono[0], month=1, day=1), datetime(year=plage_chrono[1], month=1, day=1)]

    # Filtrer les données en fonction de la plage chronologique sélectionnée
    df_filtre_chrono = df_commentaire[(df_commentaire['date'] >= plage_chrono_dates[0]) & (df_commentaire['date'] <= plage_chrono_dates[1])]

    # Générer le nouveau graphique en fonction des données filtrées
    fig = generer_graphique_chronologie(df_filtre_chrono)

    # Retourner la nouvelle figure pour la mise à jour du graphique
    return fig
"""
===========================================================================
lancement du serveur
"""
if __name__ == '__main__':
    application.run(
    host="0.0.0.0",
    port=8050,
    debug=False
)

