from random import randint, sample

def get_bingo_card():
    ranges = {
        'B': range(1, 16),
        'I': range(16, 31),
        'N': range(31, 46),
        'G': range(46, 61),
        'O': range(61, 76),
    }

    result = []

    for key in ranges:
        if key == 'N':
            
            result += [f'{key}{el}' for el in sample(ranges[key], 4)]
        else:
            result += [f'{key}{el}' for el in sample(ranges[key], 5)]

