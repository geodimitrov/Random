def nb_dig(n, d):
    nums = [i ** 2 for i in range(n + 1)]
    return sum([str(el).count(str(d)) for el in nums])