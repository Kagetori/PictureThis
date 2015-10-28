"""picturethis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url

from api import views

urlpatterns = [
    # FRIEND API
    url(r'^friend/add_friend', views.friend__add_friend, name='friend__add_friend'),
    url(r'^friend/remove_friend', views.friend__remove_friend, name='friend__remove_friend'),
    url(r'^friend/get_friends', views.friend__get_friends, name='friend__get_friends'),

    # LOGIN API
    url(r'^login/create_user', views.login__create_user, name='login__create_user'),
    url(r'^login/login', views.login__login, name='login__login'),

    # SEARCH API
    url(r'^search/find_user', views.search__find_user, name='search__find_user'),

    # POLL API
    url(r'^poll/update', views.poll__update, name='poll__update'),

    # GAME API
    url(r'^game/start_new_game', views.game__start_new_game, name='game__start_new_game'),
    url(r'^game/start_new_round', views.game__start_new_round, name='game__start_new_round'),
    url(r'^game/end_game', views.game__end_game, name='game__end_game'),
    url(r'^game/validate_guess', views.game__validate_guess, name='game__validate_guess'),
    url(r'^game/get_user_games', views.game__get_user_games, name='game__get_user_games'),
]
