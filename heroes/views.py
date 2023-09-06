from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404

from heroes.models import Heroes


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
    #if int(year) < 2000:
    #    return redirect('')
    return HttpResponse(f"<h1>Архив по годам:</h1><p>{year}</p>")