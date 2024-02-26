'''тут форматирует плоский формат'''


def plain(diff_list):
    """переводит список различий в плоский формат и отдает строку"""
    diff_list.sort(key=lambda x: x['name'])
    result = get_diff_plain_list(diff_list)
    return '\n'.join(result)


def get_diff_plain_list(diff_list, path=''):
    """поиск разницы в ключах и возвращает строку"""
    result = []
    for node in diff_list:
        if node['status'] == 'nested':
            path_to_change = path + node['name'] + '.'
            difference = get_diff_plain_list(node['children'], path_to_change)
            result.extend(difference)
        if node['status'] == 'added':
            path_to_change = path + node['name']
            change = create_change(node['data'])
            difference = (
                f"Property '{path_to_change}' was added "
                f"with value: {change}"
            )
            result.append(difference)
        if node['status'] == 'deleted':
            path_to_change = path + node['name']
            change = create_change(node['data'])
            difference = "Property '{}' was removed".format(path_to_change)
            result.append(difference)
        if node['status'] == 'changed':
            path_to_change = path + node['name']
            change_before = create_change(node['data before'])
            change_after = create_change(node['data after'])
            difference = (
                f"Property '{path_to_change}' was updated. "
                f"From {change_before} to {change_after}"
            )
            result.append(difference)
    return result


def create_change(data):
    """парсит строку,  возвращает ее в верный формат как строку"""
    if type(data) is dict or type(data) is list:
        result = '[complex value]'
    elif data is False:
        result = 'false'
    elif data is True:
        result = 'true'
    elif data is None:
        result = 'null'
    elif type(data) is str:
        result = "'{}'".format(data)
    else:
        result = '{}'.format(data)
    return result
