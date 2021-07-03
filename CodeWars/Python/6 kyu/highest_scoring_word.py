from string import ascii_lowercase

ALPHABET = list(ascii_lowercase)

def get_word_score(word):
    score = 0

    for char in word:
        char_score = ALPHABET.index(char) + 1
        score += char_score

    return score


def get_highest_scoring_word(string):
    highest_score = 0
    result = None

    for word in string.split():
        word_score = get_word_score(word)
        if word_score > highest_score:
            highest_score = word_score
            result = word

    return result


tests = [
    'man i need a taxi up to ubud',              # should return taxi
    "what time are we climbing up the volcano",  # should return volcano
    "take me to semynak",                        # should return semynak
    'aa b',                                      # should return aa
    "b aa"                                       # should return b
]

for test in tests:
    print(get_highest_scoring_word(test))