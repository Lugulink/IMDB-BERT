from dash import dcc, html
import dash_bootstrap_components as dbc

from constante import *

"""
===========================================================================
onglet 'Classification'
"""
card_prediction_film = dbc.Card(
    [
        html.H4("Méthode de prédiction:", className='card-title'),
        dcc.RadioItems(id='RadioItems_methode_prediction_film',
                       options=[{'label': " " + methode,  'value': methode} for methode in
                           ['réseau de neurones']],
                       value='réseau de neurones'),

        html.H4("Nouveau commentaire:", className='card-title mt-3'),
        dbc.Textarea(id='Textarea_commentaire'),
        dbc.Button(id='Button_predire_film', children='Prédire le film', color='primary', className='m-2')
    ],
    body=True,
    className='mt-4'
)



