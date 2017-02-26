
from timeit import repeat


def get_version_tag(num):
    return "v{}".format(num)


def measure_time_cost_by_version(version_number, times):
    tag = get_version_tag(version_number)
    func_name = "generate_short_id_{}".format(tag)
    code_setup = "from short_id_{} import generate_short_id".format(tag)
    code_use = "generate_short_id()"
    result_list = repeat(setup=code_setup, stmt=code_use, repeat=5, number=times)
    result_min = min(result_list)
    avg_usec = result_min / times * 1000000
    return result_min, avg_usec


def print_list_as_table_row(data_list):
    for item in data_list:
        print("| {:MAX}".replace("MAX", str(column_width)).format(item), end=" ")
    print("|")


def output_result_as_table(result_dict, times_list):
    version_list = sorted([ tag for tag in sorted(result_dict) ])
    table_header_row = [ "ver." ] + [ "times={}".format(times) for times in times_list ]
    print_list_as_table_row(table_header_row)
    column_count = len(table_header_row)
    print(("|:" + "-"*column_width +  ":" )* column_count + "|")
    for tag in version_list:
        result_line = [ tag ]
        for avg_time in result_dict[tag]:
            result_line.append("{:.3f}".format(avg_time) + "µs")
        print_list_as_table_row(result_line)


version_count = 5
times_list = [ 1, 10, 100, 1000, 10000 ]
column_width = 16


if __name__ == '__main__':
    result_dict = {}
    for times in times_list:
        for version in range(version_count):
            total_time, avg_time = measure_time_cost_by_version(version, times)
            tag = get_version_tag(version)
            if tag not in result_dict:
                result_dict[tag] = []
            result_dict[tag].append(avg_time)

    output_result_as_table(result_dict, times_list)
