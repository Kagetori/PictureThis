from remote_object import RemoteObject

class Game(RemoteObject):
    def __init__(self, game_id, user_id, friend_id, active, curr_round, user_score, friend_score, words_seen, curr_word=None, is_photographer=None,
            is_turn=None, current_score=None, elapsed_time=None, bank_account=None):
        """
        game_id
            the game id
        user_id
            user's id
        friend_id
            friend's id
        active
            is game active?
        curr_round
            number of rounds played
        user_score
            total score of the user so far in the game
        friend_score
            total score of the friend so far in the game
        words_seen
            the words seen
        curr_word
            the current word
        is_photographer
            if True: user is the photographer for this round
        is_turn
            if True: currently the user's turn in this round
        current_score
            current score of the round
        elapsed_time
            time elapsed in the round
        bank_account
            bank account of user, if any
        """
        self.game_id = game_id
        self.user_id = user_id
        self.friend_id = friend_id
        self.active = active
        self.curr_round = curr_round
        self.user_score = user_score
        self.friend_score = friend_score
        self.words_seen = words_seen
        self.curr_word = curr_word
        self.is_photographer = is_photographer
        self.is_turn = is_turn
        self.current_score = current_score
        self.elapsed_time = elapsed_time
        self.bank_account = bank_account
