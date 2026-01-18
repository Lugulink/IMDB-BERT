import sklearn
from dash import dcc, html
import dash_bootstrap_components as dbc

from constante import *

"""
===========================================================================
onglet 'Projection'
"""
card_projection = dbc.Card(
    [
        html.H4("Perplexité de la méthode T-SNE:", className='card-title'),
        dcc.Slider(
            id='Slider_perplexite',
            marks={i: f'{i}' for i in range(5, 70, 5)},
            min=5,
            max=60,
            step=5,
            value=PERPLEXITE_TSNE_INITIAL,
            included=False
        ),
        dcc.Dropdown(
            id='dropdown_projection',
            multi=False,
                    options=[
                        {'label': 'ACP', 'value': 'acp'},
                        {'label': 'Multidimensional Scaling', 'value': 'mds'},
                        {'label': 't-SNE', 'value': 'tsne'}
                    ],
                    value='tsne'  # Valeur par défaut
        ),
        html.H4("Distance de la méthode T-SNE:", className='card-title mt-3'),
        dcc.Dropdown(
            id='Dropdown_distance',
            multi=False,
            options=[{'label': d, 'value': d} for d in sklearn.metrics.pairwise.distance_metrics()],
            value=DISTANCE_TSNE_INITIAL,
            clearable=False
        )
    ],
    body=True,
    className='mt-4',
)
