import re

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """Функция для маскирования номеров карт и счетов."""
    if account_card == '':
        return f"Источник средств не известен"
    else:
        number_match = re.findall(r'[\d]+', account_card)
        number = ''.join(map(str,number_match))
        name_card = re.findall(r'[^\d]+', account_card)
        name_card_str = ''.join(map(str, name_card))
        if name_card_str == 'Счет ':
            return f"{name_card_str} {get_mask_account(number)}"
        else:
            return f"{name_card_str} {get_mask_card_number(number)}"


def get_date(date_str: str) -> str:
    """Функция возвращает текущую дату в формате ДД.ММ.ГГГГ."""
    return f"{date_str[8:10]}.{date_str[5:7]}.{date_str[:4]}"
