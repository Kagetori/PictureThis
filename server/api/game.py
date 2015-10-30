from models import Game, User, Turn, WordPrompt

from interface.exception import RemoteException
from interface.game import Game as RemoteGame
from interface.success import SuccessPacket
from interface.packets import GamePacket

import string
import config, utility

# Game api

def start_new_game(user_id, friend_id):
    """
    Create a new Game
    """
    if user_id is None or friend_id is None:
        raise RemoteException('User ID and friend ID cannot be blank.')

    if user_id == friend_id:
        raise RemoteException('Cannot start a game with yourself.')

    game = None

    try:
        user = User.objects.get(obfuscated_id=user_id)
    except User.DoesNotExist:
        raise RemoteException("User 1 doesn't exist")

    try:
        friend = User.objects.get(obfuscated_id=friend_id)
    except User.DoesNotExist:
        raise RemoteException("User 2 doesn't exist")

    if (_is_active_game(user_id1=user_id, user_id2=friend_id)):
        raise RemoteException("Game already exists")

    game = Game.objects.create(user_id1=user_id, user_id2=friend_id, active=True, curr_round=0)
    game.save()

    game_id = Game.objects.get(user_id1=user_id, user_id2=friend_id, active=True).id

    return start_new_round(user_id=user_id, game_id=game_id)

def start_new_round(user_id, game_id):
    """
    Starts a new round by giving the user a new word prompt 
    Only the photographer can start a new round
    """
    if user_id is None or game_id is None:
        raise RemoteException('User ID and game ID cannot be blank.')
    try:
        user = User.objects.get(obfuscated_id=user_id)
    except User.DoesNotExist:
        raise RemoteException("User does not exist")
    try:
        game = Game.objects.get(id=game_id)
    except Game.DoesNotExist:
        raise RemoteException("Game does not exist")

    friend_id = _get_friend_id(user_model=user, game_model=game)
    if (friend_id is None):
        raise RemoteException('User ID and game ID combination not valid') 

    if (game.active == False):
        raise RemoteException("Game is inactive")

    if (game.curr_round >= game.max_rounds):
        raise RemoteException("Max number of rounds reached")

    # Check if user is photographer of PREVIOUS round
    if (int(user_id) == _get_curr_photographer(game_model=game)):
        raise RemoteException("This user can't start a new round")

    words_seen = _get_words_played(game_id)
    
    new_word = _get_random_word()
    while (new_word.word in words_seen):
        new_word = _get_random_word()

    round_num = game.curr_round + 1

    turn = Turn.objects.create(turn_num=round_num, game=game, word_prompt=new_word)
    turn.save()

    game.curr_round = round_num
    game.save()
    return RemoteGame(game_id=game_id, user_id=user_id, friend_id=friend_id, active=True, curr_round=round_num, words_seen=words_seen, curr_word=new_word.word, is_photographer=True, is_turn=True)

def send_picture(user_id, game_id):
    """
    Marks a picture as sent
    """
    if user_id is None or game_id is None:
        raise RemoteException('User ID and game ID cannot be blank.')

    try:
        user = User.objects.get(obfuscated_id=user_id)
    except User.DoesNotExist:
        raise RemoteException("User does not exist")

    friend_id = _get_friend_id(user_model=user, game_model=game)
    if (friend_id is None):
        raise RemoteException('User ID and game ID combination not valid') 

    game = None

    try:
        game = Game.objects.get(id=game_id)
    except Game.DoesNotExist:
        raise RemoteException("Game does not exist")

    if game is None or game.active is False:
        raise RemoteException("Game is inactive")

    round_num = game.curr_round

    try:
        turn = Turn.objects.get(turn_num=round_num, game=game)

        turn.picture_added = True
        # TODO add picture URLs later
        turn.save()

        return _get_remote_game(user_id=user_id, friend_id=friend_id, game_id=game_id)

    except Turn.DoesNotExist:
        raise RemoteException("Invalid turn")

def end_game(user_id, game_id):
    """
    Ends a pre-existing game by setting it to inactive
    """
    if user_id is None or game_id is None:
        raise RemoteException('User ID and game ID cannot be blank.')
    try:
        user = User.objects.get(obfuscated_id=user_id)
    except User.DoesNotExist:
        raise RemoteException("User does not exist")
    try:
        game = Game.objects.get(id=game_id)
    except Game.DoesNotExist:
        raise RemoteException("Game does not exist")

    if (game.active == False):
        raise RemoteException("Game is already inactive")

    friend_id = _get_friend_id(user_model=user, game_model=game)
    if (friend_id is None):
        raise RemoteException('User ID and game ID combination not valid') 

    words_seen = _get_words_played(game_id)
    game.active = False
    game.save()
    return RemoteGame(game_id=game_id, user_id=user_id, friend_id=friend_id, active=False, curr_round=game.curr_round, words_seen=words_seen, curr_word=None, is_photographer=None, is_turn=None)

