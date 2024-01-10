from django.shortcuts import render
from .utils import import_pokemon_data, get_pokemon_by_name

def pokemon_list(request):
    pokemons = import_pokemon_data()
    return render(request, 'pokemon_list.html', {'pokemons': pokemons})

def pokemon_detail(request, name):
    pokemon = get_pokemon_by_name(name)
    return render(request, 'pokemon_detail.html', {'pokemon': pokemon})
