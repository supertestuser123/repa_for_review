"""Dictionary format formater."""


def stylish(diff_list):
    """Converts a list of differences to dictionary format. Returns string."""
    return get_diff_stylish(diff_list)


def process_nested(node, indent, level):
    data = get_diff_stylish(node['children'], level + 1)
    return f"{indent}  {node['name']}: {data}\n"


# Обновите вызов process_nested в get_diff_stylish
def get_diff_stylish(diff_list, level=0):
    result = '{\n'
    indent = '  ' * level
    diff_list.sort(key=lambda x: x['name'])

    for node in diff_list:
        result += process_node(node, indent, level)

    result += indent[:-2] + '}'
    return result


def process_node(node, indent, level):
    status_handlers = {
        'nested': process_nested,
        'not changed': process_not_changed,
        # Добавьте другие статусы и соответствующие обработчики
    }
    handler = status_handlers.get(node['status'], default_handler)
    return handler(node, indent, level)


# Добавьте параметр level к другим функциям-обработчикам
def process_not_changed(node, indent, level):
    data = format_data(node['data'], indent)
    return f"{indent}  {node['name']}: {data}\n"


def default_handler(node, indent, level):
    return f"{indent}  {node['name']}: {format_data(node['data'], indent)}\n"


def format_data(data, indent):
    """Parses the data. Returns it in the correct format as a string."""
    if type(data) is dict:
        indent += '    '
        result = '{\n'
        for key in data.keys():
            value = format_data(data[key], indent)
            result += indent + '  ' + key + ': ' + value + '\n'
        result += indent[:-2] + '}'
    elif data is False:
        result = 'false'
    elif data is True:
        result = 'true'
    elif data is None:
        result = 'null'
    else:
        result = str(data)
    return result
