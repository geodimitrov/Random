def odd_row(n):
    start_n = n ** 2 - (n - 1)
    return list(range(start_n, start_n + n * 2, 2))