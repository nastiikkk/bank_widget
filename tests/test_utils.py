import json
from unittest.mock import mock_open, patch

from src.utils import get_transactions


def test_get_transactions() -> None:
    """Проверяет чтение JSON-файла"""
    data = [{"amount": 100}, {"id": 23}]
    with patch("builtins.open", mock_open(read_data=json.dumps(data))):
        result = get_transactions("operations.json")

    assert result == data


def test_get_transactions_empty_file() -> None:
    """Проверяет обработку пустого JSON-файла"""
    with patch("builtins.open", mock_open(read_data="")):
        result = get_transactions("operations.json")
    assert result == []


def test_get_transactions_not_list() -> None:
    """Проверяет обработку JSON-файла, внутри которого не список"""
    data = {"currency": "RUB"}
    with patch("builtins.open", mock_open(read_data=json.dumps(data))):
        result = get_transactions("operations.json")
    assert result == []


def test_get_transactions_file_not_found() -> None:
    """Проверяет обработку несуществующего файла"""
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = get_transactions("operations.json")
    assert result == []
