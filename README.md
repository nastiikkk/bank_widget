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


## Тестирование

Для проверки проекта используются тесты на базе pytest.

Тестами проверяются:

* функции маскировки номеров банковских карт и счетов
* обработка корректных и некорректных данных
* преобразование дат
* фильтрация операций по состоянию
* сортировка операций по дате в прямом и обратном порядке

Для запуска тестов используется команда:

```
poetry run pytest
```

Для формирования HTML-отчета о покрытии:

```
poetry run pytest --cov=src --cov-report=html
```

