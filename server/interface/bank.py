from remote_object import RemoteObject

class Bank(RemoteObject):
    def __init__(self, stars):
        """
        stars
            Number of stars the user has
        user_id
            user's id
        """
        self.stars =  stars
