
from short_id_v0 import generate_short_id as generate_short_id_v0
from short_id_v1 import generate_short_id as generate_short_id_v1
from short_id_v2 import generate_short_id as generate_short_id_v2
from short_id_v3 import generate_short_id as generate_short_id_v3
from short_id_v4 import generate_short_id as generate_short_id_v4
from short_id_v5 import generate_short_id as generate_short_id_v5


def print_id(tag, idstr):
    print("{:>6s} | {:<30s} | {:^6d} |".format(tag, idstr, len(idstr)))


def test_generate(idx):
    tag = "v{}".format(idx)
    name = "generate_short_id_{}".format(tag)
    if name in globals():
        print_id(tag, globals()[name]())


if __name__ == '__main__':
    for idx in range(10):
        test_generate(idx)
