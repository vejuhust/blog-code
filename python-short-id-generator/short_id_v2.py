
from uuid import uuid1
from basehash import base62


def generate_short_id():
    """ Short ID generator - v2: Shuffled XOR UUID1 """
    num = uuid1().int
    mask = (1 << 64) - 1
    result = (num ^ (num >> 1)) & 0x55555555555555555555555555555555
    result = ((mask & (result >> 64)) << 1) | (mask & result)
    return base62().encode(result)


def convert_short_id(num):
    """ Short ID converter - v2: Shuffled XOR UUID1 """
    mask = (1 << 64) - 1
    result = (num ^ (num >> 1)) & 0x55555555555555555555555555555555
    result = ((mask & (result >> 64)) << 1) | (mask & result)
    return base62().encode(result)


def generate_short_id_raw():
    """ Short ID generator - v2 - without any encoding """
    num = uuid1().int
    mask = (1 << 64) - 1
    result = (num ^ (num >> 1)) & 0x55555555555555555555555555555555
    result = ((mask & (result >> 64)) << 1) | (mask & result)
    return result
