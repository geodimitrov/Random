def factorial(n):
    if n < 0 or n > 12:
        raise ValueError()

    elif n == 1 or n == 0:
        return 1

    return n * factorial(n-1)