# Classification d'Images avec Django et TensorFlow

Ce projet est une application web développée avec Django qui permet de classer des images en utilisant un modèle de deep learning basé sur EfficientNetB0. Il intègre également une fonctionnalité de génération d'images adversariales afin d'évaluer la robustesse du modèle face aux attaques par évasion.

---

## Table des Matières

- [Description](#description)
- [Fonctionnalités](#fonctionnalités)
- [Prérequis](#prérequis)
- [Installation et Configuration](#installation-et-configuration)
- [Entraînement du Modèle](#Entraînement-du-Modèle)
- [Prédiction et Génération d'Images Adversariales](#Prédiction-et-Génération-d-Images-Adversariales)
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

- **Python 3.10** 
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
   python3.10 -m venv env
   source env/bin/activate  # Sur Windows: env\Scripts\activate
3. **Installer les dépendances :**
   ```bash
   pip3.10 install -r requirements.txt

4. **Effectuer les migrations et créer un superutilisateur :**
    ```bash
    python3.10 manage.py makemigrations
    python3.10 manage.py migrate
    python3.10 manage.py createsuperuser


5. **Lancer le serveur de développement :**
    ```bash
    python3.10 manage.py runserver

6. **Utilisation de l'application :**
    
 - Entraînement du modèle :
   Suivez les étapes du pipeline d'entraînement qui incluent la 
   préparation du dataset, la data augmentation, la définition du modèle 
   (basé sur EfficientNetB0),     et l'entraînement avec des callbacks.
       
 - Prédiction et génération d'images adversariales :
   Une fois le modèle entraîné, l'application permet d'uploader des         images pour obtenir une classification et de générer des images          adversariales en fonction d'un paramètre epsilon sélectionné      par 
   l'utilisateur.
       
 - Historique des prédictions :
   Chaque utilisateur peut consulter son historique de prédictions via 
   le dashboard.
   

## Entraînement du Modèle
Le pipeline d'entraînement est le suivant :

1. Préparation du dataset :
  - Les images sont organisées dans des dossiers (ex. : Bike, Car, Ship).
  - Le dataset est chargé dans un DataFrame avec les chemins et labels.

2. Séparation du dataset :
  - Split en ensembles d'entraînement, validation et test (80%/10%/10%).
    
3. Data Augmentation :
  - Utilisation de ImageDataGenerator avec normalisation et augmentation      des données.
    
4. Définition du modèle :
  - Utilisation d'EfficientNetB0 en transfert learning avec des couches      supplémentaires (GlobalAveragePooling, BatchNormalization, Dense,        Dropout).
    
5. Entraînement :
  - Entraînement sur 20 epochs avec callbacks (ReduceLROnPlateau et          EarlyStopping).
    
## Prédiction et Génération d'Images Adversariales
  - Upload et Classification
    Les utilisateurs peuvent uploader une image et obtenir une       
    prédiction.

  - Génération d'Images Adversariales
    La fonctionnalité permet de sélectionner une intensité (epsilon) 
    pour générer une image adversariale.
    Les images originales et adversariales sont affichées, et 
    l'utilisateur peut les télécharger.

## Défense contre les Attaques par Évasion
Pour renforcer la robustesse du modèle face aux attaques par évasion :

   - Entraînement adversarial : Intégrer des exemples adversariaux            pendant l'entraînement pour rendre le modèle plus robuste.

   - Détection d'exemples adversariaux : Mettre en place des mécanismes       de détection pour identifier et rejeter les entrées suspectes.

   - Régularisation : Utiliser du Dropout et de la régularisation L2 
     pour réduire la sensibilité du modèle aux perturbations.

   - Approche combinée : Une approche combinée est souvent nécessaire 
     pour obtenir une protection optimale.
