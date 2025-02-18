def filter_by_state(data_state: list, state: str = "EXECUTED") -> list:
    '''Функция возвращает список словарей в зависимости от значения ключа "state"'''
    new_list = []
    for item in data_state:
        if item["state"] == "":
            raise ValueError("Значение ключа 'state' неопределено")
        if item["state"] == state:
            new_list.append(item)
        else:
            continue
    return new_list


def sort_by_date(sort_list: list, is_reversed: bool = True) -> list:
    '''Функция возвращает отсортированный список по ключу "date"'''
    for item in sort_list:
        if item["date"] == "":
            raise ValueError("Значение ключа 'date' не может быть пустым")
    sorted_list = sorted(sort_list, key=lambda x: x["date"], reverse=is_reversed)
    return sorted_list
