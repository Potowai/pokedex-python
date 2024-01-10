import requests
from django.shortcuts import render
from .models import Pokemon

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