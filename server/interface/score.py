from remote_object import RemoteObject

class Score(RemoteObject):
    def __init__(self, points):
        """
        points
            Number of points the user has
        """
        self.points =  points
