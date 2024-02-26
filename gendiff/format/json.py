import json


def format_json(data: dict) -> str:
    """берем словарь и делаем строку а потом отдаем джсон с отступами"""
    return json.dumps(data, sort_keys=True, indent=4)
