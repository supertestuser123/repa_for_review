from gendiff.get_diff import status, vals


def format_value(value):
    if isinstance(value, dict):
        return '[complex value]'

    elif isinstance(value, bool):
        return 'true' if value else 'false'

    elif value is None:
        return 'null'

    elif isinstance(value, int):
        return f'{value}'

    return f"'{value}'"


def make_lines(data: dict, path=[]) -> list:
    res = []

    for key, values in data.items():
        path += [key]

        if values[status] == 'nested':
            res += [value for value in make_lines(values[vals], path)]

        elif values[status] == 'add':
            value = format_value(values[vals])
            res += [f"Property '{'.'.join(path)}'"
                    + f" was added with value: {value}"]

        elif values[status] == 'removed':
            res += [f"Property '{'.'.join(path)}' was removed"]

        elif values[status] == 'changed':
            old_value = format_value(values['old_value'])
            new_value = format_value(values['new_value'])
            res += [f"Property '{'.'.join(path)}'"
                    + f" was updated. From {old_value} to {new_value}"]

        path.pop()

    return res


def make_plain(data: dict) -> str:
    lines = make_lines(data)

    # If dictionary sorting is broken.
    lines = sorted([''.join(v) for v in lines])

    res = '\n'.join(lines)

    return res
