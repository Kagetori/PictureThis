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

    friend_status = friend.get_friend_status(user_id1=user.obfuscated_id, user_id2=found_user.obfuscated_id)
    reverse_friend_status = friend.get_friend_status(user_id1=found_user.obfuscated_id, user_id2=user.obfuscated_id)

    if reverse_friend_status == config.FRIEND_STATUS_BLOCKED:
        # the found user has blocked the original user, so we might as well say that they don't exist
        raise RemoteException('User does not exist.')

    return FriendUser(username=username, user_id=found_user.obfuscated_id, relation=friend_status)
