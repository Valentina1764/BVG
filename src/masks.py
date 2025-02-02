def get_mask_card_number(loc_number_card: str) -> str:
    """Функция возвращает замаскированный номер карты"""
    return f"{loc_number_card[:4]} {loc_number_card[4:6]}** **** {loc_number_card[-4:]}"


def get_mask_account(loc_number_account: str) -> str:
    """Функция возвращает замаскированный номер счета"""
    new_number_account = "**"
    new_number_account = new_number_account + loc_number_account[-4:]

    return new_number_account
