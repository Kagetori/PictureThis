from django.contrib.auth.hashers import check_password, make_password

from models import User, Friend, Bank, Score

from interface.exception import RemoteException
from interface.packets import SuccessPacket
from interface.user import LoginUser

import friend, game, bank, config, score

import random
import string
import utility
import uuid

# Login api

def create_user(username, password, client_version=1, device_id=None):
    """
    API Function to create a user
    """
    if username is None or password is None or username == '' or password == '':
        raise RemoteException('Username and password cannot be blank.')

    user = None

    try:
        user = User.objects.get(name=username)
        raise RemoteException('Username already exists.')
    except User.DoesNotExist:
        pass

    salt = ''.join(random.choice(string.ascii_letters + string.digits + '!@#%^&*()_+-={}[]|,.<>?~') for _ in range(16))

    user = User.objects.create(name=username, password=_encrypt_password(password=password, salt=salt), auth_token=uuid.uuid4(), login_token=_generate_login_token())
    user.obfuscated_id = utility.obfuscate_id(user.id)
    user.save()

    # Create bank account for user
    bank_account = Bank.objects.create(user_id=user.obfuscated_id, stars=config.DEFAULT_STARS)

    # Create score for user
    score_account = Score.objects.create(user_id=user.obfuscated_id, points=0)

    # New user should not have friends or games
    friends = []
    games = []

    return LoginUser(username=username, user_id=user.obfuscated_id, auth_token=user.get_auth_token(), login_token=user.login_token, friends=friends, bank_account=bank_account, score=score_account)

def login(username, password, client_version=1, device_id=None):
    """
    API Function to login a user using password
    """
    if username is None or password is None or username == '' or password == '':
        raise RemoteException('Username and password cannot be blank.')

    user = None

    try:
        user = User.objects.get(name=username)
    except User.DoesNotExist:
        raise RemoteException('Username password combination not valid.')

    if user is None:
        raise RemoteException('Username password combination not valid.')

    if not check_password(password=password, encoded=user.password):
        raise RemoteException('Username password combination not valid.')

    # Get user bank account
    bank_account = bank.get_user_bank(user_id=user.obfuscated_id)

    # Get user score
    score_account = score.get_user_score(user_id=user.obfuscated_id)

    # If no login token, create one
    if user.login_token is None:
        user.login_token = _generate_login_token()

    # Create new auth token
    auth_token = uuid.uuid4()
    user.auth_token = auth_token
    user.save()

    friends = friend.get_user_friends(user_id=user.obfuscated_id).friends
    games = game.get_user_games(user_id=user.obfuscated_id).games

    return LoginUser(username=username, user_id=user.obfuscated_id, auth_token=auth_token, login_token=user.login_token, friends=friends, bank_account=bank_account, score=score_account)

def update_password(user_id, old_password, new_password):
    """
    API Function to change a user's password
    """
    user = None

    try:
        user = User.objects.get(obfuscated_id=user_id)
    except User.DoesNotExist:
        raise RemoteException('Username password combination not valid.')

    if user is None:
        raise RemoteException('Username password combination not valid.')

    if not check_password(password=old_password, encoded=user.password):
        raise RemoteException('Username password combination not valid.')

    salt = ''.join(random.choice(string.ascii_letters + string.digits + '!@#%^&*()_+-={}[]|,.<>?~') for _ in range(16))

    user.password = _encrypt_password(password=new_password, salt=salt)
    user.login_token = _generate_login_token()
    user.save()

    return SuccessPacket()

def _encrypt_password(password, salt):
    return make_password(password=password, salt=salt, hasher='sha1')

def _generate_login_token():
    return ''.join(random.choice(string.ascii_letters + string.digits + '+/') for _ in range(128))
