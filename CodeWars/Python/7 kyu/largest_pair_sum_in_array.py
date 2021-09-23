from itertools import combinations

def largest_pair_sum(numbers):
    pairs = list(combinations(numbers, 2))
    return max(map(sum, pairs))