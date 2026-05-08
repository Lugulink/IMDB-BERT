# 🎬 IMDb Sentiment Dashboard - BERT & Interactive Visualization

<div align="center">

**Application web interactive pour l'analyse de sentiments et la projection de données textuelles**

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Dash](https://img.shields.io/badge/Dash-Plotly-orange.svg)](https://dash.plotly.com/)
[![BERT](https://img.shields.io/badge/BERT-HuggingFace-red.svg)](https://huggingface.co/)


</div>

---

## 📝 Description

Ce projet est une **application web interactive** développée avec **Dash (Plotly)** permettant d'analyser des critiques de films IMDb. Elle intègre un modèle **BERT** pour l'extraction de plongements (embeddings) et propose des visualisations avancées (T-SNE, ACP, chronologie) pour explorer les données textuelles.

**Cas d'usage industriel :** Cette architecture peut être adaptée pour analyser des retours clients, des rapports de R&D, ou des feedbacks utilisateurs en temps réel, offrant aux équipes une vue d'ensemble interactive des données non structurées.

**Fonctionnalités principales :**
*   🚀 **Interface Interactive :** Navigation par onglets (Données, Projection, Prédiction, Chronologie).
*   🤖 **Intégration BERT :** Génération de plongements vectoriels en temps réel pour les commentaires utilisateurs.
*   📊 **Visualisation Avancée :** Projection T-SNE/ACP pour explorer la similarité des textes, graphiques temporels.
*   🔮 **Prédiction :** Estimation du sentiment (Positif/Négatif) avec visualisation des probabilités.
*   📅 **Analyse Temporelle :** Filtrage chronologique des données pour étudier l'évolution des sentiments.

---

## 📸 Démonstration

[Dashboard Home](./screenshots/dashboard_home.png)
*Figure 1 : Interface principale avec projection T-SNE et prédiction en temps réel.*

---

## 🛠️ Stack Technique

| Domaine | Technologies |
|---------|--------------|
| **Framework Web** | Dash (Plotly), Dash Bootstrap Components |
| **NLP & IA** | BERT (HuggingFace), Scikit-learn (RandomForest/MLP) |
| **Data Viz** | Plotly, Matplotlib, Seaborn |
| **Data Processing** | Pandas, NumPy, T-SNE, ACP |
| **Langage** | Python 3.9+ |
| **Architecture** | Modularité (fonctions séparées), Callbacks asynchrones |

---

## 🚀 Installation & Lancement

### 1. Cloner le dépôt

git clone https://github.com/Lugulink/IMDB-BERT.git
cd IMDB-BERT

### 2. Installer les dépendances

pip install -r requirements.txt

### 3. Lancer l'application

python main.py
L'application sera accessible à l'adresse : http://127.0.0.1:8050

## 📂 Structure du Projet
* IMDB-BERT/

* ├── main.py              # Point d'entrée (Layout & Callbacks)
* ├── constante_app.py     # Constantes et configuration
* ├── commentaire.py       # Prétraitement & Filtrage
* ├── graphique.py         # Fonctions de visualisation
* ├── tab_donnees.py       # Onglet Données
* ├── tab_projection.py    # Onglet Projection (T-SNE/ACP)
* ├── tab_prediction_film.py # Onglet Prédiction
* ├── tab_temporalite.py   # Onglet Chronologie
* ├── data/                # Données (ignorées par Git)
* ├── models/              # Modèles (ignorés par Git)
* ├── requirements.txt     # Dépendances
* ├── .gitignore          # Fichiers ignorés
* └── README.md           # Ce fichier

## 💡 Ce que j'ai appris
Ce projet, réalisé dans le cadre de mon BUT, m'a permis de :

* Développer une application Full-Stack Data : De la modélisation (BERT) à l'interface utilisateur (Dash).
* Gérer des callbacks complexes : Mise à jour dynamique de graphiques en fonction de multiples inputs (sliders, dropdowns).
* Structurer un code modulaire : Séparation des responsabilités (layout, logique métier, visualisation) pour une maintenabilité optimale.
* Visualiser des données haute dimension : Utilisation de T-SNE et ACP pour rendre intelligibles des plongements vectoriels.

## 📚 Références
Dataset : IMDb Movie Reviews - Kaggle
Framework : Dash Documentation
Modèle : BERT Base Uncased - HuggingFace
