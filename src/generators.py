from typing import List, Generator, Dict


def filter_by_currency(transactions: List[Dict], filter_currency: str = "USD") -> Generator[dict, None, None]:
    '''Функция возвращает список трансакций по типу валюты'''
    if not transactions:
        raise ValueError("Список трансакций пуст.")

    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == "":
            raise ValueError("Код валюты не указан.")

        if transaction["operationAmount"]["currency"]["code"] == filter_currency:
            yield transaction


def transaction_descriptions(transactions: list) -> Generator[str, None, None]:
    '''Функция возвращает значение ключа "description" из списка словарей трансакций'''
    if not transactions:
        raise ValueError("Список трансакций пуст.")

    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(first_number: int, last_number: int) -> Generator[str, None, None]:
    '''Генератор номеров кредитных карт от "0000 0000 0000 0001" до "9999 9999 9999 9999"'''
    if first_number > last_number:
        raise ValueError("Первый параметр не может быть больше второго. Попробуйте снова.")

    card_numbers = "0000000000000000"
    for card_number in range(first_number, last_number + 1):
        card_number_gen = card_numbers[: -len(str(card_number))] + str(card_number)
        card_number_format = (
            f"{card_number_gen[0:4]} {card_number_gen[4:8]} {card_number_gen[8:12]} " f"{card_number_gen[12:17]}"
        )
        yield card_number_format
