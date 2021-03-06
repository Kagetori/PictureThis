from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils import timezone
from django.utils.timesince import timesince

from models import Game, User, Turn, WordPrompt

import bank, friend, score

from interface.exception import RemoteException
from interface.game import Game as RemoteGame
from interface.packets import GamePacket, SuccessPacket
from interface.image import Image as RemoteImage

import base64
import string
import config, utility
import os.path

# Game api

def start_new_game(user_id, friend_id):
    """
    Create a new Game
    """
    if user_id is 0 or friend_id is 0:
        raise RemoteException('User ID and friend ID cannot be blank.')

    if user_id == friend_id:
        raise RemoteException('Cannot start a game with yourself.')

    game = None

    try:
        user = User.objects.get(obfuscated_id=user_id)
    except User.DoesNotExist:
        raise RemoteException('User 1 does not exist')

    try:
        User.objects.get(obfuscated_id=friend_id)
    except User.DoesNotExist:
        raise RemoteException('User 2 does not exist')

    if (friend.get_friend_status(user_id1=user_id, user_id2=friend_id) != config.FRIEND_STATUS_FRIEND or
            friend.get_friend_status(user_id1=friend_id, user_id2=user_id) != config.FRIEND_STATUS_FRIEND):
        raise RemoteException('Unable to start a game with someone who is not a friend')

    if (_is_active_game(user_id1=user_id, user_id2=friend_id)):
        raise RemoteException('Game already exists')

    game = Game.objects.create(user_id1=user_id, user_id2=friend_id, active=True, curr_round=0, max_rounds=config.MAX_ROUNDS)

    game_id = game.id

    return _start_new_round(user_id=user_id, game_id=game_id)

def send_picture(user_id, game_id, photo):
    """
    Marks a picture as sent
    """
    if user_id is 0 or game_id is 0:
        raise RemoteException('User ID and game ID cannot be blank.')

    if photo is None:
        raise RemoteException('You have to send a photo')

    try:
        user = User.objects.get(obfuscated_id=user_id)
    except User.DoesNotExist:
        raise RemoteException('User does not exist')

    game = None

    try:
        game = Game.objects.get(id=game_id)
    except Game.DoesNotExist:
        raise RemoteException('Game does not exist')

    if game is None or game.active is False:
        raise RemoteException('Game is inactive')

    if _get_curr_photographer(game) != int(user_id):
        raise RemoteException('Not your turn to send a picture')

    friend_id = _get_friend_id(user_model=user, game_model=game)
    if (friend_id is None):
        raise RemoteException('User ID and game ID combination not valid') 

    round_num = game.curr_round

    try:
        turn = Turn.objects.get(turn_num=round_num, game_id=game_id)

        turn.picture_added = True
        turn.save()

        file_photo = _decode_64_to_file(photo)

        # save photo
        with open(config.FILE_PATH + ('%s_%s.jpg' % (str(game_id), str(round_num))), 'wb+') as dest:
            for chunk in file_photo.chunks():
                dest.write(chunk)

        return _get_remote_game(user_id=user_id, friend_id=friend_id, game_model=game)

    except Turn.DoesNotExist:
        raise RemoteException('Invalid turn')

def get_picture(user_id, game_id):
    """
    Gets a picture for the specified user_id and game_id
    """

    if user_id is 0 or game_id is 0:
        raise RemoteException('User ID and game ID cannot be blank.')

    try:
        user = User.objects.get(obfuscated_id=user_id)
    except User.DoesNotExist:
        raise RemoteException('User does not exist')

    game = None

    try:
        game = Game.objects.get(id=game_id)
    except Game.DoesNotExist:
        raise RemoteException('Game does not exist')

    if game is None or game.active is False:
        raise RemoteException('Game is inactive')

    friend_id = _get_friend_id(user_model=user, game_model=game)
    if (friend_id is None):
        raise RemoteException('User ID and game ID combination not valid') 

    is_photographer = int(user_id) == _get_curr_photographer(game)

    if is_photographer:
        raise RemoteException('Not your turn to get the picture')

    round_num = game.curr_round

    try:
        turn = Turn.objects.get(turn_num=round_num, game_id=game_id)

        if not turn.picture_added:
            raise RemoteException('Picture not sent yet')

        curr_time = timezone.now()

        if not turn.picture_seen:
            turn.picture_seen = True
            turn.picture_seen_date = curr_time
            turn.save()

        current_score = _calculate_score(curr_time - turn.picture_seen_date)

        filename = config.FILE_PATH + ('%s_%s.jpg' % (str(game_id), str(round_num)))

        if os.path.isfile(filename):
            with open(filename, 'rb') as f:
                return RemoteImage(dataURL=_encode_file_to_64(f), current_score=current_score)
        else:
            raise RemoteException('Cannot find image')

    except Turn.DoesNotExist:
        raise RemoteException('Invalid turn')

