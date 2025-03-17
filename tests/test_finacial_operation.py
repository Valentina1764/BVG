import unittest
from pathlib import Path
from unittest.mock import mock_open, patch

import pandas as pd

from src.finacial_operation import read_csv_transactions, read_excel_transactions

expected_result = [
    {
        "id": "650703",
        "state": "EXECUTED",
        "date": "2023-09-05T11:30:32Z",
        "amount": "16210",
        "currency_name": "Sol",
        "currency_code": "PEN",
        "from": "Счет 58803664561298323391",
        "to": "Счет 39745660563456619397",
        "description": "Перевод организации",
    },
    {
        "id": "3598919",
        "state": "EXECUTED",
        "date": "2020-12-06T23:00:58Z",
        "amount": "29740",
        "currency_name": "Peso",
        "currency_code": "COP",
        "from": "Discover 3172601889670065",
        "to": "Discover 0720428384694643",
        "description": "Перевод с карты на карту",
    },
]


class TestReadCSVTransactions(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data="date;amount\n01/01/2020;100")
    def test_successful_read(self, mock_file):
        # Тест успешного чтения файла
        result = read_csv_transactions("test.csv")
        self.assertEqual(result, [{"date": "01/01/2020", "amount": "100"}])
        mock_file.assert_called_once_with("test.csv", "r", encoding="UTF-8")


def test_invalid_csv_file_path():
    """Тест отсутствия файла."""
    current_dir = Path(__file__).parent.parent
    invalid_file_path = current_dir / "transactions_test.csv"
    try:
        read_csv_transactions(invalid_file_path)
    except ValueError as e:
        assert str(e) == f"Файл {invalid_file_path} не найден."


class TestExcelTransactions(unittest.TestCase):

    @patch("pandas.read_excel")
    def test_successful_read(self, mock_read_excel):
        # Создаем фиктивный DataFrame
        data = {"id": [1, 2], "amount": ["100", "200"], "date": ["01/01/2020", "02/01/2020"]}
        mock_df = pd.DataFrame(data)
        mock_read_excel.return_value = mock_df

        # Вызываем функцию
        result = read_excel_transactions("test.xlsx")

        # Проверки
        expected_result = [
            {"id": "1", "amount": "100", "date": "01/01/2020"},
            {"id": "2", "amount": "200", "date": "02/01/2020"},
        ]
        self.assertEqual(result, expected_result)
        mock_read_excel.assert_called_once_with("test.xlsx")


def test_invalid_xlsx_file_path():
    """Тест отсутствия файла."""
    current_dir = Path(__file__).parent.parent
    invalid_file_path = current_dir / "transactions_excel_test.xlsx"
    try:
        read_csv_transactions(invalid_file_path)
    except ValueError as e:
        assert str(e) == f"Файл {invalid_file_path} не найден."
