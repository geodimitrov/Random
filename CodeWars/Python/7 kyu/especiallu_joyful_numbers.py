def number_joy(n):
    sum_digits = sum(map(int, str(n)))
    return sum_digits * int(str(sum_digits)[::-1]) == n