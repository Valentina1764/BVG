import ast
import json
from datetime import datetime
from pathlib import Path

from src.external_api import converter_currency
from src.finacial_operation import read_csv_transactions, read_excel_transactions
from src.generators import card_number_generator, filter_by_currency, transaction_descriptions
from src.processing import filter_by_state, sort_by_date
from src.utils import load_transactions
from src.widget import get_date, mask_account_card

simple = open("data/card_account.txt", encoding="utf-8")
for line in simple:
    print(mask_account_card(line))
simple.close()


now_date_time = str(datetime.now())
now_date = get_date(now_date_time)
print(now_date, end="\n\n")

state_now = open("data/states.txt", encoding="utf-8")
now_state = []
for line in state_now:
    line_now = ast.literal_eval(line)
    now_state.append(line_now)

state_executed = filter_by_state(now_state)
print(state_executed, end="\n\n")
state_canceled = filter_by_state(now_state, state="CANCELED")
print(state_canceled, end="\n\n")
sort_now_state = sort_by_date(now_state)
print(sort_now_state, end="\n\n")
sort_now_state = sort_by_date(now_state, False)
print(sort_now_state, end="\n\n")

state_now.close()


with open("data/transations.txt", "r", encoding="utf-8") as transactions:
    transactions_today = json.load(transactions)
    usd_transaction = filter_by_currency(transactions_today)
    for _ in range(2):
        print(next(usd_transaction))

print(end="\n\n")

descriptions = transaction_descriptions(transactions_today)
for _ in range(5):
    print(next(descriptions))

print(end="\n\n")

for card_number in card_number_generator(1, 5):
    print(card_number)
transactions.close()


current_dir = Path(__file__).parent
csv_file = current_dir / "data" / "transactions.csv"
transactions_csv = read_csv_transactions(csv_file)
output_file = current_dir / "output" / "transactions_csv.txt"
with open(output_file, "w", encoding="UTF-8") as transactions_json:
    json.dump(transactions_csv, transactions_json, ensure_ascii=False, indent=4)


current_dir = Path(__file__).parent
xlsx_file = current_dir / "data" / "transactions_excel.xlsx"
transactions_excel = read_excel_transactions(xlsx_file)
output_file = current_dir / "output" / "transactions_excel.txt"
with open(output_file, "w", encoding="UTF-8") as transactions_json:
    json.dump(transactions_excel, transactions_json, ensure_ascii=False, indent=4)


transactions = load_transactions("data/operations.json")

try:
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] != "RUB":
            result_convertion = converter_currency(transaction)
            print(result_convertion)
        else:
            print(transaction["operationAmount"]["amount"])

except KeyError:
    print("Ключ operationAmount отсутствует!")
