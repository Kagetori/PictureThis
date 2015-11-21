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
    url(r'^friend/add_friend', views.friend__add_friend, name='picturethis__friend__add_friend'),
    url(r'^friend/remove_friend', views.friend__remove_friend, name='picturethis__friend__remove_friend'),
    url(r'^friend/block_friend', views.friend__block_friend, name='picturethis__friend__block_friend'),
    url(r'^friend/get_friends', views.friend__get_friends, name='picturethis__friend__get_friends'),

    # LOGIN API
    url(r'^login/create_user', views.login__create_user, name='picturethis__login__create_user'),
    url(r'^login/login', views.login__login, name='picturethis__login__login'),
    url(r'^login/update_password', views.login__update_password, name='picturethis__login__update_password'),

    # BANK API
    url(r'^bank/get_user_bank', views.bank__get_user_bank, name='picturethis__bank__get_user_bank'),

    # SEARCH API
    url(r'^search/find_user', views.search__find_user, name='picturethis__search__find_user'),

    # POLL API
    url(r'^poll/update', views.poll__update, name='picturethis__poll__update'),

    # GAME API
    url(r'^game/start_new_game', views.game__start_new_game, name='picturethis__game__start_new_game'),
    url(r'^game/send_picture', views.game__send_picture, name='picturethis__game__send_picture'),
    url(r'^game/get_picture', views.game__get_picture, name='picturethis__game__get_picture'),
    url(r'^game/end_game', views.game__end_game, name='picturethis__game__end_game'),
    url(r'^game/validate_guess', views.game__validate_guess, name='picturethis__game__validate_guess'),
    url(r'^game/get_user_games', views.game__get_user_games, name='picturethis__game__get_user_games'),
    url(r'^game/get_game_status', views.game__get_game_status, name='picturethis__game__get_game_status'),

    # WORD_PROMPT API
    url(r'^word_prompt/request_hint', views.word_prompt__request_hint, name='picturethis__word_prompt__request_hint'),

    # BANK API
    url(r'^bank/get_user_bank', views.bank__get_user_bank, name='bank__get_user_bank'),
    url(r'^bank/decrement_bank', views.bank__decrement_bank, name='bank__decrement_bank'),
]
