from remote_object import RemoteObject

# Exceptions

class RemoteException(RemoteObject):
    def __init__(self, exception, force_logout=False):
        """
        exception:
            Description of exception
        force_logout:
            Whether the client should be forced to log out
        """
        self.exception = exception
        self.force_logout = force_logout

class NotAuthenticatedException(RemoteException):
    """
    Exception specifying that the call is not authenticated

    exception:
        Description of exception
    """
    def __init__(self, exception):
        RemoteException.__init__(self, exception, True)
