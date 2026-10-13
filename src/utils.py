import json
import logging

logger = logging.getLogger("utils")
file_handler = logging.FileHandler("logs/utils.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_transactions(path: str) -> list[dict]:
    """Читает JSON-файл с транзакциями и возвращает список словарей"""
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                logger.info("Файл успешно прочитан")
                return data
            logger.error("JSON-файл содержит не список")
            return []
    except FileNotFoundError:
        logger.error("Файл не найден")
        return []
    except json.JSONDecodeError:
        logger.error("Ошибка чтения JSON-файла")
        return []
