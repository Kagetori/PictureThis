from remote_object import RemoteObject

class FriendPacket(RemoteObject):
    def __init__(self, friends):
        """
        friends
            List of User objects
        """
        self.friends = friends