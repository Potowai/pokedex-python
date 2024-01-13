from django.shortcuts import render
from .utils import import_pokemon_data, get_pokemon_by_name,catch_pokemons_request, create_team_request,add_pokemons_to_team_request,delete_team_request
from .models import Collection, Team

# Fonction pokemon_list
# Cette vue renvoie la liste des Pokémon.
# Elle utilise la fonction import_pokemon_data() pour importer les données de Pokémon.
def pokemon_list(request):
    pokemons = import_pokemon_data()
    return render(request, 'pokemon_list.html', {'pokemons': pokemons})

# Fonction pokemon_detail
# Cette vue renvoie les détails d'un Pokémon.
# Elle utilise la fonction get_pokemon_by_name() pour récupérer les détails d'un Pokémon.
def pokemon_detail(request, name):
    pokemon = get_pokemon_by_name(name)
    return render(request, 'pokemon_detail.html', {'pokemon': pokemon})

# Fonction pokemon_teams
# Cette vue renvoie les informations des équipes et de la collection.
# Elle utilise la fonction get_or_create() pour récupérer une collection existante ou en créer une nouvelle.
def pokemon_teams(request):
    collection, created = Collection.objects.get_or_create(name="my_collection")
    teams = Team.objects.all()
    return render(request, 'pokemon_teams.html', {'collection': collection.pokemons.all(), 'teams': teams })

# Fonction credits
# Cette vue renvoie la page de crédits.
def credits(request):
    return render(request, 'credits.html')

# Fonction catch_pokemon
# Cette vue gère les requêtes POST pour "attraper" un Pokémon.
# Elle extrait l'ID du Pokémon de la requête, le récupère et l'ajoute à une collection nommée "my_collection".
def catch_pokemon(request):
    return catch_pokemons_request(request)

# Fonction create_team
# Cette vue gère les requêtes POST pour créer une équipe.
# Elle extrait le nom de l'équipe de la requête et crée une nouvelle équipe.
def create_team(request):
    return create_team_request(request)

# Fonction add_pokemons_to_team
# Cette vue gère les requêtes POST pour ajouter des Pokémon à une équipe.
# Elle extrait l'ID de l'équipe et des Pokémon de la requête et les ajoute à l'équipe.
def add_pokemons_to_team(request):
    return add_pokemons_to_team_request(request)

# Fonction delete_team
# Cette vue gère les requêtes POST pour supprimer une équipe.
# Elle extrait l'ID de l'équipe de la requête et la supprime.
def delete_team(request):
    return delete_team_request(request)