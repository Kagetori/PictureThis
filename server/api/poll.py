from models import User, Friend, Game

from interface.exception import RemoteException
from interface.poll import Poll

import config
import friend, bank, score

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

    friends = friend.get_user_friends(user_id=user_id).friends

    bank_account = bank.get_user_bank(user_id=user_id)
    score_account = score.get_user_score(user_id=user_id)

    return Poll(friends=friends, bank_account=bank_account, score=score_account)
