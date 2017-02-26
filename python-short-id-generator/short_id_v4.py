
from os import urandom
from struct import unpack
from basehash import base62


def generate_short_id():
    """ Short ID generator - v4: Urandom """
    return base62().encode(unpack("<Q", urandom(8))[0])


def convert_short_id(num):
    """ Short ID converter - v4: Urandom """
    return generate_short_id()


def generate_short_id_raw():
    """ Short ID generator - v4 - without any encoding """
    return unpack("<Q", urandom(8))[0]
