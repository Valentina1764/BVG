from datetime import datetime
from src.widget import get_date, mask_account_card

simple = open("data/card_account.txt", encoding="utf-8")
for line in simple:
    print(mask_account_card(line))

now_date_time = str(datetime.now())
now_date = get_date(now_date_time)
print(now_date)
