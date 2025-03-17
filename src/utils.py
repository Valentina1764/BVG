import json
import logging
from pathlib import Path

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
log_file = "./logs/utils.log"
file_handler = logging.FileHandler(log_file, "w", encoding="UTF-8")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def load_transactions(file_path: str) -> list:
    """функция считывает данные из файла типа JSON"""
    try:
        logger.info(f"Считываем данные из файла {file_path}")
        file_path = Path(file_path)
        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            else:
                logger.warning(f"Данные из файла {file_path} не являются списком.")
                return []
    except FileNotFoundError:
        logger.error(f"Файл {file_path} не найден.")
        return []
    except json.JSONDecodeError:
        logger.error(f"Ошибка декодирования JSON из файла {file_path}.")
        return []
