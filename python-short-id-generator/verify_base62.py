
import string
from os import urandom
from struct import unpack
from basehash import base62


def convert_short_id_v4(num):
    """ Short ID converter - v4: Urandom """
    return base62().encode(num)


def convert_short_id_v5(num):
    """ Short ID converter - v5: Base62-Encoded Urandom """
    if num <= 0:
        result = "0"
    else:
        alphabet = string.digits + string.ascii_uppercase + string.ascii_lowercase
        key = []
        while num:
            num, rem = divmod(num, 62)
            key.append(alphabet[rem])
        result = "".join(reversed(key))
    return result


times = 1000000

if __name__ == '__main__':
    print("verify v4 & v5 for {} times".format(times))
    for _ in range(times):
        num = unpack("<Q", urandom(8))[0]
        idstr_v4 = convert_short_id_v4(num)
        idstr_v5 = convert_short_id_v5(num)
        if idstr_v4 != idstr_v5:
            print("\033[91mfailed - num:{:x}, v4:{}, v5:{}\033[0m".format(num, idstr_v4, idstr_v5))
            break
    else:
        print("\033[92mok!\033[0m")
