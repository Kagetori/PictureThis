from models import Game, User, Turn, WordPrompt

from interface.exception import RemoteException
from interface.game import Game as LocalGame

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
	# should also check no active game between user 1 and user 2
	game = Game.objects.create(user_id1=user_id, user_id2=friend_id, active=True, curr_round=1)
	game.save()

	return LocalGame(user_id=user_id, friend_id=friend_id, active=True, curr_round=1, words_seen=[])

def new_round(user_id, game_id):
	"""
	Starts a new round by giving user_id a new word prompt 
	"""
	if user_id is None or game_id is None:
		return RemoteException('User ID and game ID cannot be blank.')
	try:
		user = User.objects.get(id=user_id)
	except User.DoesNotExist:
		return RemoteException("User does not exist")

	try:
		game = Game.objects.get(id=game_id)
	except Game.DoesNotExist:
		return RemoteException("Game does not exist")

	if (game.active == false):
		return RemoteException("Game is inactive")
	# TODO start a new round

	