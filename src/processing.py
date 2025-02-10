def filter_by_state(data_state: list, state="EXECUTED") -> list:
    '''Функция возвращает список словарей в зависимости от значения ключа "state"'''
    new_list = []
    for i in data_state:
        if i["state"] == state:
            new_list.append(i)
        else:
            continue
    return new_list


def sort_by_date(sort_list: list, rever: bool = False) -> list:
    '''Функция возвращает отсортированный список по ключу "date"'''
    sorted_list = sorted(sort_list, key=lambda x: x["date"], reverse=rever)
    return sorted_list
