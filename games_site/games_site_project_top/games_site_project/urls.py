"""
URL configuration for games_site_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from games_site_app.views import view_all, view_by_genre, search, recent_games,view_by_name, random_game
urlpatterns = [
    path('admin/', admin.site.urls),
    path('view_all/', view_all, name= 'view_all'),
    path('by_genre/<str:genre>', view_by_genre, name='by_genre'),
    path('search/',search, name='search'),
    path('recent_games/',recent_games, name='recent_games'),
    path('by_name/<str:title>', view_by_name, name='by_name'),
    path('random-game/', random_game, name='random_game')
]
