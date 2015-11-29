from remote_object import RemoteObject

class SuccessPacket(RemoteObject):
    def __init__(self, text=None):
        """
        text
            text to be displayed, if any
        """
        self.text = text

class FriendPacket(SuccessPacket):
    def __init__(self, friends):
        """
        friends
            List of FriendUser objects
        """
        SuccessPacket.__init__(self, text=None)
        self.friends = friends

class GamePacket(SuccessPacket):
    def __init__(self, games):
        """
        games
            List of Game objects
        """
        SuccessPacket.__init__(self, text=None)
        self.games = games
