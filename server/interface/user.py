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
        """
        User.__init__(self, username, user_id)

class LoginUser(User):
    def __init__(self, username, user_id, auth_token, friends):
        """
        username
            username of user
        user_id
            user's id
        auth_token
            user's authentication token
        friends
            list of user's friends
        """
        User.__init__(self, username=username, user_id=user_id)
        self.auth_token = auth_token
        self.friends = friends

class Game(RemoteObject):
    def __init__(self, user_id, friend_id, active, curr_round):
        """
        user_id
            user's id
        friend_id
            friend's id
        active
            is game active?
        curr_round
            number of rounds played
        """
        self.user_id = user_id
        self.friend_id = friend_id
        self.active = active
        self.curr_round = curr_round