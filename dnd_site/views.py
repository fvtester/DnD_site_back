from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404

menu = ["Создать героя", "Посмотреть список героев", "Бросить кубики"]
def index(request):
    return render(request, "index.html", {"menu": menu, "title":"Страница для игры в Dungeons&Dragons"})


def PageNotFound (request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")


def archive(request, year):
    if int(year) > 2023:
        raise Http404
    if int(year) < 2000:
        return redirect("home")
    return HttpResponse(f"<h1>Архив по годам:</h1><p>{year}</p>")