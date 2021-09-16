def narcissistic(number):
    calc_value = sum([int(d) ** len(str(number)) for d in str(number)])
    return calc_value == number