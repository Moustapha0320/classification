# Classification d'Images avec Django et TensorFlow

Ce projet est une application web développée avec Django qui permet de classer des images en utilisant un modèle de deep learning basé sur EfficientNetB0. Il intègre également une fonctionnalité de génération d'images adversariales afin d'évaluer la robustesse du modèle face aux attaques par évasion.

---

## Table des Matières

- [Description](#description)
- [Fonctionnalités](#fonctionnalités)
- [Prérequis](#prérequis)
- [Installation et Configuration](#installation-et-configuration)
- [Utilisation](#utilisation)
  - [Lancement du serveur](#lancement-du-serveur)
  - [Entraînement du modèle](#entraînement-du-modèle)
  - [Prédiction et Génération d'Images Adversariales](#prédiction-et-génération-dimages-adversariales)
- [Évaluation du Modèle](#évaluation-du-modèle)
- [Défense contre les Attaques par Évasion](#défense-contre-les-attaques-par-évasion)
- [Organisation du Dataset](#organisation-du-dataset)
- [Licence](#licence)

---

## Description

Cette application permet de classifier des images appartenant aux classes **Bike**, **Car** et **Ship**. Le modèle est construit en utilisant **EfficientNetB0** en transfert de connaissances (Transfer Learning) et est affiné avec des couches supplémentaires (GlobalAveragePooling, BatchNormalization, Dense, Dropout).  
Une fonctionnalité additionnelle permet de générer des images adversariales pour étudier la robustesse du modèle face aux attaques par évasion.

---

## Fonctionnalités

- **Authentification** : Inscription, connexion et déconnexion des utilisateurs.
- **Upload et Classification** : Les utilisateurs peuvent uploader une image pour obtenir une prédiction de la classe.
- **Historique des Prédictions** : Chaque utilisateur peut consulter l'historique de ses prédictions.
- **Génération d'Images Adversariales** : Génère une image modifiée (avec un paramètre epsilon pour contrôler le degré de floutage) pour évaluer la robustesse du modèle.
- **Téléchargement** : Possibilité de télécharger l'image adversariale générée.

---

## Prérequis

- **Python 3.10** (ou supérieur)
- **Django 5.1.6**
- **TensorFlow 2.15.1** (incluant Keras)
- Autres packages Python : `numpy`, `pandas`, `matplotlib`, `seaborn`, `scikit-learn`, `opencv-python`, `h5py`

---

## Installation et Configuration

1. **Cloner le dépôt :**
   ```bash
   git clone https://github.com/Moustapha0320/classification.git
   cd classification
2. **Créer et activer un environnement virtuel :**
   ```bash
   python3 -m venv env
   source env/bin/activate  # Sur Windows: env\Scripts\activate
3. **Installer les dépendances :**
   ```bash
   pip install -r requirements.txt

4. **Effectuer les migrations et créer un superutilisateur :**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser

5. **Configurer les chemins médias dans settings.py :**
    ```bash
    import os

    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    UPLOAD_FOLDER = os.path.join(MEDIA_ROOT, 'uploads')
    
6. **Ajouter l'URL statique pour les médias dans urls.py du projet :**
    ```bash
    from django.conf import settings
    from django.conf.urls.static import static

    urlpatterns = [
    # vos autres routes...
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

7. **Lancer le serveur de développement :**
    ```bash
    python manage.py runserver

8. **Utilisation de l'application :**
    ```bash
    Entraînement du modèle :
    Suivez les étapes du pipeline d'entraînement qui incluent la     préparation du dataset, la data augmentation, la définition du modèle (basé sur EfficientNetB0), et l'entraînement avec des callbacks.
    
    Prédiction et génération d'images adversariales :
    Une fois le modèle entraîné, l'application permet d'uploader des images pour obtenir une classification et de générer des images adversariales en fonction d'un paramètre epsilon sélectionné par l'utilisateur.
    
    Historique des prédictions :
    Chaque utilisateur peut consulter son historique de prédictions via le dashboard.

    N'hésite pas à adapter ce contenu selon tes besoins spécifiques.

