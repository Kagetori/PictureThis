from remote_object import RemoteObject

# Exceptions

class RemoteException(RemoteObject):
    def __init__(self, text):
        """
        text
            Description of exception
        """
        self.text = text
