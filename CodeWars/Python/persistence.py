# We have to find the persistence of a whole number

# Solution 1 - using while loop
def get_sum_digits(digits):
    res = 1
    for d in digits:
        res *= d
    return res


def persistence(n):
    result = 0

    while n >= 10:
        result += 1
        digits = tuple(map(int, str(n)))
        n = get_sum_digits(digits)

    return result


#Solution 2 - using recursion
def get_sum_digits(digits):
    res = 1
    for d in digits:
        res *= d
    return res


def persistence(n, result=0):
    if n < 10:
        return result

    result += 1
    digits = tuple(map(int, str(n)))
    n = get_sum_digits(digits)
    return persistence(n, result)


tests = [
    39, 999, 4, 1, 15,
]

for num in tests:
    print(persistence(num))