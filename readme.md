# Pokedex Python
## Table des Matières

- [À Propos](#about)
- [Commencer](#getting_started)
- [Installation](#installation)
- [Utilisation](#usage)
- [Contribution](#contribution)

## À Propos <a name = "about"></a>
Le Pokedex Python est un projet qui liste les pokémons et leurs compétences en utilisant Django. Ce projet permet une exploration interactive des différentes espèces de pokémons et de leurs caractéristiques.

## Commencer <a name = "getting_started"></a>
Ces instructions vous permettront d'obtenir une copie du projet en fonctionnement sur votre machine locale à des fins de développement et de test.

### Prérequis
Assurez-vous d'avoir installé Python et Git sur votre machine.

## Installation <a name = "installation"></a>
### Cloner le Repo
Pour cloner ce repository sur votre machine locale, exécutez la commande suivante dans votre terminal :
```
git clone https://github.com/Potowai/pokedex-python.git
```
### Configurer l'Environnement Virtuel
Créez un environnement virtuel pour isoler les dépendances du projet :
```
python -m pip install virtualenv
python -m virtualenv venv
```
### Activez l'Environnement Virtuel
```
.\venv\Scripts\activate
```
### Installer les Dépendances
Installez toutes les dépendances nécessaires à l'aide de :
```
pip install django requests 
```
### Initialiser Django
Effectuez les migrations initiales :
```
python manage.py migrate
```
### Lancez le serveur de développement :
```
python manage.py runserver
```
## Utilisation <a name = "usage"></a>
Une fois lancé, accédez à l'application sur le port 8000, soit à l'adresse suivante : http://localhost:8000/pokedex. Explorez l'interface pour découvrir les différentes fonctionnalités du Pokedex.

## Contribution <a name = "contribution"></a>
Alexis Fiolleau

