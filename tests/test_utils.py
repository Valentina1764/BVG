import json
import unittest
from unittest.mock import mock_open, patch

from src.utils import load_transactions


class TestLoadTransactions(unittest.TestCase):

    def test_file_not_found(self):
        """Тест отсутствия файла"""
        with patch("builtins.open", mock_open()) as mocked_file:
            mocked_file.side_effect = FileNotFoundError
            result = load_transactions("/path/to/file.json")
            print(result)
            self.assertEqual(result, [])

    def test_json_decode_error(self):
        """Тест ошибки декодирования JSON"""
        with patch(
            "builtins.open", mock_open(read_data='{"not valid json"}')
        ) as mocked_file:  # Исправлено: исправлены кавычки
            result = load_transactions("/path/to/file.json")
            self.assertEqual(result, [])

    def test_valid_json_list(self):
        """Тест успешной загрузки списка"""
        expected_data = [{"id": 1}, {"id": 2}]
        with patch("builtins.open", mock_open(read_data=json.dumps(expected_data))) as mocked_file:
            result = load_transactions("/path/to/file.json")
            self.assertEqual(result, expected_data)

    def test_valid_json_non_list(self):
        """Тест успешной загрузки данных, не являющихся списком"""
        expected_data = {"key": "value"}
        with patch("builtins.open", mock_open(read_data=json.dumps(expected_data))) as mocked_file:
            result = load_transactions("/path/to/file.json")
            self.assertEqual(result, [])
