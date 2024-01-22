import json


def format_json(diff_list):
    """тут форматирую json"""
    return json.dumps(diff_list, indent=4)
