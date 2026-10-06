import os

import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")


def get_transaction_amount(transaction: dict) -> float:
    """Возвращает сумму транзакции в рублях"""
    transaction_currency_code = transaction["operationAmount"]["currency"]["code"]
    amount = float(transaction["operationAmount"]["amount"])
    if transaction_currency_code in ("USD", "EUR"):
        amount = convert_to_rubles(amount, transaction_currency_code)
    return amount


def convert_to_rubles(amount: float, currency_code: str) -> float:
    """Конвертирует сумму транзакции в рубли"""
    response = requests.get(
        "https://api.apilayer.com/exchangerates_data/convert",
        params={"to": "RUB", "from": currency_code, "amount": amount},
        headers={"apikey": api_key},
    )

    response = response.json()
    new_amount = response["result"]
    return new_amount
