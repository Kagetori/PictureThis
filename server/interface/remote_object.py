import json

# RemoteObject class

class RemoteObject():
    """
    RemoteObjects that serialize to JSON
    """

    def __str__(self):
        return json.dumps(_get_dict(self))

    __repr__ = __str__

def _get_dict(obj):
    d = obj.__dict__

    ret = {}

    for key, value in d.iteritems():
        ret[key] = _get_obj(value)

    return ret

def _get_obj(obj):
    if isinstance(obj, list):
        arr = []

        for v in obj:
            arr.append(_get_obj(v))

        return arr

    elif isinstance(obj, RemoteObject):
        return _get_dict(obj)

    else:
        return obj