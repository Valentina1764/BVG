import functools
import logging
import time


def log(filename=None):
    """Декоратор простых функций сложения и деления"""
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    if filename:
        handler = logging.FileHandler(filename)
    else:
        handler = logging.StreamHandler()

    formatter = logging.Formatter("%(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    def my_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            try:
                result = func(*args, **kwargs)
                elapsed_time = time.time() - start_time
                logger.info(
                    f"Функция '{func.__name__}' выполнена успешно; "
                    f"Аргументы: {args}, {kwargs}; "
                    f"Результат: {result}; "
                    f"Время выполнения: {elapsed_time:.2f} сек"
                )
                return result
            except Exception as e:
                logger.error(
                    f"Ошибка в функции '{func.__name__}'; "
                    f"Тип ошибки: {type(e).__name__}; "
                    f"Аргументы: {args}, {kwargs}; "
                    f"Сообщение об ошибке: {e}"
                )
                raise

        return wrapper

    return my_decorator


@log("example.log")
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
