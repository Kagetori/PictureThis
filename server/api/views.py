from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from api import friend, game, login, poll, search
from models import User

from interface.exception import RemoteException

import urllib

# FRIEND API

@csrf_exempt
def friend__add_friend(request):
    params = _params(request)

    if not _authenticate(params):
        return JsonResponse(RemoteException('Not authenticated').ret_dict())

    user_id = _get_param(params, 'user_id', 0)
    friend_id = _get_param(params, 'friend_id', 0)

    return _response(friend.add_friend, user_id=user_id, friend_id=friend_id)

@csrf_exempt
def friend__remove_friend(request):
    params = _params(request)
    if not _authenticate(params):
        return JsonResponse(RemoteException('Not authenticated').ret_dict())

    user_id = _get_param(params, 'user_id', 0)
    friend_id = _get_param(params, 'friend_id', 0)

    return _response(friend.remove_friend, user_id=user_id, friend_id=friend_id)

@csrf_exempt
def friend__get_friends(request):
    params = _params(request)
    if not _authenticate(params):
        return JsonResponse(RemoteException('Not authenticated').ret_dict())

    user_id = _get_param(params, 'user_id', 0)

    return _response(friend.get_user_friends, user_id=user_id)

# LOGIN API

@csrf_exempt
def login__create_user(request):
    params = _params(request)
    username = _get_param(params, 'username', None)
    password = _get_param(params, 'password', None)
    client_version = _get_param(params, 'client_version', 0)
    device_id =  _get_param(params, 'device_id', None)

    return _response(login.create_user, username=username, password=password, client_version=client_version, device_id=device_id)

@csrf_exempt
def login__login(request):
    params = _params(request)
    username = _get_param(params, 'username', None)
    password = _get_param(params, 'password', None)
    client_version = _get_param(params, 'client_version', 0)
    device_id =  _get_param(params, 'device_id', None)

    return _response(login.login, username=username, password=password, client_version=client_version, device_id=device_id)


# POLL API

@csrf_exempt
def poll__update(request):
    params = _params(request)

    if not _authenticate(params):
        return JsonResponse(RemoteException('Not authenticated').ret_dict())

    user_id = _get_param(params, 'user_id', 0)

    return _response(poll.update, user_id=user_id)



# SEARCH API

@csrf_exempt
def search__find_user(request):
    params = _params(request)

    if not _authenticate(params):
        return JsonResponse(RemoteException('Not authenticated').ret_dict())

    user_id = _get_param(params, 'user_id', 0)
    username = _get_param(params, 'username', None)

    return _response(search.find_user, user_id=user_id, username=username)




@csrf_exempt# GAME API
def game__start_new_game(request):
    params = _params(request)

    if not _authenticate(params):
        return JsonResponse(RemoteException('Not authenticated').ret_dict())

    user_id = _get_param(params, 'user_id', 0)
    friend_id = _get_param(params, 'friend_id', 0)

    return _response(game.start_new_game, user_id=user_id, friend_id=friend_id)

@csrf_exempt
def game__send_picture(request):
    params = _params(request)

    if not _authenticate(params):
        return JsonResponse(RemoteException('Not authenticated').ret_dict())

    user_id = _get_param(params, 'user_id', None)
    game_id = _get_param(params, 'game_id', None)

    photo = request.FILES.get('file')

    return _response(game.send_picture, user_id=user_id, game_id=game_id, photo=photo)

@csrf_exempt
def game__get_picture(request):
    params = _params(request)

    if not _authenticate(params):
        return JsonResponse(RemoteException('Not authenticated').ret_dict())

    user_id = _get_param(params, 'user_id', None)
    game_id = _get_param(params, 'game_id', None)

    try:
        return game.get_picture(user_id=user_id, game_id=game_id)
    except RemoteException as e:
        return JsonResponse(e.ret_dict())

@csrf_exempt
def game__end_game(request):
    params = _params(request)

    if not _authenticate(params):
        return JsonResponse(RemoteException('Not authenticated').ret_dict())

    user_id = _get_param(params, 'user_id', None)
    game_id = _get_param(params, 'game_id', None)

    return _response(game.end_game, user_id=user_id, game_id=game_id)

@csrf_exempt
def game__validate_guess(request):
    params = _params(request)

    if not _authenticate(params):
        return JsonResponse(RemoteException('Not authenticated').ret_dict())

    user_id = _get_param(params, 'user_id', None)
    game_id = _get_param(params, 'game_id', None)
    guess = _get_param(params, 'guess', None)

    return _response(game.validate_guess, user_id=user_id, game_id=game_id, guess=guess)

@csrf_exempt
def game__get_user_games(request):
    params = _params(request)

    if not _authenticate(params):
        return JsonResponse(RemoteException('Not authenticated').ret_dict())

    user_id = _get_param(params, 'user_id', None)

    return _response(game.get_user_games, user_id=user_id)

@csrf_exempt
def game__get_game_status(request):
    params = _params(request)

    if not _authenticate(params):
        return JsonResponse(RemoteException('Not authenticated').ret_dict())

    user_id = _get_param(params, 'user_id', None)
    friend_id = _get_param(params, 'friend_id', None)

    return _response(game.get_game_status, user_id=user_id, friend_id=friend_id)



# HELPER FUNCTIONS

def _params(request):
    return request.POST

def _get_param(params, key, default=None):
    value = params.get(key, default)

    if value == default:
        return default
    else:
        return urllib.unquote(value).decode('utf-8')

def _response(fn, **kwargs):
    try:
        response = fn(**kwargs)
        return JsonResponse(response.ret_dict())
    except RemoteException as e:
        return JsonResponse(e.ret_dict())

def _authenticate(params):
#    return True
    auth_token = _get_param(params, 'auth_token')
    user_id = _get_param(params, 'user_id')
    if auth_token is None or user_id is None:
        return False
    try:
        user = User.objects.get(obfuscated_id=user_id)
        return user.authenticate(auth_token)
    except User.DoesNotExist:
        return False
