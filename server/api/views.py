from django.http import JsonResponse

from api import friend, login, search

from interface.success import SuccessPacket

# FRIEND API

def friend__add_friend(request):
    params = _params(request)
    
    user_id = params.get('user_id', None)
    target_id = params.get('target_id', None)

    return _response(friend.add_friend(user_id=user_id, target_id=target_id))

def friend__get_friends(request):
    params = _params(request)
    
    user_id = params.get('user_id', None)

    return _response(friend.get_user_friends(user_id=user_id))




# LOGIN API

def login__create_user(request):
    params = _params(request)
    
    username = params.get('username', None)
    password = params.get('password', None)
    client_version = params.get('client_version', 0)
    device_id =  params.get('device_id', None)

    return _response(login.create_user(username=username, password=password, client_version=client_version, device_id=device_id))

def login__login(request):
    params = _params(request)
    
    username = params.get('username', None)
    password = params.get('password', None)
    client_version = params.get('client_version', 0)
    device_id =  params.get('device_id', None)

    return _response(login.login(username=username, password=password, client_version=client_version, device_id=device_id))




# SEARCH API

def search__find_user(request):
    params = _params(request)

    username = params.get('username', None)

    return _response(search.find_user(username=username))



# HELPER FUNCTIONS

def _params(request):
    return request.GET

def _response(response):
    return JsonResponse(response.ret_dict())

