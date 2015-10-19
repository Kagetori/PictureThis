import json

# RemoteObject class

class RemoteObject():
    """
    RemoteObjects that serialize to JSON
    """

    def __str__(self):
        return json.dumps(self.__dict__)

    __repr__ = __str__
