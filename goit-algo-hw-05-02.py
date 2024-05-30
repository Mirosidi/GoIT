import re

our_text = input("text: ")

def generator_numbers(text: str):
    pattern = re.compile(r'\b\d+(\.\d+)?\b')
    matches = pattern.finditer(text)
    for match in matches:
        number = float(match.group())
        yield number

def sum_profit(text: str):
    total_sum = sum(generator_numbers(text))
    print("Total profit:", total_sum)

sum_profit(our_text)