from remote_object import RemoteObject

class Poll(RemoteObject):
    def __init__(self, friends, bank_account, score):
        """
        friends
            List of FriendUser objects
        bank_account
            User's bank account
        points
            User's points
        """
        self.friends = friends
        self.bank_account = bank_account
        self.score = score
