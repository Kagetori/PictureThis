from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from api import friend, game, login, poll, search, word_prompt, bank
from models import User

from interface.exception import RemoteException, NotAuthenticatedException

import config
import urllib

# FRIEND API

@csrf_exempt
def friend__add_friend(request):
    params = _params(request)

    try:
        _check_blocking(params)
    except NotAuthenticatedException as e:
        return JsonResponse(e.ret_dict())

    user_id = _get_param(params, 'user_id', int, 0)
    friend_id = _get_param(params, 'friend_id', int, 0)

    return _response(friend.add_friend, user_id=user_id, friend_id=friend_id)

@csrf_exempt
def friend__remove_friend(request):
    params = _params(request)

    try:
        _check_blocking(params)
    except NotAuthenticatedException as e:
        return JsonResponse(e.ret_dict())

    user_id = _get_param(params, 'user_id', int, 0)
    friend_id = _get_param(params, 'friend_id', int, 0)

    return _response(friend.remove_friend, user_id=user_id, friend_id=friend_id)

@csrf_exempt
def friend__block_friend(request):
    params = _params(request)

    try:
        _check_blocking(params)
    except NotAuthenticatedException as e:
        return JsonResponse(e.ret_dict())

    user_id = _get_param(params, 'user_id', int, 0)
    friend_id = _get_param(params, 'friend_id', int, 0)

    return _response(friend.block_friend, user_id=user_id, friend_id=friend_id)

@csrf_exempt
def friend__get_friends(request):
    params = _params(request)

    try:
        _check_blocking(params)
    except NotAuthenticatedException as e:
        return JsonResponse(e.ret_dict())

    user_id = _get_param(params, 'user_id', int, 0)

    return _response(friend.get_user_friends, user_id=user_id)

# LOGIN API

@csrf_exempt
def login__create_user(request):
    """
    Call is not authenticated, since it's a login call essentially
    """
    params = _params(request)

    try:
        _check_blocking(params, authenticate=False)
    except NotAuthenticatedException as e:
        return JsonResponse(e.ret_dict())

    username = _get_param(params, 'username')
    password = _get_param(params, 'password')
    device_id =  _get_param(params, 'device_id')

    return _response(login.create_user, username=username, password=password, device_id=device_id)

@csrf_exempt
def login__login(request):
    """
    Call is not authenticated, since it's a login call
    """
    params = _params(request)

    try:
        _check_blocking(params, authenticate=False)
    except NotAuthenticatedException as e:
        return JsonResponse(e.ret_dict())

    username = _get_param(params, 'username')
    password = _get_param(params, 'password')
    device_id =  _get_param(params, 'device_id')

    return _response(login.login, username=username, password=password, device_id=device_id)

@csrf_exempt
def login__token_login(request):
    """
    Call is not authenticated, since it's a login call
    """
    params = _params(request)

    try:
        _check_blocking(params, authenticate=False)
    except NotAuthenticatedException as e:
        return JsonResponse(e.ret_dict())

    user_id = _get_param(params, 'user_id', int, 0)
    login_token = _get_param(params, 'login_token')
    device_id =  _get_param(params, 'device_id')

    return _response(login.token_login, user_id=user_id, login_token=login_token, device_id=device_id)

# USER API
# NOTE: THIS API RESIDES IN LOGIN.PY for code reuse purposes.

@csrf_exempt
def user__update_password(request):
    params = _params(request)

    try:
        _check_blocking(params)
    except NotAuthenticatedException as e:
        return JsonResponse(e.ret_dict())

    user_id = _get_param(params, 'user_id', int, 0)
    old_password = _get_param(params, 'old_password')
    new_password = _get_param(params, 'new_password')

    return _response(login.update_password, user_id=user_id, old_password=old_password, new_password=new_password)

# BANK API

@csrf_exempt
def bank__get_user_bank(request):
    params = _params(request)

    try:
        _check_blocking(params)
    except NotAuthenticatedException as e:
        return JsonResponse(e.ret_dict())

    user_id = _get_param(params, 'user_id', int, 0)

    return _response(bank.get_user_bank, user_id=user_id)

@csrf_exempt
def bank__get_user_bank(request):
    params = _params(request)

    try:
        _check_blocking(params)
    except NotAuthenticatedException as e:
        return JsonResponse(e.ret_dict())

    user_id = _get_param(params, 'user_id', int, 0)

    return _response(bank.get_user_bank, user_id=user_id)

@csrf_exempt
def bank__decrement_bank(request):
    params = _params(request)

    try:
        _check_blocking(params)
    except NotAuthenticatedException as e:
        return JsonResponse(e.ret_dict())

    user_id = _get_param(params, 'user_id', int, 0)

    return _response(bank.decrement_bank, user_id=user_id)

# POLL API

@csrf_exempt
def poll__update(request):
    params = _params(request)

    try:
        _check_blocking(params)
    except NotAuthenticatedException as e:
        return JsonResponse(e.ret_dict())

    user_id = _get_param(params, 'user_id', int, 0)

    return _response(poll.update, user_id=user_id)

# SEARCH API

@csrf_exempt
def search__find_user(request):
    params = _params(request)

    try:
        _check_blocking(params)
    except NotAuthenticatedException as e:
        return JsonResponse(e.ret_dict())

    user_id = _get_param(params, 'user_id', int, 0)
    username = _get_param(params, 'username')

    return _response(search.find_user, user_id=user_id, username=username)


# GAME API

