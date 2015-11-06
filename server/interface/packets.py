from remote_object import RemoteObject

class SuccessPacket(RemoteObject):
    def __init__(self):
        return

class FriendPacket(SuccessPacket):
    def __init__(self, friends):
        """
        friends
            List of User objects
        """
        self.friends = friends

class GamePacket(SuccessPacket):
    def __init__(self, games):
        """
        games
            List of Game objects
        """
        self.games = games

class PollPacket(SuccessPacket):
    def __init__(self, polls):
        """
        polls
            List of Poll objects
        """
        self.polls = polls