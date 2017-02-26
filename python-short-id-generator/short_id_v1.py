
from uuid import uuid1
from basehash import base62


def generate_short_id():
    """ Short ID generator - v1: Half Unshuffle UUID1 """
    num = uuid1().int
    mask = 0x55555555555555555555555555555555
    x = (num ^ (num >> 1)) & mask
    x = (x | (x >> 1))  & 0x33333333333333333333333333333333
    x = (x | (x >> 2))  & 0x0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F
    x = (x | (x >> 4))  & 0x00FF00FF00FF00FF00FF00FF00FF00FF
    x = (x | (x >> 8))  & 0x0000FFFF0000FFFF0000FFFF0000FFFF
    x = (x | (x >> 16)) & 0x00000000FFFFFFFF00000000FFFFFFFF
    x = (x | (x >> 32)) & 0x0000000000000000FFFFFFFFFFFFFFFF
    return base62().encode(x)


def convert_short_id(num):
    """ Short ID converter - v1: Half Unshuffle UUID1 """
    mask = 0x55555555555555555555555555555555
    x = (num ^ (num >> 1)) & mask
    x = (x | (x >> 1))  & 0x33333333333333333333333333333333
    x = (x | (x >> 2))  & 0x0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F
    x = (x | (x >> 4))  & 0x00FF00FF00FF00FF00FF00FF00FF00FF
    x = (x | (x >> 8))  & 0x0000FFFF0000FFFF0000FFFF0000FFFF
    x = (x | (x >> 16)) & 0x00000000FFFFFFFF00000000FFFFFFFF
    x = (x | (x >> 32)) & 0x0000000000000000FFFFFFFFFFFFFFFF
    return base62().encode(x)


def generate_short_id_raw():
    """ Short ID generator - v1 - without any encoding """
    num = uuid1().int
    mask = 0x55555555555555555555555555555555
    x = (num ^ (num >> 1)) & mask
    x = (x | (x >> 1))  & 0x33333333333333333333333333333333
    x = (x | (x >> 2))  & 0x0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F
    x = (x | (x >> 4))  & 0x00FF00FF00FF00FF00FF00FF00FF00FF
    x = (x | (x >> 8))  & 0x0000FFFF0000FFFF0000FFFF0000FFFF
    x = (x | (x >> 16)) & 0x00000000FFFFFFFF00000000FFFFFFFF
    x = (x | (x >> 32)) & 0x0000000000000000FFFFFFFFFFFFFFFF
    return x
