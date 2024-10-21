import re
from typing import Callable

# function generator_numbers that identifies all real numbers in the text and returns a generator
def generator_numbers(text: str):
    # using a regular expression to find real numbers in the text
    pattern = r'\b\d+\.\d{2}\b'
    matches = re.finditer(pattern, text)
    for match in matches:
        yield float(match.group())

# function sum_profit that sums up all numbers found in the text using generator_numbers
def sum_profit(text: str, func: Callable):
    return sum(func(text))

# example usage
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")