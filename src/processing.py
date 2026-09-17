def filter_by_state(data: list[dict], state: str =  'EXECUTED') -> list[dict]:
    """ Функция, которая возвращает список словарей у которых ключ state
 соответствует указанному значению """
    result = []

    for i in data:
        if i['state'] == state:
            result.append(i)

    return result

