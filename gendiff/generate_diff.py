"""здесь создает разницу между двумя файлами"""


from gendiff.tools.parse_file import get_dict_from_file
from gendiff.tools.diff import diff
from gendiff.formatters.format_diff import format_diff


def generate_diff(path_file1, path_file2, format_name='stylish'):
    """создает разницу между 2 файлами в опр формате, отдает str"""
    dict1 = get_dict_from_file(path_file1)
    dict2 = get_dict_from_file(path_file2)
    list_diff = diff(dict1, dict2)
    return format_diff(list_diff, format_name)
