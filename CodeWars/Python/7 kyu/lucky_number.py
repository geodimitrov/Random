def is_lucky(n):
    sum_digits = sum(int(d) for d in str(n))
    return sum_digits == 0 or sum_digits % 9 == 0