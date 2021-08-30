# Solution 1
def iq_test(numbers):
    numbers = list(map(int, numbers.split()))

    if len([n for n in numbers if n % 2 == 0]) > 1:
        result = int([n for n in numbers if n % 2 != 0][0])
    else:
        result = int([n for n in numbers if n % 2 == 0][0])

    return numbers.index(result) + 1


# Solution 2
def iq_test1(numbers):
    numbers = [int(n) % 2 for n in numbers.split()]

    if numbers.count(0) > 1:
        return numbers.index(1) + 1
    else:
        return numbers.index(0) + 1