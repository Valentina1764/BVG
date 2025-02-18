def get_mask_card_number(loc_number_card: str) -> str:
    """Функция возвращает замаскированный номер карты"""
    if len(loc_number_card) != 16:
        raise ValueError("Ошибка ввода номера карты. Ожидается 16 цифр. Попробуйте еще раз")
    return f"{loc_number_card[:4]} {loc_number_card[4:6]}** **** {loc_number_card[-4:]}"


def get_mask_account(loc_number_account: str) -> str:
    """Функция возвращает замаскированный номер счета"""
    if len(loc_number_account) != 20:
        raise ValueError("Ошибка ввода номера счета. Ожидается 20 цифр. Попробуйте еще раз")
    return f"**{loc_number_account[-4:]}"
