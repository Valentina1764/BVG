import unittest

from src.operations import (
    count_categories,
    search_operations_by_currency,
    search_operations_by_description,
    search_operations_by_word
)


class TestOperations(unittest.TestCase):

    def test_search_operations_by_description(self):
        # Данные для теста
        test_data = [
            {"id": 1, "state": "PENDING"},
            {"id": 2, "state": "EXECUTED"},
            {"id": 3, "state": "EXECUTED"},
        ]

        # Тело теста
        result = search_operations_by_description(test_data, "PENDING")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["id"], 1)

        result = search_operations_by_description(test_data, "EXECUTED")
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["id"], 2)

        result = search_operations_by_description(test_data, "CANCELED")
        self.assertEqual(len(result), 0)

    def test_search_operations_by_currency(self):
        # Данные для теста
        test_data = [
            {"id": 1, "currency_code": "USD"},
            {"id": 2, "currency_code": "EUR"},
            {"id": 3, "currency_code": "RUB"},
        ]

        # Тело теста
        result = search_operations_by_currency(test_data, "usd")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["id"], 1)

        result = search_operations_by_currency(test_data, "EUR")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["id"], 2)

        result = search_operations_by_currency(test_data, "GBP")
        self.assertEqual(len(result), 0)

    def test_search_operations_by_word(self):
        # Данные для теста
        test_data = [
            {"id": 1, "description": "Перевод с карты на карту"},
            {"id": 2, "description": "Открытие вклада"},
            {"id": 3, "description": "Перевод с карты на счет"},
        ]

        # Тело теста
        result = search_operations_by_word(test_data, "Перевод")
        self.assertEqual(len(result), 2)
        self.assertSetEqual({op["id"] for op in result}, {1, 3})

        result = search_operations_by_word(test_data, "Открытие")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["id"], 2)

        result = search_operations_by_word(test_data, "Снятие")
        self.assertEqual(len(result), 0)

    def test_count_categories(self):
        # Данные для теста
        transactions = [
            {"id": 1, "description": "Перевод с карты на карту"},
            {"id": 2, "description": "Перевод с карты на карту"},
            {"id": 3, "description": "Открытие вклада"},
            {"id": 4, "description": "Перевод с карты на счет"},
            {"id": 5, "description": "Перевод с карты на счет"},
        ]

        description_list = ["Перевод с карты на карту", "Перевод с карты на счет"]

        # Тело теста
        result = count_categories(transactions, description_list)
        self.assertDictEqual(
            result,
            {
                "Перевод с карты на карту": 2,
                "Перевод с карты на счет": 2,
            },
        )
