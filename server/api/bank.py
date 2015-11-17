from models import Bank

from interface.exception import RemoteException
from interface.bank import Bank as RemoteBank

# Bank api

def get_user_bank(user_id):
    """
    API Function to get user's bank
    """
    try:
        bank = Bank.objects.get(user_id=user_id)
        return RemoteBank(stars=bank.stars)

    except Bank.DoesNotExist:
        raise RemoteException('Unable to find user bank account')

def add_to_bank(user_id, stars):
    """
    Adds the specified number of stars to the bank account of the
    user with the given user_id

    THIS FUNCTION SHOULD NEVER BE EXPOSED IN URLS and VIEWS.
    WE DO NOT WANT USERS TO BE ABLE TO ADD IN GAME CURRENCY
    VIA AN API CALL
    """
    try:
        bank = Bank.objects.get(user_id=user_id)

        bank.stars += stars
        bank.save()

        return RemoteBank(stars=bank.stars)

    except Bank.DoesNotExist:
        raise RemoteException('Unable to find user bank account')
