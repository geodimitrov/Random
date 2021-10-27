def bits_battle(numbers):
    even_nums = ''.join([format(n, 'b') for n in numbers if n % 2 == 0 and n != 0])
    odd_nums = ''.join([format(n, 'b') for n in numbers if n % 2 != 0 and n!= 0])

    strength_evens = sum(1 for char in even_nums if char == '0')
    strength_odds = sum(1 for char in odd_nums if char == '1')

    if strength_evens > strength_odds:
        return 'evens win'
    elif strength_evens < strength_odds:
        return 'odds win'
    else:
