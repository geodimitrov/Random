def sum_of_n(n):
    # triangular number formula: n(n + 1)/2
    result = [i * (i + 1) / 2 for i in range(abs(n) + 1)]

    if n < 0:
        return [-el for el in result]

    return result
