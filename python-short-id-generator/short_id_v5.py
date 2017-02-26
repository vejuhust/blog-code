
import string
from os import urandom
from struct import unpack


def generate_short_id():
    """ Short ID generator - v5: Base62-Encoded Urandom """
    num = unpack("<Q", urandom(8))[0]
    if num <= 0:
        result = "0"
    else:
        alphabet = string.digits + string.ascii_uppercase + string.ascii_lowercase
        key = []
        while num > 0:
            num, rem = divmod(num, 62)
            key.append(alphabet[rem])
        result = "".join(reversed(key))
    return result


def convert_short_id(num):
    """ Short ID converter - v5: Base62-Encoded Urandom """
    return generate_short_id()


def generate_short_id_raw():
    """ Short ID generator - v5 - without any encoding """
    return unpack("<Q", urandom(8))[0]
