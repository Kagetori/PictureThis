from remote_object import RemoteObject

# Exceptions

class RemoteException(RemoteObject):
    def __init__(self, exception):
        """
        exception
            Description of exception
        """
        self.exception = exception
