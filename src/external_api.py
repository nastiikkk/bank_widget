import os

from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")


def get_transaction_amount(transaction: dict) -> float:
    """Возвращает сумму транзакции"""
    amount = float(transaction["operationAmount"]["amount"])
    return amount
