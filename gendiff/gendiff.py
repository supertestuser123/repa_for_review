from gendiff.get_diff import get_diff
from gendiff.parse_data import get_value
from gendiff.format.stylish import make_stylish
from gendiff.format.plain import make_plain
from gendiff.format.json import format_json

formats = {'stylish': make_stylish,
           'plain': make_plain,
           'json': format_json,
           }
default_format = 'stylish'


def generate_diff(path_file1: str,
                  path_file2: str,
                  format=default_format
                  ) -> str:
    old_data = get_value(path_file1)
    new_data = get_value(path_file2)

    if old_data == new_data:
        return ''

    values = get_diff(old_data, new_data)

    res = formats[format](values)

    return res
