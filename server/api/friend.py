from models import User, Friend

from interface.exception import RemoteException
from interface.user import User as RemoteUser

import config

# Friend api

def add_friend(user_id, auth_token, target_id):
    return set_friendship(user_id=user_id, auth_token=auth_token, target_id=target_id, relation=config.FRIEND_STATUS_FRIEND)

def remove_friend(user_id, auth_token, target_id):
    return set_friendship(user_id=user_id, auth_token=auth_token, target_id=target_id, relation=config.FRIEND_STATUS_REMOVED)

def set_friendship(user_id, auth_token, target_id, relation):
    user1 = None
    user2 = None

    try:
        user1 = User.objects.get(obfuscated_id=user_id)
        user2 = User.objects.get(obfuscated_id=target_id)
    except User.DoesNotExist:
        return RemoteException('Invalid user id.')

    if not user1.authenticate(auth_token=auth_token):
        # ERROR
        print user1.auth_token
        print auth_token
        return RemoteException('User not authenticated.')

    # TODO NEED TO ACTUALLY ADD THE FRIENDSHIP

    return 0

def is_friend(user_id1, user_id2):
    try:
        return Friend.objects.get(id1=user_id1, id2=user_id2).relation
    except User.DoesNotExist:
        return config.FRIEND_STATUS_REMOVED

def get_user_friends(user_id):

    # TODO

    return []