def end_game(user_id, game_id, award_stars=True):
    """
    Ends a pre-existing game by setting it to inactive
    """
    if user_id is 0 or game_id is 0:
        raise RemoteException('User ID and game ID cannot be blank.')
    try:
        user = User.objects.get(obfuscated_id=user_id)
    except User.DoesNotExist:
        raise RemoteException('User does not exist')
    try:
        game = Game.objects.get(id=game_id)
    except Game.DoesNotExist:
        raise RemoteException('Game does not exist')

    if (game.active == False):
        raise RemoteException('Game is already inactive')

    friend_id = _get_friend_id(user_model=user, game_model=game)
    if (friend_id is None):
        raise RemoteException('User ID and game ID combination not valid') 

    words_seen = _get_words_played(game_id=game_id)
    game.active = False
    game.save()

    # Remove picture if exists
    filename = config.FILE_PATH + ('%s_%s.jpg' % (str(game_id), str(game.curr_round)))

    if os.path.isfile(filename):
        os.remove(filename)

    if award_stars:
        # Award stars to users
        user1_stars = int(game.user1_score / config.SCORE_PER_STAR)
        user2_stars = int(game.user2_score / config.SCORE_PER_STAR)

        if game.user1_score > game.user2_score:
            user1_stars += config.WINNER_BONUS_STAR
        elif game.user1_score < game.user2_score:
            user2_stars += config.WINNER_BONUS_STAR
        else:
            user1_stars += config.TIE_BONUS_STAR
            user2_stars += config.TIE_BONUS_STAR

        bank.add_to_bank(user_id=game.user_id1, stars=user1_stars)
        bank.add_to_bank(user_id=game.user_id2, stars=user2_stars)

        # Award points to users also
        score.add_to_score(user_id=game.user_id1, points=game.user1_score)
        score.add_to_score(user_id=game.user_id2, points=game.user2_score)

    friend_score = 0
    user_score = 0

    if game.user_id1 == user_id:
        user_score = game.user1_score
        friend_score = game.user2_score
    else:
        user_score = game.user2_score
        friend_score = game.user1_score

    return RemoteGame(game_id=game_id, user_id=user_id, friend_id=friend_id, active=False, user_score=user_score, friend_score=friend_score,
        curr_round=game.curr_round, words_seen=words_seen, bank_account=bank.get_user_bank(user_id=user_id))

def validate_guess(user_id, game_id, guess, score):
    """
    Checks if guess is correct.
    """
    game = None
    curr_time = timezone.now()

    if user_id is 0 or game_id is 0:
        raise RemoteException('User ID and game ID cannot be blank.')

    try:
        user = User.objects.get(obfuscated_id=user_id)
    except User.DoesNotExist:
        raise RemoteException('User does not exist')

    try:
        game = Game.objects.get(id=game_id)
    except Game.DoesNotExist:
        raise RemoteException('Game does not exist')

    try:
        current_turn = Turn.objects.get(turn_num=game.curr_round, game_id=game_id)
    except Turn.DoesNotExist:
        raise RemoteException('Turn does not exist')

    if not current_turn.picture_seen:
        raise RemoteException('Have not seen picture yet.')

    friend_id = _get_friend_id(user_model=user, game_model=game)
    if (friend_id is None):
        raise RemoteException('User ID and game ID combination not valid') 

    is_photographer = int(user_id) == _get_curr_photographer(game)

    if is_photographer:
        raise RemoteException('Not your turn to guess')

    current_word_id = current_turn.word_prompt_id
    try:
        current_word = WordPrompt.objects.get(id=current_word_id).word
    except WordPrompt.DoesNotExist:
        raise RemoteException('Word does not exist.')

    if (guess.strip().lower() == current_word.lower()):

        current_turn.guessed = True
        current_turn.guessed_correctly = True
        current_turn.save()

        # Add points to users
        elapsed_time = curr_time - current_turn.picture_seen_date
        guesser_score = _calculate_score(elapsed_time)

        score = int(score)

        if score - guesser_score < config.SCORE_DELTA:
            guesser_score = score

        ## OTHERWISE, we need to somehow warn user?

        sender_score = config.SCORE_SENDING

        if user_id == game.user_id1:
            game.user1_score += guesser_score
            game.user2_score += sender_score
        else:
            game.user2_score += guesser_score
            game.user1_score += sender_score

        game.save()

        round_num = game.curr_round

        filename = config.FILE_PATH + ('%s_%s.jpg' % (str(game_id), str(round_num)))

        if os.path.isfile(filename):
            os.remove(filename)

        if round_num == game.max_rounds:
            return end_game(user_id, game_id)
        else:
            return _start_new_round(user_id=user_id, game_id=game_id)
    else:
        raise RemoteException('Guess is incorrect')

