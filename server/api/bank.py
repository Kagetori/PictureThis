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
