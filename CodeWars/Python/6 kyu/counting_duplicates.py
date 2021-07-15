def duplicate_count(text):
    duplicate_counter = 0

    for char in set(text.lower()):
        if text.lower().count(char) > 1:
            duplicate_counter += 1

    return duplicate_counter


tests = [
    "abcde",    # -> 0
    "aabbcde",  # -> 2
    "aabBcde",  # -> 2
]

for test in tests:
    print(duplicate_count(test))
