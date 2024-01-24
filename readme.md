<a name="readme-top"></a>
<div align="center">
  <a href="https://github.com/Potowai/pokedex-python">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>
<h3 align="center">Pokedex Python</h3>
  <p align="center">
    Pokedex Python est un projet qui liste les pokémons et leurs compétences en utilisant Django. Ce projet permet une exploration interactive des différentes espèces de pokémons et de leurs caractéristiques.
    <br />
  </p>
</div>
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <ul>
        <li><a href="#built-with">Construit Avec</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Démarrage</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

### Built With
[![Django][Django-shield]][Django-url]
[![Python][Python-shield]][Python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Getting Started
Ces instructions vous permettront d'obtenir une copie du projet en fonctionnement sur votre machine locale à des fins de développement et de test.

### Prérequis
Assurez-vous d'avoir installé Python et Git sur votre machine.

### Installation
Cloner le Repo
Pour cloner ce repository sur votre machine locale, exécutez la commande suivante dans votre terminal :

```sh
git clone https://github.com/Potowai/pokedex-python.git
```

Configurer l'Environnement Virtuel
Créez un environnement virtuel pour isoler les dépendances du projet :

```py
python -m pip install virtualenv
```
or
```py
py -m pip install virtualenv
```

```py
python -m virtualenv venv
```

Activez l'Environnement Virtuel

```sh
.\venv\Scripts\activate
```

Installer les Dépendances
Installez toutes les dépendances nécessaires à l'aide de :

```sh
pip install django requests psycopg2
```

Initialiser Django
Effectuez les migrations initiales :

```sh
cd pokedex
python manage.py migrate
```

Lancez le serveur de développement :
```sh
python manage.py runserver
```
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Usage
Une fois lancé, accédez à l'application sur le port 8000, soit à l'adresse suivante : http://localhost:8000/pokedex. Explorez l'interface pour découvrir les différentes fonctionnalités du Pokedex.

Il existe également une version déployée, le lien ici : https://potowai.pythonanywhere.com/pokedex/.
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contact
[![User][User-img]][User-url]

Alexis Fiolleau - Potowai
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[User-img]: https://avatars.githubusercontent.com/u/81572547?v=4
[User-url]: https://github.com/Potowai
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[Python-shield]: https://img.shields.io/badge/Python-265175?style=for-the-badge&logo=python&logoColor=yellow
[Python-url]: https://python.org
[Django-shield]:https://img.shields.io/badge/Django-228b22?style=for-the-badge&logo=django&logoColor=white
[Django-url]: https://djangoproject.com
