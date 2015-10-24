from models import Game, User

from interface.exception import RemoteException
from interface.user import Game as CurrentGame

import string
import utility

# Game api

def start_new_game(user_id, friend_id):
	"""
	Create a new Game
	"""
	if user_id is None or friend_id is None:
		return RemoteException('User ID and friend ID cannot be blank.')

	if user_id == friend_id:
		return RemoteException('Cannot start a game with yourself.')

	game = None

	try:
		user = User.objects.get(id=user_id)
	except User.DoesNotExist:
		return RemoteException("User 1 doesn't exist")

	try:
		friend = User.objects.get(id=friend_id)
	except User.DoesNotExist:
		return RemoteException("User 2 doesn't exist")

	game = Game.objects.create(user_id1=user_id, user_id2=friend_id, active=True, curr_round=1)
	game.save()

	return CurrentGame(user_id=user_id, friend_id=friend_id, active=True, curr_round=1)

