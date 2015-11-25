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
    def __init__(self, username, user_id, relation):
        """
        username
            username of friend
        user_id
            friend's user id
        relation
            friend relation (e.g. friend, blocked)
        """
        User.__init__(self, username, user_id)
        self.relation = relation

class LoginUser(User):
    def __init__(self, username, user_id, auth_token, friends, games, stars, points):
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
        points
            number of points the user has
        """
        User.__init__(self, username=username, user_id=user_id)
        self.auth_token = auth_token
        self.friends = friends
        self.games = games
        self.stars = stars
        self.points = points
