import csv
import pandas as pd
from typing import List, Dict


def read_csv_transactions(csv_file_path: str) -> List[Dict]:
    """Функция для считывания финансовых операций из CSV файла."""
    try:
        collect_list = []
        with open(csv_file_path, "r", encoding="UTF-8") as csv_file:
            df = csv.DictReader(csv_file, delimiter=";")
            for row in df:
                collect_list.append(row)
            return collect_list
    except FileNotFoundError:
        raise ValueError(f"Файл {csv_file_path} не найден.")


def read_excel_transactions(excel_file_path: str) -> List[Dict]:
    """Функция для считывания финансовых операций из Excel файла."""
    try:
        df = pd.read_excel(excel_file_path)
        df["id"] = df["id"].astype(int, errors="ignore")
        df = df.applymap(lambda x: str(x))
        records = df.to_dict("records")
        return records
    except FileNotFoundError:
        raise ValueError(f"Файл {excel_file_path} не найден.")
