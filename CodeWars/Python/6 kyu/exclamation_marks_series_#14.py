import re


def convert(s):
    EX = '!{0,}|\?{0,}'
    number = int(''.join([str(len(el)) for el in re.findall(EX, s) if el]))
    is_prime = False

    while not is_prime:

        for i in range(2, number):
            if number % i == 0:
                number //= i
                break
            elif i == number - 1:
                is_prime = True

        if number < 3:
            is_prime = True

    return number