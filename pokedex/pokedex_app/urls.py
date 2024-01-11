from django.urls import path
from . import views

urlpatterns = [
    path('', views.pokemon_list, name='pokemon_list'),
    path('details/<name>/', views.pokemon_detail, name='pokemon_detail'),
    path('teams/', views.pokemon_teams, name='pokemon_teams'),
    path('catch_pokemon/', views.catch_pokemon, name='catch_pokemon'),
    path('create_team/', views.create_team, name='create_team'),
    path('add_pokemons_to_team/', views.add_pokemons_to_team, name='add_pokemons_to_team'),
]

