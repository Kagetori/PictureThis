from django.http import JsonResponse

from api import friend, game, login, poll, search

from interface.success import SuccessPacket
from interface.exception import RemoteException

# FRIEND API

def friend__add_friend(request):
    params = _params(request)
    
    user_id = params.get('user_id', 0)
    friend_id = params.get('friend_id', 0)

    return _response(friend.add_friend, user_id=user_id, friend_id=friend_id)

def friend__remove_friend(request):
    params = _params(request)
    
    user_id = params.get('user_id', 0)
    friend_id = params.get('friend_id', 0)

    return _response(friend.remove_friend, user_id=user_id, friend_id=friend_id)

def friend__get_friends(request):
    params = _params(request)
    
    user_id = params.get('user_id', 0)

    return _response(friend.get_user_friends, user_id=user_id)

# LOGIN API

def login__create_user(request):
    params = _params(request)
    
    username = params.get('username', None)
    password = params.get('password', None)
    client_version = params.get('client_version', 0)
    device_id =  params.get('device_id', None)

    return _response(login.create_user, username=username, password=password, client_version=client_version, device_id=device_id)

def login__login(request):
    params = _params(request)
    
    username = params.get('username', None)
    password = params.get('password', None)
    client_version = params.get('client_version', 0)
    device_id =  params.get('device_id', None)

    return _response(login.login, username=username, password=password, client_version=client_version, device_id=device_id)


# POLL API

def poll__update(request):
    params = _params(request)

    user_id = params.get('user_id', 0)

    return _response(poll.update, user_id=user_id)



# SEARCH API

def search__find_user(request):
    params = _params(request)

    username = params.get('username', None)

    return _response(search.find_user, username=username)



# GAME API
def game__start_new_game(request):
    params = _params(request)

    user_id = params.get('user_id', 0)
    friend_id = params.get('friend_id', 0)

    return _response(game.start_new_game, user_id=user_id, friend_id=friend_id)

def game__send_picture(request):
    params = _params(request)

    user_id = params.get('user_id', None)
    game_id = params.get('game_id', None)

    return _response(game.send_picture, user_id=user_id, game_id=game_id)

def game__end_game(request):
    params = _params(request)

    user_id = params.get('user_id', None)
    game_id = params.get('game_id', None)

    return _response(game.end_game, user_id=user_id, game_id=game_id)

def game__validate_guess(request):
    params = _params(request)

    user_id = params.get('user_id', None)
    game_id = params.get('game_id', None)
    guess = params.get('guess', None)

    return _response(game.validate_guess, user_id=user_id, game_id=game_id, guess=guess)

def game__get_user_games(request):
    params = _params(request)

    user_id = params.get('user_id', None)

    return _response(game.get_user_games, user_id=user_id)


# HELPER FUNCTIONS

def _params(request):
    return request.GET

def _response(fn, **kwargs):
    try:
        response = fn(**kwargs)
        return JsonResponse(response.ret_dict())
    except RemoteException as e:
        return JsonResponse(e.ret_dict())
