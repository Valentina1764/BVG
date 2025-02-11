def filter_by_state(data_state: list, state: str = "EXECUTED") -> list:
    '''Функция возвращает список словарей в зависимости от значения ключа "state"'''
    new_list = []
    for item in data_state:
        if item["state"] == state:
            new_list.append(item)
        else:
            continue
    return new_list


def sort_by_date(sort_list: list, is_reversed: bool = False) -> list:
    '''Функция возвращает отсортированный список по ключу "date"'''
    sorted_list = sorted(sort_list, key=lambda x: x["date"], reverse=is_reversed)
    return sorted_list
