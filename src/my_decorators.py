# https://genchat.ru/chat/neyroset-dlya-napisaniya-koda
import functools
import time
import logging


def log(filename=None):
    # Настройка логгера
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Определение обработчика для записи в файл или в консоль
    if filename:
        handler = logging.FileHandler(filename)
    else:
        handler = logging.StreamHandler()

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    def my_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            try:
                result = func(*args, **kwargs)
                elapsed_time = time.time() - start_time
                logger.info(f"Функция '{func.__name__}' выполнена успешно; "
                            f"Аргументы: {args}, {kwargs}; "
                            f"Результат: {result}; "
                            f"Время выполнения: {elapsed_time:.2f} сек")
                return result
            except Exception as e:
                logger.error(f"Ошибка в функции '{func.__name__}'; "
                             f"Тип ошибки: {type(e).__name__}; "
                             f"Аргументы: {args}, {kwargs}; "
                             f"Сообщение об ошибке: {e}")
                raise  # Перебрасываем исключение для обработки его выше

        return wrapper

    return my_decorator

@log('example.log')
def add(a, b):
    """Функция сложения двух чисел."""
    return a + b

@log()
def divide(a, b):
    """Функция деления двух чисел."""
    return a / b

if __name__ == "__main__":
    add(2, 3)
    divide(6, 2)  # Заменили деление на ноль на корректный случай

    # Тесты с использованием py и фикстур:

    import pytest
    from decorator import log_to_file

    @pytest.fixture(autouse=True)
    def setup_logging(caplog):
        # Настраиваем уровень логирования на DEBUG для тестирования
        caplog.set_level(logging.DEBUG)

    def test_add(caplog):
        @log_to_file()
        def add(a, b):
            return a + b

        add(2, 3)
        assert len(caplog.records) == 1
        record = caplog.records[0]
        assert record.levelno == logging.INFO
        assert "Arguments: (2, 3)" in record.message
        assert "Result: 5" in record.message

    def test_divide(caplog):
        @log_to_file()
        def divide(a, b):
            return a / b

        divide(6, 2)
        assert len(caplog.records) == 1
        record = caplog.records[0]
        assert record.levelno == logging.INFO
        assert "Arguments: (6, 2)" in record.message
        assert "Result: 3.0" in record.message

    def test_divide_by_zero(caplog):
        @log_to_file()
        def divide(a, b):
            return a / b

        with pytest.raises(ZeroDivisionError):
            divide(6, 0)
        assert len(caplog.records) == 1
        record = caplog.records[0]
        assert record.levelno == logging.ERROR
        assert "Arguments: (6, 0)" in record.message
        assert "Error: ZeroDivisionError" in record.message

        return a / b

    if __name__ == "__main__":
        add(2, 3)
        divide(6, 2)  # Заменили деление на ноль на корректный случай

    # Тесты с использованием pytest и фикстур:

    import pytest
    from my_decorators import log_to_file

    @pytest.fixture(autouse=True)
    def setup_logging(caplog):
        # Настраиваем уровень логирования на DEBUG для тестирования
        caplog.set_level(logging.DEBUG)

    def test_add(caplog):
        @log_to_file()
        def add(a, b):
            return a + b

        add(2, 3)
        assert len(caplog.records) == 1
        record = caplog.records[0]
        assert record.levelno == logging.INFO
        assert "Arguments: (2, 3)" in record.message
        assert "Result: 5" in record.message

    def test_divide(caplog):
        @log_to_file()
        def divide(a, b):
            return a / b

        divide(6, 2)
        assert len(caplog.records) == 1
        record = caplog.records[0]
        assert record.levelno == logging.INFO
        assert "Arguments: (6, 2)" in record.message
        assert "Result: 3.0" in record.message

    def test_divide_by_zero(caplog):
        @log_to_file()
        def divide(a, b):
            return a / b

        with pytest.raises(ZeroDivisionError):
            divide(6, 0)
        assert len(caplog.records) == 1
        record = caplog.records[0]
        assert record.levelno == logging.ERROR
        assert "Arguments: (6, 0)" in record.message
        assert "Error: ZeroDivisionError" in record.message
