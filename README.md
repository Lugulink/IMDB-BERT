🧠 IMDB Movie Sentiment Analysis
Dash Web App powered by BERT embeddings

This project is an interactive web application for analyzing and visualizing IMDB movie review sentiments, based on BERT sentence embeddings and classical machine learning models.

The application is built with Dash & Plotly and is fully dockerized for easy reproducibility.

🚀 Features

Sentiment analysis of IMDB movie reviews

Sentence embeddings using BERT (Sentence-Transformers)

Dimensionality reduction with PCA, t-SNE, and MDS

Interactive visualizations with Plotly

Movie-level sentiment prediction

Modular Dash layout with multiple tabs

Fully containerized with Docker

🛠️ Tech Stack

Python 3.10

Dash / Plotly

Sentence-Transformers (BERT)

Scikit-learn

Pandas / NumPy

Docker

## Data

The datasets used for training are not included in this repository.
Please place the CSV files in the `data/` directory following this structure:
## Dataset

The dataset used in this project consists of IMDB movie reviews.
CSV files are intentionally not included in this repository due to
size and licensing considerations.

To run the application locally, you must provide your own CSV files
matching the expected format and place them in:

data/commentaire/
