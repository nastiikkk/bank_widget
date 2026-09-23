from typing import Generator


def filter_by_currency(
    transactions: list[dict], currency_code: str
) -> Generator[dict, None, None]:
    """Возвращает транзакции только с указанной валютой"""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency_code:
            yield transaction


def transaction_descriptions(transactions: list[dict]) -> Generator[str, None, None]:
    """Возвращает описание операции"""
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, stop: int) -> Generator[str, None, None]:
    """Генерирует номера банковских карт"""
    for number in range(start, stop + 1):
        number_str = f"{number:016d}"
        yield f"{number_str[:4]} {number_str[4:8]} {number_str[8:12]} {number_str[12:16]}"
