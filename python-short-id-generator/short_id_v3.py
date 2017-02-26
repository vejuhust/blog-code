
from uuid import uuid4
from basehash import base62


def generate_short_id():
    """ Short ID generator - v3: Shuffled XOR UUID4 """
    num = uuid4().int
    mask = (1 << 64) - 1
    result = (num ^ (num >> 1)) & 0x55555555555555555555555555555555
    result = ((mask & (result >> 64)) << 1) | (mask & result)
    return base62().encode(result)


def convert_short_id(num):
    """ Short ID converter - v3: Shuffled XOR UUID4 """
    mask = (1 << 64) - 1
    result = (num ^ (num >> 1)) & 0x55555555555555555555555555555555
    result = ((mask & (result >> 64)) << 1) | (mask & result)
    return base62().encode(result)


def generate_short_id_raw():
    """ Short ID generator - v3 - without any encoding """
    num = uuid4().int
    mask = (1 << 64) - 1
    result = (num ^ (num >> 1)) & 0x55555555555555555555555555555555
    result = ((mask & (result >> 64)) << 1) | (mask & result)
    return result
