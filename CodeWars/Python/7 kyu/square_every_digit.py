def square_digits(num):
    squared_num = ''.join(map(str, [int(n) ** 2 for n in str(num)]))
    return int(squared_num)