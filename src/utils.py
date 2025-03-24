import json
# import logging
from pathlib import Path

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)
# formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
# log_file = "./logs/utils.log"
# file_handler = logging.FileHandler(log_file, "w", encoding="UTF-8")
# file_handler.setFormatter(formatter)
# logger.addHandler(file_handler)


def load_transactions(file_path: str) -> list:
    """функция считывает данные из файла типа JSON"""
    try:
        # logger.info(f"Считываем данные из файла {file_path}")
        file_path = Path(file_path)
        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                results = []
                for dict_in_data in data:
                    result = {
                        "id": get_safe_value(dict_in_data, "id"),
                        "state": get_safe_value(dict_in_data, "state"),
                        "date": get_safe_value(dict_in_data, "date"),
                        "amount": get_safe_value(get_safe_value(dict_in_data, "operationAmount", {}), "amount", ""),
                        "currency_name": get_safe_value(
                            get_safe_value(get_safe_value(dict_in_data, "operationAmount", {}), "currency", {}),
                            "name",
                            "",
                        ),
                        "currency_code": get_safe_value(
                            get_safe_value(get_safe_value(dict_in_data, "operationAmount", {}), "currency", {}),
                            "code",
                            "",
                        ),
                        "description": get_safe_value(dict_in_data, "description"),
                        "from": get_safe_value(dict_in_data, "from"),
                        "to": get_safe_value(dict_in_data, "to"),
                    }
                    results.append(result)
                return results
            else:
                # logger.warning(f"Данные из файла {file_path} не являются списком.")
                return []
    except FileNotFoundError:
        # logger.error(f"Файл {file_path} не найден.")
        return []
    except json.JSONDecodeError:
        # logger.error(f"Ошибка декодирования JSON из файла {file_path}.")
        return []


def get_safe_value(obj, key, default=""):
    """Безопасная функция получения значения по ключу."""
    return obj.get(key, default)
