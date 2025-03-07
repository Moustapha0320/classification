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
