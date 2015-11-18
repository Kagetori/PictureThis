from models import User, Friend

from interface.exception import RemoteException
from interface.packets import FriendPacket
from interface.user import FriendUser

import config

# Friend api

def add_friend(user_id, friend_id):
    return _set_friendship(user_id=user_id, friend_id=friend_id, relation=config.FRIEND_STATUS_FRIEND)

def remove_friend(user_id, friend_id):
    return _set_friendship(user_id=user_id, friend_id=friend_id, relation=config.FRIEND_STATUS_REMOVED)

def block_friend(user_id, friend_id):
    return _set_friendship(user_id=user_id, friend_id=friend_id, relation=config.FRIEND_STATUS_BLOCKED)

def get_friend_status(user_id1, user_id2):
    try:
        return Friend.objects.get(user_id1=user_id1, user_id2=user_id2).relation
    except Friend.DoesNotExist:
        return config.FRIEND_STATUS_REMOVED

def get_user_friends(user_id):
    friends = Friend.objects.filter(user_id1=user_id, relation=config.FRIEND_STATUS_FRIEND)

    result = []

    for f in friends:
        friend_user_id = f.user_id2

        friend_user = User.objects.get(obfuscated_id=friend_user_id)

        result.append(FriendUser(username=friend_user.name, user_id=friend_user.obfuscated_id, relation=config.FRIEND_STATUS_FRIEND))

    return FriendPacket(result)

def _set_friendship(user_id, friend_id, relation):
    try:
        User.objects.get(obfuscated_id=user_id)
        User.objects.get(obfuscated_id=friend_id)
    except User.DoesNotExist:
        raise RemoteException('Invalid user id.')

    if user_id == friend_id:
        raise RemoteException('Cannot set friendship between two identical users')

    # If friend_id has blocked user_id, return invalid user id
    friendship, _ = Friend.objects.get_or_create(user_id1=friend_id, user_id2=user_id)
    if friendship.relation == config.FRIEND_STATUS_BLOCKED:
        raise RemoteException('Invalid user id.')

    # Otherwise, do as normal
    friendship.relation = relation
    friendship.save()

    friendship, _ = Friend.objects.get_or_create(user_id1=user_id, user_id2=friend_id)
    friendship.relation = relation
    friendship.save()

    return get_user_friends(user_id)
