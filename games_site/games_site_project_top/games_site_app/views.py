import random
from django.shortcuts import render
from django.shortcuts import redirect
from.models import games_data
from.forms import ReviewForm


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


def recent_games(request):
    games = games_data.objects.order_by('-release_date')[:10]
    context = {'games': games}
    return render(request, 'recent_games.html', context)

def view_by_name(request, title:str):
    games_list = games_data.objects.filter(title=title)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.game = games_list
            review.save()
            return redirect(request.path(f'by_name/{title}'))
    else:
        form = ReviewForm()

    if request.method == 'GET':
        context = {'games_list': games_list, 'title': title, 'form': form}
        return render(request, "view_name.html", context)


def random_game(request):
    games = games_data.objects.all()
    random_game = random.choice(games)
    context = {'game': random_game}
    return render(request, 'random_game.html', context)

