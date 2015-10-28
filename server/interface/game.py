from remote_object import RemoteObject

class Game(RemoteObject):
    def __init__(self, game_id, user_id, friend_id, active, curr_round, words_seen, curr_word):
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
        """
        self.game_id = game_id
        self.user_id = user_id
        self.friend_id = friend_id
        self.active = active
        self.curr_round = curr_round
        self.words_seen = words_seen
        self.curr_word = curr_word
