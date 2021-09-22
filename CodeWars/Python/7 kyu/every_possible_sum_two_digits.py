from itertools import combinations

def digits(num):
    combs = tuple(combinations(map(int, str(num)), 2))
    return [sum(comb) for comb in combs]