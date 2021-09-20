import re


def valid_number(n):
    EX = '^[+-]{0,1}\d*\.\d{2}$'
    return True if re.findall(EX, n) else False