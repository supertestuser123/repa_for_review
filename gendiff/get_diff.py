status = 'status'
vals = 'value'


def get_diff(old_data: dict, new_data: dict) -> dict:
    '''
    здесь создается новый словарь с разницами
    между двумя словарями у каждого ключа есть свой статус
    '''
    old_keys = list(old_data.keys())
    new_keys = list(new_data.keys())
    keys = set(old_keys + new_keys)

    result = {}

    for key in sorted(keys):
        old_value = old_data.get(key)
        new_value = new_data.get(key)

        if isinstance(old_value, dict) and isinstance(new_value, dict):
            result[key] = {status: 'nested',
                           vals: get_diff(old_value, new_value)
                           }

        elif key in old_keys and key not in new_keys:
            result[key] = {status: 'removed',
                           vals: old_value}

        elif key not in old_keys and key in new_keys:
            result[key] = {status: 'add',
                           vals: new_value}

        elif old_value == new_value:
            result[key] = {status: 'unchanged', vals: old_value}

        else:
            result[key] = {status: 'changed',
                           'old_value': old_value,
                           'new_value': new_value}

    return result
