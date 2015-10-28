from models import User, Friend

from interface.exception import RemoteException
from interface.user import User as RemoteUser

# Search api

def find_user(username):
    if username is None:
        raise RemoteException('Username cannot be blank.')

    user = None

    try:
        user = User.objects.get(name=username)
    except User.DoesNotExist:
        raise RemoteException('User does not exist.')

    return RemoteUser(username=username, user_id=user.obfuscated_id)
