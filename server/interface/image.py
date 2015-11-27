from remote_object import RemoteObject

class Image(RemoteObject):
    def __init__(self, dataURL, current_score):
        """
        dataURL
            data URL of image
        current_score
            current score of the user
        """
        self.dataURL = dataURL
        self.current_score = current_score
