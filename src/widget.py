import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card: str) -> str:
    """Функция, которая возвращает строку с замаскированным номером"""
    if not card:
        raise ValueError("Введите строку")

    first_num_card = None
    for i in range(len(card)):
        if card[i].isdigit():
            first_num_card = i
            break

    if first_num_card is None:
        raise ValueError("Некорректный ввод")

    card_name = card[:first_num_card].strip()
    card_number = card[first_num_card:].strip()

    if not card_number.isdigit() or len(card_name) == 0:
        raise ValueError("Некорректный ввод")

    if "Счет" in card:
        result = get_mask_account(card_number)
    else:
        result = get_mask_card_number(card_number)

    return f"{card_name} {result}"


def get_date(date: str) -> str:
    """Функция, которая возвращает строку с датой в формате 'ДД.ММ.ГГГГ'"""
    new_date = datetime.datetime.fromisoformat(date)
    return new_date.strftime("%d.%m.%Y")
