import re


def valid_phone_number(phone_number):
    EX = '^\(\d{3}\) \d{3}-\d{4}$'
    return True if re.match(EX, phone_number) else False


test = [
    "(123) 456-7890",   # True
    "(1111)555 2345",   # False
    "(098) 123 4567",   # False
]