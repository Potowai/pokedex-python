import requests
from django.shortcuts import render
from .models import Pokemon, Collection, Team
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


def import_pokemon_data():
    response = requests.get("https://pokeapi.co/api/v2/pokemon/?offset=0&limit=20")
    data = response.json()
    pokemons = [get_pokemon_by_name(result["name"]) for result in data["results"]]
    return pokemons

def get_pokemon_by_name(_name):
    if Pokemon.objects.filter(name=_name).exists():
        pokemon = Pokemon.objects.get(name=_name)
        print(f"Pokemon {pokemon} already exists in database")
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
        
        print("Pokemon added to database")
    return pokemon

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

@csrf_exempt
def add_pokemons_to_team_request(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        team_name = data.get('name')
        pokemon_ids = data.get('pokemon_ids')
        if team_name and pokemon_ids:
            team = Team.objects.get(name=team_name)
            pokemon = Pokemon.objects.get(pokeid=pokemon_id)
            team.pokemons.add(pokemon)
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False})

    return JsonResponse({'success': False})