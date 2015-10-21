import json

# RemoteObject class

class RemoteObject():
    """
    RemoteObjects that serialize to JSON
    """

    def __str__(self):
        return json.dumps(self._get_dict(self))

    __repr__ = __str__

    def _get_dict(self, obj):
        d = obj.__dict__

        ret = {}

        for key, value in d.iteritems():
            if value is not None:
                ret[key] = self._get_obj(value)

        return ret

    def _get_obj(self, obj):
        if isinstance(obj, list):
            arr = []

            for v in obj:
                arr.append(self._get_obj(v))

            return arr

        elif isinstance(obj, RemoteObject):
            return self._get_dict(obj)

        else:
            return obj
