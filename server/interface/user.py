from remote_object import RemoteObject

class LoginUser(RemoteObject):
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
        self.username =  username
        self.user_id = user_id
        self.auth_token = auth_token
        self.friends = friends

