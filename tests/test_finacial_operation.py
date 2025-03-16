from pathlib import Path
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


def test_read_csv_transactions():
    """Тест на корректность вывода списка словарей трансакций из файла .csv ."""
    current_dir = Path(__file__).parent.parent
    csv_file = current_dir / "data" / "transactions_test.csv"
    result = read_csv_transactions(csv_file)
    assert result == expected_result


def test_invalid_csv_file_path():
    """Тест отсутствия файла."""
    current_dir = Path(__file__).parent.parent
    invalid_file_path = current_dir / "transactions_test.csv"
    try:
        read_csv_transactions(invalid_file_path)
    except ValueError as e:
        assert str(e) == f"Файл {invalid_file_path} не найден."


def test_read_excel_transactions():
    """Тест на корректность вывода списка словарей трансакций из файла .xlsx ."""
    current_dir = Path(__file__).parent.parent
    xlsx_file = current_dir / "data" / "transactions_excel_test.xlsx"
    result = read_excel_transactions(xlsx_file)
    print(result)
    assert result == expected_result


def test_invalid_xlsx_file_path():
    """Тест отсутствия файла."""
    current_dir = Path(__file__).parent.parent
    invalid_file_path = current_dir / "transactions_excel_test.xlsx"
    try:
        read_csv_transactions(invalid_file_path)
    except ValueError as e:
        assert str(e) == f"Файл {invalid_file_path} не найден."
