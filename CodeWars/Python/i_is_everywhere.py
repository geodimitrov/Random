def vowels_gt_consonants(word):
    vowels = [char for char in word if char.lower() in "aeiou"]
    return len(vowels) >= len(word) - len(vowels)


def is_valid(word):

    if not word or word[0] == "I" \
            or word[0].islower() \
            or vowels_gt_consonants(word):
        return False

    return True


def add_i_to_word(word):

    if not is_valid(word):
        return "Invalid word"

    return "i" + word

tests = [
    "Phone",
    "World",
    "Inspire",
    "",
    "road",
    "East",
    "Peace"

]

for test in tests:
    print(add_i_to_word(test))