
from short_id_v0 import convert_short_id as convert_short_id_v0
from short_id_v1 import convert_short_id as convert_short_id_v1
from short_id_v2 import convert_short_id as convert_short_id_v2
from short_id_v3 import convert_short_id as convert_short_id_v3

from uuid import uuid1, uuid4, UUID



# Helpers

def get_random_numbers(uuid_method=uuid1):
    return [
        uuid_method().int,
        uuid_method().int,
        uuid_method().int,
        uuid_method().int,
    ]


def print_numbers_as_uuid(numbers, display_uuid=True):
    for num in numbers:
        if display_uuid:
            print("    {}".format(UUID(int=num)))
        else:
            print("    0x{:032x}".format(num))



# Setting

times = 1000000
convert_method = convert_short_id_v3
uuid_method = uuid4
display_uuid = True



# Run Tests

if __name__ == '__main__':
    collision_set = set()
    idstr_num = {}

    for _ in range(times):
        numbers = get_random_numbers(uuid_method)
        for num in numbers:
            idstr = convert_method(num)
            if idstr in collision_set:
                idstr_num[idstr].append(num)
            else:
                collision_set.add(idstr)
                idstr_num[idstr] = [ num ]

    total_times = times*len(get_random_numbers())
    total_count = 0
    max_count = 0
    max_idstr = None
    for key in sorted(idstr_num):
        value = idstr_num[key]
        count = len(value)
        if count > 1:
            total_count += count
            print("{} - {}".format(key, count))
            if count > max_count:
                max_count = count
                max_idstr = key

    print("\033[94m\033[4mverified {} {} with '{}'\033[0m".format(total_times, uuid_method.__name__, convert_method.__name__))
    if max_idstr is None:
        print("no collision detected")
    else:
        numbers = idstr_num[max_idstr]
        print("{} - {}".format(max_idstr, len(numbers)))
        print_numbers_as_uuid(numbers, display_uuid)
        print("\ncollision rate = {:.2f}%".format(total_count / total_times * 100))
