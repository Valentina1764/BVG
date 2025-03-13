import pytest

from src.masks_old import get_mask_account, get_mask_card_number


def test_get_mask_card_number(number_card):
    """Тестирование правильности маскирования номера карты"""
    assert get_mask_card_number(number_card) == "1596 83** **** 5199"


def test_mask_card_number_error(number_card_error):
    """Проверка работы функции на случай нестандартной длины номеров"""
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(number_card_error)
    assert str(exc_info.value) == "Ошибка ввода номера карты. Ожидается 16 цифр. Попробуйте еще раз"


def test_mask_account_number(number_account):
    """Тестирование правильности маскирования номера счета"""
    assert get_mask_account(number_account) == "**5560"


def test_mask_account_error(number_account_error):
    """Проверка работы функции на случай нестандартной длины номера счета"""
    with pytest.raises(ValueError) as exc_info:
        get_mask_account(number_account_error)
    assert str(exc_info.value) == "Ошибка ввода номера счета. Ожидается 20 цифр. Попробуйте еще раз"
