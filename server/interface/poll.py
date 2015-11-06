from remote_object import RemoteObject

class Poll(RemoteObject):
    def __init__(self, user_id, friend_id, friend_username, active_game, is_turn, is_photographer):
        """
        user_id
            user's id
        friend_id
            friend's user id
        friend_username
            friend's username
        active_game
            if True: currently an active game between 
        is_turn
            if True: currently user's turn
        is_photographer
            if True: user is the photographer for this turn
        """
        self.user_id = user_id
        self.friend_id = friend_id
        self.friend_username = friend_username
        self.active_game = active_game
        self.is_turn = is_turn
        self.is_photographer = is_photographer
