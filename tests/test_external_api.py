from src.external_api import get_transaction_amount


def test_get_transaction_amount_rub() -> None:
    """Проверяет получение суммы транзакции в рублях"""
    transaction = {"operationAmount": {"amount": "1000", "currency": {"code": "RUB"}}}
    result = get_transaction_amount(transaction)
    assert result == 1000.0
