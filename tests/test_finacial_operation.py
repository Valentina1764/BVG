import unittest
from pathlib import Path
from unittest.mock import mock_open, patch

import pandas as pd

from src.finacial_operation import read_csv_transactions, read_excel_transactions


class TestReadCSVTransactions(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data="date;amount\n01/01/2020;100")
    def test_successful_read(self, mock_file):
        """Тест успешного чтения .csv файла"""
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
        """Тест успешного чтения .xlsx файла"""
        data = {"id": [1, 2], "amount": ["100", "200"], "date": ["01/01/2020", "02/01/2020"]}
        mock_df = pd.DataFrame(data)
        mock_read_excel.return_value = mock_df

        result = read_excel_transactions("test.xlsx")

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
