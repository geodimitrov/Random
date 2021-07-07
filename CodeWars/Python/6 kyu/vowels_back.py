SPECIAL_CHARS = (
    'c', 'o', 'd', 'e',
)

VOWELS = 'aeiou'

def move_char(char, char_dec):
    if char in VOWELS:
        places_to_move = -5
    else:
        places_to_move = 9

    char_dec += places_to_move

    if char_dec > 122:
        char_dec = 96 + (char_dec - 122)
    elif char_dec < 97:
        char_dec = 123 - (97 - char_dec)

    return char_dec

def vowel_back(string):
    modified_string = ''

    for char in string:

        if char in ('c', 'o'):
            char_dec = ord(char) - 1
        elif char == 'd':
            char_dec = ord(char) - 3
        elif char == 'e':
            char_dec = ord(char) - 4
        else:
            char_dec = move_char(char, ord(char))

            if chr(char_dec) in SPECIAL_CHARS:
               char_dec = ord(char)

        modified_string += chr(char_dec)

    return modified_string



tests = [
    "testcase",         # -> "tabtbvba"
    "codewars",         # -> "bnaafvab"
    "exampletesthere",  # -> "agvvyuatabtqaaa"

]


for test in tests:
    print(vowel_back(test))
