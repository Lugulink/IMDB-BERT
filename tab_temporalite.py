import sklearn
from dash import dcc, html
import dash_bootstrap_components as dbc
from graphique import generer_graphique_chronologie
from main import df_commentaire
from constante import *
"""
===========================================================================
onglet 'temporalite'
"""
# Utiliser la fonction generer_graphique_chronologie pour générer le graphique
fig = generer_graphique_chronologie(df_commentaire)
card_chronologie = dbc.Card(
    [
        html.H4("Plage chronologique", className='card-title mt-3'),
        dcc.RangeSlider(
            id='RangeSlider_plage_chrono',
            marks={i: f'{i}' for i in range(1940, 2024, 5)},
            min=1940,
            max=2024,
            step=5,
            value=MIN_MAX_MOT_INITIAL,
            included=True
        ),
        dcc.Graph(
            id='graphique_evolution_temporelle',
            figure=fig
        )
    ],
    body=True,
    className='mt-4'
)

