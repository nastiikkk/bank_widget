# Bank Project

## Описание 

Bank Project - учебный проект для обработки данных о банковских операциях.

## Установка

1. Клонируйте репозиторий:

```
git clone https://github.com/nastiikkk/bank_widget.git
```

2. Установите зависимости:

```
poetry install
```

## Использование:

### Функция `filter_by_state`

Функция фильтрует список банковских операций по значению ключа `state`.

По умолчанию используются операции со статусом `EXECUTED`.

```python
from src.processing import filter_by_state

operations = [
    {
        'id': 1,
        'state': 'EXECUTED',
        'date': '2019-07-03T18:35:29.512364'
    },
    {
        'id': 2,
        'state': 'CANCELED',
        'date': '2018-09-12T21:27:25.241689'
    },
    {
        'id': 3,
        'state': 'EXECUTED',
        'date': '2018-06-30T02:08:58.425572'
    }
]

print(filter_by_state(operations))
```

Результат:

```python
[
    {
        'id': 1,
        'state': 'EXECUTED',
        'date': '2019-07-03T18:35:29.512364'
    },
    {
        'id': 3,
        'state': 'EXECUTED',
        'date': '2018-06-30T02:08:58.425572'
    }
]
```

Чтобы получить операции со статусом `CANCELED`, передайте нужное значение:

```python
print(filter_by_state(operations, 'CANCELED'))
```

### Функция `sort_by_date`

Функция сортирует список банковских операций по дате.

По умолчанию операции сортируются по убыванию.

```python
from src.processing import sort_by_date

print(sort_by_date(operations))
```

Результат:

```python
[
    {
        'id': 1,
        'state': 'EXECUTED',
        'date': '2019-07-03T18:35:29.512364'
    },
    {
        'id': 2,
        'state': 'CANCELED',
        'date': '2018-09-12T21:27:25.241689'
    },
    {
        'id': 3,
        'state': 'EXECUTED',
```


### Функция `mask_account_card`

Функция определяет тип банковского продукта и возвращает его название вместе с замаскированным номером.

```python
from src.widget import mask_account_card

print(mask_account_card("Visa Platinum 1234567890123456"))
```

### Функция `get_date`

Функция преобразует дату из формата ISO в формат `ДД.ММ.ГГГГ`.

```python
from src.widget import get_date

print(get_date("2019-07-03T18:35:29.512364"))
```

Результат:
```
03.07.2019
```

## Модуль generators

Модуль generators содержит генераторы для работы с транзакциями и номерами банковских карт.

### filter_by_currency

Возвращает транзакции только с указанной валютой.

Пример:

```python
from src.generators import filter_by_currency

transactions = [
    {
        "id": 1,
        "operationAmount": {
            "currency": {
                "code": "USD"
            }
        }
    },
    {
        "id": 2,
        "operationAmount": {
            "currency": {
                "code": "RUB"
            }
        }
    }
]

usd_transactions = filter_by_currency(transactions, "USD")

for transaction in usd_transactions:
    print(transaction)
```

Результат:
```
{
    "id": 1,
    "operationAmount": {
        "currency": {
            "code": "USD"
        }
    }
}
```

### transaction_descriptions

Возвращает описания операций из списка транзакций.

Пример:

```python
from src.generators import transaction_descriptions

descriptions = transaction_descriptions(transactions)

for description in descriptions:
    print(description)
```

Результат:
```
Перевод организации
Перевод со счета на счет
Перевод с карты на карту
```

### card_number_generator

Генерирует номера банковских карт в заданном диапазоне.

Пример:

```python
from src.generators import card_number_generator

cards = card_number_generator(1, 3)

for card in cards:
    print(card)

```

Результат:
```
0000 0000 0000 0001
0000 0000 0000 0002
0000 0000 0000 0003
```