from pathlib import Path
import json


def load_transactions(file_path: str) -> str:
    '''функция считывает данные из файла типа JSON'''
    try:
        file_path = Path(file_path)
        with open(file_path, encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            else:
                return []
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
