LETTERS_TO_NUMS = {
    'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5', 'F': '6', 'G': '7', 'H': '8',
    'J': '1', 'K': '2', 'L': '3', 'M': '4', 'N': '5', 'P': '7', 'R': '9', 'S': '2',
    'T': '3', 'U': '4', 'V': '5', 'W': '6', 'X': '7', 'Y': '8', 'Z': '9'
}
WEIGHTS = [8, 7, 6, 5, 4, 3, 2, 10, 0, 9, 8, 7, 6, 5, 4, 3, 2]
INVALID_LETTERS = 'IOQ'


def is_valid_length(vin):
    return len(vin) == 17


def contains_only_valid_letters(vin):
    letters = [char for char in vin if char.isalpha()]

    for l in letters:
        if l in INVALID_LETTERS or l.islower():
            return False

    return True


def contains_digits(vin):
    return [char for char in vin if char.isdigit()]


def modify_vin(vin):
    return ''.join(LETTERS_TO_NUMS[char] if char in LETTERS_TO_NUMS else char for char in vin)


def has_valid_modulus_11(init_vin, modified_vin):
    sum_digits = sum(int(modified_vin[i]) * WEIGHTS[i] for i in range(len(modified_vin)))
    modulus_11 = sum_digits % 11

    if modulus_11 == 10:
        return init_vin[8] == 'X'

    return str(sum_digits % 11) == init_vin[8]


def check_vin(vin):
    if not is_valid_length(vin) or not contains_digits(vin) or not contains_only_valid_letters(vin):
        return False

    modified_vin = modify_vin(vin)

    if not has_valid_modulus_11(vin, modified_vin):
        return False

    return True