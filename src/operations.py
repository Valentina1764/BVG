import re
from collections import Counter


def search_operations_by_description(operations: list, search_string: str) -> list:
    """ Функция для поиска в списке словарей операций по заданной строке состояния."""
    pattern = re.compile(search_string, re.IGNORECASE)
    results = []
    for operation in operations:
        if pattern.search(operation.get('state', '')):
            results.append(operation)

    return results


def search_operations_by_currency(operations: list, search_string: str) -> list:
    """ Функция для поиска в списке словарей операций по заданной валюте."""
    pattern = re.compile(search_string, re.IGNORECASE)
    results = []
    for operation in operations:
        if pattern.search(operation.get('currency_code', '')):
            results.append(operation)

    return results


def search_operations_by_word(operations: list, search_string: str) -> list:
    """ Функция для поиска в списке словарей операций по заданному слову."""
    pattern = re.compile(search_string, re.IGNORECASE)
    results = []
    for operation in operations:
        if pattern.search(operation.get('description', '')):
            results.append(operation)
    return results


def count_categories(transactions: list, description_list: list) -> dict:
    """ Функция для подсчета количества банковских операций определенного типа."""
    counter = Counter()
    for transaction in transactions:
        if 'description' in transaction and transaction['description'] in description_list:
            counter[transaction['description']] += 1

    return dict(counter)
