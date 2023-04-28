from django.shortcuts import render
from.models import games_data

# Create your views here.
def view_all(request):
    games_all = games_data.objects.all()
    context = {'games_list': games_all}
    return render(request, "view_all.html", context)

def search(request):
    genre_list = games_data.objects.values_list('genre', flat=True).distinct()
    context = {'genre_list': genre_list}
    return render(request, "search.html", context)



def view_by_genre(request, genre: str):
    games_list = games_data.objects.filter(genre=genre)
    context = {'games_list': games_list, 'genre': genre}
    return render(request, "view_genre.html", context)
