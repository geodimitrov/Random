from itertools import combinations

def int_diff(lst, n):
    combs = combinations(lst, 2)
    return sum(1 for comb in combs if abs(comb[0] - comb[1]) == n)