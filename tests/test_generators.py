import pytest

from src.generators import (card_number_generator, filter_by_currency,
                            transaction_descriptions)


@pytest.fixture
def transactions() -> list[dict]:
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {"name": "RUB", "code": "RUB"},
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 643487541,
            "state": "CANCELLED",
            "date": "2026-09-22T14:00:06.263278",
            "operationAmount": {
                "amount": "0.0001",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод с карты на карту",
            "from": "Счет 00001267834520912",
            "to": "Счет 75651667383060284188",
        },
    ]


@pytest.mark.parametrize(
    "currency_code, expected_id",
    [("USD", [939719570, 643487541]), ("RUB", [142264268]), ("THB", [])],
)
def test_filter_by_currency(transactions: list[dict], currency_code: str, expected_id: list[int]) -> None:
    result = list(filter_by_currency(transactions, currency_code))
    result_ids = [transaction["id"] for transaction in result]
    assert result_ids == expected_id


def test_filter_by_currency_no_transactions() -> None:
    result = list(filter_by_currency([], "USD"))
    assert result == []


@pytest.mark.parametrize(
    "expected_description",
    [["Перевод организации", "Перевод со счета на счет", "Перевод с карты на карту"]],
)
def test_transaction_descriptions(transactions: list[dict], expected_description: list[str]) -> None:
    result = list(transaction_descriptions(transactions))
    assert result == expected_description


def test_transaction_descriptions_empty() -> None:
    result = list(transaction_descriptions([]))
    assert result == []


@pytest.mark.parametrize(
    "start, stop, expected_card_numbers",
    [
        (1, 2, ["0000 0000 0000 0001", "0000 0000 0000 0002"]),
        (3, 5, ["0000 0000 0000 0003", "0000 0000 0000 0004", "0000 0000 0000 0005"]),
        (1000, 1000, ["0000 0000 0000 1000"]),
        (134, 133, []),
    ],
)
def test_card_number_generator(start: int, stop: int, expected_card_numbers: list[str]) -> None:
    result = list(card_number_generator(start, stop))
    assert result == expected_card_numbers
