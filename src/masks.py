def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера банковской карты"""
    if len(card_number) == 16 and card_number.isdigit():
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
    raise ValueError('Некорректный номер карты')


def get_mask_account(account: str) -> str:
    """Функция маскировки номера банковского счета"""
    if len(account) >= 4 and account.isdigit():
        return f"**{account[-4:]}"
    raise ValueError('Некорректный номер счета')