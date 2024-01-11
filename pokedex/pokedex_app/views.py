from django.shortcuts import render
from .utils import import_pokemon_data, get_pokemon_by_name,catch_pokemons_request, create_team_request,add_pokemons_to_team_request
from .models import Collection, Team

def pokemon_list(request):
    pokemons = import_pokemon_data()
    return render(request, 'pokemon_list.html', {'pokemons': pokemons})

def pokemon_detail(request, name):
    pokemon = get_pokemon_by_name(name)
    return render(request, 'pokemon_detail.html', {'pokemon': pokemon})

def pokemon_teams(request):
    collection = Collection.objects.get(name="my_collection")
    teams = list(Team.objects.all())
    for team in teams:
        print(team.name)
    return render(request, 'pokemon_teams.html', {'collection': collection.pokemons.all(), 'teams': teams})

def catch_pokemon(request):
    return catch_pokemons_request(request)

def create_team(request):
    return create_team_request(request)

def add_pokemons_to_team(request):
    return add_pokemons_to_team_request(request)