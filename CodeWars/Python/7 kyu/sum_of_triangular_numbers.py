def sum_triangular_numbers(n):
    # x(x+1)/2
    triuangular_nums = [i * (i +1) / 2 for i in range(1, n + 1)]
    return sum(triuangular_nums)
