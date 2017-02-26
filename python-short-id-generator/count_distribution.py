
from short_id_v0 import generate_short_id as generate_short_id_v0
from short_id_v1 import generate_short_id as generate_short_id_v1
from short_id_v2 import generate_short_id as generate_short_id_v2
from short_id_v3 import generate_short_id as generate_short_id_v3
from short_id_v4 import generate_short_id as generate_short_id_v4

from datetime import datetime



def get_version_tag(num):
    return "v{}".format(num)


idstr_dict = {}
def count_record_id(idstr, tag):
    idlen = len(idstr)
    if idlen not in idstr_dict:
        idstr_dict[idlen] = []
    idstr_dict[idlen].append((tag, idstr))


collision_dict = {}
def check_id_unique(idstr, tag):
    if tag not in collision_dict:
        collision_dict[tag] = set()
    collision_set = collision_dict[tag]
    result = idstr not in collision_set
    collision_set.add(idstr)
    return result


def analyze_special_version(version_number, times):
    tag = get_version_tag(version_number)
    func_name = "generate_short_id_{}".format(tag)
    count = 0
    while (count < times):
        idstr = globals()[func_name]()
        if check_id_unique(idstr, tag):
            count_record_id(idstr, tag)
            count += 1


results = {}
def aggregate_result(version_count):
    idlen_set = set()
    idlen_min = 100
    idlen_max = 0
    for idlen in sorted(idstr_dict):
        idlen_set.add(idlen)
        idlen_max = max(idlen_max, idlen)
        idlen_min = min(idlen_min, idlen)
    for version in range(version_count):
        tag = get_version_tag(version)
        results[tag] = {}
        for idlen in idlen_set:
            results[tag][idlen] = 0
    for idlen in sorted(idstr_dict):
        idstr_list = idstr_dict[idlen]
        for (tag, idstr) in idstr_list:
            results[tag][idlen] += 1


def print_list_as_table_row(data_list):
    for item in data_list:
        print("| {:MAX}".replace("MAX", str(column_width)).format(item), end=" ")
    print("|")


def print_clean_float(num):
    return "{:.3f}".format(num).rstrip('0').rstrip('.')


def output_result_as_table(times = 1):
    version_list = sorted([ tag for tag in sorted(results) ])
    idlen_list = sorted([ idlen for idlen in sorted(results[version_list[0]]) ])
    table_header_row = [ "ver." ] + [ "len={}".format(idlen) for idlen in idlen_list ] + ["avg. len."]
    print_list_as_table_row(table_header_row)
    column_count = len(table_header_row)
    print(("|:" + "-"*column_width +  ":" )* column_count + "|")
    for version in version_list:
        result_line = [ version ]
        average_len = 0
        for idlen in sorted(results[version]):
            count = results[version][idlen]
            rate = count / times
            average_len += idlen * rate
            result_item = "{:d} / ".format(count) + print_clean_float(rate * 100) + "%"
            result_line.append(result_item)
        result_line.append(print_clean_float(average_len))
        print_list_as_table_row(result_line)
    print()


version_count = 5
times = 10000
column_width = 16


if __name__ == '__main__':
    for version in range(version_count):
        print("[{}] start {} - {} times".format(datetime.now().isoformat(), get_version_tag(version), times))
        analyze_special_version(version, times)
    print()

    aggregate_result(version_count)
    output_result_as_table(times)
