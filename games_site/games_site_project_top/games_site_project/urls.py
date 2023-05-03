from django.contrib import admin
from django.urls import path, include
from games_site_app.views import view_all, view_by_genre, search, recent_games,view_name, random_game

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view_all, name= 'view_all'),
    path('by_genre/<str:genre>', view_by_genre, name='by_genre'),
    path('search/',search, name='search'),
    path('recent_games/',recent_games, name='recent_games'),
    path('by_name/<int:id>', view_name, name='by_name'),
    path('random-game/', random_game, name='random_game'),
    path('accounts/' , include('accounts.urls'))
]
