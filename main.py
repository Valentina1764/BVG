import json
from pathlib import Path

from src.finacial_operation import read_csv_transactions, read_excel_transactions
from src.operations import (
    count_categories,
    search_operations_by_currency,
    search_operations_by_description,
    search_operations_by_word
)
from src.processing import sort_by_date
from src.utils import load_transactions
from src.widget import get_date, mask_account_card

categories_operations = [
    "Перевод с карты на карту",
    "Перевод организации",
    "Перевод со счета на счет",
    "Открытие вклада",
    "Перевод с карты на счет",
]


def main():
    """Функция получения информации от пользователя для обработки списка банковских операций,
    получения списков трансакций и обработки с помощью внешних функций."""

    print(
        "Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n"
        "Выберите необходимый пункт меню:\n"
        "1. Получить информацию о транзакциях из JSON-файла\n"
        "2. Получить информацию о транзакциях из CSV-файле\n"
        "3. Получить информацию о транзакциях из XLSX-файла",
        end="\n\n",
    )

    type_input_file = input()
    print(end="\n\n")
    if type_input_file == "1":
        current_dir = Path(__file__).parent
        json_file = current_dir / "data" / "operations.json"
        transactions = load_transactions(json_file)
        output_file = current_dir / "output" / "transactions_json.txt"
        with open(output_file, "w", encoding="UTF-8") as transactions_json:
            json.dump(transactions, transactions_json, ensure_ascii=False, indent=4)
        # print(transactions)
    elif type_input_file == "2":
        current_dir = Path(__file__).parent
        csv_file = current_dir / "data" / "transactions.csv"
        transactions = read_csv_transactions(csv_file)
        output_file = current_dir / "output" / "transactions_csv.txt"
        with open(output_file, "w", encoding="UTF-8") as transactions_json:
            json.dump(transactions, transactions_json, ensure_ascii=False, indent=4)
    elif type_input_file == "3":
        current_dir = Path(__file__).parent
        xlsx_file = current_dir / "data" / "transactions_excel.xlsx"
        transactions = read_excel_transactions(xlsx_file)
        output_file = current_dir / "output" / "transactions_excel.txt"
        with open(output_file, "w", encoding="UTF-8") as transactions_json:
            json.dump(transactions, transactions_json, ensure_ascii=False, indent=4)

    while True:
        print(
            "Введите статус, по которому необходимо выполнить фильтрацию.\n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING",
            end="\n\n",
        )
        state_transactions = ["EXECUTED", "CANCELED", "PENDING"]
        user_state_transactions = input()
        print(end="\n\n")
        if user_state_transactions.upper() in state_transactions:
            transactions_by_state = search_operations_by_description(transactions, user_state_transactions)
            break
        else:
            print(f"Статус операции '{user_state_transactions}' недоступен.")
            continue

    print("Отсортировать операции по дате? Да/Нет", end="\n\n")
    user_sort_by_date = input()
    print(end="\n\n")
    if user_sort_by_date.lower() == "да":
        print("Отсортировать по возрастанию или по убыванию?", end="\n\n")
        user_sort = input()
        print(end="\n\n")
        if user_sort.lower() == "по возрастанию":
            transactions_by_state = sort_by_date(transactions_by_state, False)
        else:
            transactions_by_state = sort_by_date(transactions_by_state)

    print("Выводить только рублевые транзакции? Да/Нет", end="\n\n")
    user_sort_by_currency = input()
    print(end="\n\n")
    if user_sort_by_currency.lower() == "да":
        transactions_by_state = search_operations_by_currency(transactions_by_state, "RUB")

    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет", end="\n\n")
    user_answer = input()
    print(end="\n\n")
    if user_answer.lower() == "да":
        print("Введите слово, пример: 'Перевод', 'счет', 'карты', 'карту' и т.д.", end="\n\n")
        user_filtr_word = input()
        print(end="\n\n")
        transactions_by_state = search_operations_by_word(transactions_by_state, user_filtr_word)

    print("Распечатываю итоговый список транзакций...", end="\n\n")

    count_operations_by_state = count_categories(transactions_by_state, categories_operations)
    if count_operations_by_state == {}:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Всего банковских операций в выборке: {count_operations_by_state}", end="\n\n")

    for transaction in transactions_by_state:
        date_operation = get_date(transaction["date"])
        print(date_operation, transaction["description"])
        print(f"{mask_account_card(transaction['from'])} -> {mask_account_card(transaction['to'])}")
        print(f"Сумма: {transaction['amount']} {transaction['currency_name']}", end="\n\n")


if __name__ == "__main__":
    main()
