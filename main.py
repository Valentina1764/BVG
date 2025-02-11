import ast
from datetime import datetime

from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card

simple = open("data/card_account.txt", encoding="utf-8")
for line in simple:
    print(mask_account_card(line))

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
sort_now_state = sort_by_date(now_state, True)
print(sort_now_state)
