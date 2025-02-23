import re

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """Функция для маскирования номеров карт и счетов."""
    number_pattern = r"\d+"
    number_match = re.search(number_pattern, account_card)
    number = number_match.group(0)
    if "Maestro" in account_card:
        return f"Maestro {get_mask_card_number(number)}"
    elif "MasterCard" in account_card:
        return f"MasterCard {get_mask_card_number(number)}"
    elif "Visa Classic" in account_card:
        return f"Visa Classic {get_mask_card_number(number)}"
    elif "Visa Platinum" in account_card:
        return f"Visa Platinum {get_mask_card_number(number)}"
    elif "Visa Gold" in account_card:
        return f"Visa Gold {get_mask_card_number(number)}"
    elif "Счет" in account_card:
        return f"Счет {get_mask_account(number)}"
    else:
        raise ValueError("Ошибка ввода типа карты. Попробуйте еще раз")


def get_date(date_str: str) -> str:
    """Функция возвращает текущую дату в формате ДД.ММ.ГГГГ."""
    return f"{date_str[8:10]}.{date_str[5:7]}.{date_str[:4]}"