def give_up_turn(user_id, game_id):
    """
    Give up on the current turn
    """
    game = None
    curr_time = timezone.now()

    if user_id is 0 or game_id is 0:
        raise RemoteException('User ID and game ID cannot be blank.')

    try:
        user = User.objects.get(obfuscated_id=user_id)
    except User.DoesNotExist:
        raise RemoteException('User does not exist')

    try:
        game = Game.objects.get(id=game_id)
    except Game.DoesNotExist:
        raise RemoteException('Game does not exist')

    try:
        current_turn = Turn.objects.get(turn_num=game.curr_round, game_id=game_id)
    except Turn.DoesNotExist:
        raise RemoteException('Turn does not exist')

    if not current_turn.picture_seen:
        raise RemoteException('Have not seen picture yet.')

    friend_id = _get_friend_id(user_model=user, game_model=game)
    if (friend_id is None):
        raise RemoteException('User ID and game ID combination not valid') 

    is_photographer = int(user_id) == _get_curr_photographer(game)

    if is_photographer:
        raise RemoteException('Not your turn to guess')

    current_turn.guessed = True
    current_turn.guessed_correctly = False
    current_turn.save()

    # Don't add points since users don't get points

    round_num = game.curr_round

    filename = config.FILE_PATH + ('%s_%s.jpg' % (str(game_id), str(round_num)))

    if os.path.isfile(filename):
        os.remove(filename)

    if round_num == game.max_rounds:
        return end_game(user_id, game_id)
    else:
        return _start_new_round(user_id=user_id, game_id=game_id)

def get_user_games(user_id):
    """
    Returns all the user's active games
    """
    if user_id is 0:
        raise RemoteException('User ID cannot be blank')
    try:
         User.objects.get(obfuscated_id=user_id)
    except User.DoesNotExist:
        raise RemoteException('User does not exist')

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

def get_game_status(user_id, friend_id):
    """
    Returns the most recent game
    """
    if user_id is 0 or friend_id is 0:
        raise RemoteException('User ID and Friend ID cannot be blank')
    try:
         User.objects.get(obfuscated_id=user_id)
         User.objects.get(obfuscated_id=friend_id)
    except User.DoesNotExist:
        raise RemoteException('User does not exist')

    games1 = Game.objects.filter(user_id1=user_id, user_id2=friend_id).order_by('-id')
    games2 = Game.objects.filter(user_id2=user_id, user_id1=friend_id).order_by('-id')

    most_recent_game = None

    if len(games1) > 0:
        game_1 = games1[0]
        if len(games2) > 0:
            game_2 = games2[0]
            # Both are not empty, choose bigger id
            if game_1.id > game_2.id:
                most_recent_game = game_1
            else:
                most_recent_game = game_2
        else:
            most_recent_game = game_1
    elif len(games2) > 0:
        most_recent_game = games2[0]

    if most_recent_game is None:
        raise RemoteException('No game between the users')

    return _get_remote_game(user_id=user_id, friend_id=friend_id, game_model=most_recent_game)

def get_new_word(user_id, game_id):
    """
    Get new word prompt
    """
    try:
        user = User.objects.get(obfuscated_id=user_id)
    except User.DoesNotExist:
        raise RemoteException('User does not exist')
    try:
        game = Game.objects.get(id=game_id)
    except Game.DoesNotExist:
        raise RemoteException('Game does not exist')

    friend_id = _get_friend_id(user_model=user, game_model=game)

    if friend_id is None:
        raise RemoteException('User ID and game ID combination not valid') 

    if not game.active:
        raise RemoteException('Game is inactive')

    # Remove a star
    bank.decrement_bank(user_id=user_id)

    if int(user_id) != _get_curr_photographer(game_model=game):
        raise RemoteException('This user cannot get a new word prompt')

    words_seen = _get_words_played(game_id=game_id)

    new_word = _get_random_word()
    while (new_word.word in words_seen):
        new_word = _get_random_word()

    round_num = game.curr_round

    turn = Turn.objects.get(turn_num=round_num, game_id=game_id)
    old_word = WordPrompt.objects.get(id=turn.word_prompt_id).word

    words_seen.remove(old_word)

    turn.word_prompt_id = new_word.id
    turn.save()

    words_seen.append(new_word.word)

    friend_score = 0
    user_score = 0

    if game.user_id1 == user_id:
        user_score = game.user1_score
        friend_score = game.user2_score
    else:
        user_score = game.user2_score
        friend_score = game.user1_score

    return RemoteGame(game_id=game_id, user_id=user_id, friend_id=friend_id, active=True, curr_round=round_num, user_score=user_score, friend_score=friend_score,
        words_seen=words_seen, curr_word=new_word.word, is_photographer=True, is_turn=True, bank_account=bank.get_user_bank(user_id=user_id))

# Helper functions

