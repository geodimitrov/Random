def single_digit(n):
    while len(str(n)) > 1:
        n = sum(map(int, bin(n).replace('0b', '')))

    return n