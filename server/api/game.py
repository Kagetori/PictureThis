from models import Game, User, Turn, WordPrompt

from interface.exception import RemoteException
from interface.game import Game as RemoteGame
from interface.success import SuccessPacket

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
        user = User.objects.get(obfuscated_id=user_id)
    except User.DoesNotExist:
        return RemoteException("User 1 doesn't exist")

    try:
        friend = User.objects.get(obfuscated_id=friend_id)
    except User.DoesNotExist:
        return RemoteException("User 2 doesn't exist")
    # TODO: check no active game already exists between user 1 and 2

    game = Game.objects.create(user_id1=user_id, user_id2=friend_id, active=True, curr_round=0)
    game.save()

    return RemoteGame(user_id=user_id, friend_id=friend_id, active=True, curr_round=0, words_seen=[], curr_word=None)

def start_new_round(user_id, game_id):
    """
    Starts a new round by giving the user a new word prompt 
    Only the photographer can start a new round
    """
    if user_id is None or game_id is None:
        return RemoteException('User ID and game ID cannot be blank.')
    try:
        user = User.objects.get(obfuscated_id=user_id)
    except User.DoesNotExist:
        return RemoteException("User does not exist")
    try:
        game = Game.objects.get(id=game_id)
    except Game.DoesNotExist:
        return RemoteException("Game does not exist")

    friend_id = _get_friend_id(user_model=user, game_model=game)
    if (friend_id is None):
        return RemoteException('User ID and game ID combination not valid') 

    if (game.active == False):
        return RemoteException("Game is inactive")

    if (game.curr_round >= game.max_rounds):
        return RemoteException("Max number of rounds reached")

    # Check if user is photographer of PREVIOUS round
    if (int(user_id) == _get_curr_photographer(game_model=game)):
        return RemoteException("This user can't start a new round")

    words_seen = _get_words_played(game_id)
    
    new_word = _get_random_word()
    while (new_word.word in words_seen):
        new_word = _get_random_word()

    round_num = game.curr_round + 1

    turn = Turn.objects.create(turn_num=round_num, game=game, word_prompt=new_word)
    turn.save()

    game.curr_round = round_num
    game.save()
    return RemoteGame(user_id=user_id, friend_id=friend_id, active=True, curr_round=round_num, words_seen=words_seen, curr_word=new_word.word)

def end_game(user_id, game_id):
    """
    Ends a pre-existing game by setting it to inactive
    """
    if user_id is None or game_id is None:
        return RemoteException('User ID and game ID cannot be blank.')
    try:
        user = User.objects.get(obfuscated_id=user_id)
    except User.DoesNotExist:
        return RemoteException("User does not exist")
    try:
        game = Game.objects.get(id=game_id)
    except Game.DoesNotExist:
        return RemoteException("Game does not exist")

    if (game.active == False):
        return RemoteException("Game is already inactive")

    friend_id = _get_friend_id(user_model=user, game_model=game)
    if (friend_id is None):
        return RemoteException('User ID and game ID combination not valid') 

    words_seen = _get_words_played(game_id)
    game.active = False
    game.save()
    return RemoteGame(user_id=user_id, friend_id=friend_id, active=False, curr_round=game.curr_round, words_seen=words_seen, curr_word=None)

def validate_guess(user_id, game_id, guess):
    """
    Checks if guess is correct. Return a sucess packet if guess matches latest word prompt
    """
    if user_id is None or game_id is None:
        return RemoteException('User ID and game ID cannot be blank.')
    try:
        user = User.objects.get(obfuscated_id=user_id)
    except User.DoesNotExist:
        return RemoteException("User does not exist")
    try:
        game = Game.objects.get(id=game_id)
    except Game.DoesNotExist:
        return RemoteException("Game does not exist")
    try:
        current_turn = Turn.objects.get(turn_num=game.curr_round, game=game)
    except Turn.DoesNotExist:
        return RemoteException("Turn does not exist")

    friend_id = _get_friend_id(user_model=user, game_model=game)
    if (friend_id is None):
        return RemoteException('User ID and game ID combination not valid') 

    if (int(user_id) == _get_curr_photographer(game)):
        return RemoteException("Not this user's turn to guess")

    current_word = current_turn.word_prompt.word
    if (guess.strip() == current_word):
        return SuccessPacket()
    else:
        return RemoteException("Guess is incorrect")

# Helper functions

def _get_words_played(game_model):

    turns = Turn.objects.filter(game=game_model)

    words_played = []

    for t in turns:
        word = t.word_prompt.word
        words_played.append(word)
    return words_played

def _get_curr_photographer(game_model):
    """
    Returns the id of the user who is the photographer for the current round
    For a new game, photographer is set to the user who DIDN'T initiate the game
    """
    curr_round = game_model.curr_round
    photographer_id = None
    if (curr_round % 2 == 1):
        photographer_id = game_model.user_id1
    elif (curr_round % 2 == 0):
        photographer_id = game_model.user_id2
    return photographer_id

def _get_random_word():
    """
    Returns a random word from the database
    """
    # TODO: find a more efficent method to grab random object
    return WordPrompt.objects.order_by('?').first() 

def _get_friend_id(user_model, game_model):
    user_id = user_model.obfuscated_id
    if (user_id == game_model.user_id1):
        return game_model.user_id2
    elif (user_id == game_model.user_id2):
        return game_model.user_id1
    else:
        return None
