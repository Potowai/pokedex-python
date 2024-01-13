import requests
from django.shortcuts import render
from .models import Pokemon, Collection, Team
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

# Fonction import_pokemon_data
# Cette fonction récupère les données de Pokémon à partir de l'API externe pokeapi.co. 
# Elle renvoie une liste de Pokémon après avoir récupéré les données de chacun via la fonction get_pokemon_by_name.
def import_pokemon_data():
    response = requests.get("https://pokeapi.co/api/v2/pokemon/?offset=0&limit=151")
    data = response.json()
    pokemons = [get_pokemon_by_name(result["name"]) for result in data["results"]]
    return pokemons

# Fonction get_pokemon_by_name
# Cette fonction vérifie d'abord si un Pokémon avec le nom spécifié existe déjà dans la base de données. 
# Si c'est le cas, elle le renvoie. Sinon, elle récupère les données de ce Pokémon à partir de l'API externe, crée une nouvelle instance de Pokemon, la sauvegarde dans la base de données et la renvoie.
def get_pokemon_by_name(_name):
    if Pokemon.objects.filter(name=_name).exists():
        pokemon = Pokemon.objects.get(name=_name)
    else:
        url = f"https://pokeapi.co/api/v2/pokemon/{_name}"
        response = requests.get(url)
        pokemon_data = response.json()
        pokemon = Pokemon(
            name=pokemon_data["name"],
            url_link = url,
            pokeid = pokemon_data['id'],
            height=pokemon_data["height"]*0.1,
            weight=pokemon_data["weight"]*0.1,
            abilities = pokemon_data["abilities"],
            types = pokemon_data["types"],
            moves = pokemon_data["moves"],
            stats = pokemon_data["stats"],
            sprites = pokemon_data["sprites"],
            base_experience=pokemon_data["base_experience"])
        pokemon.save()
        
    return pokemon

# Fonction catch_pokemons_request
# Une vue Django qui gère les requêtes POST pour "attraper" un Pokémon. 
# Elle extrait l'ID du Pokémon de la requête, le récupère et l'ajoute à une collection nommée "my_collection".
@csrf_exempt
def catch_pokemons_request(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        pokemon_id = data.get('pokemon_id')
        if pokemon_id :
            pokemon = Pokemon.objects.get(pokeid=pokemon_id)
            collection, created = Collection.objects.get_or_create(name="my_collection")
            collection.pokemons.add(pokemon)
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False})

    return JsonResponse({'success': False})

# Fonction create_team_request
# Cette vue gère les requêtes POST pour créer une équipe de Pokémon. 
# Si une équipe avec le nom spécifié n'existe pas, elle est créée.
@csrf_exempt
def create_team_request(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        team_name = data.get('name')
        if team_name:
            team, created = Team.objects.get_or_create(name=team_name)
            if created:
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False})

    return JsonResponse({'success': False})

# Fonction add_pokemons_to_team_request
# Cette vue gère les requêtes POST pour ajouter des Pokémon à une équipe.
# Elle extrait le nom de l'équipe et les ID des Pokémon de la requête, puis ajoute chaque Pokémon à l'équipe.
@csrf_exempt
def add_pokemons_to_team_request(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        team_name = data.get('name')
        pokemon_ids = data.get('pokemon_ids')
        if team_name and pokemon_ids:
            team = Team.objects.get(name=team_name)
            if team.pokemons.count() + len(pokemon_ids) > 6:
                return JsonResponse({'success': False})
            for pokemon_id in pokemon_ids:
                pokemon = Pokemon.objects.get(pokeid=pokemon_id)
                team.pokemons.add(pokemon)
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False})

    return JsonResponse({'success': False})

# Fonction delete_team_request
# Cette vue gère les requêtes POST pour supprimer une équipe.
# Elle extrait le nom de l'équipe de la requête et la supprime.
@csrf_exempt
def delete_team_request(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        team_id = data.get('team_id')
        if team_id:
            team = Team.objects.get(id=team_id)
            team.delete()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False})

    return JsonResponse({'success': False})