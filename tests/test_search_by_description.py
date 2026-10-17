from src.search_by_description import (process_bank_operations,
                                       process_bank_search)


def test_process_bank_search_finds_match():
    transactions = [
        {"description": "Перевод со счета на счет"},
        {"description": "Открытие вклада"},
    ]

    result = process_bank_search(transactions, "перевод")

    assert result == [{"description": "Перевод со счета на счет"}]


def test_process_bank_search_no_matches():
    transactions = [{"description": "Открытие вклада"}]

    result = process_bank_search(transactions, "перевод")

    assert result == []


def test_process_bank_operations():
    data = [
        {"description": "Перевод организации"},
        {"description": "Открытие вклада"},
        {"description": "Перевод организации"},
    ]
    categories = ["перевод", "вклад"]

    result = process_bank_operations(data, categories)

    assert result == {
        "Перевод организации": 2,
        "Открытие вклада": 1,
    }


def test_process_bank_operations_case_insensitive():
    data = [
        {"description": "Перевод организации"},
        {"description": "ПЕРЕВОД клиенту"},
    ]
    categories = ["перевод"]

    result = process_bank_operations(data, categories)

    assert result == {
        "Перевод организации": 1,
        "ПЕРЕВОД клиенту": 1,
    }


def test_process_bank_operations_empty_data():
    result = process_bank_operations([], ["перевод"])

    assert result == {}
