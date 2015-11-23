from remote_object import RemoteObject

class Image(RemoteObject):
    def __init__(self, dataURL):
        """
        dataURL
            data URL of image
        """
        self.dataURL = dataURL
