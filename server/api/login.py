from django.contrib.auth.hashers import make_password

from models import User, Friend

import utility
import uuid

# Login api

def encrypt_password(password):
    return make_password(password=password, salt=None, hasher='unsalted_sha1')

def login(username, password, client_version=1):
    """
    API Function to login a user
    """
    user = None

    try:
        user = User.objects.get(name=username)
    except User.DoesNotExist:
        # TODO make json exception
        return -1

    if user.password != encrypt_password(password):
        # TODO make json exception
        return -1

    # TODO GET FRIEND LISTS

    # TODO return stuff in JSON format
    return user

def create_user(username, password, client_version=1):
    """
    API Function to create a user
    """
    user = None

    try:
        user = User.objects.get(name=username)
        # TODO make json exception
        return -1
    except User.DoesNotExist:
        pass

    user = User.objects.create(name=username, password=encrypt_password(password), auth_token=uuid.uuid4())
    user.obfuscated_id = utility.obfuscate_id(user.id)
    user.save()

    # TODO GET FRIEND LISTS

    # TODO return stuff in JSON format
    return user
