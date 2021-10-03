from collections import Counter

def is_language_diverse(lst):
    a, b, c = sorted(Counter([el['language'] for el in lst]).values())
    return a * 2 >= c and b * 2 >= c