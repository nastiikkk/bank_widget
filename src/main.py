from pathlib import Path

from src.external_api import get_transaction_amount
from src.file_readers import read_csv_file, read_excel_file
from src.generators import filter_by_currency, transaction_descriptions
from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.search_by_description import process_bank_search
from src.utils import get_transactions
from src.widget import get_date

base_path = Path(__file__).resolve().parent.parent


def main():
    """Запускает основную логику программы обработки банковских транзакций.
       Предлагает выбрать формат файла, фильтрует и сортирует транзакции
       по заданным пользователем параметрам, затем выводит результат
       """
    file_type = greeting()
    file_paths = {
        1: (base_path / "data" / "transactions.json", get_transactions),
        2: (base_path / "data" / "transactions.csv", read_csv_file),
        3: (base_path / "data" / "transactions.xlsx", read_excel_file),
    }
    path, func = file_paths[file_type]
    transactions = func(path)
    status = get_status()
    transactions = filter_by_state(transactions, status)

    sort_date, ascending, rubles_only, search_description, search_word = how_sort()

    if sort_date:
        transactions = sort_by_date(transactions, not ascending)

    if rubles_only:
        transactions = list(filter_by_currency(transactions, "RUB"))

    if search_description:
        transactions = process_bank_search(transactions, search_word)

    print_transactions(transactions)


def greeting() -> int:
    """Приветствует пользователя и предлагает выбрать формат файла"""
    print(
        "Привет! Добро пожаловать в программу работы "
        "с банковскими транзакциями.\n"
        "Выберите необходимый пункт меню:\n"
        "1. Получить информацию о транзакциях из JSON-файла\n"
        "2. Получить информацию о транзакциях из CSV-файла\n"
        "3. Получить информацию о транзакциях из XLSX-файла"
    )
    answers = {1: "JSON-файл", 2: "CSV-файл", 3: "XLSX-файл"}
    answer = int(input())
    while answer not in answers:
        print("Выберите необходимый пункт меню")
        answer = int(input())

    print(f"Для обработки выбран {answers[answer]}.\n")
    return answer


def get_status() -> str:
    """Запрашивает статус для фильтрации банковских транзакций"""
    start_message = [
        "Введите статус, по которому необходимо выполнить фильтрацию.",
        "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING",
    ]
    statuses = ["executed", "canceled", "pending"]

    for message in start_message:
        print(message)

    answer = input()
    while answer.lower().strip() not in statuses:
        print(f'Статус операции "{answer}" недоступен.\n')
        for message in start_message:
            print(message)
        answer = input()
    print(f'Операции отфильтрованы по статусу "{answer.upper().strip()}"\n')
    return answer.upper().strip()


def how_sort() -> list:
    """Запрашивает параметры сортировки и фильтрации транзакций"""
    settings = []
    print("Отсортировать операции по дате? Да/Нет")
    answer1 = input().lower().strip()
    settings.append(True if answer1 == "да" else False)
    if answer1 == "да":
        print("Отсортировать по возрастанию или по убыванию? ")
        answer2 = input().lower().strip()
        settings.append(True if answer2 == "по возрастанию" else False)
    else:
        settings.append(False)
    print("Выводить только рублевые транзакции? Да/Нет")
    answer3 = input().lower().strip()
    settings.append(True if answer3 == "да" else False)
    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    answer4 = input().lower().strip()
    if answer4 == "да":
        search_word = input("Введите слово для поиска в описании транзакций\n")
        settings.append(True)
        settings.append(search_word)
    else:
        settings.append(False)
        settings.append(None)

    return settings


def get_transaction_info(transaction: dict, descriptions) -> dict:
    """Подготавливает информацию о банковской транзакции для вывода"""
    new_date = get_date(transaction["date"])

    transaction_description = next(descriptions)

    transaction_info_from = transaction.get("from", "")
    if transaction_info_from != "":
        transaction_info_number_from = transaction_info_from.split()[-1]
        transaction_info_name_from = transaction_info_from.split()[:-1]
        if len(transaction_info_number_from) == 16:
            masked_transaction_from = get_mask_card_number(transaction_info_number_from)
        else:
            masked_transaction_from = get_mask_account(transaction_info_number_from)
    else:
        masked_transaction_from = ""
        transaction_info_name_from = ""
    transaction_info_to = transaction.get("to", "")
    if transaction_info_to != "":
        transaction_info_number_to = transaction_info_to.split()[-1]
        transaction_info_name_to = transaction_info_to.split()[:-1]
        if len(transaction_info_number_to) == 16:
            masked_transaction_to = get_mask_card_number(transaction_info_number_to)
        else:
            masked_transaction_to = get_mask_account(transaction_info_number_to)
    else:
        masked_transaction_to = ""
        transaction_info_name_to = ""
    transaction_amount = get_transaction_amount(transaction)

    return {
        "date": new_date,
        "description": transaction_description,
        "from": f"{' '.join(transaction_info_name_from)} {masked_transaction_from}".strip(),
        "to": f"{' '.join(transaction_info_name_to)} {masked_transaction_to}".strip(),
        "amount": transaction_amount,
    }


def print_transactions(transactions: list[dict]):
    """Выводит отфильтрованные банковские транзакции"""
    print("Распечатываю итоговый список транзакций...\n")
    if len(transactions) > 0:
        print(f"Всего банковских операций в выборке: {len(transactions)}\n")

        descriptions = transaction_descriptions(transactions)
        for transaction in transactions:
            transaction_info = get_transaction_info(transaction, descriptions)

            print(transaction_info["date"], transaction_info["description"])
            if transaction_info["from"] != "":
                print(f"{transaction_info['from']} -> {transaction_info['to']}")
            else:
                print(transaction_info["to"])
            print(
                f"Сумма: {transaction_info["amount"]} {transaction["operationAmount"]["currency"]["code"]}"
            )
            print()

    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")


if __name__ == "__main__":
    main()
