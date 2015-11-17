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
    def __init__(self, username, user_id):
        """
        username
            username of friend
        user_id
            friend's user id
        active_game
            whether or not there is an active game with the friend
        game_id
            if user has an active game, the game_id
        """
        User.__init__(self, username, user_id)

class LoginUser(User):
    def __init__(self, username, user_id, auth_token, friends, games, stars):
        """
        username
            username of user
        user_id
            user's id
        auth_token
            user's authentication token
        friends
            list of user's friends
        games
            list of user's games
        stars
            number of stars the user has
        """
        User.__init__(self, username=username, user_id=user_id)
        self.auth_token = auth_token
        self.friends = friends
        self.games = games
        self.stars = stars
