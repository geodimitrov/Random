def fizzbuzz(n):
    result = []

    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            value = 'FizzBuzz'
        elif i % 3 == 0:
            value = 'Fizz'
        elif i % 5 == 0:
            value = 'Buzz'
        else:
            value = i
        result.append(value)

    return result