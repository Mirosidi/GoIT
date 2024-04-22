#Перше завдання

from datetime import datetime

def get_days_from_today(date):
    try:
        input_date = datetime.strptime(date, format("%Y-%m-%d"))
        current_date = datetime.today()
        diff = current_date - input_date
        return diff.days
    except:
        if ValueError:
            return None

print (get_days_from_today("2021-10-09"))

# The second task

import random

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or quantity < 1 or quantity > max - min + 1:
        return []

    numbers_set = set()
    while len(numbers_set) < quantity:
        numbers_set.add(random.randint(min, max))

    return sorted(list(numbers_set))

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Your lottery numbers:", lottery_numbers)

# The third task

import re

def normalize_phone(phone_number):
    phone_number = re.sub(r'\D', '', phone_number)

    if not phone_number.startswith('+'):
        if phone_number.startswith('380'):
            phone_number = '+' + phone_number
        else:
            phone_number = '+38' + phone_number

    return phone_number

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Normalized phone numbers for SMS distribution:", sanitized_numbers)