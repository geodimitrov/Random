import re

def count_smileys(arr):
    EX = r'[:;]{1}[\-\~]{0,}[)D]{1}'
    return sum(1 for el in arr if re.findall(EX, el))