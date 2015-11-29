from models import User, Friend

import config, friend

from interface.exception import RemoteException
from interface.user import FriendUser

# Search api

def find_user(user_id, username):
    if username is None or username == '':
        raise RemoteException('Username cannot be blank.')

    user = None

    try:
        user = User.objects.get(obfuscated_id=user_id)
    except User.DoesNotExist:
        raise RemoteException('Username password combination not valid.')

    found_user = None

    try:
        found_user = User.objects.get(name=username)
    except User.DoesNotExist:
        raise RemoteException('User does not exist.')

    return friend.get_friend_details(user_id=user_id, friend_id=found_user.obfuscated_id)
