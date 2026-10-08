import json


def get_transactions(path: str) -> list[dict]:
    """Читает JSON-файл с транзакциями и возвращает список словарей"""
    try:
        with open(path, "r") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            return []
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
