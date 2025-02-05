from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(loc_account_card: str) -> str:
    """ "Функция возвращения замаскерованных карт и счетов"""
    if "Maestro" in loc_account_card:
        return f"Maestro {get_mask_card_number(loc_account_card[-16:])}"
    elif "MasterCard" in loc_account_card:
        return f"MasterCard {get_mask_card_number(loc_account_card[-16:])}"
    elif "Visa Classic" in loc_account_card:
        return f"Visa Classic {get_mask_card_number(loc_account_card[-16:])}"
    elif "Visa Platinum" in loc_account_card:
        return f"Visa Platinum {get_mask_card_number(loc_account_card[-16:])}"
    elif "Visa Gold" in loc_account_card:
        return f"Visa Gold {get_mask_card_number(loc_account_card[-16:])}"
    else:
        return f"Счет {get_mask_account(loc_account_card[-20:])}"


def get_date(dt_now: str) -> str:
    """Функция возвращает текущую дату"""
    return f"{dt_now[8:10]}.{dt_now[5:7]}.{dt_now[:4]}"
