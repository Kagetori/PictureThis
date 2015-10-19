from django.http import HttpResponse

from api import friend, login

from interface.success import SuccessPacket

def _params(request):
    return request.GET

def login__create_user(request):
    params = _params(request)
    
    username = params.get('username', None)
    password = params.get('password', None)
    client_version = params.get('client_version', 0)
    device_id =  params.get('device_id', None)

    return HttpResponse(login.create_user(username=username, password=password, client_version=client_version, device_id=device_id))


def login__login(request):
    params = _params(request)
    
    username = params.get('username', None)
    password = params.get('password', None)
    client_version = params.get('client_version', 0)
    device_id =  params.get('device_id', None)

    return HttpResponse(login.login(username=username, password=password, client_version=client_version, device_id=device_id))
