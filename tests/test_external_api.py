from unittest.mock import Mock, patch

from src.external_api import convert_to_rubles, get_transaction_amount


def test_get_transaction_amount_rub() -> None:
    """Проверяет получение суммы транзакции в рублях"""
    transaction = {"operationAmount": {"amount": "1000", "currency": {"code": "RUB"}}}
    result = get_transaction_amount(transaction)
    assert result == 1000.0


@patch("src.external_api.convert_to_rubles")
def test_get_transaction_amount_usd(mock_convert: Mock) -> None:
    """Проверяет конвертацию USD в рубли"""
    mock_convert.return_value = 90000.0
    transaction = {"operationAmount": {"amount": "1000", "currency": {"code": "USD"}}}
    result = get_transaction_amount(transaction)
    mock_convert.assert_called_once_with(1000.0, "USD")
    assert result == 90000.0


@patch("src.external_api.requests.get")
def test_convert_to_rubles(mock_get: Mock) -> None:
    """Проверяет конвертацию валюты через API"""
    mock_get.return_value.json.return_value = {"result": 95000.0}
    result = convert_to_rubles(1000.0, "USD")
    assert result == 95000.0
    mock_get.assert_called_once()
