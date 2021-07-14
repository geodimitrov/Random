# Solution 1 - long and explicit
def count_divisors(n):
    divisors_count = 1  # we start from 1
    divisor = 1

    while divisor < n:

        if n % divisor == 0:
            divisors_count += 1

        divisor += 1

    return divisors_count


# Solution 2 - short and concise
def count_divisors2(n):
    return sum([1 for i in range(1, n + 1) if n % i == 0])


tests = [
    4,      # -> 3
    5,      # -> 2
    12,     # -> 6
]

for test in tests:
    print(count_divisors(test))
    print(count_divisors2(test))