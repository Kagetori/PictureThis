from remote_object import RemoteObject

class SuccessPacket(RemoteObject):
    def __init__(self):
        return

class FriendPacket(SuccessPacket):
    def __init__(self, friends):
        """
        friends
            List of FriendUser objects
        """
        self.friends = friends

class GamePacket(SuccessPacket):
    def __init__(self, games):
        """
        games
            List of Game objects
        """
        self.games = games
