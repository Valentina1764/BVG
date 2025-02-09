def filter_by_state(data_state: list[dict], state = "EXECUTED") -> tuple[list[dict], list[dict]]:
    new_list_1 = []
    new_list_2 = []
    for i in data_state:
        if state == True:
            new_list_1 += i
        else:
            new_list_2 += i
    return f'{new_list_1}{new_list_2}'
