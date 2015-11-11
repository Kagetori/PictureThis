from models import User, Friend, Game

from interface.exception import RemoteException
from interface.poll import Poll
from interface.packets import PollPacket

import config
import game

# Poll api

def update(user_id):
    """
    Returns all the user's friends and games associated with friends
    """
    if user_id is None:
        raise RemoteException('User ID cannot be blank.')

    try:
        user = User.objects.get(obfuscated_id=user_id)
    except User.DoesNotExist:
        raise RemoteException("User doesn't exist")

    friends = Friend.objects.filter(user_id1=user_id, relation=config.FRIEND_STATUS_FRIEND)

    result = []

    for f in friends:
        friend_id = f.user_id2

        result.append(_get_poll(user_id=user_id, friend_id=friend_id))

    return PollPacket(result)

def _get_poll(user_id, friend_id):
    friend_user = User.objects.get(obfuscated_id=friend_id)

    try:
        game_obj = game.get_game_status(user_id=user_id, friend_id=friend_id)
    except RemoteException:
        return Poll(user_id=user_id, friend_id=friend_id, friend_username=friend_user.name, active_game=False, is_turn=None, is_photographer=None)

    return Poll(user_id=user_id, friend_id=friend_id, friend_username=friend_user.name, active_game=game_obj.active, is_turn=game_obj.is_turn, is_photographer=game_obj.is_photographer)
