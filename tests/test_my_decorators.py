import os

from src.my_decorators import log


def test_error_handling_in_function(capsys):
    """Тест обработки ошибки в функции с логированием в консоль."""

    @log()
    def divide(a, b):
        return a / b


def test_logging_to_file(tmpdir):
    """Тест логирования в файл."""
    log_filename = os.path.join(tmpdir, "log.txt")

    @log(log_filename)
    def multiply(a, b):
        return a * b

    result = multiply(3, 4)
    assert result == 12

    with open(log_filename, "r") as file:
        logs = file.read()
        expected_logs = (
            "INFO - Функция 'multiply' выполнена успешно; Аргументы: (3, 4), {}; "
            "Результат: 12; Время выполнения: 0.00 сек"
        )
        assert logs.strip() == expected_logs
