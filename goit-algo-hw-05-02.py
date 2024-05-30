import re
from typing import Generator, Callable

our_text = input("text: ")

def generator_numbers(text: str) -> Generator[float, None, None]:
    pattern = re.compile(r'\b\d+(\.\d+)?\b')
    matches = pattern.finditer(text)
    for match in matches:
        number = float(match.group())
        yield number

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    total_sum = sum(func(text))
    print("Total profit:", total_sum)

sum_profit(our_text, generator_numbers)