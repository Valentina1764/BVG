import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "account_card, expected_result",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
    ],
)
def test_mask_account_card(account_card, expected_result):
    assert mask_account_card(account_card) == expected_result


@pytest.mark.parametrize(
    "account_card, expected_result",
    [
        ("MaserCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
    ],
)
def test_mask_account_card_error(account_card, expected_result):
    with pytest.raises(ValueError) as exc_info:
        assert mask_account_card(account_card)
    assert str(exc_info.value) == "Ошибка ввода типа карты. Попробуйте еще раз"


# Дополнение функции для тестирования get_date()
def test_get_date():
    assert get_date("2025-02-15") == "15.02.2025"
