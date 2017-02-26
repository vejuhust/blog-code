
from uuid import uuid1
from basehash import base62


def generate_short_id():
    """ Short ID generator - v0: Base62 Encoded UUID1 """
    return base62().encode(uuid1().int)


def convert_short_id(num):
    """ Short ID converter - v0: Base62 Encoded UUID1 """
    return base62().encode(num)


def generate_short_id_raw():
    """ Short ID generator - v0 - without any encoding """
    return uuid1().int
