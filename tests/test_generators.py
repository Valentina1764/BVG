import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions

list_transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]

result_list_transactions_USD = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
]


result_list_transactions_RUB = [
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]


result_description = [
    "Перевод организации",
    "Перевод со счета на счет",
    "Перевод со счета на счет",
    "Перевод с карты на карту",
    "Перевод организации",
]


@pytest.mark.parametrize(
    "transactions, filter_currency, expected_result",
    [
        (list_transactions, "USD", result_list_transactions_USD),
        (list_transactions, "RUB", result_list_transactions_RUB),
    ],
)
def test_filter_by_currency(transactions, filter_currency, expected_result):
    """Тест на правильность фильтрации трансакций по заданной валюте"""
    actual_result = list(filter_by_currency(transactions, filter_currency))
    assert actual_result == expected_result


# def test_empty_list_transactions(empty_list_transactions):
#    """Тестирование """
#    with pytest.raises(ValueError) as exc_info:
#        filter_by_currency(empty_list_transactions)
#    assert str(exc_info.value) == "Список трансакций пуст."


# def test_empty_code(error_list_transactions):
#    with pytest.raises(ValueError) as exc_info:
#        assert filter_by_currency(error_list_transactions)
#    assert str(exc_info.value) == "Код валюты не указан."


@pytest.mark.parametrize(
    "transactions, expected_result",
    [
        (list_transactions, result_description),
    ],
)
def test_transaction_descriptions(transactions, expected_result):
    """Проверяем, что функция возвращает корректные описания для каждой транзакции"""
    actual_result = list(transaction_descriptions(transactions))
    assert actual_result == expected_result


# def test_empty_list_transactions_for_transaction_descriptions(empty_list_transactions):
#    """Тестирование """
#    with pytest.raises(ValueError) as exc_info:
#        assert transaction_descriptions(empty_list_transactions)
#    assert str(exc_info.value) == "Список трансакций пуст."


list_number_card_1_5 = [
    "0000 0000 0000 0001",
    "0000 0000 0000 0002",
    "0000 0000 0000 0003",
    "0000 0000 0000 0004",
    "0000 0000 0000 0005",
]

list_number_card_234_240 = [
    "0000 0000 0000 0234",
    "0000 0000 0000 0235",
    "0000 0000 0000 0236",
    "0000 0000 0000 0237",
    "0000 0000 0000 0238",
    "0000 0000 0000 0239",
    "0000 0000 0000 0240",
]

list_number_card_99999999_100000004 = [
    "0000 0000 9999 9999",
    "0000 0001 0000 0000",
    "0000 0001 0000 0001",
    "0000 0001 0000 0002",
    "0000 0001 0000 0003",
    "0000 0001 0000 0004",
]


@pytest.mark.parametrize(
    "start, end, expected_result",
    [
        (1, 5, list_number_card_1_5),
        (234, 240, list_number_card_234_240),
        (99999999, 100000004, list_number_card_99999999_100000004),
    ],
)
def test_card_number_generator(start, end, expected_result):
    """Тест функции на корректность генерации номера карты"""
    actual_result = list(card_number_generator(start, end))
    assert actual_result == expected_result
