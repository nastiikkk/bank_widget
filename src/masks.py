import logging

logger = logging.getLogger("masks")
file_handler = logging.FileHandler("logs/masks.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера банковской карты"""
    if len(card_number) == 16 and card_number.isdigit():
        logger.info("Номер карты успешно замаскирован")
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
    logger.error("Ошибка при маскировании номера карты")
    raise ValueError("Некорректный номер карты")


def get_mask_account(account: str) -> str:
    """Функция маскировки номера банковского счета"""
    if len(account) >= 4 and account.isdigit():
        logger.info("Номер счета успешно замаскирован")
        return f"**{account[-4:]}"
    logger.error("Ошибка при маскировании номера счета")
    raise ValueError("Некорректный номер счета")
