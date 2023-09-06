from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from rest_framework import viewsets, permissions

from django.contrib.auth.models import User
from heroes.models import Heroes
from heroes.serializer import HeroesSerializer, UserSerializer


def categories(request):
    return HttpResponse("Персонажи по категориям")

def category(request, catid):
    return HttpResponse(f"Персонажи по категориям: {catid}")

def heroes(request):
    characters = Heroes.objects.all()
    return render(request, "heroes/index.html", {"title":"Список созданных персонажей", "characters": characters})


def hero(request, hero_id):
    character = Heroes.objects.get(pk=hero_id)
    hero_dict = {"hero":
                     {"name": character.name,
                      "race": character.race,
                      "hero_class": character.hero_class,
                      "description": character.description},
                 "stats": {
                     "сила": character.strength,
                    "ловкость": character.dexterity,
                    "телосложение": character.constitution,
                    "интеллект": character.intelligence,
                    "мудрость": character.wisdom,
                    "харизма": character.charisma}}
    return render(request, "heroes/hero.html", hero_dict)

def archive(request, year):
    if int(year) > 2023:
        raise Http404
    return HttpResponse(f"<h1>Архив по годам:</h1><p>{year}</p>")

class UserViewSet(viewsets.ModelViewSet):
    """
    Provides basic CRUD functions for the User model
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class HeroesViewSet(viewsets.ModelViewSet):
    """
        Provides basic CRUD functions for the Heroes model
        """
    queryset = Heroes.objects.all()
    serializer_class = HeroesSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
