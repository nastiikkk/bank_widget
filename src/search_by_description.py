import re
from collections import Counter


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Фильтрует операции по строке"""
    filtered_data = []
    for transaction in data:
        match = re.search(search, transaction.get("description", ""), re.IGNORECASE)
        if match:
            filtered_data.append(transaction)
    return filtered_data


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Фильтрует операции по категориям"""
    filtered = []
    for transaction in data:
        description = transaction.get("description", "")
        for category in categories:
            if category.lower() in description.lower():
                filtered.append(description)
    return dict(Counter(filtered))
