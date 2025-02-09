from datetime import datetime
from src.widget import get_date, mask_account_card
from src.processing import filter_by_state


simple = open("data/card_account.txt", encoding = "utf-8")
for line in simple:
    print(mask_account_card(line))

now_date_time = str(datetime.now())
now_date = get_date(now_date_time)
print(now_date)

state_now = open("Data/states.txt", encoding ="utf-8")
for line in state_now:
    print(import filter_by_state(line))
