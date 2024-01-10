
#Pokedex Python 

#Description
Liste des pokemons et de leurs compétences avec Django

#Prérequis
Assurez-vous d'avoir installé Python et Git sur votre machine.

#Installation
Cloner le Repo
Pour cloner ce repository sur votre machine locale, exécutez la commande suivante dans votre terminal :

git clone https://lien-du-repo.git

#Configurer l'Environnement Virtuel
Créez un environnement virtuel pour isoler les dépendances du projet :

python -m pip install virtualenv
python -m virtualenv venv

#Activez l'environnement virtuel :
.\venv\Scripts\activate

#Installer les Dépendances
Installez toutes les dépendances nécessaires à l'aide de :

pip install django requests 

#Initialiser Django
Effectuez les migrations initiales :
python manage.py migrate
Lancez le serveur de développement :

python manage.py runserver

#Utilisation
Une fois lancé, l'application sur le port 8000, soit à l'addresse suivante.
http://localhost:8000/pokedex

#Contribution
Alexis Fiolleau
