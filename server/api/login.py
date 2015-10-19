from django.contrib.auth.hashers import make_password

from models import User, Friend

from interface.exception import RemoteException
from interface.user import LoginUser

import random
import string
import utility
import uuid

# Login api

def encrypt_password(password, salt):
    return make_password(password=password, salt=salt, hasher='sha1')

def login(username, password, client_version=1, device_id=None):
    """
    API Function to login a user
    """
    user = None

    try:
        user = User.objects.get(name=username)
    except User.DoesNotExist:
        # TODO make json exception
        return RemoteException('Username password combination not valid.')

    if user.password != encrypt_password(password=password, salt=user.salt):
        # TODO make json exception
        return RemoteException('Username password combination not valid.')

    # TODO GET FRIEND LISTS

    # TODO return stuff in JSON format
    return LoginUser(username=username, user_id=user.obfuscated_id, auth_token=user.get_auth_token(), friends=[])

def create_user(username, password, client_version=1, device_id=None):
    """
    API Function to create a user
    """
    user = None

    try:
        user = User.objects.get(name=username)
        # TODO make json exception
        return RemoteException('Username already exists.')
    except User.DoesNotExist:
        pass

    salt = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(16))

    user = User.objects.create(name=username, password=encrypt_password(password=password, salt=salt), salt=salt, auth_token=uuid.uuid4())
    user.obfuscated_id = utility.obfuscate_id(user.id)
    user.save()

    # TODO GET FRIEND LISTS

    # TODO return stuff in JSON format
    return LoginUser(username=username, user_id=user.obfuscated_id, auth_token=user.get_auth_token(), friends=[])
