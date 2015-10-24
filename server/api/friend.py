from models import User, Friend

from interface.exception import RemoteException
from interface.packets import FriendPacket
from interface.success import SuccessPacket
from interface.user import FriendUser

import config

# Friend api

def add_friend(user_id, target_id):
    return _set_friendship(user_id=user_id, target_id=target_id, relation=config.FRIEND_STATUS_FRIEND)

def remove_friend(user_id, target_id):
    return _set_friendship(user_id=user_id, target_id=target_id, relation=config.FRIEND_STATUS_REMOVED)

def is_friend(user_id1, user_id2):
    try:
        return Friend.objects.get(user_id1=user_id1, user_id2=user_id2).relation
    except User.DoesNotExist:
        return config.FRIEND_STATUS_REMOVED

def get_user_friends(user_id):

    friends = Friend.objects.filter(user_id1=user_id, relation=config.FRIEND_STATUS_FRIEND)

    result = []

    for f in friends:
        friend_user_id = f.user_id2

        friend_user = User.objects.get(obfuscated_id=friend_user_id)

        result.append(FriendUser(username=friend_user.name, user_id=friend_user.obfuscated_id))

    return FriendPacket(result)

def _set_friendship(user_id, target_id, relation):
    user1 = None
    user2 = None

    try:
        user1 = User.objects.get(obfuscated_id=user_id)
        user2 = User.objects.get(obfuscated_id=target_id)
    except User.DoesNotExist:
        return RemoteException('Invalid user id.')

    friendship, _ = Friend.objects.get_or_create(user_=user_id, user_id2=target_id)
    friendship.relation = relation
    friendship.save()

    friendship, _ = Friend.objects.get_or_create(user_=target_id, user_id2=user_id)
    friendship.relation = relation
    friendship.save()

    return get_user_friends(user_id)
