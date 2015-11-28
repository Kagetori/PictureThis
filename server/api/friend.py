from models import User, Friend

from interface.exception import RemoteException
from interface.packets import FriendPacket, SuccessPacket
from interface.user import FriendUser

import config, game

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

def get_friend_details(user_id, friend_id):
    friend_user = User.objects.get(obfuscated_id=friend_id)

    game_obj = None

    try:
        game_obj = game.get_game_status(user_id=user_id, friend_id=friend_id)
    except RemoteException:
        pass

    friend_status = get_friend_status(user_id1=user_id, user_id2=friend_id)
    reverse_status = get_friend_status(user_id1=friend_id, user_id2=user_id)

    if reverse_status == config.FRIEND_STATUS_BLOCKED and friend_status == config.FRIEND_STATUS_REMOVED:
        raise RemoteException('Invalid user id.')

    if game_obj is None or not game_obj.active:
        return FriendUser(user_id=friend_id, username=friend_user.name, relation=friend_status, has_active_game=False)
    else:
        return FriendUser(user_id=friend_id, username=friend_user.name, relation=friend_status, has_active_game=True, is_turn=game_obj.is_turn, is_photographer=game_obj.is_photographer)

def get_user_friends(user_id):
    friends = Friend.objects.filter(user_id1=user_id, relation=config.FRIEND_STATUS_FRIEND)

    result = []

    for f in friends:
        friend_user_id = f.user_id2

        result.append(get_friend_details(user_id=user_id, friend_id=friend_user_id))

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

    # Otherwise, do as normal for the reverse relation
    if relation == config.FRIEND_STATUS_BLOCKED:
        friendship.relation = config.FRIEND_STATUS_REMOVED
    else:
        friendship.relation = relation
    friendship.save()

    # If removing or blocking friend and there is an active game, end the game
    if relation == config.FRIEND_STATUS_BLOCKED or relation == config.FRIEND_STATUS_REMOVED:
        existing_game = None
        try:
            existing_game = game.get_game_status(user_id=user_id, friend_id=friend_id)
        except RemoteException:
            pass
        if existing_game is not None and existing_game.active:
            game.end_game(user_id=user_id, game_id=existing_game.game_id, award_stars=False)

    # This relation is a straightforward assignment
    friendship, _ = Friend.objects.get_or_create(user_id1=user_id, user_id2=friend_id)
    friendship.relation = relation
    friendship.save()

    return SuccessPacket()
