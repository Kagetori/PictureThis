from django.contrib.auth.hashers import check_password, make_password

from models import User, Friend

from interface.exception import RemoteException
from interface.user import LoginUser

import friend

import random
import string
import utility
import uuid

# Login api

def create_user(username, password, client_version=1, device_id=None):
    """
    API Function to create a user
    """
    if username is None or password is None:
        return RemoteException('Username and password cannot be blank.')

    user = None

    try:
        user = User.objects.get(name=username)
        return RemoteException('Username already exists.')
    except User.DoesNotExist:
        pass

    salt = ''.join(random.choice(string.ascii_letters + string.digits + '!@#%^&*()_+-={}[]|,.<>?~') for _ in range(16))

    user = User.objects.create(name=username, password=_encrypt_password(password=password, salt=salt), auth_token=uuid.uuid4())
    user.obfuscated_id = utility.obfuscate_id(user.id)
    user.save()

    # New user should not have friends
    friends = []

    return LoginUser(username=username, user_id=user.obfuscated_id, auth_token=user.get_auth_token(), friends=friends)

def login(username, password, client_version=1, device_id=None):
    """
    API Function to login a user using password
    """
    if username is None or password is None:
        return RemoteException('Username and password cannot be blank.')

    user = None

    try:
        user = User.objects.get(name=username)
    except User.DoesNotExist:
        return RemoteException('Username password combination not valid.')

    if user is None:
        return RemoteException('Username password combination not valid.')

    if not check_password(password=password, encoded=user.password):
        return RemoteException('Username password combination not valid.')

    friends = friend.get_user_friends(user_id=user.obfuscated_id)

    return LoginUser(username=username, user_id=user.obfuscated_id, auth_token=user.get_auth_token(), friends=friends)

def _encrypt_password(password, salt):
    return make_password(password=password, salt=salt, hasher='sha1')
