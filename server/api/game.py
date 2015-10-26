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

	return LocalGame(user_id=user_id, friend_id=friend_id, active=True, curr_round=1, words_seen=[], curr_word=None)

def start_new_round(user_id, game_id):
	"""
	Starts a new round by giving the user a new word prompt 
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

	if (game.active == False):
		return RemoteException("Game is inactive")

	if (game.curr_round >= game.max_rounds):
		return RemoteException("Max number of rounds reached")

	words_seen = get_words_played(game_id)

	new_word = WordPrompt.objects.order_by('?').first() # can be slow
	while (new_word.word in words_seen):
	 	new_word = WordPrompt.objects.order_by('?').first()

	friend_id = None
	if (user_id == game.user_id1):
		friend_id = game.user_id2
	else:
		friend_id = game.user_id1	

	round_num = int(game.curr_round) + 1

	turn = Turn.objects.create(turn_num=round_num, game=game, word_prompt=new_word)
	turn.save()

	game.curr_round = round_num
	game.save()
	return LocalGame(user_id=user_id, friend_id=friend_id, active=True, curr_round=round_num, words_seen=words_seen, curr_word=new_word.word)

def get_words_played(game_id):

	game = Game.objects.filter(id=game_id)
	turns = Turn.objects.filter(game=game)

	words_played = []

	for t in turns:
		word = t.word_prompt.word
		words_played.append(word)
	return words_played
