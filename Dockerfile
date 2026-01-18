# Image Python officielle
FROM python:3.10-slim

# Variables d’environnement (bonne pratique)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Dossier de travail dans le container
WORKDIR /app

# Dépendances système minimales (torch, sklearn)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copier les dépendances Python
COPY requirements.txt .

# Installer pip et les libs
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le projet
COPY . .

# Port utilisé par Dash
EXPOSE 8050

# Commande de lancement
CMD ["python", "IMDB_app.py"]
