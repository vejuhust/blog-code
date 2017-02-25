
from uuid import uuid4
from basehash import base62


def generate_short_id():
    """ Short ID generator - v3: Shuffled XOR UUID4 """
    num = uuid4().int
    mask_shuffle = 0x55555555555555555555555555555555
    mask_half = (1 << 64) - 1
    result = (num ^ (num >> 1)) & mask_shuffle
    result = ((mask_half & (result >> 64)) << 1) | (mask_half & result)
    return base62().encode(result)


def convert_short_id(num):
    """ Short ID converter - v3: Shuffled XOR UUID4 """
    mask_shuffle = 0x55555555555555555555555555555555
    mask_half = (1 << 64) - 1
    result = (num ^ (num >> 1)) & mask_shuffle
    result = ((mask_half & (result >> 64)) << 1) | (mask_half & result)
    return base62().encode(result)
