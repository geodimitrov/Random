# Solution 1 - long and explicit
def get_letter_position(letter):
    return ord(letter) - 96


def get_double_letter(word):
    for i in range(len(word) - 1):
        if word[i] == word[i+1]:
            return word[i]


def pass_the_door_man(word):
    letter = get_double_letter(word.lower())
    letter_position = get_letter_position(letter)
    return letter_position * 3


# Solution 2 - short and concise
def pass_the_door_man2(word):
    letter = [char for char in word if char * 2 in word][0]
    return (ord(letter) - 96) * 3


tests = [
    "lettuce",      # -> 60
    "hill",         # -> 36
    "apple",        # -> 48
]

for test in tests:
    print(pass_the_door_man(test))
    print(pass_the_door_man2(test))