def _start_new_round(user_id, game_id):
    """
    Starts a new round by giving the user a new word prompt 
    Only the photographer can start a new round
    """
    try:
        user = User.objects.get(obfuscated_id=user_id)
    except User.DoesNotExist:
        raise RemoteException('User does not exist')
    try:
        game = Game.objects.get(id=game_id)
    except Game.DoesNotExist:
        raise RemoteException('Game does not exist')

    friend_id = _get_friend_id(user_model=user, game_model=game)

    if friend_id is None:
        raise RemoteException('User ID and game ID combination not valid') 

    if not game.active:
        raise RemoteException('Game is inactive')

    if game.curr_round >= game.max_rounds:
        raise RemoteException('Max number of rounds reached')

    # Check if user is photographer of PREVIOUS round
    if int(user_id) == _get_curr_photographer(game_model=game):
        raise RemoteException('This user cannot start a new round')

    words_seen = _get_words_played(game_id=game_id)
    
    new_word = _get_random_word()
    while (new_word.word in words_seen):
        new_word = _get_random_word()

    # Add the new word into the list
    words_seen.append(new_word.word)

    round_num = game.curr_round + 1

    Turn.objects.create(turn_num=round_num, game_id=game_id, word_prompt_id=new_word.id)

    game.curr_round = round_num
    game.save()

    friend_score = 0
    user_score = 0

    if game.user_id1 == user_id:
        user_score = game.user1_score
        friend_score = game.user2_score
    else:
        user_score = game.user2_score
        friend_score = game.user1_score

    return RemoteGame(game_id=game_id, user_id=user_id, friend_id=friend_id, active=True, curr_round=round_num, user_score=user_score, friend_score=friend_score,
        words_seen=words_seen, curr_word=new_word.word, is_photographer=True, is_turn=True)

def _get_words_played(game_id):
    turns = Turn.objects.filter(game_id=game_id)

    words_played = []

    for t in turns:
        word_id = t.word_prompt_id
        try:
            word = WordPrompt.objects.get(id=word_id).word
        except WordPrompt.DoesNotExist:
            raise RemoteException('Error: unable to find words')
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
    return WordPrompt.objects.filter(active=True).order_by('?').first() 

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

    words_seen = []
    curr_word = None
    words_played = _get_words_played(game_id=game_model.id)

    if (len(words_played) > 0):
        words_seen = words_played
        if active:
            curr_word = words_played[-1]

    is_photographer = None
    is_turn = None
    elapsed_time = None
    current_score = None

    friend_score = 0
    user_score = 0

    if game_model.user_id1 == user_id:
        user_score = game_model.user1_score
        friend_score = game_model.user2_score
    else:
        user_score = game_model.user2_score
        friend_score = game_model.user1_score

    if active:
        try:
            current_turn = Turn.objects.get(turn_num=game_model.curr_round, game_id=game_model.id)

            is_photographer = (_get_curr_photographer(game_model) == int(user_id))

            is_turn = (is_photographer != current_turn.picture_added)

            if is_turn and not is_photographer and current_turn.picture_seen:
                # Guessing
                elapsed_time = timezone.now() - current_turn.picture_seen_date
                current_score = _calculate_score(elapsed_time)
                elapsed_time = elapsed_time.seconds

        except Turn.DoesNotExist:
            raise RemoteException('Turn does not exist')

    return RemoteGame(game_id=game_id, user_id=user_id, friend_id=friend_id, active=active, curr_round=curr_round, user_score=user_score,
        friend_score=friend_score, words_seen=words_seen, curr_word=curr_word, is_photographer=is_photographer, is_turn=is_turn,
        current_score=current_score, elapsed_time=elapsed_time)

def _calculate_score(elapsed_time):
    milliseconds = max(0, 1000 * elapsed_time.seconds + elapsed_time.microseconds // 1000)
    if milliseconds < config.SCORE_GUESSING_TIME:
        return config.MAX_SCORE_GUESSING - int((config.MAX_SCORE_GUESSING - config.MIN_SCORE_GUESSING) * milliseconds / config.SCORE_GUESSING_TIME)
    else:
        return config.MIN_SCORE_GUESSING

def _encode_file_to_64(f):
    return 'data:image/jpeg;base64,' + base64.encodestring(f.read()).replace('\n', '')

def _decode_64_to_file(dataURL):
    return SimpleUploadedFile(name='file.jpg', content=base64.decodestring(dataURL.split(',')[1]), content_type='image/jpeg')

# WARNING: THE FOLLOWING ARE DEBUGGING FUNCTIONS ONLY
# EXTERNAL APIs SHOULD NOT HAVE ACCECSS TO THESE
def _end_all_games():
    games = Game.objects.filter(active=True)

    for game in games:
        end_game(user_id=game.user_id1, game_id=game.id, award_stars=False)

    return SuccessPacket('Success!')
