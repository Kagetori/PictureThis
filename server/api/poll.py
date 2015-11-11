from models import User, Friend, Game

from interface.exception import RemoteException
from interface.poll import Poll
from interface.packets import PollPacket

import config

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

    game = None

    try:
        game = Game.objects.get(user_id1=user_id, user_id2=friend_id, active=True)
    except Game.DoesNotExist:
        pass

    if game is None:
        try:
            Game.objects.get(user_id2=user_id, user_id1=friend_id, active=True)
        except Game.DoesNotExist:
            pass

    friend_username = friend_user.name
    if (game is None or not game.active):
        active_game=False
        is_turn=None
        is_photographer=None
    else:
        active_game=True
        game_initiator=game.user_id1
        round_num=game.curr_round

        if (user_id==game_initiator):
            return (round_num % 2 == 0)
        else:
            return (round_num % 2 != 0)

    return Poll(user_id=user_id, friend_id=friend_id, friend_username=friend_username, active_game=active_game, is_turn=is_turn, is_photographer=is_photographer)


