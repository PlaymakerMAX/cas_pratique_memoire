# Dockerfile pour l'application Django

# 1. Partir d'une image Python officielle et légère
FROM python:3.11-slim

# 2. Définir des variables d'environnement
# Empêche Python de créer des fichiers .pyc
ENV PYTHONDONTWRITEBYTECODE 1
# Empêche Python de mettre en mémoire tampon les sorties, pour des logs plus directs
ENV PYTHONUNBUFFERED 1

# 3. Définir le répertoire de travail dans le conteneur
WORKDIR /app

# 4. Copier et installer les dépendances
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copier le reste du code de l'application dans le conteneur
COPY . /app/

# 6. La commande qui sera exécutée pour démarrer l'application
# On expose l'application sur le port 8000 pour que tout le monde puisse s'y connecter
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]