def validate_guess(user_id, game_id, guess):
    """
    Checks if guess is correct. Return a sucess packet if guess matches latest word prompt
    """
    game = None

    if user_id is None or game_id is None:
        raise RemoteException('User ID and game ID cannot be blank.')

    try:
        user = User.objects.get(obfuscated_id=user_id)
    except User.DoesNotExist:
        raise RemoteException("User does not exist")

    try:
        game = Game.objects.get(id=game_id)
    except Game.DoesNotExist:
        raise RemoteException("Game does not exist")

    try:
        current_turn = Turn.objects.get(turn_num=game.curr_round, game=game)
    except Turn.DoesNotExist:
        raise RemoteException("Turn does not exist")

    friend_id = _get_friend_id(user_model=user, game_model=game)
    if (friend_id is None):
        raise RemoteException('User ID and game ID combination not valid') 

    is_photographer = int(user_id) == _get_curr_photographer(game)

    if is_photographer:
        raise RemoteException("Not this user's turn to guess")

    current_word = current_turn.word_prompt.word
    if (guess.strip() == current_word):

        current_turn.guessed = True
        current_turn.save()

        if game.curr_round == game.max_rounds:
            return end_game(user_id, game_id)
        else:
            return start_new_round(user_id=user_id, game_id=game_id)
    else:
        raise RemoteException("Guess is incorrect")

def get_user_games(user_id):
    """
    Returns all the user's active games
    """
    if user_id is None:
        raise RemoteException('User ID cannot be blank')
    try:
         user = User.objects.get(obfuscated_id=user_id)
    except User.DoesNotExist:
        raise RemoteException("User does not exist")

    games1 = Game.objects.filter(user_id1=user_id, active=True) 
    games2 = Game.objects.filter(user_id2=user_id, active=True)

    result = []

    for g in games1:
        game_friend_id = g.user_id2

        result.append(_get_remote_game(user_id=user_id, friend_id=game_friend_id, game_model=g))

    for g in games2:
        game_friend_id = g.user_id1

        result.append(_get_remote_game(user_id=user_id, friend_id=game_friend_id, game_model=g))

    return GamePacket(result)

# Helper functions

def _get_words_played(game_model):

    turns = Turn.objects.filter(game=game_model).order_by('turn_num')

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
    else:
        photographer_id = game_model.user_id2
    return int(photographer_id)

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
        raise RemoteException('Not a player in this game.')

def _is_active_game(user_id1, user_id2):
    games1 = Game.objects.filter(user_id1=user_id1, user_id2=user_id2, active=True) 
    games2 = Game.objects.filter(user_id1=user_id2, user_id2=user_id1, active=True)
    if (games1.count() + games2.count() > 0):
        return True
    else:
        return False

def _get_remote_game(user_id, friend_id, game_model):
    curr_round = game_model.curr_round
    game_id = game_model.id
    active = game_model.active
    is_photographer = (_get_curr_photographer(game_model) == int(user_id))

    words_seen = []
    curr_word = None
    words_played = _get_words_played(game_model)

    try:
        current_turn = Turn.objects.get(turn_num=game_model.curr_round, game=game_model)

        is_turn = (is_photographer != current_turn.picture_added)

        if (len(words_played) > 0):
            words_seen = words_played[:-1]
            curr_word = words_played[-1]
            
        return RemoteGame(game_id=game_id, user_id=user_id, friend_id=friend_id, active=active, curr_round=curr_round, words_seen=words_seen, curr_word=curr_word, is_photographer=is_photographer, is_turn=is_turn)

    except Turn.DoesNotExist:
        raise RemoteException("Turn does not exist")

# WARNING: THE FOLLOWING ARE DEBUGGING FUNCTIONS ONLY
# EXTERNAL APIs SHOULD NOT HAVE ACCECSS TO THESE
def _end_all_games():
    games = Game.objects.filter(active=True)

    for game in games:
        end_game(user_id=game.user_id1, game_id=game.id)
