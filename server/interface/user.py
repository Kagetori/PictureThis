from remote_object import RemoteObject

class User(RemoteObject):
    def __init__(self, username, user_id):
        """
        username
            username of user
        user_id
            user's id
        """
        self.username =  username
        self.user_id = user_id

class FriendUser(User):
    def __init__(self, username, user_id, relation, has_active_game=None, is_turn=None, is_photographer=None):
        """
        username
            username of friend
        user_id
            friend's user id
        relation
            friend relation (e.g. friend, blocked)
        has_active_game
            if True: currently an active game between 
        is_turn
            if True: currently user's turn
        is_photographer
            if True: user is the photographer for this turn
        """
        User.__init__(self, username, user_id)
        self.relation = relation
        self.has_active_game = has_active_game
        self.is_turn = is_turn
        self.is_photographer = is_photographer

class LoginUser(User):
    def __init__(self, username, user_id, auth_token, login_token, friends, bank_account, score):
        """
        username
            username of user
        user_id
            user's id
        auth_token
            user's authentication token
        login_token
            user's login token
        friends
            list of user's friends
        bank_account
            user's bank account
        score
            user's score
        """
        User.__init__(self, username=username, user_id=user_id)
        self.auth_token = auth_token
        self.login_token = login_token
        self.friends = friends
        self.bank_account = bank_account
        self.score = score
