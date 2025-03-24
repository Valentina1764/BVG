import unittest
from unittest.mock import MagicMock, patch

from dotenv import load_dotenv

from src.external_api import converter_currency

load_dotenv()  # Загружаем переменные окружения


class TestConverterCurrency(unittest.TestCase):

    def setUp(self):
        self.transaction_usd = {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        }
        self.transaction_eur = {
            "id": 736942989,
            "state": "EXECUTED",
            "date": "2019-09-06T00:48:01.081967",
            "operationAmount": {"amount": "6357.56", "currency": {"name": "EUR", "code": "EUR"}},
            "description": "Перевод организации",
            "from": "Visa Gold 3654412434951162",
            "to": "Счет 59986621134048778289",
        }
        self.invalid_transaction = {
            "id": 490100847,
            "state": "EXECUTED",
            "date": "2018-12-22T02:02:49.564873",
            "operationAmount": {"amount": "56516.63", "currency": {"name": "CAD", "code": "CAD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Gold 8326537236216459",
            "to": "MasterCard 6783917276771847",
        }

    @patch("requests.get")
    def test_converter_usd(self, mock_get):
        # Настройка мока для успешного ответа
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"result": 12345.67}
        mock_get.return_value = mock_response

        # Тестируем конверсию USD
        result = converter_currency(self.transaction_usd)
        self.assertEqual(result, 12345.67)

    @patch("requests.get")
    def test_converter_eur(self, mock_get):
        # Настройка мока для успешного ответа
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"result": 9876.54}
        mock_get.return_value = mock_response

        # Тестируем конверсию EUR
        result = converter_currency(self.transaction_eur)
        self.assertEqual(result, 9876.54)

    @patch("requests.get")
    def test_invalid_currency(self, mock_get):
        # Тестируем случай с недействительной валютой
        with self.assertRaises(Exception):
            converter_currency(self.invalid_transaction)

    @patch("requests.get")
    def test_api_error(self, mock_get):
        # Настройка мока для ошибки API
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        # Тестируем случай ошибки API
        with self.assertRaises(Exception):
            converter_currency(self.transaction_usd)


if __name__ == "__main__":
    unittest.main()
