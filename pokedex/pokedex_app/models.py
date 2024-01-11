from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User

class Pokemon(models.Model):
    pokeid = models.IntegerField()
    name = models.TextField()
    url_link = models.URLField(default="https://blob:https://imgur.com/0")
    height = models.FloatField()
    weight = models.FloatField()
    abilities = models.JSONField()
    types = models.JSONField()
    moves = models.JSONField()
    stats = models.JSONField()
    sprites = models.JSONField()
    base_experience = models.SmallIntegerField()
    
    def __str__(self):
        return self.name


class Collection(models.Model):
    name = models.CharField(max_length=100)
    pokemons = models.ManyToManyField(Pokemon, max_length=151)
    
class Team(models.Model):
    name = models.CharField(max_length=100)
    pokemons = models.ManyToManyField(Pokemon, max_length=6)
    