@csrf_exempt
def game__start_new_game(request):
    params = _params(request)

    try:
        _check_blocking(params)
    except NotAuthenticatedException as e:
        return JsonResponse(e.ret_dict())

    user_id = _get_param(params, 'user_id', int, 0)
    friend_id = _get_param(params, 'friend_id', int, 0)

    return _response(game.start_new_game, user_id=user_id, friend_id=friend_id)

@csrf_exempt
def game__send_picture(request):
    params = _params(request)

    try:
        _check_blocking(params)
    except NotAuthenticatedException as e:
        return JsonResponse(e.ret_dict())

    user_id = _get_param(params, 'user_id', int, 0)
    game_id = _get_param(params, 'game_id', int, 0)
    photo = _get_param(params, 'file')

    if photo is None:
        return JsonResponse(NotAuthenticatedException('Unable to upload image').ret_dict())

    return _response(game.send_picture, user_id=user_id, game_id=game_id, photo=photo)

@csrf_exempt
def game__get_picture(request):
    params = _params(request)

    try:
        _check_blocking(params)
    except NotAuthenticatedException as e:
        return JsonResponse(e.ret_dict())

    user_id = _get_param(params, 'user_id', int, 0)
    game_id = _get_param(params, 'game_id', int, 0)

    return _response(game.get_picture, user_id=user_id, game_id=game_id)

@csrf_exempt
def game__end_game(request):
    params = _params(request)

    try:
        _check_blocking(params)
    except NotAuthenticatedException as e:
        return JsonResponse(e.ret_dict())

    user_id = _get_param(params, 'user_id', int, 0)
    game_id = _get_param(params, 'game_id', int, 0)

    return _response(game.end_game, user_id=user_id, game_id=game_id)

@csrf_exempt
def game__validate_guess(request):
    params = _params(request)

    try:
        _check_blocking(params)
    except NotAuthenticatedException as e:
        return JsonResponse(e.ret_dict())

    user_id = _get_param(params, 'user_id', int, 0)
    game_id = _get_param(params, 'game_id', int, 0)
    guess = _get_param(params, 'guess')
    score = _get_param(params, 'score', int, 0)

    return _response(game.validate_guess, user_id=user_id, game_id=game_id, guess=guess, score=score)

@csrf_exempt
def game__give_up_turn(request):
    params = _params(request)

    try:
        _check_blocking(params)
    except NotAuthenticatedException as e:
        return JsonResponse(e.ret_dict())

    user_id = _get_param(params, 'user_id', int, 0)
    game_id = _get_param(params, 'game_id', int, 0)

    return _response(game.give_up_turn, user_id=user_id, game_id=game_id)

@csrf_exempt
def game__get_user_games(request):
    params = _params(request)

    try:
        _check_blocking(params)
    except NotAuthenticatedException as e:
        return JsonResponse(e.ret_dict())

    user_id = _get_param(params, 'user_id', int, 0)

    return _response(game.get_user_games, user_id=user_id)

@csrf_exempt
def game__get_game_status(request):
    params = _params(request)

    try:
        _check_blocking(params)
    except NotAuthenticatedException as e:
        return JsonResponse(e.ret_dict())

    user_id = _get_param(params, 'user_id', int, 0)
    friend_id = _get_param(params, 'friend_id', int, 0)

    return _response(game.get_game_status, user_id=user_id, friend_id=friend_id)

@csrf_exempt
def game__get_new_word(request):
    params = _params(request)

    try:
        _check_blocking(params)
    except NotAuthenticatedException as e:
        return JsonResponse(e.ret_dict())

    user_id = _get_param(params, 'user_id', int, 0)
    game_id = _get_param(params, 'game_id', int, 0)

    return _response(game.get_new_word, user_id=user_id, game_id=game_id)

# REMOVE LATER
@csrf_exempt
def game__end_all_games(request):
    return _response(game._end_all_games)

# WORD PROMPT API

@csrf_exempt
def word_prompt__request_hint(request):
    params = _params(request)

    try:
        _check_blocking(params)
    except NotAuthenticatedException as e:
        return JsonResponse(e.ret_dict())

    word = _get_param(params, 'word')
    user_id = _get_param(params, 'user_id', int, 0)

    return _response(word_prompt.request_hint, word=word, user_id=user_id)

# HELPER FUNCTIONS

def _params(request):
    return request.POST

def _get_param(params, key, fn=str, default=None):
    value = params.get(key, default)

    if value == default:
        return default
    else:
        return fn(urllib.unquote(value).decode('utf-8'))

def _response(fn, **kwargs):
    json_response = None
    try:
        response = fn(**kwargs)
        return JsonResponse(response.ret_dict())
    except RemoteException as e:
        return JsonResponse(e.ret_dict())

def _check_blocking(params, authenticate=True):
    client_version = _get_param(params, 'client_version', int, 0)

    if client_version < config.MIN_CLIENT_VERSION:
        raise NotAuthenticatedException('Please upgrade your app (i.e. merge master).')

    client_secret = _get_param(params, 'client_secret')

    if client_secret != config.CLIENT_SECRET_KEY:
        raise NotAuthenticatedException('Not authenticated.')

    if authenticate:
        auth_token = _get_param(params, 'auth_token')
        user_id = _get_param(params, 'user_id', int, 0)
        if auth_token is None or user_id is None:
            raise NotAuthenticatedException('Not authenticated.')
        try:
            user = User.objects.get(obfuscated_id=user_id)
            if not user.authenticate(auth_token):
                raise NotAuthenticatedException('Not authenticated.')

        except User.DoesNotExist:
            raise NotAuthenticatedException('User does not exist.')
